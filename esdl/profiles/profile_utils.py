import uuid
from collections import defaultdict
from datetime import datetime
from typing import Any

from esdl import (
    DatabaseConfiguration,
    DatabaseTypeEnum,
    DataConfigurations,
    DataSource,
    DataTableProfile,
    DateTimeProfile,
    EnergySystem,
    EnergySystemInformation,
    GenericProfile,
    InfluxDBProfile,
    ProfileReference,
    ProfileTypeEnum,
    QuantityAndUnitReference,
    QuantityAndUnits,
    TimeSeriesProfile,
)
from esdl.profiles.credentials import Credentials
from esdl.profiles.data_configurations.postgresql import PostgresqlDataTableManager
from esdl.profiles.datatableprofilemanager import DataTableProfileManager
from esdl.profiles.influxdbprofilemanager import ConnectionSettings, InfluxDBProfileManager
from esdl.profiles.profilemanager import ProfileManager

profile_data_cache: dict[str, tuple[list, list | None]] = {}


def _create_profile_cache_key(
    config_id: str,
    table_name: str,
    column_name: str | None,
    start_date: Any | None,
    end_date: Any | None,
    schema: str | None = None,
) -> str:
    """
    Create a profile cache key from configuration id, table name, column name, start date, and end date.

    :param config_id: The configuration id.
    :param table_name: The table name.
    :param column_name: The column name, or None.
    :param start_date: The start date, or None.
    :param end_date: The end date, or None.
    :param schema: The schema name, or None.
    :return: A unique profile cache key.
    """
    table_part = table_name
    column_part = column_name if column_name is not None else ""
    start_part = str(start_date) if start_date is not None else ""
    end_part = str(end_date) if end_date is not None else ""
    schema_part = schema if schema is not None else ""
    return f"{config_id}:{table_part}:{column_part}:{start_part}:{end_part}:{schema_part}"


def _clone_qau(qau: Any) -> Any:
    """Return a deep clone of qau."""
    if not qau:
        return None

    if isinstance(qau, QuantityAndUnitReference):
        qau = qau.reference
    return qau.deepcopy()


def _influxdbprofile_to_datatableprofile(
    profile: InfluxDBProfile,
) -> DataTableProfile:
    """Translate InfluxDBProfile into DataTableProfile."""

    dtp = DataTableProfile(
        id=profile.id,
        name=profile.name,
        tableName=profile.measurement,
        columnName=profile.field,
        filter=profile.filters,
        multiplier=profile.multiplier,
        startDate=profile.startDate,
        endDate=profile.endDate,
        profileType=profile.profileType,
        profileQuantityAndUnit=_clone_qau(profile.profileQuantityAndUnit),
    )

    dtp.configuration = DatabaseConfiguration(
        database=profile.database,
        type=DatabaseTypeEnum.INFLUXDB,
        host=profile.host,
        port=profile.port,
        tls=False,
    )

    return dtp


def _get_referenced_profile(profile: GenericProfile) -> GenericProfile:
    """Return the profile referenced by the given profile."""
    if not hasattr(profile, "reference"):
        raise TypeError(f"ProfileReference '{profile.id}': missing 'reference' attribute.")
    if isinstance(profile.reference, ProfileReference):
        return _get_referenced_profile(profile.reference)
    return profile.reference


@staticmethod
def close_db_connections() -> None:
    """
    Closes all database connections in the cache.
    Should be called when the application is shutting down to properly close resources.
    """
    DataTableProfileManager.close_db_connections()


def load_profile_data_and_header(
    profile: DataTableProfile | InfluxDBProfile | TimeSeriesProfile | DateTimeProfile | ProfileReference,
    enable_cache: bool = False,
    apply_multiplier: bool = True,
    close_connection_after_load: bool = True,
) -> tuple[Any | None, list[Any] | None]:
    """
    Retrieve the profile data list and header for a given profile with time varying data, any of type:
        DataTableProfile, InfluxDBProfile, TimeSeriesProfile, DateTimeProfile or ProfileReference.

    Converts InfluxDBProfile to DataTableProfile if necessary.
    Profile data can be cached for database profiles to avoid requerying the same data.

    :param profile: The profile to process.
    :param enable_cache: Whether to cache profile data for database profiles.
    :param apply_multiplier: Whether to apply the profile multiplier to the data values, default is True.
    :param close_connection_after_load: If True (default), close DB connection after loading data.
        If False, callers must close connections manually via close_db_connections().
    :return: The profile header and data list, or (None, None).
    """
    if isinstance(profile, ProfileReference):
        profile = _get_referenced_profile(profile)

    if isinstance(profile, (DataTableProfile, InfluxDBProfile)):
        dtp = profile if isinstance(profile, DataTableProfile) else _influxdbprofile_to_datatableprofile(profile)

        if enable_cache:
            cache_key = _create_profile_cache_key(
                dtp.configuration.id, dtp.tableName, dtp.columnName, dtp.startDate, dtp.endDate, dtp.schema
            )
            if cache_key in profile_data_cache:  # return cached profile
                data_list, header = profile_data_cache[cache_key]
                if apply_multiplier and dtp.multiplier is not None and data_list is not None:
                    # apply multiplier to cached data, skip first datetime column
                    data_list = [[row[0]] + [value * dtp.multiplier for value in row[1:]] for row in data_list]
                return (data_list, header)

        # load from database
        dtp_manager = DataTableProfileManager(dtp)
        dtp_manager.load_from_database(close_connection_after_load=close_connection_after_load)
        header = dtp_manager.profile_header
        data_list = dtp_manager.profile_data_list

        if enable_cache:  # store raw in cache
            profile_data_cache[cache_key] = (data_list, header)

        if apply_multiplier and dtp.multiplier is not None and data_list is not None:
            # apply multiplier, skip first datetime column
            data_list = [[row[0]] + [value * dtp.multiplier for value in row[1:]] for row in data_list]
    elif isinstance(profile, (TimeSeriesProfile, DateTimeProfile)):
        profile_manager = ProfileManager()
        profile_manager.parse_esdl(profile)
        header = profile_manager.profile_header
        data_list = profile_manager.profile_data_list
    else:
        raise NotImplementedError(f"Unsupported profile (id={profile.id}) class: {type(profile).__name__}")

    return data_list, header


def attr_matches(left, right, attr_name):
    left_has_attr = hasattr(left, attr_name)
    right_has_attr = hasattr(right, attr_name)

    if not left_has_attr and not right_has_attr:
        return True
    if left_has_attr != right_has_attr:
        return False

    left_value = getattr(left, attr_name, None)
    right_value = getattr(right, attr_name, None)

    if left_value is None and right_value is None:
        return True
    return left_value == right_value


def create_data_table_profile(
    es: EnergySystem,
    database_name: str,
    table_name: str,
    column_name: str,
    start_date: datetime,
    end_date: datetime,
    db_host: str,
    db_port: int | None = None,
    filter: str | None = None,
    multiplier: float = 1.0,
    db_type=DatabaseTypeEnum.POSTGRESQL,  # EEnumLiteral cannnot be typed, so check if used in function
    profile_type: "ProfileTypeEnum | None" = None,  # type: ignore[valid-type]
    quantity_and_unit_type: QuantityAndUnitReference | None = None,
    data_source: DataSource | None = None,
) -> DataTableProfile:
    """Create and add DataTableProfile to a port, and related database configuration to the energy system information
      if not already present.

    :param es: energy system.
    :param database_name: database name for the configuration.
    :param table_name: table name referenced by the data table profile, measurement for influxdb.
    :param column_name: column name referenced by the data table profile, tag for influxdb.
    :param start_date: profile start datetime.
    :param end_date: profile end datetime.
    :param db_host: database host.
    :param db_port: database port, default is None.
    :param filter: filter string for the profile, default is None.
    :param multiplier: multiplier, default is 1.0.
    :param db_type: database type: one of [DatabaseTypeEnum.POSTGRESQL, DatabaseTypeEnum.INFLUXDB], default is DatabaseTypeEnum.POSTGRESQL.
    :param profile_type: optional profile type for this profile, default is None.
    :param quantity_and_unit_type: quantity and unit type reference, default is None.
    :param data_source: optional data source information for this profile, default is None.
    :return: created and attached data table profile.
    """
    if db_type not in {DatabaseTypeEnum.POSTGRESQL, DatabaseTypeEnum.INFLUXDB}:
        raise ValueError("DataTableProfile type must be DatabaseTypeEnum.POSTGRESQL or DatabaseTypeEnum.INFLUXDB")

    data_table_profile = DataTableProfile(
        id=str(uuid.uuid4()),
        tableName=table_name,
        columnName=column_name,
        startDate=start_date,
        endDate=end_date,
        multiplier=multiplier,
        filter=filter,
    )

    # ensure EnergySystemInformation exists in the ESDL
    esi = es.energySystemInformation
    if not esi:
        esi = EnergySystemInformation(id=str(uuid.uuid4()))
        es.energySystemInformation = esi
    # ensure DataConfigurations container exists in EnergySystemInformation
    if not esi.dataconfigurations:
        esi.dataconfigurations = DataConfigurations(id=str(uuid.uuid4()))

    db_config = DatabaseConfiguration(
        type=db_type,
        id=str(uuid.uuid4()),
        database=database_name,
        host=db_host,
    )
    if db_port is not None:
        db_config.port = db_port

    # add the database configuration to the global registry if it does not already exist.
    db_config_match_attributes = [
        "database",
        "host",
        "name",
        "port",
        "tls",
        "type",
    ]
    existing_db_config = next(
        (
            existing_config
            for existing_config in esi.dataconfigurations.configurations
            if all(attr_matches(existing_config, db_config, attr_name) for attr_name in db_config_match_attributes)
        ),
        None,
    )
    if existing_db_config is None:
        esi.dataconfigurations.configurations.append(db_config)
    else:
        db_config = existing_db_config

    data_table_profile.configuration = db_config

    if quantity_and_unit_type:
        # Ensure QuantityAndUnits container exists in EnergySystemInformation
        if not esi.quantityAndUnits:
            esi.quantityAndUnits = QuantityAndUnits(id=str(uuid.uuid4()))

        # Add the quantity and unit to the global registry only if it does not already exist.
        qau_match_attributes = [
            "description",
            "multiplier",
            "perMultiplier",
            "perScope",
            "perTimeUnit",
            "perUnit",
            "physicalQuantity",
            "unit",
        ]

        existing_qau = next(
            (
                qau
                for qau in esi.quantityAndUnits.quantityAndUnit
                if all(attr_matches(qau, quantity_and_unit_type, attr_name) for attr_name in qau_match_attributes)
            ),
            None,
        )
        if existing_qau is None:
            esi.quantityAndUnits.quantityAndUnit.append(quantity_and_unit_type)
        else:
            quantity_and_unit_type = existing_qau
        data_table_profile.profileQuantityAndUnit = QuantityAndUnitReference(reference=quantity_and_unit_type)

    if data_source:
        data_table_profile.dataSource = data_source
    if profile_type:
        data_table_profile.profileType = profile_type

    return data_table_profile


def save_data_table_profiles_to_database(
    dtp_managers: list[DataTableProfileManager], additional_tags: dict[str, str] | None = None
) -> None:
    """Save the given list of data table profile managers to their respective databases, using as few DB queries as possible.

    Managers that target the same table are combined into a single write query.
    Each manager must have ``profile_data_list`` set.

    :param dtp_managers: list of DataTableProfileManager instances to save.
    :param additional_tags: optional dict of additional filter tags to save (not filtered on by DataTableProfile).
    :raises ValueError: If a manager has no profile data or header, or if a configuration is missing.
    """
    if not dtp_managers:
        return

    # Validate all managers have data loaded.
    for dtp_manager in dtp_managers:
        if not dtp_manager.data_table_profile.configuration:
            raise ValueError(
                f"DataTableProfileManager for profile id={dtp_manager.data_table_profile.id} has no configuration set."
            )
        if not dtp_manager.profile_data_list:
            raise ValueError(
                f"DataTableProfileManager for profile id={dtp_manager.data_table_profile.id} has no profile_data_list set."
            )

    # Group managers by write destination and datetime sequence (values + order).
    # Managers in the same group can be merged row-by-row without datetime lookups.
    groups: dict[tuple, list[DataTableProfileManager]] = defaultdict(list)
    for dtp_manager in dtp_managers:
        dtp = dtp_manager.data_table_profile
        datetime_col = dtp.datetimeColumnName

        datetime_sequence = tuple(row[0] for row in dtp_manager.profile_data_list)
        key = (
            dtp.configuration.type,
            dtp.configuration.host,
            dtp.configuration.port,
            dtp.configuration.database,
            dtp.schema,
            dtp.tableName,
            dtp.filter,
            dtp.datetimeColumnName,
            datetime_col,
            datetime_sequence,
        )
        groups[key].append(dtp_manager)

    for group in groups.values():
        first_dtp_manager = group[0]

        # start with the first profile values.
        merged_header: list[str] = list([
            first_dtp_manager.data_table_profile.datetimeColumnName,
            first_dtp_manager.data_table_profile.columnName,
        ])
        merged_rows: list[list[Any]] = [list(row) for row in first_dtp_manager.profile_data_list]

        for dtp_manager in group[1:]:
            col_name = dtp_manager.data_table_profile.columnName
            if col_name in merged_header:
                raise ValueError(
                    f"Error saving to database for profile id={dtp_manager.data_table_profile.id}:"
                    f" duplicate column '{col_name}' detected."
                )
            merged_header.append(col_name)
            for idx, row in enumerate(dtp_manager.profile_data_list):
                merged_rows[idx].append(row[1])

        configuration = first_dtp_manager.data_table_profile.configuration

        # Parse and merge filters once for both PostgreSQL and InfluxDB
        merged_filters = DataTableProfileManager._parse_profile_filter(
            first_dtp_manager.data_table_profile.filter, as_dict=True
        )
        if additional_tags:
            if isinstance(merged_filters, dict):
                merged_filters = {**merged_filters, **additional_tags}
            else:
                merged_filters = additional_tags

        if configuration.type == DatabaseTypeEnum.POSTGRESQL:
            pdt_manager = PostgresqlDataTableManager.get_from_cache_or_create(first_dtp_manager.data_table_profile)
            pdt_manager.save_data(
                merged_rows,
                merged_header,
                profile_dict={mgr.data_table_profile.columnName: mgr.data_table_profile for mgr in group},
                overwrite=False,
                filter_dict=merged_filters,
            )
        elif configuration.type == DatabaseTypeEnum.INFLUXDB:
            credential = Credentials.get_credential(configuration)
            influx_port = configuration.port if configuration.port is not None else 8086
            use_ssl = "https" in configuration.host or influx_port == 443
            conn_settings = ConnectionSettings(
                host=configuration.host,
                port=influx_port,
                username=credential.username if credential and credential.username else "",
                password=credential.password if credential and credential.password else "",
                database=configuration.database,
                ssl=use_ssl,
                verify_ssl=use_ssl,
            )
            influxdb_profile_manager = InfluxDBProfileManager.get_from_cache_or_create(conn_settings)
            influxdb_profile_manager.start_datetime = first_dtp_manager.data_table_profile.startDate
            influxdb_profile_manager.end_datetime = first_dtp_manager.data_table_profile.endDate
            influxdb_profile_manager.profile_header = merged_header
            influxdb_profile_manager.profile_data_list = merged_rows
            influxdb_profile_manager.save_influxdb(
                measurement=first_dtp_manager.data_table_profile.tableName,
                field_names=[c for c in merged_header if c != first_dtp_manager.data_table_profile.datetimeColumnName],
                tags=merged_filters,
            )
        else:
            raise ValueError(f"Unsupported database type: {configuration.type}")
