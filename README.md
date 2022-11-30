# pyESDL

pyESDL is a library for using ESDL in python programs. ESDL stands for Energy System Description
Language and is created to support developers creating, parsing, generating ESDL-files with the 
goal to create interoperable energy system transition tooling.

This package contains all the ESDL classes of the ESDL language and an `EnergySystemHandler`
that helps the developer to read and write ESDL-files.

More information about ESDL can be found at:
1. [ESDL gitbook documentation](https://energytransition.gitbook.io/esdl/) with a general introduction,
   example applications and some code samples.
2. [ESDL Model Reference documentation](https://energytransition.github.io/) that describes all the 
   classes and definitions in detail using a clickable UML diagram.

## Installing
Use the following command to install the pyESDL python module from the PyPi registry:

`pip install pyESDL`


## Usage

### Example 1 - Creating an ESDL-file and saving it to disk
```python
from esdl.esdl_handler import EnergySystemHandler
from esdl import esdl
esh = EnergySystemHandler()
es = esh.create_empty_energy_system(name="ES1", es_description='Nice Energy System',
                                   inst_title='instance 1', area_title="Area 51")
print(es)
esh.save(filename="test.esdl")
```

### Example 2 - Loading an ESDL file and adding a WindTurbine to an area
```python
from esdl.esdl_handler import EnergySystemHandler
from esdl import esdl
from pprint import pprint

esh = EnergySystemHandler()
# load an ESDL file and use type hinting to help the IDE to do auto completion
es: esdl.EnergySystem = esh.load_file('test.esdl')
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
```

## Changes
### Version 22.11
- Add support for Energy Data Repository files (*.edd)
- Add supoprt for linking to external files (e.g. stored in the EDR) using `get_external_reference(url, object_id)`
- Add function to instantiate a class by its class name (`instantiate_esdltype(className)`) 

### Version 22.10
- Update to ESDL v2210

### Version 21.9.0
- Fix pyecore 0.12.1 dependency issue

### Version 21.7.1
- Add support for ESDL release 21.7 (with BufferDistance, ATES)

#### Version 21.6.2
- Fix issue with version definition, making the EnergySystemHandler unusable.
- Add get_all_instances_of_type() to EnergySystemHandler to retrieve all the instances of a certain type in an EnergySystem.
  
  E.g. ```esh.get_all_instances_of_type(esdl.GenericProfile)``` will give you all the profiles defined in the EnergySystem.

#### Version 21.6.1
- Add support for InputOutputRelation 


## Releasing
The release process is as follows:
1. Do a `git tag` with the new version number
2. Do `python setup.py sdist bdist_wheel` to create the tarball and wheel in the `dist` folder
3. upload to PyPi: `python3 -m twine upload --repository pyESDL dist/*`

