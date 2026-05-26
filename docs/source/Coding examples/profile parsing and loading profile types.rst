Creating and parsing multiple types of ESDL profiles
====================================================

This example shows how to create and assign ESDL profiles, and how to load profile data.
The following profile types are covered in this example:

- DataTableProfile (PostgreSQL/INFLUXDB)
- InfluxDBProfile (deprecated, reading/loading only)
- TimeSeriesProfile
- DateTimeProfile

This example consists of the following steps:

1. Database configuration and credential management

2. Setup demo profile data and energy system with assets and ports:

   - Read profile data from CSV
   - Create an EnergySystem with assets and ports

3. Create and assign multiple profile types:

   - DataTableProfile (PostgreSQL)
   - DataTableProfile (InfluxDB)
   - TimeSeriesProfile
   - DateTimeProfile

4. Save DataTableProfile data efficiently to databases
5. Read all profiles back

.. note::
   Start the local test databases first:

   .. code-block:: bash

      docker compose up --wait


.. code-block:: python

    import logging
    import os
    import uuid
    from datetime import datetime
    from pathlib import Path

    import esdl
    from esdl.esdl_handler import EnergySystemHandler
    from esdl.profiles.credentials import Credentials
    from esdl.profiles.datatableprofilemanager import DataTableProfileManager
    from esdl.profiles.profile_utils import (
        close_db_connections,
        create_data_table_profile,
        create_date_time_profile,
        create_time_series_profile,
        load_profile_data_and_header,
        save_data_table_profiles_to_database,
    )


    def add_electricity_demand_to_area(area, name, lat, lon):
        electricity_demand = esdl.ElectricityDemand(name=name, id=str(uuid.uuid4()))
        electricity_demand_location = esdl.Point(lat=lat, lon=lon)
        electricity_demand.geometry = electricity_demand_location
        area.asset.append(electricity_demand)
        return electricity_demand


    def add_port_to_asset(asset):
        asset_in_port = esdl.InPort(id=str(uuid.uuid4()))
        asset.port.append(asset_in_port)
        return asset_in_port


    if __name__ == "__main__":
        ### 1. Database configuration and credential management
        logging.basicConfig(level=logging.INFO)

        postgres_host = os.getenv("PYESDL_POSTGRES_HOST", "localhost")
        postgres_port = int(os.getenv("PYESDL_POSTGRES_PORT", "1432"))
        postgres_user = os.getenv("PYESDL_POSTGRES_USER", "postgres")
        postgres_password = os.getenv("PYESDL_POSTGRES_PASSWORD", "password")

        influxdb_host = os.getenv("PYESDL_INFLUXDB_HOST", "localhost")
        influxdb_port = int(os.getenv("PYESDL_INFLUXDB_PORT", "1086"))
        influxdb_user = os.getenv("PYESDL_INFLUXDB_USER", "admin")
        influxdb_password = os.getenv("PYESDL_INFLUXDB_PASSWORD", "admin")

        Credentials.add_credential(f"{postgres_host}:{postgres_port}", postgres_user, postgres_password)
        Credentials.add_credential(f"{influxdb_host}:{influxdb_port}", influxdb_user, influxdb_password)

        ### 2. Setup demo profile data and energy system with assets and ports
        model_run_id = str(uuid.uuid4())
        carrier_network_id = str(uuid.uuid4())
        
        # Read source profile data from CSV
        csv_path = Path("tests/data/test_profile.csv")
        csv_profile = esdl.DataTableProfile(
            id=str(uuid.uuid4()),
            configuration=esdl.FileConfiguration(uri=str(csv_path), type=esdl.FileTypeEnum.CSV),
        )
        csv_profile_manager = DataTableProfileManager.load(csv_profile)

        datetime_col = csv_profile_manager.profile_header[0]
        profile_data_list1 = [[row[0], row[1]] for row in csv_profile_manager.profile_data_list]
        profile_data_list2 = [[row[0], row[2]] for row in csv_profile_manager.profile_data_list]

        # Build an empty energy system and add assets/ports
        energy_system_handler = EnergySystemHandler()
        es = energy_system_handler.create_empty_energy_system(
            name="Test_EnergySystem",
            es_description="For profile parsing example",
            inst_title="Tutorial_Instance",
            area_title="Tutorial_Area",
        )
        area = es.instance[0].area
        demand1 = add_electricity_demand_to_area(area, name="ElectricityDemand1", lat=52.0, lon=5.0)
        demand1_p1 = add_port_to_asset(demand1)
        demand1_p2 = add_port_to_asset(demand1)

        demand2 = add_electricity_demand_to_area(area, name="ElectricityDemand2", lat=52.0, lon=5.1)
        demand2_p1 = add_port_to_asset(demand2)
        demand2_p2 = add_port_to_asset(demand2)
        demand2_p3 = add_port_to_asset(demand2)

        qau_power = esdl.QuantityAndUnitType(
            description="Power in kW",
            id=str(uuid.uuid4()),
            physicalQuantity=esdl.PhysicalQuantityEnum.POWER,
            unit=esdl.UnitEnum.WATT,
            multiplier=esdl.MultiplierEnum.KILO,
        )

        ### 3. Create and assign multiple profile types:
        dtp_postgres1 = create_data_table_profile(
            es=es,
            database_name=model_run_id,
            table_name=carrier_network_id,
            column_name="column1",
            start_date=datetime(2019, 1, 1),
            end_date=datetime(2019, 1, 2),
            db_host=postgres_host,
            db_port=postgres_port,
            filter='"assetId"=' + f"'{str(demand1.id)}'",
            multiplier=2.0,
            db_type=esdl.DatabaseTypeEnum.POSTGRESQL,
            profile_type=esdl.ProfileTypeEnum.OUTPUT,
            quantity_and_unit_type=qau_power,
        )
        demand1_p1.profile.append(dtp_postgres1)

        dtp_postgres2 = create_data_table_profile(
            es=es,
            database_name=model_run_id,
            table_name=carrier_network_id,
            column_name="column2",
            start_date=datetime(2019, 1, 1),
            end_date=datetime(2019, 1, 2),
            db_host=postgres_host,
            db_port=postgres_port,
            filter='"assetId"=' + f"'{str(demand1.id)}'",
            db_type=esdl.DatabaseTypeEnum.POSTGRESQL,
            quantity_and_unit_type=qau_power,
        )
        demand1_p2.profile.append(dtp_postgres2)

        dtp_influx1 = create_data_table_profile(
            es=es,
            database_name=model_run_id,
            table_name=carrier_network_id,
            column_name="column1",
            start_date=datetime(2019, 1, 1),
            end_date=datetime(2019, 1, 2),
            db_host=influxdb_host,
            db_port=influxdb_port,
            filter='"assetId"=' + f"'{str(demand2.id)}'",
            db_type=esdl.DatabaseTypeEnum.INFLUXDB,
            quantity_and_unit_type=qau_power,
        )
        demand2_p1.profile.append(dtp_influx1)

        dtp_influx2 = create_data_table_profile(
            es=es,
            database_name=model_run_id,
            table_name=carrier_network_id,
            column_name="column2",
            start_date=datetime(2019, 1, 1),
            end_date=datetime(2019, 1, 2),
            db_host=influxdb_host,
            db_port=influxdb_port,
            filter='"assetId"=' + f"'{str(demand2.id)}'",
            db_type=esdl.DatabaseTypeEnum.INFLUXDB,
            quantity_and_unit_type=qau_power,
        )
        demand2_p2.profile.append(dtp_influx2)

        time_series_profile = create_time_series_profile(
            es=es,
            name="TimeSeriesProfile1",
            start_date=datetime(2019, 1, 1),
            timestep_in_seconds=3600,
            values=[row[1] for row in profile_data_list1],
            profile_type=esdl.ProfileTypeEnum.OUTPUT,
            quantity_and_unit_type=qau_power,
        )
        demand2_p3.profile.append(time_series_profile)

        date_time_profile = create_date_time_profile(
            es=es,
            name="DateTimeProfile1",
            datetime_and_values=profile_data_list1,
            profile_type=esdl.ProfileTypeEnum.OUTPUT,
            quantity_and_unit_type=qau_power,
        )
        demand2_p3.profile.append(date_time_profile)

        ### 4. Save DataTableProfile data efficiently to databases
        dtp_postgres1_manager = DataTableProfileManager(dtp_postgres1)
        dtp_postgres1_manager.profile_data_list = profile_data_list1

        dtp_postgres2_manager = DataTableProfileManager(dtp_postgres2)
        dtp_postgres2_manager.profile_data_list = profile_data_list2

        dtp_influx1_manager = DataTableProfileManager(dtp_influx1)
        dtp_influx1_manager.profile_data_list = profile_data_list1

        dtp_influx2_manager = DataTableProfileManager(dtp_influx2)
        dtp_influx2_manager.profile_data_list = profile_data_list2

        save_data_table_profiles_to_database(
            [dtp_postgres1_manager, dtp_postgres2_manager, dtp_influx1_manager, dtp_influx2_manager],
            additional_tags={"model_run_id": model_run_id},
        )

        ### 5. Read all profiles back
        for el in es.eAllContents():
            if isinstance(el, esdl.Asset) and hasattr(el, "port") and el.port is not None:
                for port in el.port:
                    if hasattr(port, "profile") and port.profile is not None:
                        for profile in port.profile:
                            profile_data, profile_header = load_profile_data_and_header(
                                profile,
                                enable_cache=True,
                                apply_multiplier=True,
                                close_connection_after_load=False,
                            )
                            print(type(profile), profile_header, profile_data[:3])

        close_db_connections()
