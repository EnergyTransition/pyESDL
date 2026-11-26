from uuid import uuid4

import geojson
import shapely
from geojson import FeatureCollection, MultiPolygon

import esdl
from esdl.esdl_handler import EnergySystemHandler
from esdl.geometry.shape import Shape

esh = EnergySystemHandler()
es = esh.create_empty_energy_system(name="MultiPolygon test")
area = es.instance[0].area

with open("ESDL multi-polygon test.geojson") as f:
    data = geojson.load(f)

print(data)

if isinstance(data, FeatureCollection):
    for f in data.features:
        if isinstance(f.geometry, MultiPolygon):
            mp_geojson = f.geometry

            shapely_shp = shapely.geometry.shape(mp_geojson)
            shp = Shape.create(Shape.transform_crs(shapely_shp, "EPSG:23031"))

            print(shp)

            mp_esdl = shp.get_esdl()

            print(mp_esdl)

            asset = esdl.CCS(id=str(uuid4()))
            asset.geometry = mp_esdl
            area.asset.append(asset)

esh.save("MultiPolygon test.esdl")


