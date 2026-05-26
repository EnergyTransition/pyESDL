import os
import socket
import uuid
from datetime import datetime
from pathlib import Path

import pytest

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


def _service_reachable(host: str, port: int, timeout: float = 1.0) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        try:
            sock.connect((host, port))
            return True
        except OSError:
            return False


def _add_electricity_demand_to_area(area, name, lat, lon):
    electricity_demand = esdl.ElectricityDemand(name=name, id=str(uuid.uuid4()))
    electricity_demand.geometry = esdl.Point(lat=lat, lon=lon)
    area.asset.append(electricity_demand)
    return electricity_demand


def _add_port_to_asset(asset):
    asset_in_port = esdl.InPort(id=str(uuid.uuid4()))
    asset.port.append(asset_in_port)
    return asset_in_port


@pytest.fixture(scope="module")
def profile_fixture():
    postgres_host = os.getenv("PYESDL_POSTGRES_HOST", "localhost")
    postgres_port = int(os.getenv("PYESDL_POSTGRES_PORT", "1432"))
    postgres_user = os.getenv("PYESDL_POSTGRES_USER", "postgres")
    postgres_password = os.getenv("PYESDL_POSTGRES_PASSWORD", "password")

    influxdb_host = os.getenv("PYESDL_INFLUXDB_HOST", "localhost")
    influxdb_port = int(os.getenv("PYESDL_INFLUXDB_PORT", "1086"))
    influxdb_user = os.getenv("PYESDL_INFLUXDB_USER", "admin")
    influxdb_password = os.getenv("PYESDL_INFLUXDB_PASSWORD", "admin")

    if not _service_reachable(postgres_host, postgres_port):
        pytest.skip(f"PostgreSQL test service not reachable on {postgres_host}:{postgres_port}")
    if not _service_reachable(influxdb_host, influxdb_port):
        pytest.skip(f"InfluxDB test service not reachable on {influxdb_host}:{influxdb_port}")

    Credentials.add_credential(f"{postgres_host}:{postgres_port}", postgres_user, postgres_password)
    Credentials.add_credential(f"{influxdb_host}:{influxdb_port}", influxdb_user, influxdb_password)

    model_run_id = str(uuid.uuid4())
    carrier_network_id = str(uuid.uuid4())

    csv_profile = esdl.DataTableProfile(
        id=str(uuid.uuid4()),
        configuration=esdl.FileConfiguration(
            uri=str(Path(__file__).parent / "data" / "test_profile.csv"),
            type=esdl.FileTypeEnum.CSV,
        ),
    )
    csv_profile_manager = DataTableProfileManager.load(csv_profile)

    datetime_col = csv_profile_manager.profile_header[0]
    profile_header1 = [datetime_col, csv_profile_manager.profile_header[1]]
    profile_data_list1 = [[row[0], row[1]] for row in csv_profile_manager.profile_data_list]

    profile_header2 = [datetime_col, csv_profile_manager.profile_header[2]]
    profile_data_list2 = [[row[0], row[2]] for row in csv_profile_manager.profile_data_list]

    energy_system_handler = EnergySystemHandler()
    es = energy_system_handler.create_empty_energy_system(
        name="Test_EnergySystem",
        es_description="For profile parsing tests",
        inst_title="Test_Instance",
        area_title="Test_Area",
    )
    area = es.instance[0].area
    electricity_demand1 = _add_electricity_demand_to_area(area, name="ElectricityDemand1", lat=52.0, lon=5.0)
    electricity_demand1_port1 = _add_port_to_asset(electricity_demand1)
    electricity_demand1_port2 = _add_port_to_asset(electricity_demand1)
    electricity_demand2 = _add_electricity_demand_to_area(area, name="ElectricityDemand2", lat=52.0, lon=5.1)
    electricity_demand2_port1 = _add_port_to_asset(electricity_demand2)
    electricity_demand2_port2 = _add_port_to_asset(electricity_demand2)
    electricity_demand2_port3 = _add_port_to_asset(electricity_demand2)

    qau_power = esdl.QuantityAndUnitType(
        description="Power in kW",
        id=str(uuid.uuid4()),
        physicalQuantity=esdl.PhysicalQuantityEnum.POWER,
        unit=esdl.UnitEnum.WATT,
        multiplier=esdl.MultiplierEnum.KILO,
    )

    dtp_postgres1 = create_data_table_profile(
        es=es,
        database_name=model_run_id,
        table_name=carrier_network_id,
        column_name="column1",
        start_date=datetime(2019, 1, 1),
        end_date=datetime(2019, 1, 2),
        db_host=postgres_host,
        db_port=postgres_port,
        filter='"assetId"=' + f"'{str(electricity_demand1.id)}'",
        multiplier=2.0,
        db_type=esdl.DatabaseTypeEnum.POSTGRESQL,
        profile_type=esdl.ProfileTypeEnum.OUTPUT,
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
        db_host=postgres_host,
        db_port=postgres_port,
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
        db_host=influxdb_host,
        db_port=influxdb_port,
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
        db_host=influxdb_host,
        db_port=influxdb_port,
        filter='"assetId"=' + f"'{str(electricity_demand2.id)}'",
        db_type=esdl.DatabaseTypeEnum.INFLUXDB,
        quantity_and_unit_type=qau_power,
    )
    electricity_demand2_port2.profile.append(dtp_influx2)

    time_series_profile = create_time_series_profile(
        es=es,
        name="TimeSeriesProfile1",
        start_date=datetime(2019, 1, 1),
        timestep_in_seconds=3600,
        values=[row[1] for row in profile_data_list1],
        profile_type=esdl.ProfileTypeEnum.OUTPUT,
        quantity_and_unit_type=qau_power,
    )
    electricity_demand2_port3.profile.append(time_series_profile)

    date_time_profile = create_date_time_profile(
        es=es,
        name="DateTimeProfile1",
        datetime_and_values=profile_data_list1,
        profile_type=esdl.ProfileTypeEnum.OUTPUT,
        quantity_and_unit_type=qau_power,
    )
    electricity_demand2_port3.profile.append(date_time_profile)

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

    yield {
        "dtp_postgres1": dtp_postgres1,
        "dtp_postgres2": dtp_postgres2,
        "dtp_influx1": dtp_influx1,
        "dtp_influx2": dtp_influx2,
        "time_series_profile": time_series_profile,
        "date_time_profile": date_time_profile,
        "profile_header1": profile_header1,
        "profile_header2": profile_header2,
        "profile_data_list1": profile_data_list1,
        "profile_data_list2": profile_data_list2,
    }

    close_db_connections()


def _assert_first_three_values(data, expected_values):
    assert len(data) >= 3
    actual_values = [data[i][1] for i in range(3)]
    assert actual_values == pytest.approx(expected_values)


def _assert_first_three_datetimes(data, expected_datetimes):
    assert len(data) >= 3
    actual_datetimes = [data[i][0] for i in range(3)]
    assert actual_datetimes == expected_datetimes


def test_postgresql_datatable_profile_column1(profile_fixture):
    data, header = load_profile_data_and_header(profile_fixture["dtp_postgres1"])
    assert header == profile_fixture["profile_header1"]
    _assert_first_three_datetimes(
        data,
        [
            datetime(2019, 1, 1, 0, 0),
            datetime(2019, 1, 1, 1, 0),
            datetime(2019, 1, 1, 2, 0),
        ],
    )
    _assert_first_three_values(data, [46.0, 24.0, 0.6])


def test_postgresql_datatable_profile_column2(profile_fixture):
    data, header = load_profile_data_and_header(profile_fixture["dtp_postgres2"])
    assert header == profile_fixture["profile_header2"]
    _assert_first_three_datetimes(
        data,
        [
            datetime(2019, 1, 1, 0, 0),
            datetime(2019, 1, 1, 1, 0),
            datetime(2019, 1, 1, 2, 0),
        ],
    )
    _assert_first_three_values(data, [45.0, 900.0, 5.6])


def test_influxdb_datatable_profile_column1(profile_fixture):
    data, header = load_profile_data_and_header(profile_fixture["dtp_influx1"])
    assert header == profile_fixture["profile_header1"]
    _assert_first_three_datetimes(
        data,
        [row[0] for row in profile_fixture["profile_data_list1"][0:3]],
    )
    _assert_first_three_values(data, [23.0, 12.0, 0.3])


def test_influxdb_datatable_profile_column2(profile_fixture):
    data, header = load_profile_data_and_header(profile_fixture["dtp_influx2"])
    assert header == profile_fixture["profile_header2"]
    _assert_first_three_datetimes(
        data,
        [row[0] for row in profile_fixture["profile_data_list2"][0:3]],
    )
    _assert_first_three_values(data, [45.0, 900.0, 5.6])


def test_time_series_profile(profile_fixture):
    data, header = load_profile_data_and_header(profile_fixture["time_series_profile"])
    assert header[0] == "datetime"
    _assert_first_three_datetimes(
        data,
        [row[0] for row in profile_fixture["profile_data_list1"][0:3]],
    )
    _assert_first_three_values(data, [23.0, 12.0, 0.3])


def test_date_time_profile(profile_fixture):
    data, header = load_profile_data_and_header(profile_fixture["date_time_profile"])
    assert header == ["datetime", "DateTimeProfile1"]
    _assert_first_three_datetimes(
        data,
        [row[0] for row in profile_fixture["profile_data_list1"][0:3]],
    )
    _assert_first_three_values(data, [23.0, 12.0, 0.3])
