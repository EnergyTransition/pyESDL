Release notes
=============

Version 24.2
------------
- Fix bug when no tags are given for an InfluxDBProfile
- Fix issue with multi-valued attribute values (such as values in TableRow)
- Start with the ReadTheDocs documentation

Version 24.1
-------------
- Add support for ESDL release 24.01 

Version 23.12.1
---------------
- Fix bug in ProfileManager
- InfluxDBProfileManager.load_influxdb now returns an esdl.InfluxDBProfile
- InfluxDBProfileManager: improved handling of situations where no data is returned

Version 23.12
-------------
- Bug fixes in InfluxDBProfileManager

Version 23.11.2
---------------
- Add support for ESDL release 23.11 (with powerCurveTable for WindTurbine)

Version 23.11.1
---------------
- Fix bug in determining the end_datetime of profiles

Version 23.11
-------------
- Implement EDR client
- Added more predefined QaUs
- Support for tags in InfluxDBProfileManager

Version 23.10.1
---------------
- Implement set_profile function
- Corrected some bugs (datetime_utils missing, support for fields with '-')

Version 23.10
-------------
- Add support functions for handling profiles, geometries and qunatity and units.

Version 23.03
-------------
- Add support for ESDL release 23.03 (added 2 PowerPlant types, referenceYear for CostInformation, added fullLoadHours and operationalHours attributes to Consumer and Transport classes)

Version 22.11.1
---------------
- Add support for ESDL release 22.11 (with KPI-KPI and Sector-Sector relation, ElectricBoiler, PowerPlant types, ...)

Version 22.11
-------------
- Add support for Energy Data Repository files (\*.edd)
- Add supoprt for linking to external files (e.g. stored in the EDR) using `get_external_reference(url, object_id)`
- Add function to instantiate a class by its class name (`instantiate_esdltype(className)`) 

Version 22.10.0
---------------
- Add support for ESDL release 22.10 (with Port-Constraint relation, support for modelling material flows, added powerFactor attribute for electricity related assets, DataSourceList)

Version 22.7.0
--------------
- Add support for ESDL release 22.07 (with ConnectableAsset, ExposedPortsAsset, PumpedHydroPower and CAES assets, restructured some LabelJump information, asset Constraints)

Version 21.12.0
---------------
- Add support for ESDL release 21.12 (with quantity and unit information for InputOutputRelation, renaming of some distribution information classes of AggregatedBuildings)

Version 21.11.0
---------------
- Add support for ESDL release 21.11 (with HybridHeatpump, developmentCosts, Commodity emission attribute)

Version 21.10.0
---------------
- Add support for ESDL release 21.10 (with storage volumes)

Version 21.9.1
--------------
- Add support for ESDL release 21.9 (with pipe and cable relations)

Version 21.9.0
--------------
- Fix pyecore 0.12.1 dependency issue

Version 21.7.1
--------------
- Add support for ESDL release 21.7 (with BufferDistance, ATES)

Version 21.6.2
--------------
- Fix issue with version definition, making the EnergySystemHandler unusable.
- Add get_all_instances_of_type() to EnergySystemHandler to retrieve all the instances of a certain type in an EnergySystem.
  
  E.g. ``esh.get_all_instances_of_type(esdl.GenericProfile)`` will give you all the profiles defined in the EnergySystem.

Version 21.6.1
--------------
- Add support for InputOutputRelation
