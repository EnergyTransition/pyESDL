Handling ECore types
====================

EDate
-----

.. code-block:: Python

   dt = datetime.now()
   ed = EDate.from_string(dt.strftime('%Y-%m-%dT%H:%M:%S.%f%z'))

EEnum
-----

Instantiating an ESDL attribute with type EEnum and comparing EEnums:

.. code-block:: Python

   asset = esdl.WindTurbine(id=str(uuid4()), name="WT1", state=esdl.AssetStateEnum.ENABLED)

   if asset.state == esdl.AssetStateEnum.ENABLED:
       ...

Instantiating an ESDL attribute with type EEnum from a string value:

.. code-block:: Python

   state_string = "ENABLED"

   asset = esdl.WindTurbine(id=str(uuid4()), name="WT1")
   asset.state = esdl.AssetStateEnum.from_string(state_string)