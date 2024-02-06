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
import copy
import unittest
import uuid

from pyecore.ecore import EObject
from pyecore.resources import ResourceSet, URI
from esdl.resources.xmi import XMIResource

from esdl.esdl_handler import EnergySystemHandler, StringURI
from esdl import esdl, EnergySystemInformation, Carriers
from pprint import pprint

from esdl.resources.xmlresource import XMLResource


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
        try:
            esh.load_file('test_attr_error.esdl')
        except FileNotFoundError as e:  # when running from command line
            esh.load_file('tests/test_attr_error.esdl')
        self.assertEqual(["Attribute 'trype' does not exists for type WindTurbine and is ignored (asset line 5)."], esh.resource.get_parse_information())

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

    # def test_external_reference(self):
    #     import edd # make sure edd model is loaded.
    #     """Load a remote carrier from the EDR and add it to our energy system"""
    #     esh = EnergySystemHandler()
    #     es = esh.create_empty_energy_system(name="External reference Carrier test")
    #     es.energySystemInformation = esdl.EnergySystemInformation()
    #     es.energySystemInformation.carriers = esdl.Carriers()
    #     gasoline_carrier: EObject = esh.get_external_reference("https://drive.esdl.hesi.energy/store/edr/Public/Key%20figures/Emissiefactoren%20energiedragers%202017.edd",
    #                                                   object_id='c871e7db-f55c-4cee-9a22-12bebb523a54')
    #     gc_resource:XMLResource = gasoline_carrier.eResource
    #     print('# external defined carriers', len(gc_resource.contents[0].esdl.carrier))
    #     print('Uri', gasoline_carrier.eResource.uri.plain)
    #     print('Gasoline carrier', gasoline_carrier)
    #     # When adding an external specified carrier to a containment relation (such as Carriers),
    #     # the reference is copied into the file and removed
    #     # from the external reference. That's why the #carriers count is reduced by 1 after adding.
    #     # If you don't want it to be removed, deepcopy the returned value using eobject.deepcopy()
    #     es.energySystemInformation.carriers.carrier.append(gasoline_carrier)
    #     print(esh.to_string())
    #     print('Uri after', gasoline_carrier.eResource.uri.plain)
    #     print('# external defined carriers after adding it to a containment relation', len(gc_resource.contents[0].esdl.carrier))
    #     print('RSet: ', esh.rset.resources)
    #
    #     p = esdl.PowerPlant(name="PowerPlant")
    #     es.instance[0].area.asset.append(p)
    #     pp_ip = esdl.InPort(name="InPort")
    #     p.port.append(pp_ip)
    #     lng = esh.get_external_reference("https://drive.esdl.hesi.energy/store/edr/Public/Key%20figures/Emissiefactoren%20energiedragers%202017.edd",
    #                                                   object_id='72a373a8-c174-463c-ab39-fb33f612c066')
    #     # When adding an external specified carrier to a reference, it will create a href link
    #     pp_ip.carrier = lng
    #     print(esh.to_string())

    def test_deepcopy_with_context(self):
        esh = EnergySystemHandler()
        es = esh.load_file('tests/Test_ES_deepcopy.esdl')
        gen_cons = esh.get_by_id('87d5b022-e509-4620-9d99-5f67eaf91848')
        cons_copy = gen_cons.deepcopy()
        es2 = esh.create_empty_energy_system(name="target ES")
        es2.energySystemInformation = EnergySystemInformation(id=str(uuid.uuid4()))
        es2.energySystemInformation.carriers = Carriers(id=str(uuid.uuid4()))
        es2.energySystemInformation.carriers.carrier.append(es.energySystemInformation.carriers.carrier[0].deepcopy())
        print(es2.energySystemInformation.carriers.carrier)
        esh.update_uuid_dict(es2)
        # use target energy system, to find references
        print("copy.deepcopy(target_es=es2)")
        cons_copy = gen_cons.deepcopy(target_es=es2)
        es2.instance[0].area.asset.append(cons_copy)
        print(esh.to_string())

        print("copy.deepcopy()")
        copy2 = copy.deepcopy(gen_cons)

        print("IDs in the two energysystems:")
        print("---------------")
        for item in es.eAllContents():
            if hasattr(item, 'id'):
                print(item.eClass.__name__, item.id)
        print("---------------")
        for item in es2.eAllContents():
            if hasattr(item, 'id'):
                print(item.eClass.__name__, item.id)

    def test_deepcopy_simple(self):
        import pyecore
        print('PyEcore version:', pyecore.__version__)
        esh = EnergySystemHandler()
        es = esh.load_file('tests/Test_ES_deepcopy.esdl')
        gen_cons = esh.get_by_id('87d5b022-e509-4620-9d99-5f67eaf91848')
        cons_copy = gen_cons.deepcopy()
        for item in gen_cons.eAllContents():
            if hasattr(item, 'id'):
                print(item.eClass.__name__, item.id)
        print("---------------")
        for item in cons_copy.eAllContents():
            if hasattr(item, 'id'):
                print(item.eClass.__name__, item.id)

        #rs = ResourceSet()
        #u = StringURI("string.json")
        #r = rs.create_resource(u)
        #r.append(cons_copy)
        #r.save(u)
        #import json
        #print(pprint(json.loads(u.getvalue())))

    def test_deepcopy_windturbine_pyecore014_issue(self):
        import pyecore
        print('PyEcore version:', pyecore.__version__)
        esh = EnergySystemHandler()
        wt:esdl.WindTurbine = esh.load_file('tests/windturbine_pyecore014_issue_values.esdl')
        #rset = ResourceSet()
        #rset.resource_factory['esdl'] = lambda uri: XMIResource(uri)
        #rset.resource_factory['xmlesdl'] = lambda uri: XMLResource(uri)
        #resource = rset.get_resource(URI('tests/windturbine_pyecore014_issue_values.esdl'))
        # At this point, the model instance is loaded!
        #wt = resource.contents[0]
        table = wt.powerCurveTable
        print(table.row[0].value)
        print(table.row[1].value)
        uri = StringURI('to_string.esdl')
        #resource = rset.create_resource(uri)
        #resource.append(wt)
        #resource.save(uri)
        # return the string
        #print( uri.getvalue())
        string = esh.to_string()
        print(string)


