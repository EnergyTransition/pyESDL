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

import esdl
from esdl.edr.client import EDRClient
# from esdl.profiles.influxdbprofilemanager import InfluxDBProfileManager


class TestEDRClient(unittest.TestCase):

    def test_retrieve_asset_list(self):
        edr_client = EDRClient()

        energy_asset_list = edr_client.get_objects_list("EnergyAsset")
        self.assertTrue(len(energy_asset_list) > 0, "No EnergyAssets found in EDR")

        first_asset = energy_asset_list[0]
        self.assertTrue(
            hasattr(first_asset, "id") and first_asset.id is not None,
            "No ID found for first EnergyAsset"
        )
        self.assertTrue(
            hasattr(first_asset, "title") and first_asset.title is not None,
            "No title found for first EnergyAsset"
        )
        self.assertTrue(
            hasattr(first_asset, "description"),
            "No description found for first EnergyAsset"
        )
        self.assertTrue(
            hasattr(first_asset, "esdl_type") and first_asset.esdl_type is not None,
            "No esdl_type found for first EnergyAsset"
        )

        profiles_list = edr_client.get_objects_list("InfluxDBProfile")
        self.assertTrue(len(profiles_list) > 0, "No profiles found in EDR")
        carriers_list = edr_client.get_objects_list("Carriers")
        self.assertTrue(len(carriers_list) > 0, "No Carrier lists found in EDR")
        sectors_list = edr_client.get_objects_list("Sectors")
        self.assertTrue(len(sectors_list) > 0, "No Sector lists found in EDR")

    def test_retrieve_asset(self):
        edr_client = EDRClient()
        wind_turbine_list = edr_client.get_objects_list("WindTurbine")
        self.assertTrue(len(wind_turbine_list) > 0, "No WindTurbines found in EDR")

        for wt_info in wind_turbine_list:
            wt = edr_client.get_object_esdl(wt_info.id)

            self.assertTrue(isinstance(wt, esdl.WindTurbine))

    # def test_retrieve_profile(self):
    #     edr_client = EDRClient()
    #     profiles_list = edr_client.get_objects_list("InfluxDBProfile")
    #     self.assertTrue(len(profiles_list) > 0, "No InfluxDBProfiles found in EDR")
    #
    #     for profile_info in profiles_list:
    #         influxdb_profile = edr_client.get_object_esdl(profile_info.id)
    #         print(influxdb_profile.name)
    #
    #         prof_mngr = InfluxDBProfileManager.create_esdl_influxdb_profile_manager(
    #             esdl_profile=influxdb_profile,
    #             use_ssl=True,
    #             verify_ssl=True,
    #         )
    #
    #         for i in range(0, 10):
    #             print(prof_mngr.profile_data_list[i])
