from pyecore.ecore import EEnum

import esdl
from esdl import DatabaseConfiguration
from esdl.profiles.datatableprofilemanager import DataTableProfileManager, Credentials

if __name__ == '__main__':

    # create a new datatable profile with data from e.g. excel or csv
    dtp = esdl.DataTableProfile(name="test profile", id="test")
    dtp.configuration = esdl.FileConfiguration(uri="test_profile.csv", type=esdl.FileTypeEnum.CSV)
    dtpman = DataTableProfileManager.load(dtp)


    print(dtpman.profile_header)
    print(dtpman.profile_data_list)
    columnName = "column2"
    print(dtpman.get_esdl_timeseries_profile(columnName).values)


    # store this in Postgres by creating a new configuration
    dtp.configuration = esdl.DatabaseConfiguration(type=esdl.DatabaseTypeEnum.POSTGRESQL,
                                                    id="my_database",
                                                    database="datatableprofile2",
                                                    host="localhost")
    cred = Credentials.create_dict("my_database", "drive", "password")


    # save data in database configured in dtp.configuration
    dtpman.save(cred)



    dtp2 = esdl.DataTableProfile(name="test profile", id="test",
                                 columnName=columnName,
                                 tableName="test_profile",
                                 schema="public")
    dtp2.configuration = esdl.DatabaseConfiguration(type=esdl.DatabaseTypeEnum.POSTGRESQL,
                                                   id="my_database",
                                                   database="datatableprofile2",
                                                   host="localhost")
    dtpm2 = DataTableProfileManager(dtp2)
    dtpm2.add_credential(Credentials.create_dict("my_database", "drive", "password"))
    dtpm2.load_database_configuration()
    print([ value[1] for value in dtpm2.profile_data_list ])



    # load an existing datatable profile in postgres from an ESDL
    dtp = esdl.DataTableProfile(name="test profile", id="test", tableName="csv_data_table")
    dtp.configuration = esdl.FileConfiguration(uri="test_profile.csv", type=esdl.FileTypeEnum.CSV)
    dtpman = DataTableProfileManager.load(dtp)
    print(dtpman.profile_header)
    nw_table_config = DatabaseConfiguration(name="nw_table", id="postgres_db", database="datatableprofile",
                                            type=esdl.DatabaseTypeEnum.POSTGRESQL,
                                            host="localhost")
    dtp.configuration = nw_table_config
    dtp.schema = "essim_run_20250804"
    dtpman.add_credential(Credentials.create_dict("postgres_db", "drive", "password"))
    dtpman.save()

    # save this to Excel or CSV

