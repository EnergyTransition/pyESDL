import unittest
from esdl.esdl_handler import EnergySystemHandler

class TestPyESDL(unittest.TestCase):
    def test_esh(self):
        esh = EnergySystemHandler()
        es = esh.create_empty_energy_system(name="Nice", es_description="Description", inst_title="Instance0", area_title='Area1')
        print(es)
