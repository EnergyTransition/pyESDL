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