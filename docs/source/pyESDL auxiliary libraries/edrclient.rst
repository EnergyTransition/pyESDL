EDRClient functionality
=======================

Very simple implementation, might be changed/improved in the near future

Examples
--------

Retrieve a list of WindTurbines from the EDR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following code

.. code-block:: python

  edr_client = EDRClient()
  wind_turbine_list = edr_client.get_objects_list("WindTurbine")
  print(wind_turbine_list)

results in

.. code-block::

  [
    EDRInfo(id='/edr/Public/Assets/Factsheets-experimental/2050/Wind offshore.edd', title='Wind offshore', description='...', esdl_type='WindTurbine'),
    EDRInfo(id='/edr/Public/Assets/Factsheets-experimental/2030/Wind onshore.edd', title='Wind onshore', description='...', esdl_type='WindTurbine'),
    EDRInfo(id='/edr/Public/Assets/ETM/ETM WindTurbine land.edd', title='Wind turbine onshore', description=None, esdl_type='WindTurbine'),
    EDRInfo(id='/edr/Public/Assets/Factsheets-experimental/2020/Wind onshore.edd', title='Wind onshore', description='...', esdl_type='WindTurbine'),
    EDRInfo(id='/edr/Public/Assets/ETM/ETM WindTurbine offshore.edd', title='Wind turbine offshore', description=None, esdl_type='WindTurbine'),
    EDRInfo(id='/edr/Public/Assets/ETM/ETM WindTurbine op Land.edd', title='ETM WindTurbine on Land', description='...', esdl_type='WindTurbine'),
    EDRInfo(id='/edr/Public/Assets/Factsheets-experimental/2020/Wind offshore.edd', title='Wind offshore', description='...', esdl_type='WindTurbine'),
    EDRInfo(id='/edr/Public/Assets/Energie & Ruimte/Windturbine met buffer distances.edd', title='Windturbine met buffer distances', description='...', esdl_type='WindTurbine'),
    EDRInfo(id='/edr/Public/Assets/Factsheets-experimental/2030/Wind offshore.edd', title='Wind offshore', description='...', esdl_type='WindTurbine'),
    EDRInfo(id='/edr/Public/Assets/North Sea Energy/Wind turbines/20 MW Wind turbine at sea.edd', title='20 MW Wind turbine at sea', description=None, esdl_type='WindTurbine'),
    EDRInfo(id='/edr/Public/Assets/North Sea Energy/Wind turbines/15 MW Wind turbine at sea .edd', title='15 MW Wind turbine at sea ', description=None, esdl_type='WindTurbine'),
    EDRInfo(id='/edr/Public/Assets/North Sea Energy/Wind turbines/18 MW Wind turbine at sea.edd', title='18 MW Wind turbine at sea', description=None, esdl_type='WindTurbine')
  ]

Retrieve a specific WindTurbine from the EDR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following code

.. code-block:: python

  edr_client = EDRClient()
  wt = edr_client.get_object_esdl("/edr/Public/Assets/North Sea Energy/Wind turbines/20 MW Wind turbine at sea.edd")
  print(wt)

results in

.. code-block::

  <esdl.esdl.WindTurbine object at 0x00000242E7D37970>