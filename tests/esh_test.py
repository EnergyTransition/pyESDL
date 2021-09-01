#  This work is based on original code developed and copyrighted by TNO 2020.
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
from esdl.esdl_handler import EnergySystemHandler
from esdl import esdl
from pprint import pprint

class TestPyESDL(unittest.TestCase):

    def test_print_version(self):
        print('pyESDL version', EnergySystemHandler.version())

    def test_esh(self):
        esh = EnergySystemHandler()
        es = esh.create_empty_energy_system(name="Nice", es_description="Description", inst_title="Instance0", area_title='Area1')
        print(es)
        copy = es.deepcopy()
        pprint(copy)
        pprint(esh.attr_to_dict(copy))

    def test_error_attribute(self):
        esh = EnergySystemHandler()
        # this should print a warning:
        # Attribute 'trype' does not exists for type WindTurbine and is ignored (asset line 5).
        print("Expect warning: Attribute 'trype' does not exists for type WindTurbine and is ignored (asset line 5).")
        esh.load_file('test_attr_error.esdl')




    def test_example1(self):
        esh = EnergySystemHandler()
        es = esh.create_empty_energy_system(name="ES1", es_description='Nice Energy System',
                                            inst_title='instance 1', area_title="Area 51")
        print(es)
        esh.save(filename="test.esdl")

    def test_example2(self):
        esh = EnergySystemHandler()
        # load an ESDL file and use type hinting to help the IDE to do auto completion
        es = esh.load_file('test.esdl')
        print(es)
        # Create a WindTurbine
        wind_turbine = esdl.WindTurbine(name='WindTurbine at coast', rotorDiameter=50.0, height=100.0,
                                        type=esdl.WindTurbineTypeEnum.WIND_ON_COAST)

        # print the wind turbines properties in ESDL as a dict
        pprint(esh.attr_to_dict(wind_turbine))

        # Get the area where this windturbine should be added
        area51: esdl.Area = es.instance[0].area
        # add the WindTurbine to the area
        area51.asset.append(wind_turbine)
        # save the file
        esh.save()

        # Give the WindTurbine a location on the map
        location = esdl.Point(lat=52.6030475337285, lon=4.729614257812501)
        wind_turbine.geometry = location

        esh.save()
        # Convert the Energy System to an XML string and print it
        xml_string = esh.to_string()
        print(xml_string)
