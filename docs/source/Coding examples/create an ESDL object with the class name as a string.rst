Create an ESDL object with the class name as a string
=====================================================

The following code:

.. code-block:: python

   asset_class = "WindTurbine"
   asset = esdl.getEClassifier(asset_class)()
   print(asset)

results in::

   <esdl.esdl.WindTurbine object at 0x00000246E64DD150>
