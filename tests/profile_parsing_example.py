import logging
import uuid
from datetime import datetime

import pandas as pd

import esdl
from esdl.esdl_handler import EnergySystemHandler
from esdl.profiles.credentials import Credentials
from esdl.profiles.datatableprofilemanager import DataTableProfileManager
from esdl.profiles.profile_utils import (
    close_db_connections,
    create_data_table_profile,
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


def add_profile_to_port(port, profile: esdl.DataTableProfile):
    if not hasattr(port, "profile") or port.profile is None:
        raise TypeError(f"Port '{port.id}': missing 'profile' attribute.")
    port.profile.append(profile)


if __name__ == "__main__":
    # ================================================================================= #
    #  first start databases locally: run `docker compose up --wait` in `tests` folder  #
    # ================================================================================= #

    # set db credentials
    logging.basicConfig(level=logging.INFO)
    Credentials.add_credential("localhost:1432", "postgres", "password")
    Credentials.add_credential("localhost:1086", "admin", "admin")

    # use 'model run id' as database name and 'carrier network id' as table name
    model_run_id = str(uuid.uuid4())
    carrier_network_id = str(uuid.uuid4())

    # =================
    # get data from CSV
    df = pd.read_csv("test_profile.csv")
    datetime_col = "datetime" if "datetime" in df.columns else df.columns[0]
    df[datetime_col] = pd.to_datetime(
        df[datetime_col].astype(str).str.strip().str.strip("'").str.strip('"'),
        utc=True,
    ).dt.to_pydatetime()

    profile_header1 = [datetime_col, df.columns[1]]
    profile_data_list1 = df[[datetime_col, df.columns[1]]].values.tolist()

    profile_header2 = [datetime_col, df.columns[2]]
    profile_data_list2 = df[[datetime_col, df.columns[2]]].values.tolist()

    print(f"Profile 1 Header: {profile_header1}")
    print(f"Profile 1 Data (first 2 rows): {profile_data_list1[:2]}")
    print(f"Profile 2 Header: {profile_header2}")
    print(f"Profile 2 Data (first 2 rows): {profile_data_list2[:2]}")

    # ===============================================================================
    # create a new energy system with several assets (not connected for this example)
    energy_system_handler = EnergySystemHandler()
    es = energy_system_handler.create_empty_energy_system(
        name="Test_EnergySystem",
        es_description="For profile parsing example",
        inst_title="Tutorial_Instance",
        area_title="Tutorial_Area",
    )
    area = es.instance[0].area
    electricity_demand1 = add_electricity_demand_to_area(area, name="ElectricityDemand1", lat=52.0, lon=5.0)
    electricity_demand1_port1 = add_port_to_asset(electricity_demand1)
    electricity_demand1_port2 = add_port_to_asset(electricity_demand1)
    electricity_demand2 = add_electricity_demand_to_area(area, name="ElectricityDemand2", lat=52.0, lon=5.1)
    electricity_demand2_port1 = add_port_to_asset(electricity_demand2)
    electricity_demand2_port2 = add_port_to_asset(electricity_demand2)

    # create quantity and unit type for power in kW
    qau_power = esdl.QuantityAndUnitType(
        description="Power in kW",
        id=str(uuid.uuid4()),
        physicalQuantity=esdl.PhysicalQuantityEnum.POWER,
        unit=esdl.UnitEnum.WATT,
        multiplier=esdl.MultiplierEnum.KILO,
    )

    # ================================
    # add data table profiles to ports
    dtp_postgres1 = create_data_table_profile(
        es=es,
        database_name=model_run_id,
        table_name=carrier_network_id,
        column_name="column1",  # column header in "test_profile.csv"
        start_date=datetime(2019, 1, 1),
        end_date=datetime(2019, 1, 2),
        db_host="localhost",
        db_port=1432,  # optional
        # filter optional: needed if profiles for multiple assets are written to the same table_name
        filter='"assetId"=' + f"'{str(electricity_demand1.id)}'",
        multiplier=2.0,  # optional: default is 1.0
        db_type=esdl.DatabaseTypeEnum.POSTGRESQL,  # default: other option DatabaseTypeEnum.INFLUXDB
        profile_type=esdl.ProfileTypeEnum.OUTPUT,  # default: other option esdl.ProfileTypeEnum.POINTS
        quantity_and_unit_type=qau_power,
    )
    electricity_demand1_port1.profile.append(dtp_postgres1)

    dtp_postgres2 = create_data_table_profile(
        es=es,
        database_name=model_run_id,
        table_name=carrier_network_id,
        column_name="column2",
        start_date=datetime(2019, 1, 1),
        end_date=datetime(2019, 1, 2),
        db_host="localhost",
        db_port=1432,
        filter='"assetId"=' + f"'{str(electricity_demand1.id)}'",
        db_type=esdl.DatabaseTypeEnum.POSTGRESQL,
        quantity_and_unit_type=qau_power,
    )
    electricity_demand1_port2.profile.append(dtp_postgres2)

    dtp_influx1 = create_data_table_profile(
        es=es,
        database_name=model_run_id,
        table_name=carrier_network_id,
        column_name="column1",
        start_date=datetime(2019, 1, 1),
        end_date=datetime(2019, 1, 2),
        db_host="localhost",
        db_port=1086,
        filter='"assetId"=' + f"'{str(electricity_demand2.id)}'",
        db_type=esdl.DatabaseTypeEnum.INFLUXDB,
        quantity_and_unit_type=qau_power,
    )
    electricity_demand2_port1.profile.append(dtp_influx1)

    dtp_influx2 = create_data_table_profile(
        es=es,
        database_name=model_run_id,
        table_name=carrier_network_id,
        column_name="column2",
        start_date=datetime(2019, 1, 1),
        end_date=datetime(2019, 1, 2),
        db_host="localhost",
        db_port=1086,
        filter='"assetId"=' + f"'{str(electricity_demand2.id)}'",
        db_type=esdl.DatabaseTypeEnum.INFLUXDB,
        quantity_and_unit_type=qau_power,
    )
    electricity_demand2_port2.profile.append(dtp_influx2)

    # =============================================================
    # save profile data to database: aggregate for efficient saving
    profiles_to_save = []

    dtp_postgres1_manager = DataTableProfileManager(dtp_postgres1)
    # list of value rows where each row is a list: [datetime.datetime object, profile value]
    dtp_postgres1_manager.profile_data_list = profile_data_list1
    profiles_to_save.append(dtp_postgres1_manager)

    dtp_postgres2_manager = DataTableProfileManager(dtp_postgres2)
    dtp_postgres2_manager.profile_data_list = profile_data_list2
    profiles_to_save.append(dtp_postgres2_manager)

    dtp_influx1_manager = DataTableProfileManager(dtp_influx1)
    dtp_influx1_manager.profile_data_list = profile_data_list1
    profiles_to_save.append(dtp_influx1_manager)

    dtp_influx2_manager = DataTableProfileManager(dtp_influx2)
    dtp_influx2_manager.profile_data_list = profile_data_list2
    profiles_to_save.append(dtp_influx2_manager)

    # aggregate save, will minimize number of database queries
    additional_tags = {"model_run_id": model_run_id}
    save_data_table_profiles_to_database(profiles_to_save, additional_tags=additional_tags)

    # =================
    # read all profiles
    for el in es.eAllContents():
        if isinstance(el, esdl.Asset) and hasattr(el, "port") and el.port is not None:
            for port in el.port:
                if hasattr(port, "profile") and port.profile is not None:
                    for profile in port.profile:
                        print(f"\n==== Profile ==== {type(profile)}")
                        if isinstance(profile, esdl.DataTableProfile):
                            print(f"DB type: {profile.configuration.type}")

                        profile_raw_data, profile_header = load_profile_data_and_header(
                            profile,
                            True,
                            False,  # for performance, must close_db_connections() in the end
                        )
                        if profile_header and profile_raw_data:
                            print(f"Header from profile: {profile_header}")
                            print(f"Data from profile (first 2 rows): {profile_raw_data[:3]}")

    close_db_connections()
