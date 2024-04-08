Tutorial 3: Adding an EDR profile
=================================

This tutorial shows how to add an EDR (Energy Data Repository) profile to an ESDL asset using the EDR client. In this example, a wind turbine EDR profile is added to a wind park (consisting of a 100 such wind turbines). By extension, this tutorial shows how to create a wind park with its geometry in ESDL.

Start with importing the required libraries

.. code-block:: python

    from esdl import esdl
    from esdl.esdl_handler import EnergySystemHandler
    from esdl.edr.client import EDRClient

Define the names of the file to edit and a file to save (if the original file should not be overwritten)

.. code-block:: python

    if __name__ == '__main__':
        folder_name = "ESDLs"
        file_name_to_edit = "Tutorial2_pyESDL.esdl"
        file_name_to_save = "Tutorial3_pyESDL.esdl"

Create an EnergySystemHandler - a class that helps a developer to read and write ESDL-files

.. code-block:: python

        energy_system_handler = EnergySystemHandler()

Load an existing energy system from and ESDL file

.. code-block:: python

        # Get the Tutorial2
        energy_system: esdl.EnergySystem = energy_system_handler.load_file(folder_name + "/" + file_name_to_edit)

Create a WindPark to which an EDR profile will be appended

.. code-block:: python

        # Create a wind park
        wind_park = esdl.WindPark(id='wind-park-ID', name='WindPark')

Create the WindPark's surface are with a set of points (coordinates) where it is located. The points should be added in clockwise or anti-clockwise order, one by one (i.e. the order matters)

.. code-block:: python

        # Create a polygon
        point1 = esdl.Point(lat=52.04386412846831, lon=4.3002596497535714)
        point2 = esdl.Point(lat=52.04386577818243, lon=4.300523847341538)
        point3 = esdl.Point(lat=52.04376349579175, lon=4.300515800714494)
        point4 = esdl.Point(lat=52.043746173750776, lon=4.30023953318596)

To create the WindPark's polygon, the points are first added to a SubPolygon (the exterior of the Polygon). For more details, refer to the ESDL reference model

.. code-block:: python

        subpolygon = esdl.SubPolygon()
        subpolygon.point.append(point1)
        subpolygon.point.append(point2)
        subpolygon.point.append(point3)
        subpolygon.point.append(point4)

        polygon = esdl.Polygon()
        polygon.exterior = subpolygon

Add the created Polygon to the WindPark's geometry (i.e. specify its location)

.. code-block:: python

        wind_park.geometry = polygon

To connect the WindPark to the ElectricityDemand (ED), first get the ED's InPort ID

.. code-block:: python

        # Get ElectricityDemand InPort to connect to
        electricity_demand_in_port_id = energy_system_handler.get_by_id('electricity-demand-in-port-ID')

Create the WIndPark's OutPort

.. code-block:: python

        # Create an OutPort and attach a profile to it
        wind_park_out_port = esdl.OutPort(id='wind-park-out-port-ID', connectedTo=[electricity_demand_in_port_id])

To assign ElectricityCommodity to the WindPark, get the ElectricityCommodity's ID

.. code-block:: python

        # Get the electricity commodity by ID
        electricity_commodity = energy_system_handler.get_by_id('electricity-commodity-ID')

Assign ElectricityCommodity to the WindPark's OutPort

.. code-block:: python

        wind_park_out_port.carrier = electricity_commodity

Instantiate an EDR client to be able to retrieve EDR profiles

.. code-block:: python

        # Get EDR wind profile
        edr_client = EDRClient()

Get the list of all the InfluxDBProfiles from EDR to check the profile IDs (this step is not necessary is the desired ID is already known)

.. code-block:: python

        profiles_list = edr_client.get_objects_list("InfluxDBProfile")

Get the EDR InfluxDBProfile using a profile ID (this ID returns a profile of one specific WindTurbine)

.. code-block:: python

        e1_test_influxdb_profile = edr_client.get_object_esdl(
            '/edr/Public/Profiles/North Sea Energy/profile_kW_2015_Hub_east_160m - power_kW [POWER in kW].edd')

To create a WindPark with 100 such WindTurbines, change the multiplier to 100

.. code-block:: python

        # WindPark with 100 wind turbines
        e1_test_influxdb_profile.multiplier = 100.0

Append the InfluxDBProfile to the WindPark's OutPort

.. code-block:: python

        wind_park_out_port.profile.append(e1_test_influxdb_profile)
        wind_park.port.append(wind_park_out_port)

Retrieve the ESDL Area, and append the WindPark to it

.. code-block:: python

        # Add WindPark to the area
        energy_system_area: esdl.Area = energy_system.instance[0].area
        energy_system_area.asset.append(wind_park)

Save the new ESDL file

.. code-block:: python

        energy_system_handler.save(folder_name + "/" + file_name_to_save)