from pyecore.ecore import EEnum

import esdl
from esdl import DatabaseConfiguration
from esdl.profiles.data_configurations.postgresql import DEBUG_SQL
from esdl.profiles.datatableprofilemanager import DataTableProfileManager, Credentials
from esdl.support_functions import deepcopy
from esdl.units.conversion import POWER_IN_kW, POWER_IN_MW, POWER_IN_W, ENERGY_IN_MJ, ENERGY_IN_GJ
from esdl.units.parser import qau_to_string



def read_data_from_postgres():
    dtp = esdl.DataTableProfile(name="standard_electricity_profiles", id="test",
                                tableName="standard_electricity_profiles_2023",
                                datetimeColumnName='datetime_UTC',
                                schema="energy_profiles")
    nw_table_config = DatabaseConfiguration(name="postgres", id="postgres_db", database="datatableprofile",
                                            type=esdl.DatabaseTypeEnum.POSTGRESQL,
                                            host="localhost")
    dtp.configuration = nw_table_config
    dtpm = DataTableProfileManager.load(dtp, Credentials.create_dict("postgres_db", "drive", "password"))
    print(dtpm.profile_header)
    print(dtpm.profile_data_list[0])
    print(dtpm.get_esdl_timeseries_profile("E1A"))
    esdl_profiles = dtpm.get_data_table_profile()
    print(esdl_profiles)
    esdl_profile = dtpm.get_data_table_profile("E2A")
    print(esdl_profiles.name, esdl_profile.columnName, qau_to_string(esdl_profile.profileQuantityAndUnit), esdl_profile.tableName)


def write_data_to_postgres():
    # load data from CSV into postgres from an ESDL DataTable profile definition
    dtp = esdl.DataTableProfile(name="standard_electricity_profiles", id="test",
                                tableName="standard_electricity_profiles_2023",
                                datetimeColumnName='datetime_UTC')
    dtp.profileQuantityAndUnit = ENERGY_IN_GJ.deepcopy()
    dtp.configuration = esdl.FileConfiguration(uri="essim_data/standard_electricity_profiles_2023.csv", type=esdl.FileTypeEnum.CSV)

    # read CSV
    dtpman = DataTableProfileManager.load(dtp)
    print(dtpman.profile_header)

    # configure to write to Postgres
    nw_table_config = DatabaseConfiguration(name="postgres", id="postgres_db", database="datatableprofile",
                                            type=esdl.DatabaseTypeEnum.POSTGRESQL,
                                            host="localhost")
    dtp.schema = "energy_profiles"
    dtp.configuration = nw_table_config
    dtpman.add_credential(Credentials.create_dict("postgres_db", "drive", "password"))
    dtpman.save()


if __name__ == '__main__':
    #esdl.profiles.data_configurations.postgresql.DEBUG_SQL = True
    #write_data_to_postgres()
    read_data_from_postgres()

