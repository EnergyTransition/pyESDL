import unittest

from esdl import esdl
from esdl.ecore_documentation import EcoreDocumentation
from esdl.units.conversion import get_attribute_unit, convert_to_unit, POWER_IN_W, POWER_IN_GW, ENERGY_IN_J, \
    ENERGY_IN_MWh


class ESDLUnitTest(unittest.TestCase):

    def test_get_version(self):
        doc = EcoreDocumentation()  # loads esdl ecore from github
        version = doc.get_esdl_version()
        self.assertEqual(version[0], "v")

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


if __name__ == '__main__':
    unittest.main()
