Release notes
=============

Version 26.6.1
--------------
- Fix missing files for automatic ESDL version migration

Version 26.6
------------
- Add support for ESDL release 26.6
- Implement automatic ESDL version migration mappings on loading ESDL files with older ESDL formats

Version 26.5
------------
- Add support for ESDL release 26.5
- Add general profile parsing and adding/writing to database functions, including profile data caching
- Add automated testing with postgres/influxdb databases

Version 26.4.1
--------------
- Fix bug of table index creation error in postgresql configuration
- Add initial support for loading DataTableProfile data with profiles stored in InfluxDB database using DataTableProfileManager
- Extend coding examples of DataTableProfile in the readthedocs documentation

Version 26.4
------------
- Updated python dependencies for geometry and profiles functionalities (Python 3.10, 3.11, 3.12, 3.13, 3.14)

Version 26.3.1
--------------
- Update readthedocs documentation related to DataTableProfileManager API and a coding example of assigning and querying a profile with DataTableProfile

Version 26.3
------------
- Add support for ESDL release 26.3
- Add initial support for new DataTableProfiles using the DataTableProfileManager with a postgres backend. Allows to easily store CSV/Excel files in postgres and add these profiles to an ESDL

Version 26.2
------------
- Add support for ESDL release 26.2

Version 25.12
-------------
- Add functions to create QuantityAndUnit objects
- Add unit conversion from gram to tonne and vice versa (e.g. kg to Mt)
- Support setting PhysicalQuantity when using `build_qau_from_unit_string()`, e.g.
  `build_qau_from_unit_string("TWh", 'Energy')`

Version 25.7
------------
- Add support for ESDL release 25.7
- Small bugfix in generating a QuantityAndUnitType instance from a string
- Fix bug in unit conversion when physical quantities are not the same

Version 25.5.2
--------------
- Fix bug in unit conversion when physical quantities are not the same

Version 25.5.1
--------------
- Add support for ESDL release 25.5.1

Version 25.5
------------
- Add support for ESDL release 25.5

Version 25.2
------------
- Add support for ESDL release 25.2

Version 24.11.2
---------------
- Add link to documentation of pyESDL on readthedocs
- Fix geojson dependency 

Version 24.11.1
---------------
- Downgrade pyEcore to 0.13.2 again, due to error with rows in tables

Version 24.11
-------------
- Update build system and dependencies
- Fix wrong import in `support_functions` on Python > 3.12
- Update pyEcore to 0.15.1

Version 24.9
------------
- Add support for ESDL release 24.09
- Upgrade shapely and geojson versions

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
