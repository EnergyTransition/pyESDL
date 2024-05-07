Storing a Pandas DataFrame with timeseries in InfluxDB
======================================================
... and create an InfluxDBProfile specification for each column in the dataset.

When working with timeseries data, sometimes the Panda library can be
useful to manipulate the data.

In this example a CSV file without proper timestamps is updated,
such that it can be loaded into InfluxDB, and the associated :code:`InfluxDBProfile`
are available to be assigned in bulk to Consumer assets in an ESDL file.

.. code-block:: python

    esh = EnergySystemHandler()  # load esdl core, including deepcopy() and clone() support
    es = esh.load_file('data/input.esdl')

    # read profiles from CSV in pandas dataframe
    df = pd.read_csv('profiles.csv')
    # make all columns floats
    df = df.astype(float)
    # Time column is the amount of seconds since start of 2021
    df['Time'] = df['Time'].astype(int)
    # Convert seconds to datetime objects for the time column
    year2021 = datetime(year=2021, month=1, day=1)
    df['Time'] = df['Time'].apply(lambda x: year2021 + timedelta(seconds=x))
    # make sure we adhere to the correct internal/influxdb terminology in InfluxDBProfileManager
    # time axis should be named 'datetime'
    df.rename(columns={'Time': 'datetime'}, inplace=True)

    # Convert dataframe to list of list (row-based)
    df_as_list = df.values.tolist()

    # influx db configuration
    measurement = 'my_profiles'
    field_names = df.columns.values.tolist()[1:]  # header of the CSV, excluding the datetime column

    influx_settings = ConnectionSettings(
        host="localhost",
        port=8086,
        database="profiles",
        ssl=False,
        username="",
        password="",
        verify_ssl=True
    )

    ipm = InfluxDBProfileManager(settings=influx_settings)
    # set Dataframe data to InfluxDBProfileManager
    ipm.set_profile(profile_header=df.columns.values.tolist(), profile_data_list=df_as_list, profile_type=ProfileType.CSV)
    # generate a list of InfluxDBProfile objects for this data, one for each column.
    influxdb_profiles = ipm.get_esdl_influxdb_profile(measurement=measurement, field_names=field_names)
    # Create a map between the name of the profile (header name) and the InfluxDBProfile
    profile_map = {}
    for p in influxdb_profiles:
        profile_map[p.name] = p

    # add Power Quantity and unit to the global list of quantity and units in this ESDL
    # Create the structure if it does not exist
    esi = es.energySystemInformation
    if not esi:
        esi = esdl.EnergySystemInformation()
        es.energySystemInformation = esi
    quas: esdl.QuantityAndUnits = esi.quantityAndUnits
    if not quas:
        qaus = esdl.QuantityAndUnits()
        esi.quantityAndUnits = qaus
    power_unit: esdl.QuantityAndUnitType = POWER_IN_W.clone() # clone the definition of the Watt unit such that we can add it to our ESDL
    power_unit.id = str(uuid.uuid4())
    quas.quantityAndUnit.append(power_unit)

    # save data to InfluxDB
    ipm.save_influxdb(measurement=measurement, field_names=field_names)

    # assign the generated esdl.InfluxDBProfile profiles to the correct Consumer in the ESDL
    cnt = 1
    for eobj in es.eAllContents():
        if isinstance(eobj, esdl.Consumer):
            consumer: esdl.Consumer = eobj  # cast to the correct ESDL type, so autocompletion works
            print(f"{cnt}\t<{consumer.eClass.name} name={consumer.name}>")
            cnt += 1
            if consumer.name in profile_map:
                inport = get_inport(consumer)
                profile = profile_map[consumer.name]
                # Create a quantity and unit reference to the global Unit defined in EnergySystemInformation.
                profile.profileQuantityAndUnit = esdl.QuantityAndUnitReference(reference=power_unit)
                # add the profile to the InPort of this Consumer
                inport.profile.append(profile)
                print(f"\t- Assigning profile {profile} to {consumer}")
            else:
                print(f"Error: Cannot find profile for Consumer {consumer.name}")

    esh.save_as('data/output_with_influxdbprofiles.esdl')




    def get_inport(asset: EnergyAsset):
    """
    Find the first InPort of an ESDL EnergyAsset.
    """
        for p in asset.port:
            if isinstance(p, esdl.InPort):
                return p
        raise RuntimeError("Cannot find an InPort for " + asset)
