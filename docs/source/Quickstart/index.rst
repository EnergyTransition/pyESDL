Quickstart
==========

After installing pyESDL, you can immediately start working in Python to read and write ESDL files.
Below a few examples are given to show how to work with pyESDL.

The ``EnergySystemHandler`` class is created to handle most use cases with ESDL. It
allows you to load an ESDL file, write ESDL files to disk and manipulate ESDL object when
loaded into Python.

To gain more experience with pyESDL, please have a look at the :doc:`/Tutorials/index` section

Example 1 - Creating an ESDL-file and saving it to disk
-------------------------------------------------------
.. code-block:: python

  from esdl.esdl_handler import EnergySystemHandler
  from esdl import esdl
  esh = EnergySystemHandler()
  es = esh.create_empty_energy_system(name="ES1", es_description='Nice Energy System',
                                   inst_title='instance 1', area_title="Area 51")
  print(es)
  esh.save(filename="test.esdl")


Example 2 - Loading an ESDL file and adding a WindTurbine to an area
--------------------------------------------------------------------

.. code-block:: python

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


Converting ESDL units
---------------------

Different energy transition models use different units of measure. pyESDL contains some
convenient methods to convert one unit to another. In this case it uses predefined
units in the ``esdl.units.conversion`` package, but you can create any unit using the
``QuantityAndUnitType`` class.

The following code converts 5 MWh to Joules:

.. code-block:: python

  from esdl.units.conversion import convert_to_unit, ENERGY_IN_J, ENERGY_IN_MWh

  converted = convert_to_unit(5, ENERGY_IN_MWh, ENERGY_IN_J)
  18E9 == converted
  >> True
