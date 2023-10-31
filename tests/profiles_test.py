#  This work is based on original code developed and copyrighted by TNO 2023.
#  Subsequent contributions are licensed to you by the developers of such code and are
#  made available to the Project under one or several contributor license agreements.
#
#  This work is licensed to you under the Apache License, Version 2.0.
#  You may obtain a copy of the license at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Contributors:
#      TNO         - Initial implementation
#  Manager:
#      TNO

import unittest
from datetime import datetime
from uuid import uuid4

from pyecore.utils import alias

from esdl import esdl
from esdl.esdl_handler import StringURI
from esdl.profiles.excelprofilemanager import ExcelProfileManager
from esdl.profiles.influxdbprofilemanager import InfluxDBProfileManager, ConnectionSettings
from esdl.profiles.profilemanager import ProfileManager

from pyecore.resources import ResourceSet, URI


def get_esdl_string(object):
    rset = ResourceSet()
    resource = rset.create_resource(URI("test.esdl"))
    resource.append(object)

    uri = StringURI('to_string.esdl')
    resource.save(uri)
    return uri.getvalue()


class ESDLUnitTest(unittest.TestCase):

    def test_load_csv_profile_data(self):
        print("Load profile data from a CSV...")
        profile = ProfileManager()
        profile.load_csv("test_profile.csv")
        self.assertEqual(profile.num_profile_items, 4)

        print("Generate an esdl.TimeSeriesProfile...")
        ts_prof = profile.get_esdl_timeseries_profile('column1')
        print(get_esdl_string(ts_prof))
        self.assertTrue(isinstance(ts_prof, esdl.TimeSeriesProfile))

        print("Generate an esdl.DateTimeProfile...")
        dt_prof = profile.get_esdl_datetime_profile('column2')
        print(get_esdl_string(dt_prof))
        self.assertTrue(isinstance(dt_prof, esdl.DateTimeProfile))
        self.assertEqual(dt_prof.element[0].value, 45)

    def test_influxdbprofile(self):
        profile = ProfileManager()
        profile.load_csv("test_profile.csv")

        conn_settings = ConnectionSettings(
            host="localhost",
            port=8086,
            username="pyesdl",
            password="pyesdl",
            database="pyesdl_test",
            ssl=False,
            verify_ssl=False
        )

        influxdb_profile_manager = InfluxDBProfileManager(conn_settings, profile)
        try:
            influxdb_profile_manager.influxdb_client.drop_measurement("test")
        except:
            pass

        print("save loaded CSV data into influxdb")
        profs = influxdb_profile_manager.save_influxdb(measurement="test", field_names=influxdb_profile_manager.profile_header[1:])
        esdl_infl_prof = profs[0]
        self.assertTrue(isinstance(esdl_infl_prof, esdl.InfluxDBProfile))

        print("instantiate InfluxDBProfileManager using esdl.InfluxDBProfile and read data")
        prof2 = InfluxDBProfileManager.create_esdl_influxdb_profile_manager(esdl_infl_prof)

        print("save ESDL profile data to excel")
        excel_prof = ExcelProfileManager(source_profile=prof2)
        excel_prof.save_excel("output.xlsx")

        print("read data from Excel")
        excel_prof2 = ExcelProfileManager()
        excel_prof2.load_excel("output.xlsx")

        print("Generate esdl.TimeSeriesProfile from the data")
        dt_prof = excel_prof2.get_esdl_datetime_profile('column1')
        print(get_esdl_string(dt_prof))

        print("Instantiate a new profile manager with the esdl.TimeSeriesProfile")
        prof2 = ProfileManager()
        prof2.parse_esdl(dt_prof)

        self.assertEqual(prof2.profile_data_list[0][1], 23)
        self.assertEqual(prof2.profile_data_list[1][1], 12)
        self.assertEqual(prof2.profile_data_list[2][1], 0.3)
        self.assertEqual(prof2.profile_data_list[3][1], 78)
        self.assertEqual(prof2.num_profile_items, 4)

        print("Reading InfluxDB profile from test...")
        prof3 = InfluxDBProfileManager(conn_settings)
        prof3.load_influxdb("test", ['column1', 'column2'])
        ts_prof = prof3.get_esdl_timeseries_profile('column2')
        print(get_esdl_string(ts_prof))

        self.assertEqual(ts_prof.values[0], 45)
        self.assertEqual(ts_prof.values[1], 900)
        self.assertEqual(ts_prof.values[2], 5.6)
        self.assertEqual(ts_prof.values[3], 1.2)
        self.assertEqual(len(ts_prof.values), 4)
