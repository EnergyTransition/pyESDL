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
from esdl.esdl_handler import EnergySystemHandler


class TestVersionMigration(unittest.TestCase):

    def test_parsing_esdl(self):
        esh = EnergySystemHandler()
        esh.load_file("tests/test_esdl_with_deprecated_attribute.esdl")

        es = esh.get_energy_system()
        print(es)

        area = es.instance[0].area
        asset = area.asset[0]
        if isinstance(asset, esdl.GeothermalSource):
            print(asset.eClass.name)
            self.assertEqual(asset.eClass.name, "GeothermalSource")
            print(asset.maximumFlowRate)
            self.assertEqual(asset.maximumFlowRate, 3.0)
            print(asset.port[0].profile[0].profileQuantityAndUnit.multiplier)
            self.assertEqual(asset.port[0].profile[0].profileQuantityAndUnit.multiplier, esdl.MultiplierEnum.TERA)
