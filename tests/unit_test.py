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

from esdl import esdl
from esdl.ecore_documentation import EcoreDocumentation
from esdl.units.conversion import get_attribute_unit, convert_to_unit, POWER_IN_W, POWER_IN_GW, ENERGY_IN_J, \
    ENERGY_IN_MWh
from esdl.units.parser import build_qau_from_unit_string, qau_to_string


class ESDLUnitTest(unittest.TestCase):

    def test_get_version(self):
        doc = EcoreDocumentation()  # loads esdl ecore from github
        version = doc.get_esdl_version()
        print('ESDL version', version)
        self.assertEqual(version[0], "v")
    def test_pyESDL_version(self):
        from esdl import _version
        version = _version.get_versions()['version']
        if '+' in version:
            version = version.split('+')[0]
        print('pyESDL version', version)

    def test_attribute_unit(self):
        unit = get_attribute_unit("PowerPlant", "power")
        self.assertEqual(unit, "W")

    def test_attribute_unit2(self):
        esdl_class = esdl.Producer  # note, without ()
        unit = get_attribute_unit(esdl_class, "power")
        self.assertEqual(unit, "W")

        esdl_object = esdl.Battery()
        unit = get_attribute_unit(esdl_object, "capacity")
        self.assertEqual(unit, "J")

    def test_convert_unit(self):
        converted = convert_to_unit(5, POWER_IN_GW, POWER_IN_W)
        self.assertEqual(5E9, converted)

        converted = convert_to_unit(5, ENERGY_IN_MWh, ENERGY_IN_J)
        self.assertEqual(18E9, converted)

    def test_unit_parser(self):
        unit = build_qau_from_unit_string("TWh")
        self.assertEqual(unit.multiplier, esdl.MultiplierEnum.TERA)

    def test_convert_tonne_unit(self):
        tonne_unit = build_qau_from_unit_string("t", "weight")
        kg_unit = build_qau_from_unit_string("kg", "weight")
        converted = convert_to_unit(1, tonne_unit, kg_unit)
        self.assertEqual(converted, 1E3) # 1 TONNE is 1000 KG

        megaton_unit = build_qau_from_unit_string("Mt", "weight")
        converted = convert_to_unit(1, kg_unit, megaton_unit)
        self.assertEqual(converted, 1E-9) # 1 kg = 1E-9 Mt
        milliton_unit = build_qau_from_unit_string("mt", "weightt")
        print(qau_to_string(milliton_unit))
        converted = convert_to_unit(converted, megaton_unit, milliton_unit)
        self.assertEqual(converted, 1)  # 1E-9 Mt = 1 mt (milli tonne)




if __name__ == '__main__':
    unittest.main()
