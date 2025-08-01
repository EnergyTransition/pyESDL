from pyecore.ecore import EEnum

import esdl
from esdl.profiles.datatableprofilemanager import DataTableProfileManager, Credentials

if __name__ == '__main__':

    # create a new datatable profile with data from e.g. excel or csv
    dtp = esdl.DataTableProfile(name="test profile", id="test", tableName=None)
    dtp.configuration = esdl.FileConfiguration(uri="test_profile.csv", type=esdl.FileTypeEnum.CSV)
    dtpman = DataTableProfileManager.create(dtp)
    print(dtpman.profile_header)
    print(dtpman.profile_data_list)
    columnName = "column2"
    print(dtpman.get_esdl_timeseries_profile(columnName).values)
    # store this in Postgres and Excel and influxdb

    dtp2 = esdl.DataTableProfile(name="test profile", id="test",
                                 columnName=columnName,
                                 tableName="test_profile",
                                 schema="public")
    dtp2.configuration = esdl.DatabaseConfiguration(type=esdl.DatabaseTypeEnum.POSTGRESQL,
                                                    id="my_database",
                                                    database="datatableprofile",
                                                    host="localhost")
    cred = Credentials.create_dict("my_database", "drive", "password")

    dtpm = DataTableProfileManager.create(dtp2, cred)
    print(dtpm.profile_header)
    print(dtpm.profile_data_list)
    print(dtpm.get_esdl_timeseries_profile(columnName).values)

    # load an existing datatable profile in postgres from an ESDL
    # save this to Excel or CSV

