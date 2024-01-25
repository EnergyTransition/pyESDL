Geometry functionality
======================

- Uses shapely internally to store the data
- Provides conversion to and from ESDL, Shapely, GeoJSON, WKT, WKB, leaflet data types.
- Provides CRS transformation to WGS84/EPSG:4326 used by Shapely

Structure
---------
The following classes are provide:

- class Shape: generic representation of a shape. Has a static method ``create(shepe_input)`` that tries to determine the type of the input parameter and creates an instance of one of the other classes.
- class ShapePoint(Shape)
- class ShapeLine(Shape)
- class ShapePolygon(Shape)
- class ShapeMultiPolygon(Shape)
- class ShapeGeometryCollection(Shape)


Examples
--------

Create a GeoJSON feature from an esdl.Point
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following code

.. code-block:: python

  p = esdl.Point(lat=51.96835818888323, lon=4.352849721908569)
  shp = Shape.create(p)
  print(shp.get_geojson_feature(properties={"key": "value"}))

results in

.. code-block:: json

  {"type": "Feature", "geometry": {"type": "Point", "coordinates": [4.352849721908569, 51.96835818888323]}, "properties": {"key": "value"}}

Create an esdl.Polygon from a WKT string
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following code

.. code-block:: python

  wkt_str = "POLYGON((4.352463483810425 51.968569708352845,4.352656602859497 51.968206158647774,4.353482723236084 51.968371408879335,4.352463483810425 51.968569708352845))"
  shp = Shape.parse_wkt(wkt_str)
  print(shp.get_esdl())

results in

.. code-block::

  <esdl.esdl.Polygon object at 0x000001347528A380>

Check if an esdl.Point is within an esdl.Polygon
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following code

.. code-block:: python

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

results in

.. code-block:: python

  True