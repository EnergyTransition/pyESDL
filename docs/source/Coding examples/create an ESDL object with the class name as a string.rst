Create an ESDL object with the class name as a string
=====================================================

When creating ESDLs in scripts, it is often convenient to create an instance of an ESDL class using a string. 

For example when parsing an Excel file to create an ESDL instance based on a column in the Excel. To do that you can do the following in python:


.. code-block:: python

   asset_class = "WindTurbine"
   asset = esdl.getEClassifier(asset_class)()
   print(asset)

results in::

   <esdl.esdl.WindTurbine object at 0x00000246E64DD150>

the :code:`esdl.getEClassifier()` method will return the associated class for the requested class name as string; by adding :code:`()` it will instantiate this class directly.

The :code:`EnergySystemHandler` also contains a convenient method to do this, see the method :code:`instantiate_esdltype(className: str)`.

