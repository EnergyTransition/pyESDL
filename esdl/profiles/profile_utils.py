from typing import Any

from esdl import (
    DatabaseConfiguration,
    DatabaseTypeEnum,
    DataTableProfile,
    DateTimeProfile,
    GenericProfile,
    InfluxDBProfile,
    ProfileReference,
    QuantityAndUnitReference,
    TimeSeriesProfile,
)
from esdl.profiles.datatableprofilemanager import DataTableProfileManager
from esdl.profiles.profilemanager import ProfileManager

profile_data_cache: dict[str, tuple[Any, list[Any]]] = {}


def _create_profile_cache_key(
    config_id: str,
    table_name: str | None,
    column_name: str | None,
    start_date: Any | None,
    end_date: Any | None,
) -> str:
    """
    Create a profile cache key from configuration id, table name, column name, start date, and end date.

    Parameters
    ----------
    config_id : str
        The configuration id.
    table_name : str | None
        The table name, or None.
    column_name : str | None
        The column name, or None.
    start_date : Any | None
        The start date, or None.
    end_date : Any | None
        The end date, or None.

    Returns
    -------
    str
        A unique profile cache key.
    """
    table_part = table_name if table_name is not None else ""
    column_part = column_name if column_name is not None else ""
    start_part = str(start_date) if start_date is not None else ""
    end_part = str(end_date) if end_date is not None else ""
    return f"{config_id}:{table_part}:{column_part}:{start_part}:{end_part}"


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


def get_time_varying_profile_header_and_raw_data(
    profile: DataTableProfile | InfluxDBProfile | TimeSeriesProfile | DateTimeProfile | ProfileReference,
    enable_cache: bool = False,
) -> tuple[Any | None, list[Any] | None]:
    """
    Retrieve the profile header and data list for a given profile with time varying data:
        DataTableProfile, InfluxDBProfile, TimeSeriesProfile, DateTimeProfile or ProfileReference.

    Converts InfluxDBProfile to DataTableProfile if necessary, then loads data for PostgreSQL profiles.
    Profile data can be cached to avoid requerying the same table/column combinations. or

    Parameters
    ----------
    profile : GenericProfile
        The profile to process.
    enable_cache : bool, optional
        Whether to cache profile data, by default True.

    Returns
    -------
    tuple[Any | None, list[Any] | None]
        The profile header and data list, or (None, None).
    """
    if isinstance(profile, ProfileReference):
        profile = _get_referenced_profile(profile)

    if isinstance(profile, (DataTableProfile, InfluxDBProfile)):
        if isinstance(profile, DataTableProfile):
            tableName = profile.tableName
            columnName = profile.columnName
            dtp = profile
        elif isinstance(profile, InfluxDBProfile):
            tableName = profile.measurement
            columnName = profile.field
            dtp = _influxdbprofile_to_datatableprofile(profile)

        dtp_manager = DataTableProfileManager(dtp)

        if enable_cache:
            cache_key = _create_profile_cache_key(
                dtp.configuration.id, tableName, columnName, dtp.startDate, dtp.endDate
            )
            if cache_key in profile_data_cache:  # return cached profile
                return profile_data_cache[cache_key]

        # load from database
        dtp_manager.load_database_configuration()
        header = dtp_manager.profile_header
        data_list = dtp_manager.profile_data_list

        if enable_cache:  # store in cache
            profile_data_cache[cache_key] = (header, data_list)
    elif isinstance(profile, (TimeSeriesProfile, DateTimeProfile)):
        profile_manager = ProfileManager()
        profile_manager.parse_esdl(profile)
        header = profile_manager.profile_header
        data_list = profile_manager.profile_data_list
    else:
        raise NotImplementedError(f"Unsupported profile (id={profile.id}) class: {type(profile).__name__}")

    return header, data_list
