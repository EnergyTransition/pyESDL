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

import json

import esdl
from esdl.esdl_handler import EnergySystemHandler
from esdl.version_migrations.mapping import MappingList, RenameAttribute, RenameClass, RemoveReassignEnumValue
from esdl.version_migrations.migration import VersionMigration


class TestVersionMigration(unittest.TestCase):

    def test_create_version_migrations_mappings_file(self):

        mappings = [
            {
                "id": "1",
                "type": "RENAME_ATTRIBUTE",
                "class_name": "GeothermalSource",
                "attribute_name": "flowRate",
                "attribute_new_name": "maximumFlowRate"
            },
            {
                "id": "1b",             # To test the mechanism without changing ESDL
                "type": "RENAME_ATTRIBUTE",
                "class_name": "GeothermalSource",
                "attribute_name": "maximumFlowRate",
                "attribute_new_name": "flowRate"
            },
            {
                "id": "2",
                "type": "RENAME_CLASS",
                "class_name": "GeothermalSourceOld",
                "class_new_name": "GeothermalSource",
            },
            # {
            #     "id": "3",
            #     "type": "REMOVE_CLASS_AND_REASSIGN",
            #     "class_name": "PVPanel",
            #     "class_to_reassign": "PVInstallation"
            # },
            {
                "id": "4",
                "type": "REMOVE_AND_REPLACE_ENUM_VALUE",
                "enum_name": "MultiplierEnum",
                "enum_value_name": "TERRA",
                "enum_value_to_reassign": "TERA"
            }
        ]

        with open("version_migration_mappings.json", "w") as file:
            json.dump(mappings, file)

    def test_parsing_esdl(self):
        esh = EnergySystemHandler()
        esh.load_file("test_esdl_with_deprecated_attribute.esdl")

        es = esh.get_energy_system()
        print(es)

        area = es.instance[0].area
        asset = area.asset[0]
        if isinstance(asset, esdl.GeothermalSource):
            print(asset.eClass.name)
            self.assertEqual(asset.eClass.name, "GeothermalSource")
            print(asset.flowRate)
            self.assertEqual(asset.flowRate, 3.0)
            print(asset.port[0].profile[0].profileQuantityAndUnit.multiplier)
            self.assertEqual(asset.port[0].profile[0].profileQuantityAndUnit.multiplier, esdl.MultiplierEnum.TERA)
