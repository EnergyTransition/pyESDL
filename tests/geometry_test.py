#  This work is based on original code developed and copyrighted by TNO 2023.
#  Subsequent contributions are licensed to you by the developers of such code and are
#  made available to the Project under one or several contributor license agreements.
#
#  This work is licensed to you under the Apache License, Version 2.0.
#  You may obtain a copy of the license at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Contributors:
#      TNO         - Initial implementation
#  Manager:
#      TNO
import unittest

from esdl import esdl
from esdl.geometry.shape import Shape


class TestPyESDLGeometry(unittest.TestCase):

    def test_parse_wkt_str(self):
        wkt_str = "POLYGON((4.352463483810425 51.968569708352845,4.352656602859497 51.968206158647774,4.353482723236084 51.968371408879335,4.352463483810425 51.968569708352845))"
        shp = Shape.parse_wkt(wkt_str)
        print(shp.get_esdl())

    def test_esdl_polygon(self):
        # Create an esdl.Polygon with three coordinates
        pol = esdl.Polygon()
        subpol = esdl.SubPolygon()
        subpol.point.extend([
            esdl.Point(lat=51.968569708352845, lon=4.352463483810425),
            esdl.Point(lat=51.968206158647774 , lon=4.352656602859497),
            esdl.Point(lat=51.968371408879335, lon=4.353482723236084)
        ])
        pol.exterior = subpol

        # Convert it to a Shapely polygon and print the WKT (contains 4 coordinates)
        shp = Shape.create(pol)
        print(shp.get_wkt())

        # Create a esdl.Polygon out of the Shapely polygon (contains 4 coordinates)
        esdl_pol = shp.get_esdl()
        for p in esdl_pol.exterior.point:
            print(p)

    def test_create(self):
        p = esdl.Point(lat=51.96835818888323, lon=4.352849721908569)
        shp = Shape.create(p)
        print(shp.get_geojson_feature(properties={"key": "value"}))

    def test_shapely_contains(self):
        esdl_p = esdl.Point(lat=51.96835818888323, lon=4.352849721908569)
        point_shp = Shape.create(esdl_p)
        shapely_point = point_shp.get_shape()

        esdl_polygon = esdl.Polygon(exterior=esdl.SubPolygon(
            point=[
                esdl.Point(lat=51.968569708352845, lon=4.352463483810425),
                esdl.Point(lat=51.968206158647774, lon=4.352656602859497),
                esdl.Point(lat=51.968371408879335, lon=4.353482723236084)
            ]
        ))
        polygon_shp = Shape.create(esdl_polygon)
        shapely_polygon = polygon_shp.get_shape()

        print(shapely_polygon.contains(shapely_point))


