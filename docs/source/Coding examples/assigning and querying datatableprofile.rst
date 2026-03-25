Assigning and querying a profile with DataTableProfile
=======================================================

The examples below demonstrate how to work with DataTableProfile for:

1. Assigning a DataTableProfile to an asset port
2. Querying profile data from a DataTableProfile

Example 1 - Assigning a DataTableProfile to an asset port
---------------------------------------------------------

The example demonstrates the workflow for creating and assigning a DataTableProfile to an asset port.

.. note::
    This example shows an explicit workflow that stores quantity/unit and database configuration in EnergySystemInformation before
    referencing them from a profile. This is recommended for reusability and consistency across an ESDL file.

    If the same quantity/unit or database configuration already exists, you can skip creation and reference the existing entry directly.

Load an ESDL file
~~~~~~~~~~~~~~~~~

.. code-block:: python

    import uuid
    import esdl
    from esdl.esdl_handler import EnergySystemHandler
    from datetime import datetime

    # Load an existing ESDL
    esh = EnergySystemHandler()
    es = esh.load_file("test/example.esdl")

Create a DataTableProfile instance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See `DataTableProfile <https://energytransition.github.io/#router/doc-content/687474703a2f2f7777772e746e6f2e6e6c2f6573646c/DataTableProfile.html>`_
for the complete attributes and references supported in the class.

.. code-block:: python

    dtp = esdl.DataTableProfile(
        id="my_dtp_profile", # or UUID
        tableName="Space Heat default profiles",
        columnName="SpaceHeat_and_HotWater_PowerProfile_1900_2000",
        startDate=datetime(2019, 1, 1),
        endDate=datetime(2019, 12, 31),
        multiplier=10.0,
    )

Register and reference a global Quantity and Unit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Store the quantity and unit in the energy system's global registry for reuse across multiple profiles.

.. code-block:: python

    # Define a quantity and unit
    qau_power = esdl.QuantityAndUnitType(
        id=str(uuid.uuid4()),
        physicalQuantity="POWER",
        unit="WATT",
        multiplier="MEGA",
        description="Power in MW",
    )

    # Ensure EnergySystemInformation exists in the ESDL
    esi = es.energySystemInformation
    if not esi:
        esi = esdl.EnergySystemInformation(id=str(uuid.uuid4()))
        es.energySystemInformation = esi

    # Ensure QuantityAndUnits container exists in EnergySystemInformation
    if not esi.quantityAndUnits:
        esi.quantityAndUnits = esdl.QuantityAndUnits(id=str(uuid.uuid4()))

    # Add the quantity and unit to the global registry
    # NOTE: Check first if the same QaU already exists in the list of quantityAndUnits (the implementation is skipped here)
    esi.quantityAndUnits.quantityAndUnit.append(qau_power)

Once the quantity and unit is registered in EnergySystemInformation, it can be referenced by one or more profiles.

.. code-block:: python

    # Attach the quantity and unit to the profile
    dtp.profileQuantityAndUnit = esdl.QuantityAndUnitReference(reference=qau_power)

Register and reference a global Database Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Store the database configuration in the energy system's global registry for reuse.

See `DatabaseConfiguration <https://energytransition.github.io/#router/doc-content/687474703a2f2f7777772e746e6f2e6e6c2f6573646c/DatabaseConfiguration.html>`_
for the complete attributes and references supported in the class.

.. code-block:: python

    # Define a database configuration for PostgreSQL
    db_config = esdl.DatabaseConfiguration(
        type=esdl.DatabaseTypeEnum.POSTGRESQL,
        id="my_database_id", # or UUID
        database="energy_profiles",
        host="localhost",
        port=5432,
    )

    # Alternatively, define an InfluxDB database configuration
    # db_config = esdl.DatabaseConfiguration(
    #     type=esdl.DatabaseTypeEnum.INFLUXDB,
    #     id="my_database_id", # or UUID
    #     database="energy_profiles",
    #     host="public-profiles.nwn-design-toolkit.nl",
    # )

    # Ensure DataConfigurations container exists in EnergySystemInformation
    if not esi.dataconfigurations:
        esi.dataconfigurations = esdl.DataConfigurations(id=str(uuid.uuid4()))

    # Add the database configuration to the global registry
    # NOTE: Check first if the same config already exists in the list of dataconfigurations (the implementation is skipped here)
    esi.dataconfigurations.configurations.append(db_config)

Once the database configuration is registered in EnergySystemInformation, it can be referenced by one or multiple profiles.

.. code-block:: python

    # Attach the database configuration to the profile
    dtp.configuration = db_config

Create an asset and assign the profile to its port
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    # Create a heating demand asset with a location on the map
    heating_demand = esdl.HeatingDemand(
        id=str(uuid.uuid4()),
        name="Heating Demand 01",
        geometry=esdl.Point(lat=52.6030475337285, lon=4.729614257812501)
    )

    # Create an input port
    in_port = esdl.InPort(id=str(uuid.uuid4()))
    heating_demand.port.append(in_port)

    # Assign the profile to the port
    in_port.profile.append(dtp)

    # Add the asset to the area
    area = es.instance[0].area
    area.asset.append(heating_demand)

Save the updated ESDL
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    # Save the ESDL with the new profile assignment
    esh.save_as("test/example_with_datatableprofiles.esdl")

The output ESDL would look like below.

.. code-block:: xml

    <?xml version='1.0' encoding='UTF-8'?>
    <esdl:EnergySystem xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:esdl="http://www.tno.nl/esdl" name="Untitled EnergySystem" description="" id="2d141aa4-6c63-4b21-be99-63c0a8608ab8" esdlVersion="v2603" version="1">
        <instance xsi:type="esdl:Instance" id="74de4e29-6ecc-4009-a8c3-4de108687dff" name="Untitled Instance">
            <area xsi:type="esdl:Area" id="676be387-23c4-493e-97bc-fec4f8c73702" name="Untitled Area">
                <asset xsi:type="esdl:HeatingDemand" id="18821a73-d095-41a0-ad6e-bb9ff503ef38" name="Heating Demand 01">
                    <geometry xsi:type="esdl:Point" lat="52.6030475337285" lon="4.729614257812501"/>
                    <port xsi:type="esdl:InPort" id="af4efa28-d372-469a-97c2-baac8ba6864e">
                        <profile xsi:type="esdl:DataTableProfile" id="my_dtp_profile" multiplier="10.0" startDate="2019-01-01T00:00:00.000000" endDate="2019-12-31T00:00:00.000000" tableName="Space Heat default profiles" columnName="SpaceHeat_and_HotWater_PowerProfile_1900_2000" configuration="my_database_id">
                            <profileQuantityAndUnit xsi:type="esdl:QuantityAndUnitReference" reference="3fc13b89-11ac-4f27-9f18-1979123e476e"/>
                        </profile>
                    </port>
                </asset>
            </area>
        </instance>
        <energySystemInformation xsi:type="esdl:EnergySystemInformation" id="d3024d4c-7633-4a60-8a75-0768fd2b28e9">
            <quantityAndUnits xsi:type="esdl:QuantityAndUnits" id="d31f7b34-9714-4028-a3c4-b35390aef97c">
                <quantityAndUnit xsi:type="esdl:QuantityAndUnitType" physicalQuantity="POWER" multiplier="MEGA" unit="WATT" description="Power in MW" id="3fc13b89-11ac-4f27-9f18-1979123e476e"/>
            </quantityAndUnits>
            <dataconfigurations xsi:type="esdl:DataConfigurations" id="afbf57dc-f95b-44bb-a9b1-59e25ba8a9f7">
                <configurations xsi:type="esdl:DatabaseConfiguration" id="my_database_id" database="energy_profiles" type="POSTGRESQL" host="localhost" port="5432"/>
            </dataconfigurations>
        </energySystemInformation>
    </esdl:EnergySystem>


Example 2 - Querying a profile data from a DataTableProfile
-----------------------------------------------------------

The example demonstrates the workflow for querying profile data from a DataTableProfile in an ESDL.

Load an ESDL file
~~~~~~~~~~~~~~~~~

Reuse the ESDL just created.

.. code-block:: python

    from esdl.esdl_handler import EnergySystemHandler
    from esdl.profiles.datatableprofilemanager import DataTableProfileManager, Credentials

    # Load an existing ESDL
    esh = EnergySystemHandler()
    es = esh.load_file("test/example_with_datatableprofiles.esdl")

Retrieve and query DataTableProfile data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using :code:`DataTableProfileManager` and providing the connection credential to retrieve profile data. 

.. code-block:: python

    # Get DataTableProfile from an ESDL using its id.
    dtp = esh.get_by_id("my_dtp_profile")

    dtp_manager = DataTableProfileManager(dtp)
    # Provide the connection credentials for the DatabaseConfiguration that is registered in EnergySystemInformation
    dtp_manager.add_credential(
        Credentials.create_dict("my_database_id", "postgres", "password")
    )
    dtp_manager.load_database_configuration()

    print("-------------- get raw profile data from database ------------------")
    
    # profile_data_list will list data in its raw values stored in the database (no multiplier being applied)
    raw_data = dtp_manager.profile_data_list
    for data in raw_data[0:10]:
        print(data)

To retrieve profile data while taking the :code:`multiplier` attribute into account. Use :code:`get_profile_with_multiplier` method.

.. code-block:: python

    print("-------------- get scaled profile data from database ------------------")

    column_based = False
    scaled_data = dtp_manager.get_profile_with_multiplier(column_based=column_based)

    if column_based:
        print(scaled_data[0][:10])
        print(scaled_data[1][:10])
    else:
        for data in scaled_data[:10]:
            print(data)

To have the maximum flexibility with querying (e.g., for visualization purposes), use the static :code:`DataTableProfileManager.query` method.

.. code-block:: python

    print("-------------- get profile data with custom  query ------------------")

    from datetime import datetime

    cred_dict = Credentials.create_dict("my_database_id", "postgres", "password")
    
    multiplier = 20.0
    start_date = datetime(2019, 3, 1)
    end_date = datetime(2019, 5, 1)
    column_based = False

    profile_values, header, metadata = DataTableProfileManager.query(
        data_table_profile=dtp,
        credentials_dict=cred_dict,
        table_name=dtp.tableName,
        column_name=dtp.columnName,
        start_date=start_date,
        end_date=end_date,
        multiplier=multiplier,
        column_based=column_based,
    )

    if column_based:
        print(profile_values[0][:10])
        print(profile_values[1][:10])
    else:
        for data in profile_values[:10]:
            print(data)
