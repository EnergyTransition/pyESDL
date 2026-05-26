from pyecore.ecore import EInt
from pyecore.resources import ResourceSet, URI

from esdl import esdl
from esdl.esdl_handler import StringURI
from esdl.resources.json import JsonResource
from esdl.resources.xmlresource import XMLResource

wt = esdl.WindTurbine(id='123', name='MyWindTurbine')

rset = ResourceSet()
# Assign files with the .esdl extension to the XMLResource instead of default XMI
rset.resource_factory['esdl'] = lambda uri: XMLResource(uri)
uri = StringURI('to_string.esdl')
resource = rset.create_resource(uri)
resource.append(wt)

resource.save(uri)
print(uri.getvalue())

rset = ResourceSet()
# Assign files with the .esdl extension to the XMLResource instead of default XMI
rset.resource_factory['json'] = lambda uri: JsonResource(uri, indent=2)
uri = StringURI('to_string.json')
resource = rset.create_resource(uri)
resource.append(wt)


resource.save(uri)
print(uri.getvalue())