Getting an ESDL object as an XML string
=======================================

The following code:

.. code-block:: python

  from pyecore.resources import ResourceSet, URI

  from esdl import esdl
  from esdl.esdl_handler import StringURI

  wt = esdl.WindTurbine(id='123', name='MyWindTurbine')

  rset = ResourceSet()
  resource = rset.create_resource(URI("test.esdl"))
  resource.append(wt)

  uri = StringURI('to_string.esdl')
  resource.save(uri)
  print(uri.getvalue())

results in:

.. code-block:: XML

  <?xml version='1.0' encoding='UTF-8'?>
  <esdl:WindTurbine xmlns:xmi="http://www.omg.org/XMI" xmlns:esdl="http://www.tno.nl/esdl" id="123" name="MyWindTurbine" xmi:version="2.0"/>
