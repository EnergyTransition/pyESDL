Getting an ESDL object as an XML/JSON string
============================================

The :code:`EnergySystemHandler` class contains a method :code:`to_string()` to serialize a complete ESDL to a string.
Sometimes only a part of the ESDL object tree needs to be saved or communicated to other systems.
To do so, the following code is of help:

.. code-block:: python

  from pyecore.resources import ResourceSet, URI

  from esdl import esdl
  from esdl.esdl_handler import StringURI
  from esdl.resources.xmlresource import XMLResource

  wt = esdl.WindTurbine(id='123', name='MyWindTurbine')
  # Assign files with the .esdl extension to the XMLResource instead of default XMI
  rset.resource_factory['esdl'] = lambda uri: XMLResource(uri)
  uri = StringURI('to_string.esdl')
  resource = rset.create_resource(uri)
  resource.append(wt)

  resource.save(uri)
  print(uri.getvalue())

results in:

.. code-block:: XML

  <?xml version='1.0' encoding='UTF-8'?>
  <esdl:WindTurbine xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:esdl="http://www.tno.nl/esdl" id="123" name="MyWindTurbine"/>


To convert the (part of) the ESDL object to JSON use the following code:

.. code-block:: python

  from pyecore.resources import ResourceSet, URI

  from esdl.resources.json import JsonResource
  from esdl import esdl
  from esdl.esdl_handler import StringURI

  wt = esdl.WindTurbine(id='123', name='MyWindTurbine')

  rset = ResourceSet()
  # Assign files with the .json extension to the JSONResource instead of default XMI
  rset.resource_factory['json'] = lambda uri: JsonResource(uri, indent=2)
  uri = StringURI('to_string.json')
  resource = rset.create_resource(uri)
  resource.append(wt)

  resource.save(uri)
  print(uri.getvalue())

This results in:

.. code-block:: json

  {
    "eClass": "http://www.tno.nl/esdl#//WindTurbine",
    "id": "123",
    "name": "MyWindTurbine"
  }
