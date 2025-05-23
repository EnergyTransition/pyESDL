"""Definition of meta model 'esdl'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *


name = 'esdl'
nsURI = 'http://www.tno.nl/esdl'
nsPrefix = 'esdl'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)
CommodityEnum = EEnum('CommodityEnum', literals=[
                      'UNDEFINED', 'ELECTRICITY', 'GAS', 'HEAT', 'H2', 'BIOGAS', 'CO2', 'ENERGY'])

AreaScopeEnum = EEnum('AreaScopeEnum', literals=['UNDEFINED', 'BUILDING', 'STREET', 'ZIPCODE', 'NEIGHBOURHOOD', 'DISTRICT',
                      'VILLAGE', 'CITY', 'MUNICIPALITY', 'REGION', 'PROVINCE', 'STATE', 'COUNTRY', 'CONTINENT', 'SERVICE_AREA'])

ProfileTypeEnum = EEnum('ProfileTypeEnum', literals=['UNDEFINED', 'SOLARIRRADIANCE_IN_W_PER_M2', 'WINDSPEED_IN_M_PER_S', 'STATEOFCHARGE_IN_WS', 'ENERGY_IN_WH', 'ENERGY_IN_KWH', 'ENERGY_IN_MWH', 'ENERGY_IN_GWH', 'ENERGY_IN_J', 'ENERGY_IN_KJ', 'ENERGY_IN_MJ', 'ENERGY_IN_GJ', 'ENERGY_IN_TJ',
                        'ENERGY_IN_PJ', 'TEMPERATURE_IN_C', 'TEMPERATURE_IN_K', 'POWER_IN_W', 'POWER_IN_KW', 'POWER_IN_MW', 'POWER_IN_GW', 'POWER_IN_TW', 'MONEY_IN_EUR', 'MONEY_IN_KEUR', 'MONEY_IN_MEUR', 'PERCENTAGE', 'MONEY_IN_EUR_PER_KW', 'MONEY_IN_EUR_PER_KWH', 'VOLUME_IN_M3', 'VOLUME_IN_LITERS'])

DurationUnitEnum = EEnum('DurationUnitEnum', literals=[
                         'SECOND', 'MINUTE', 'HOUR', 'DAY', 'WEEK', 'MONTH', 'YEAR'])

BuildingTypeEnum = EEnum('BuildingTypeEnum', literals=['UNDEFINED', 'RESIDENTIAL', 'GATHERING', 'PRISON', 'HEALTHCARE',
                         'INDUSTRY', 'OFFICE', 'EDUCATION', 'SPORTS', 'SHOPPING', 'HOTEL', 'AGRICULTURE', 'GREENHOUSE', 'UTILITY', 'OTHER'])

ConsTypeEnum = EEnum('ConsTypeEnum', literals=['PRIMARY', 'FINAL'])

SourceTypeEnum = EEnum('SourceTypeEnum', literals=[
                       'UNDEFINED', 'AIR', 'SUB_SURFACE', 'AQUIFER', 'SURFACE_WATER', 'HEAT_NETWORK'])

AggrTypeEnum = EEnum('AggrTypeEnum', literals=[
                     'UNDEFINED', 'NOT_AGGREGATED', 'PER_COMMODITY', 'TOTAL_ENERGY', 'TOTAL_CAPABILITY', 'PER_CAPIBILITY'])

AreaTypeEnum = EEnum('AreaTypeEnum', literals=['UNDEFINED', 'ROAD', 'RAILWAY', 'TERRAIN',
                     'RURAL_AREA', 'BUILT', 'WATER', 'SEA', 'RIVER', 'CANAL', 'LAKE', 'LAND', 'PARCEL'])

HeatDemandTypeEnum = EEnum('HeatDemandTypeEnum', literals=[
                           'UNDEFINED', 'SPACE_HEATING', 'HOT_TAPWATER', 'SH_AND_HTW', 'COOKING', 'OTHER'])

OwnershipRentalTypeEnum = EEnum('OwnershipRentalTypeEnum', literals=[
                                'UNDEFINED', 'PRIVATELY_OWNED', 'PRIVATE_RENTAL', 'HOUSING_ASSOCIATION'])

RoofTypeEnum = EEnum('RoofTypeEnum', literals=[
                     'UNDEFINED', 'FLATROOF', 'SLANTEDROOF', 'COMBINATION'])

EnergyLabelEnum = EEnum('EnergyLabelEnum', literals=['UNDEFINED', 'LABEL_G', 'LABEL_F', 'LABEL_E',
                        'LABEL_D', 'LABEL_C', 'LABEL_B', 'LABEL_A', 'LABEL_AP', 'LABEL_APP', 'LABEL_APPP', 'LABEL_APPPP'])

ResidentialBuildingTypeEnum = EEnum('ResidentialBuildingTypeEnum', literals=['UNDEFINED', 'VRIJSTAANDE_WONING', 'TWEE_ONDER_EEN_KAP_WONING', 'RIJWONING',
                                    'MAISONNETTEWONING', 'GALERIJWONING', 'PORTIEKWONING', 'FLATWONING', 'TUSSENWONING', 'HOEKWONING', 'GALERIJCOMPLEX', 'APPARTEMENTENCOMPLEX', 'APPARTEMENT'])

PowerPlantFuelEnum = EEnum('PowerPlantFuelEnum', literals=[
                           'UNDEFINED', 'COAL', 'BLAST_FURNACE_GAS', 'NATURAL_GAS', 'URANIUM', 'HYDROGEN'])

SectorEnum = EEnum('SectorEnum', literals=[
                   'UNDEFINED', 'GEBOUWDE_OMGEVING', 'ZAKELIJKE_DIENSTVERLENING', 'INDUSTRIE', 'AGRO_TUINBOUW'])

RenewableTypeEnum = EEnum('RenewableTypeEnum', literals=['UNDEFINED', 'RENEWABLE', 'FOSSIL'])

StateOfMatterEnum = EEnum('StateOfMatterEnum', literals=['UNDEFINED', 'SOLID', 'LIQUID', 'GASEOUS'])

GeothermalSourceTypeEnum = EEnum('GeothermalSourceTypeEnum', literals=[
                                 'UNDEFINED', 'HEAT', 'ELECTRICITY'])

CHPTypeEnum = EEnum('CHPTypeEnum', literals=['UNDEFINED', 'STEG', 'GAS_TURBINE', 'GAS_MOTOR'])

GlazingTypeEnum = EEnum('GlazingTypeEnum', literals=[
                        'UNDEFINED', 'ENKEL_GLAS', 'DUBBEL_GLAS', 'HR_GLAS', 'HRP_GLAS', 'HRPP_GLAS', 'HRPPP_GLAS'])

VentilationTypeEnum = EEnum('VentilationTypeEnum', literals=[
                            'UNDEFINED', 'NATURAL', 'MECHANIC_IN', 'MECHANIC_OUT', 'MECHANIC_INOUT', 'BALANCED', 'BALANCED_WITH_HEATRECUPERATION'])

GasHeaterTypeEnum = EEnum('GasHeaterTypeEnum', literals=[
                          'UNDEFINED', 'CR', 'VR', 'HR100', 'HR104', 'HR107', 'HRE', 'HRWW'])

InhabitantsTypeEnum = EEnum('InhabitantsTypeEnum', literals=[
                            'UNDEFINED', 'ALLEENSTAAND', 'TWEEVERDIENERS', 'GEZIN_MET_KINDEREN', 'SENIOREN'])

AdditionalHeatingSourceTypeEnum = EEnum(
    'AdditionalHeatingSourceTypeEnum', literals=['NONE', 'ELECTRIC', 'GAS'])

GeothermalPotentialEnum = EEnum('GeothermalPotentialEnum', literals=['UNKNOWN', 'POSSIBLE', 'GOOD'])

GeothermalPowerEnum = EEnum('GeothermalPowerEnum', literals=[
                            'UNKNOWN', 'POSSIBLE_GT5MWTH', 'GOOD_GT5MWTH', 'GOOD_GT7P5MWTH', 'GOOD_GT10MWTH'])

ResidualHeatSourceTypeEnum = EEnum('ResidualHeatSourceTypeEnum', literals=[
                                   'UNDEFINED', 'INDUSTRIAL', 'DATACENTER', 'COOLING_HOUSE', 'OTHER'])

MobilityFuelTypeEnum = EEnum('MobilityFuelTypeEnum', literals=[
                             'UNDEFINED', 'PETROL', 'DIESEL', 'HYDROGEN', 'LPG', 'BIOFUEL', 'ELECTRICITY', 'OIL', 'LNG', 'KEROSENE'])

VehicleTypeEnum = EEnum('VehicleTypeEnum', literals=['UNDEFINED', 'CAR', 'TRUCK', 'VAN', 'BUS', 'METRO', 'TRAM', 'TRAIN', 'PASSENGER_TRAIN',
                        'FREIGHT_TRAIN', 'SCOOTER', 'MOTOR_CYCLE', 'NONROAD_VEHICLE', 'AGRARIAN_VEHICLE', 'BARGE', 'INTERNATIONAL_SHIPPING', 'AIRCRAFT', 'OTHER', 'TOTAL'])

MultiplierEnum = EEnum('MultiplierEnum', literals=['NONE', 'ATTO', 'FEMTO', 'PICO', 'NANO', 'MICRO',
                       'MILLI', 'CENTI', 'DECI', 'DEKA', 'HECTO', 'KILO', 'MEGA', 'GIGA', 'TERA', 'TERRA', 'PETA', 'EXA'])

PhysicalQuantityEnum = EEnum('PhysicalQuantityEnum', literals=['UNDEFINED', 'ENERGY', 'POWER', 'VOLTAGE', 'PRESSURE', 'TEMPERATURE', 'EMISSION', 'COST', 'TIME', 'LENGTH', 'DISTANCE', 'IRRADIANCE',
                             'SPEED', 'STATE_OF_CHARGE', 'VOLUME', 'AREA', 'POWER_REACTIVE', 'COMPOSITION', 'FLOW', 'STATE', 'HEAD', 'POSITION', 'COEFFICIENT', 'WEIGHT', 'FORCE', 'CURRENT', 'RELATIVE_HUMIDITY', 'DIRECTION'])

UnitEnum = EEnum('UnitEnum', literals=['NONE', 'JOULE', 'WATTHOUR', 'WATT', 'VOLT', 'BAR', 'PSI', 'DEGREES_CELSIUS', 'KELVIN', 'GRAM', 'EURO', 'DOLLAR', 'SECOND', 'MINUTE', 'QUARTER', 'HOUR', 'DAY', 'WEEK',
                 'MONTH', 'YEAR', 'METRE', 'SQUARE_METRE', 'CUBIC_METRE', 'LITRE', 'WATTSECOND', 'ARE', 'HECTARE', 'PERCENT', 'VOLT_AMPERE', 'VOLT_AMPERE_REACTIVE', 'PASCAL', 'NEWTON', 'AMPERE', 'DEGREES', 'TONNE'])

TimeUnitEnum = EEnum('TimeUnitEnum', literals=[
                     'NONE', 'SECOND', 'MINUTE', 'QUARTER', 'HOUR', 'DAY', 'WEEK', 'MONTH', 'YEAR'])

GasConversionTypeEnum = EEnum('GasConversionTypeEnum', literals=[
                              'UNDEFINED', 'SMR', 'ATR', 'METHANATION'])

PVInstallationTypeEnum = EEnum('PVInstallationTypeEnum', literals=[
                               'UNDEFINED', 'ROOFTOP_PV', 'BUILDING_INTEGRATED_PV', 'WINDOW', 'ROAD', 'FIELD', 'WATER', 'CONCENTRATED_SOLAR'])

WindTurbineTypeEnum = EEnum('WindTurbineTypeEnum', literals=[
                            'UNDEFINED', 'WIND_ON_LAND', 'WIND_AT_SEA', 'WIND_ON_COAST', 'WIND_ON_BUILDING'])

WaterToPowerTypeEnum = EEnum('WaterToPowerTypeEnum', literals=[
                             'UNDEFINED', 'HYDRO_POWER', 'WAVE_POWER', 'TIDAL_POWER', 'OSMOTIC_POWER'])

SolarCollectorTypeEnum = EEnum('SolarCollectorTypeEnum', literals=[
                               'UNDEFINED', 'ROOFTOP', 'BUILDING_INTEGRATED_SC', 'ROAD', 'FIELD', 'WATER'])

HeatRadiationDeviceTypeEnum = EEnum('HeatRadiationDeviceTypeEnum', literals=[
                                    'UNDEFINED', 'HT_RADIATOR', 'LT_RADIATOR', 'FLOOR_HEATING', 'WALL_HEATING', 'INFRARED_PANEL', 'AIR_HANDLING_UNIT'])

CoolingDeviceType = EEnum('CoolingDeviceType', literals=[
                          'UNDEFINED', 'FLOOR_COOLING', 'AIR_HANDLING_UNIT'])

RoomHeaterTypeEnum = EEnum('RoomHeaterTypeEnum', literals=[
                           'UNDEFINED', 'GAS_STOVE', 'WOOD_STOVE', 'ELECTRIC', 'INFRARED_PANEL'])

BiomassHeaterTypeEnum = EEnum('BiomassHeaterTypeEnum', literals=[
                              'UNDEFINED', 'FULLY_AUTOMATED', 'SEMI_AUTOMATED', 'PELLET_FIRED', 'CHP'])

UTESPotentialTypeEnum = EEnum('UTESPotentialTypeEnum', literals=[
                              'UNDEFINED', 'HEAT_OPEN', 'HEAT_CLOSED', 'COLD_OPEN', 'COLD_CLOSED'])

UTESTypeEnum = EEnum('UTESTypeEnum', literals=[
                     'UNDEFINED', 'AQUIFER_TES', 'BOREHOLE_TES', 'CAVERN_TES', 'OTHER'])

InterpolationMethodEnum = EEnum('InterpolationMethodEnum', literals=[
                                'UNDEFINED', 'NONE', 'LINEAR', 'CUBIC', 'NEAREST', 'PREVIOUS', 'NEXT', 'OTHER'])

PipeDiameterEnum = EEnum('PipeDiameterEnum', literals=['VALUE_SPECIFIED', 'DN6', 'DN8', 'DN10', 'DN15', 'DN20', 'DN25', 'DN32', 'DN40', 'DN50', 'DN65', 'DN80', 'DN100',
                         'DN125', 'DN150', 'DN200', 'DN250', 'DN300', 'DN350', 'DN400', 'DN450', 'DN500', 'DN600', 'DN650', 'DN700', 'DN800', 'DN900', 'DN1000', 'DN1100', 'DN1200'])

AssetStateEnum = EEnum('AssetStateEnum', literals=['ENABLED', 'DISABLED', 'OPTIONAL'])

QuantityAndUnitScopeEnum = EEnum('QuantityAndUnitScopeEnum', literals=[
                                 'UNDEFINED', 'CONNECTION', 'BUILDING', 'HOUSEHOLD'])

ValveTypeEnum = EEnum('ValveTypeEnum', literals=[
                      'UNDEFINED', 'BUTTERFLY', 'BALL', 'GATE', 'GATE_VALVE_SQUARE'])

CompoundTypeEnum = EEnum('CompoundTypeEnum', literals=['UNDEFINED', 'MIXED', 'LAYERED'])

CombinationFunctionEnum = EEnum('CombinationFunctionEnum', literals=['MULTIPLICATION', 'ADDITION'])

TransferFunctionTypeEnum = EEnum('TransferFunctionTypeEnum', literals=[
                                 'UNDEFINED', 'POWER_SETPOINT_RESPONSE', 'TEMPERATURE_SETPOINT_RESPONSE'])

MeasureTypeEnum = EEnum('MeasureTypeEnum', literals=[
                        'UNDEFINED', 'ADD_GEOMETRY', 'MODEL_RESTRICTION'])

BufferDistanceTypeEnum = EEnum('BufferDistanceTypeEnum', literals=[
                               'UNDEFINED', 'RISK', 'ENVIRONMENT', 'NOISE', 'PARTICULATE_MATTER', 'NOX_EMISSIONS'])

PowerPlantTypeEnum = EEnum('PowerPlantTypeEnum', literals=['UNDEFINED', 'STEAM_TURBINE', 'INTERNAL_COMBUSTION', 'COMBINED_CYCLE_GAS_TURBINE', 'OPEN_CYCLE_GAS_TURBINE',
                           'INTEGRARED_COMBUSTION_COMBINED_CYCLE', 'SUPER_CRITICAL_STEAM_TURBINE', 'NUCLEAR_2ND_GENERATION', 'NUCLEAR_3RD_GENERATION', 'NUCLEAR_4TH_GENERATION', 'WASTE_INCENERATION'])

DatabaseTypeEnum = EEnum('DatabaseTypeEnum', literals=[
                         'UNDEFINED', 'SQL', 'POSTGRESQL', 'MYSQL', 'MSSQL', 'DUCKDB', 'INFLUXDB', 'TIMESCALE'])

FileTypeEnum = EEnum('FileTypeEnum', literals=['UNDEFINED', 'CSV', 'EXCEL', 'PARQUET', 'NETCDF'])


class EnergySystem(EObject, metaclass=MetaEClass):
    """This is the main class to describe an EnergySystem in ESDL. Each energy system description should start with this class. More information about ESDL and the Energy System can be found in the gitbook at https://energytransition.gitbook.io/esdl/"""
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    description = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    geographicalScope = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    sector = EAttribute(eType=SectorEnum, unique=True, derived=False, changeable=True, upper=-1)
    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True, iD=True)
    version = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    esdlVersion = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    measures = EReference(ordered=True, unique=True, containment=True, derived=False)
    instance = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    energySystemInformation = EReference(ordered=True, unique=True, containment=True, derived=False)
    parties = EReference(ordered=True, unique=True, containment=True, derived=False)
    services = EReference(ordered=True, unique=True, containment=True, derived=False)
    templates = EReference(ordered=True, unique=True, containment=True, derived=False)
    group = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, name=None, description=None, geographicalScope=None, sector=None, measures=None, instance=None, energySystemInformation=None, parties=None, services=None, id=None, version=None, templates=None, esdlVersion=None, group=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if description is not None:
            self.description = description

        if geographicalScope is not None:
            self.geographicalScope = geographicalScope

        if sector:
            self.sector.extend(sector)

        if id is not None:
            self.id = id

        if version is not None:
            self.version = version

        if esdlVersion is not None:
            self.esdlVersion = esdlVersion

        if measures is not None:
            self.measures = measures

        if instance:
            self.instance.extend(instance)

        if energySystemInformation is not None:
            self.energySystemInformation = energySystemInformation

        if parties is not None:
            self.parties = parties

        if services is not None:
            self.services = services

        if templates is not None:
            self.templates = templates

        if group:
            self.group.extend(group)


class Area(EObject, metaclass=MetaEClass):
    """The Area class represents a physical geographic area or a more abstract logical area. In both cases it is the 'asset container', in a sense that all assets within the area are contained by the Area instance."""
    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True, iD=True)
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    scope = EAttribute(eType=AreaScopeEnum, unique=True, derived=False,
                       changeable=True, default_value=AreaScopeEnum.UNDEFINED)
    type = EAttribute(eType=AreaTypeEnum, unique=True, derived=False, changeable=True)
    geometryReference = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    buildingDensity = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    logicalGroup = EAttribute(eType=EBoolean, unique=True, derived=False,
                              changeable=True, default_value=False)
    socialProperties = EReference(ordered=True, unique=True, containment=True, derived=False)
    economicProperties = EReference(ordered=True, unique=True, containment=True, derived=False)
    asset = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    area = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    containingArea = EReference(ordered=True, unique=True, containment=False, derived=False)
    isOwnedBy = EReference(ordered=True, unique=True, containment=False, derived=False)
    mobilityProperties = EReference(ordered=True, unique=True, containment=True, derived=False)
    KPIs = EReference(ordered=True, unique=True, containment=True, derived=False)
    potential = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    geometry = EReference(ordered=True, unique=True, containment=True, derived=False)
    measures = EReference(ordered=True, unique=True, containment=True, derived=False)
    sector = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, id=None, name=None, scope=None, type=None, socialProperties=None, economicProperties=None, asset=None, area=None, containingArea=None, isOwnedBy=None, geometryReference=None, mobilityProperties=None, buildingDensity=None, KPIs=None, potential=None, geometry=None, measures=None, sector=None, logicalGroup=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if name is not None:
            self.name = name

        if scope is not None:
            self.scope = scope

        if type is not None:
            self.type = type

        if geometryReference is not None:
            self.geometryReference = geometryReference

        if buildingDensity is not None:
            self.buildingDensity = buildingDensity

        if logicalGroup is not None:
            self.logicalGroup = logicalGroup

        if socialProperties is not None:
            self.socialProperties = socialProperties

        if economicProperties is not None:
            self.economicProperties = economicProperties

        if asset:
            self.asset.extend(asset)

        if area:
            self.area.extend(area)

        if containingArea is not None:
            self.containingArea = containingArea

        if isOwnedBy is not None:
            self.isOwnedBy = isOwnedBy

        if mobilityProperties is not None:
            self.mobilityProperties = mobilityProperties

        if KPIs is not None:
            self.KPIs = KPIs

        if potential:
            self.potential.extend(potential)

        if geometry is not None:
            self.geometry = geometry

        if measures is not None:
            self.measures = measures

        if sector is not None:
            self.sector = sector


@abstract
class Port(EObject, metaclass=MetaEClass):
    """Ports allow connections between EnergyAssets. Ports can be connected to one or more other ports. There are two types of ports: InPort and OutPort, which defines the primary direction of positive energy flow. InPorts can only be connected to OutPorts and vice versa."""
    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True, iD=True)
    maxPower = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    simultaneousPower = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    energyasset = EReference(ordered=True, unique=True, containment=False, derived=False)
    profile = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    carrier = EReference(ordered=True, unique=True, containment=False, derived=False)
    constraint = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, id=None, maxPower=None, energyasset=None, profile=None, carrier=None, simultaneousPower=None, name=None, constraint=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if maxPower is not None:
            self.maxPower = maxPower

        if simultaneousPower is not None:
            self.simultaneousPower = simultaneousPower

        if name is not None:
            self.name = name

        if energyasset is not None:
            self.energyasset = energyasset

        if profile:
            self.profile.extend(profile)

        if carrier is not None:
            self.carrier = carrier

        if constraint:
            self.constraint.extend(constraint)


class EconomicProperties(EObject, metaclass=MetaEClass):
    """(experimental) Can be used to define the economic properties of an area"""
    averageIncome = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    averageWOZvalue = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    percentageOwnerOccupiedProperties = EAttribute(
        eType=EDouble, unique=True, derived=False, changeable=True)
    percentageHousingAssociation = EAttribute(
        eType=EDouble, unique=True, derived=False, changeable=True)
    percentagePrivateRental = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, averageIncome=None, averageWOZvalue=None, percentageOwnerOccupiedProperties=None, percentageHousingAssociation=None, percentagePrivateRental=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if averageIncome is not None:
            self.averageIncome = averageIncome

        if averageWOZvalue is not None:
            self.averageWOZvalue = averageWOZvalue

        if percentageOwnerOccupiedProperties is not None:
            self.percentageOwnerOccupiedProperties = percentageOwnerOccupiedProperties

        if percentageHousingAssociation is not None:
            self.percentageHousingAssociation = percentageHousingAssociation

        if percentagePrivateRental is not None:
            self.percentagePrivateRental = percentagePrivateRental


class SocialProperties(EObject, metaclass=MetaEClass):
    """(experimental) Can be used to define the social properties of an area"""
    socialCohesion = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    populationDensity = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    numberOfInhabitants = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)

    def __init__(self, *, socialCohesion=None, populationDensity=None, numberOfInhabitants=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if socialCohesion is not None:
            self.socialCohesion = socialCohesion

        if populationDensity is not None:
            self.populationDensity = populationDensity

        if numberOfInhabitants is not None:
            self.numberOfInhabitants = numberOfInhabitants


@abstract
class Item(EObject, metaclass=MetaEClass):
    """Class describing an abstract thing in an energy system. It is the parent of many other classes in ESDL, such as Assets, Services and Potentials. Parties can own Items"""
    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True, iD=True)
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    shortName = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    description = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    originalIdInSource = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    isOwnedBy = EReference(ordered=True, unique=True, containment=False, derived=False)
    dataSource = EReference(ordered=True, unique=True, containment=True, derived=False)
    sector = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, id=None, name=None, shortName=None, isOwnedBy=None, description=None, originalIdInSource=None, dataSource=None, sector=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if name is not None:
            self.name = name

        if shortName is not None:
            self.shortName = shortName

        if description is not None:
            self.description = description

        if originalIdInSource is not None:
            self.originalIdInSource = originalIdInSource

        if isOwnedBy is not None:
            self.isOwnedBy = isOwnedBy

        if dataSource is not None:
            self.dataSource = dataSource

        if sector is not None:
            self.sector = sector


class Instance(EObject, metaclass=MetaEClass):
    """Instances are used to represent different representations of the same EnergySystem. Most of the times only one Instance will be used. The primary use case for having more than one Instance is when you have different aggregations of the same EnergySystem in the same model (e.g. the same region on house level and aggregated on neighbourhood level). Another option would be to create different instances for different years (to describe the progress of the energy transition)."""
    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True, iD=True)
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    description = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    detailLevel = EAttribute(eType=AreaScopeEnum, unique=True, derived=False,
                             changeable=True, default_value=AreaScopeEnum.UNDEFINED)
    aggrType = EAttribute(eType=AggrTypeEnum, unique=True, derived=False, changeable=True)
    area = EReference(ordered=True, unique=True, containment=True, derived=False)
    date = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, id=None, name=None, description=None, detailLevel=None, aggrType=None, area=None, date=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if name is not None:
            self.name = name

        if description is not None:
            self.description = description

        if detailLevel is not None:
            self.detailLevel = detailLevel

        if aggrType is not None:
            self.aggrType = aggrType

        if area is not None:
            self.area = area

        if date is not None:
            self.date = date


class Carriers(EObject, metaclass=MetaEClass):
    """Collection of carriers as part of the Energy System Information. Both energy carriers and commodities."""
    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True, iD=True)
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    description = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    carrier = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    dataSource = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, carrier=None, dataSource=None, id=None, name=None, description=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if name is not None:
            self.name = name

        if description is not None:
            self.description = description

        if carrier:
            self.carrier.extend(carrier)

        if dataSource is not None:
            self.dataSource = dataSource


class EnergySystemInformation(EObject, metaclass=MetaEClass):
    """Describes reusable information of the energy system, that other classes can refer to in this energy system, such as carriers, profiles, data sources, quantity and units."""
    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True, iD=True)
    carriers = EReference(ordered=True, unique=True, containment=True, derived=False)
    profiles = EReference(ordered=True, unique=True, containment=True, derived=False)
    dataSources = EReference(ordered=True, unique=True, containment=True, derived=False)
    mobilityFuelInformation = EReference(ordered=True, unique=True, containment=True, derived=False)
    quantityAndUnits = EReference(ordered=True, unique=True, containment=True, derived=False)
    sectors = EReference(ordered=True, unique=True, containment=True, derived=False)
    buildingUsageInformation = EReference(
        ordered=True, unique=True, containment=True, derived=False)
    notes = EReference(ordered=True, unique=True, containment=True, derived=False)
    matters = EReference(ordered=True, unique=True, containment=True, derived=False)
    environmentalProfiles = EReference(ordered=True, unique=True, containment=True, derived=False)
    dataconfigurations = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, carriers=None, profiles=None, dataSources=None, mobilityFuelInformation=None, quantityAndUnits=None, sectors=None, id=None, buildingUsageInformation=None, notes=None, matters=None, environmentalProfiles=None, dataconfigurations=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if carriers is not None:
            self.carriers = carriers

        if profiles is not None:
            self.profiles = profiles

        if dataSources is not None:
            self.dataSources = dataSources

        if mobilityFuelInformation is not None:
            self.mobilityFuelInformation = mobilityFuelInformation

        if quantityAndUnits is not None:
            self.quantityAndUnits = quantityAndUnits

        if sectors is not None:
            self.sectors = sectors

        if buildingUsageInformation is not None:
            self.buildingUsageInformation = buildingUsageInformation

        if notes is not None:
            self.notes = notes

        if matters is not None:
            self.matters = matters

        if environmentalProfiles is not None:
            self.environmentalProfiles = environmentalProfiles

        if dataconfigurations is not None:
            self.dataconfigurations = dataconfigurations


@abstract
class GenericProfile(EObject, metaclass=MetaEClass):
    """All profiles should describe these fields: a name and a ProfileType. There are two different profile types: static, with static values stored in the ESDL model itself. And External, which allows you to refer to an externally defined profile (e.g. in an Energy Information System or a timeseries database)"""
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    profileType = EAttribute(eType=ProfileTypeEnum, unique=True, derived=False,
                             changeable=True, default_value=ProfileTypeEnum.UNDEFINED)
    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True, iD=True)
    interpolationMethod = EAttribute(eType=InterpolationMethodEnum, unique=True,
                                     derived=False, changeable=True, default_value=InterpolationMethodEnum.UNDEFINED)
    dataSource = EReference(ordered=True, unique=True, containment=True, derived=False)
    profileQuantityAndUnit = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, name=None, profileType=None, id=None, dataSource=None, profileQuantityAndUnit=None, interpolationMethod=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if profileType is not None:
            self.profileType = profileType

        if id is not None:
            self.id = id

        if interpolationMethod is not None:
            self.interpolationMethod = interpolationMethod

        if dataSource is not None:
            self.dataSource = dataSource

        if profileQuantityAndUnit is not None:
            self.profileQuantityAndUnit = profileQuantityAndUnit

    def getProfile(self, from_=None, to=None, aggregationPrecision=None):

        raise NotImplementedError('operation getProfile(...) not yet implemented')

    def setProfile(self, profileElementList=None):

        raise NotImplementedError('operation setProfile(...) not yet implemented')


class ProfileElement(EObject, metaclass=MetaEClass):
    """ProfileElement describes a single profile element describing a range and a value which is valid for this range. From-field is inclusive, To-field is exclusive, allowing you to describe ranges such as 1-1-2017T00:00:00.000 to 1-1-2018T00:00:00.000 instead of 31-12-2017T23:59:59:999. The to-field may be ommitted, meaning this value is valid for all time after the specified to-datetime.
Examples: The heat demand of a municipality in 2013 is 20 PJ. The range you define is then from 1-1-2013T to 1-1-2014T and the value 20 and ProfileType ENERGY_IN_PJ"""
    from_ = EAttribute(eType=EDate, unique=True, derived=False, changeable=True)
    to = EAttribute(eType=EDate, unique=True, derived=False, changeable=True)
    value = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, from_=None, to=None, value=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if from_ is not None:
            self.from_ = from_

        if to is not None:
            self.to = to

        if value is not None:
            self.value = value


@abstract
class GenericDistribution(EObject, metaclass=MetaEClass):
    """Abstract class to represent different types of distributions"""
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, name=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name


class Percentile(EObject, metaclass=MetaEClass):
    """Defines the percentile of a percentile distribution"""
    percentile = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    value = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, percentile=None, value=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if percentile is not None:
            self.percentile = percentile

        if value is not None:
            self.value = value


class CostInformation(EObject, metaclass=MetaEClass):
    """Describes the costs to acquire, install and maintain a certain asset."""
    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True, iD=True)
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    description = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    referenceYear = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    investmentCosts = EReference(ordered=True, unique=True, containment=True, derived=False)
    installationCosts = EReference(ordered=True, unique=True, containment=True, derived=False)
    fixedOperationalAndMaintenanceCosts = EReference(
        ordered=True, unique=True, containment=True, derived=False)
    marginalCosts = EReference(ordered=True, unique=True, containment=True, derived=False)
    variableOperationalAndMaintenanceCosts = EReference(
        ordered=True, unique=True, containment=True, derived=False)
    discountRate = EReference(ordered=True, unique=True, containment=True, derived=False)
    variableOperationalCosts = EReference(
        ordered=True, unique=True, containment=True, derived=False)
    fixedMaintenanceCosts = EReference(ordered=True, unique=True, containment=True, derived=False)
    fixedOperationalCosts = EReference(ordered=True, unique=True, containment=True, derived=False)
    variableMaintenanceCosts = EReference(
        ordered=True, unique=True, containment=True, derived=False)
    developmentCosts = EReference(ordered=True, unique=True, containment=True, derived=False)
    decommissioningCosts = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, investmentCosts=None, installationCosts=None, fixedOperationalAndMaintenanceCosts=None, marginalCosts=None, variableOperationalAndMaintenanceCosts=None, id=None, discountRate=None, variableOperationalCosts=None, fixedMaintenanceCosts=None, fixedOperationalCosts=None, variableMaintenanceCosts=None, developmentCosts=None, name=None, description=None, referenceYear=None, decommissioningCosts=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if name is not None:
            self.name = name

        if description is not None:
            self.description = description

        if referenceYear is not None:
            self.referenceYear = referenceYear

        if investmentCosts is not None:
            self.investmentCosts = investmentCosts

        if installationCosts is not None:
            self.installationCosts = installationCosts

        if fixedOperationalAndMaintenanceCosts is not None:
            self.fixedOperationalAndMaintenanceCosts = fixedOperationalAndMaintenanceCosts

        if marginalCosts is not None:
            self.marginalCosts = marginalCosts

        if variableOperationalAndMaintenanceCosts is not None:
            self.variableOperationalAndMaintenanceCosts = variableOperationalAndMaintenanceCosts

        if discountRate is not None:
            self.discountRate = discountRate

        if variableOperationalCosts is not None:
            self.variableOperationalCosts = variableOperationalCosts

        if fixedMaintenanceCosts is not None:
            self.fixedMaintenanceCosts = fixedMaintenanceCosts

        if fixedOperationalCosts is not None:
            self.fixedOperationalCosts = fixedOperationalCosts

        if variableMaintenanceCosts is not None:
            self.variableMaintenanceCosts = variableMaintenanceCosts

        if developmentCosts is not None:
            self.developmentCosts = developmentCosts

        if decommissioningCosts is not None:
            self.decommissioningCosts = decommissioningCosts


class StringItem(EObject, metaclass=MetaEClass):
    """Defines a label and a percentage, used in StringLabelDistribution"""
    label = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    value = EAttribute(eType=EDouble, unique=True, derived=False,
                       changeable=True, default_value=0.0)

    def __init__(self, *, label=None, value=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if label is not None:
            self.label = label

        if value is not None:
            self.value = value


class EnergyLabelBin(EObject, metaclass=MetaEClass):
    """Defines a bin for an energy label with a percentage, used in EnergyLabelDistribution"""
    energyLabel = EAttribute(eType=EnergyLabelEnum, unique=True, derived=False, changeable=True)
    percentage = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, energyLabel=None, percentage=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if energyLabel is not None:
            self.energyLabel = energyLabel

        if percentage is not None:
            self.percentage = percentage


@abstract
class FromToItem(EObject, metaclass=MetaEClass):
    """Defines a range and a percentage, used in the FromToDistribution class"""
    value = EAttribute(eType=EDouble, unique=True, derived=False,
                       changeable=True, default_value=0.0)

    def __init__(self, *, value=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if value is not None:
            self.value = value


class PItemStat(EObject, metaclass=MetaEClass):
    """(experimental) Used to define statistical information"""
    value = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    sigma = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, value=None, sigma=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if value is not None:
            self.value = value

        if sigma is not None:
            self.sigma = sigma


@abstract
class AbstractVariance(EObject, metaclass=MetaEClass):
    """(experimental) Used to define statistical information"""

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


class Party(EObject, metaclass=MetaEClass):
    """Defines a stakeholder in the energy system, to represent ownership"""
    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True, iD=True)
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    shortName = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    owns = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    ownsArea = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    sector = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, owns=None, id=None, name=None, shortName=None, ownsArea=None, sector=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if name is not None:
            self.name = name

        if shortName is not None:
            self.shortName = shortName

        if owns:
            self.owns.extend(owns)

        if ownsArea:
            self.ownsArea.extend(ownsArea)

        if sector is not None:
            self.sector = sector


@abstract
class Geometry(EObject, metaclass=MetaEClass):
    """Abstract class to define the shape/location of an asset or area. Parent class of e.g. Point, Line and Polygon"""
    CRS = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, CRS=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if CRS is not None:
            self.CRS = CRS


@abstract
class Carrier(EObject, metaclass=MetaEClass):
    """Abstract class to define the carrier of energy, e.g. a energy carrier or a commodity (such as electricity)"""
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True, iD=True)
    cost = EReference(ordered=True, unique=True, containment=True, derived=False)
    dataSource = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, name=None, id=None, cost=None, dataSource=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if id is not None:
            self.id = id

        if cost is not None:
            self.cost = cost

        if dataSource is not None:
            self.dataSource = dataSource


class Duration(EObject, metaclass=MetaEClass):
    """Defines the duration of a profile query"""
    value = EAttribute(eType=ELong, unique=True, derived=False, changeable=True)
    durationUnit = EAttribute(eType=DurationUnitEnum, unique=True, derived=False,
                              changeable=True, default_value=DurationUnitEnum.SECOND)

    def __init__(self, *, value=None, durationUnit=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if value is not None:
            self.value = value

        if durationUnit is not None:
            self.durationUnit = durationUnit


class Profiles(EObject, metaclass=MetaEClass):
    """Container for profiles in the Energy System Information where other profiles can refer to"""
    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    description = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    profile = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, profile=None, id=None, name=None, description=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if name is not None:
            self.name = name

        if description is not None:
            self.description = description

        if profile:
            self.profile.extend(profile)


class Parties(EObject, metaclass=MetaEClass):
    """Container for parties that have a role in the energy system"""
    party = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, party=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if party:
            self.party.extend(party)


class DataSources(EObject, metaclass=MetaEClass):
    """Collection of datasources used in the energy system"""
    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True, iD=True)
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    description = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    dataSource = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, dataSource=None, id=None, name=None, description=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if name is not None:
            self.name = name

        if description is not None:
            self.description = description

        if dataSource:
            self.dataSource.extend(dataSource)


class SubPolygon(EObject, metaclass=MetaEClass):
    """Part of a Polygon used to describe the internal or external boundary"""
    point = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, point=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if point:
            self.point.extend(point)


class MobilityFuelInformation(EObject, metaclass=MetaEClass):
    """Collection of information about vehicles, fuels and efficiency"""
    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True, iD=True)
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    description = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    vehicleFuelEfficiency = EReference(ordered=True, unique=True,
                                       containment=True, derived=False, upper=-1)
    dataSource = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, vehicleFuelEfficiency=None, dataSource=None, id=None, name=None, description=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if name is not None:
            self.name = name

        if description is not None:
            self.description = description

        if vehicleFuelEfficiency:
            self.vehicleFuelEfficiency.extend(vehicleFuelEfficiency)

        if dataSource is not None:
            self.dataSource = dataSource


class VehicleFuelEfficiency(EObject, metaclass=MetaEClass):
    """Information about vehicles, fuels and efficiency, used in MobilityFuelInformation"""
    vehicleType = EAttribute(eType=VehicleTypeEnum, unique=True, derived=False, changeable=True)
    fuel = EAttribute(eType=MobilityFuelTypeEnum, unique=True, derived=False, changeable=True)
    efficiency = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, vehicleType=None, fuel=None, efficiency=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if vehicleType is not None:
            self.vehicleType = vehicleType

        if fuel is not None:
            self.fuel = fuel

        if efficiency is not None:
            self.efficiency = efficiency


class MobilityProperties(EObject, metaclass=MetaEClass):
    """(experimental) Can be used to define the mobility properties of an area"""
    numberOfVehicles = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, numberOfVehicles=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if numberOfVehicles is not None:
            self.numberOfVehicles = numberOfVehicles


class NumberOfVehicles(EObject, metaclass=MetaEClass):
    """(experimental) Provides the ability to define the number of vehicles of an area"""
    vehicleCount = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, vehicleCount=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if vehicleCount:
            self.vehicleCount.extend(vehicleCount)


class VehicleCount(EObject, metaclass=MetaEClass):
    """(experimental) Defines the number of vehicles per vehicle type"""
    type = EAttribute(eType=VehicleTypeEnum, unique=True, derived=False, changeable=True)
    count = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)

    def __init__(self, *, type=None, count=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if type is not None:
            self.type = type

        if count is not None:
            self.count = count


class Services(EObject, metaclass=MetaEClass):
    """Defines a collection of logical services used in the energy system, e.g. Demand-Response, Aggregator services, Energy markets and control strategies."""
    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True, iD=True)
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    description = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    service = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, service=None, id=None, name=None, description=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if name is not None:
            self.name = name

        if description is not None:
            self.description = description

        if service:
            self.service.extend(service)


@abstract
class AbstractDataSource(EObject, metaclass=MetaEClass):
    """Abstract class to describe data sources or references to data sources"""
    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True, iD=True)

    def __init__(self, *, id=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id


class KPIs(EObject, metaclass=MetaEClass):
    """Collection of key performance indicators of areas or assets"""
    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    description = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    kpi = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, kpi=None, id=None, description=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if description is not None:
            self.description = description

        if kpi:
            self.kpi.extend(kpi)


@abstract
class KPI(EObject, metaclass=MetaEClass):
    """Defines a key performance indicator (KPI)"""
    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    description = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    quantityAndUnit = EReference(ordered=True, unique=True, containment=True, derived=False)
    kpi = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    sector = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    carrier = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    matter = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, id=None, name=None, quantityAndUnit=None, kpi=None, description=None, sector=None, carrier=None, matter=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if name is not None:
            self.name = name

        if description is not None:
            self.description = description

        if quantityAndUnit is not None:
            self.quantityAndUnit = quantityAndUnit

        if kpi:
            self.kpi.extend(kpi)

        if sector:
            self.sector.extend(sector)

        if carrier:
            self.carrier.extend(carrier)

        if matter:
            self.matter.extend(matter)


class QuantityAndUnits(EObject, metaclass=MetaEClass):
    """Collection of QuantityAndUnitTypes defined in the EnergySystemInformation section"""
    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True, iD=True)
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    description = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    quantityAndUnit = EReference(ordered=True, unique=True,
                                 containment=True, derived=False, upper=-1)

    def __init__(self, *, quantityAndUnit=None, id=None, name=None, description=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if name is not None:
            self.name = name

        if description is not None:
            self.description = description

        if quantityAndUnit:
            self.quantityAndUnit.extend(quantityAndUnit)


@abstract
class AbstractQuantityAndUnit(EObject, metaclass=MetaEClass):
    """Abstract class to describe QuantityAndUnitTypes or references to these"""

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


@abstract
class Parameters(EObject, metaclass=MetaEClass):
    """Used to describe properties of an EnergyMarket"""
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    parameterUnit = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, name=None, parameterUnit=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if parameterUnit is not None:
            self.parameterUnit = parameterUnit


class Sectors(EObject, metaclass=MetaEClass):
    """Collection of sectors. Both Party and Item can link to a sector"""
    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True, iD=True)
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    description = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    sector = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    dataSource = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, sector=None, dataSource=None, id=None, name=None, description=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if name is not None:
            self.name = name

        if description is not None:
            self.description = description

        if sector:
            self.sector.extend(sector)

        if dataSource is not None:
            self.dataSource = dataSource


class Sector(EObject, metaclass=MetaEClass):
    """Defines a sector. Can be used for the Standaard Bedrijfsindeling (SBI) of the CBS in the Netherlands"""
    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True, iD=True)
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    description = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    code = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    dataSource = EReference(ordered=True, unique=True, containment=True, derived=False)
    sector = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, id=None, name=None, description=None, dataSource=None, code=None, sector=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if name is not None:
            self.name = name

        if description is not None:
            self.description = description

        if code is not None:
            self.code = code

        if dataSource is not None:
            self.dataSource = dataSource

        if sector:
            self.sector.extend(sector)


@abstract
class AbstractInstanceDate(EObject, metaclass=MetaEClass):
    """Abstract class to define the date or period of the validity of the data that is used in this instance """

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


class WeekSchedule(EObject, metaclass=MetaEClass):
    """Specifies a week schedule for building usage"""
    mon = EReference(ordered=True, unique=True, containment=True, derived=False)
    tue = EReference(ordered=True, unique=True, containment=True, derived=False)
    wed = EReference(ordered=True, unique=True, containment=True, derived=False)
    thu = EReference(ordered=True, unique=True, containment=True, derived=False)
    fri = EReference(ordered=True, unique=True, containment=True, derived=False)
    sat = EReference(ordered=True, unique=True, containment=True, derived=False)
    sun = EReference(ordered=True, unique=True, containment=True, derived=False)
    weekdays = EReference(ordered=True, unique=True, containment=True, derived=False)
    weekenddays = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, mon=None, tue=None, wed=None, thu=None, fri=None, sat=None, sun=None, weekdays=None, weekenddays=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if mon is not None:
            self.mon = mon

        if tue is not None:
            self.tue = tue

        if wed is not None:
            self.wed = wed

        if thu is not None:
            self.thu = thu

        if fri is not None:
            self.fri = fri

        if sat is not None:
            self.sat = sat

        if sun is not None:
            self.sun = sun

        if weekdays is not None:
            self.weekdays = weekdays

        if weekenddays is not None:
            self.weekenddays = weekenddays


class DaySchedule(EObject, metaclass=MetaEClass):
    """Specifies a day schedule as part of a week schedule. A day schedule is a collection of events with a timestamp"""
    event = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, event=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if event:
            self.event.extend(event)


class Event(EObject, metaclass=MetaEClass):
    """Event with a timestamp"""
    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    time = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    description = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    value = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, id=None, time=None, description=None, value=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if time is not None:
            self.time = time

        if description is not None:
            self.description = description

        if value is not None:
            self.value = value


@abstract
class AbstractBuildingUsage(EObject, metaclass=MetaEClass):
    """Abstract class to support references to building usages"""

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


class BuildingUsageInformation(EObject, metaclass=MetaEClass):
    """Part of Energy System Information that specifies generic building usage information that can be referenced from multiple individual buildings"""
    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True, iD=True)
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    description = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    buildingUsage = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, buildingUsage=None, id=None, name=None, description=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if name is not None:
            self.name = name

        if description is not None:
            self.description = description

        if buildingUsage:
            self.buildingUsage.extend(buildingUsage)


class BuildingTypeBin(EObject, metaclass=MetaEClass):
    """Defines a bin for a building type with a percentage, used in BuildingTypeDistribution """
    buildingType = EAttribute(eType=BuildingTypeEnum, unique=True, derived=False, changeable=True)
    percentage = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, buildingType=None, percentage=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if buildingType is not None:
            self.buildingType = buildingType

        if percentage is not None:
            self.percentage = percentage


class ResidentialBuildingTypeBin(EObject, metaclass=MetaEClass):
    """Defines a bin for a residential building type with a percentage, used in ResidentialBuildingTypeDistribution """
    residentialBuildingType = EAttribute(
        eType=ResidentialBuildingTypeEnum, unique=True, derived=False, changeable=True)
    percentage = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, residentialBuildingType=None, percentage=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if residentialBuildingType is not None:
            self.residentialBuildingType = residentialBuildingType

        if percentage is not None:
            self.percentage = percentage


class OwnershipRentalTypeBin(EObject, metaclass=MetaEClass):
    """Defines a bin for a ownership/rental type with a percentage, used in OwnershipRentalTypeDistribution """
    ownershipRentalType = EAttribute(eType=OwnershipRentalTypeEnum, unique=True,
                                     derived=False, changeable=True, default_value=OwnershipRentalTypeEnum.UNDEFINED)
    percentage = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, ownershipRentalType=None, percentage=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if ownershipRentalType is not None:
            self.ownershipRentalType = ownershipRentalType

        if percentage is not None:
            self.percentage = percentage


class CompoundMatterComponent(EObject, metaclass=MetaEClass):
    """One of the components of a CompoundMatter instance"""
    mixFraction = EAttribute(eType=EDouble, unique=True, derived=False,
                             changeable=True, default_value=0.0)
    layerWidth = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    matter = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, mixFraction=None, matter=None, layerWidth=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if mixFraction is not None:
            self.mixFraction = mixFraction

        if layerWidth is not None:
            self.layerWidth = layerWidth

        if matter is not None:
            self.matter = matter


class IntTargetKPI(EObject, metaclass=MetaEClass):

    value = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    year = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)

    def __init__(self, *, value=None, year=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if value is not None:
            self.value = value

        if year is not None:
            self.year = year


class DoubleTargetKPI(EObject, metaclass=MetaEClass):

    value = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    year = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)

    def __init__(self, *, value=None, year=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if value is not None:
            self.value = value

        if year is not None:
            self.year = year


class StringTargetKPI(EObject, metaclass=MetaEClass):

    value = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    year = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)

    def __init__(self, *, value=None, year=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if value is not None:
            self.value = value

        if year is not None:
            self.year = year


class Templates(EObject, metaclass=MetaEClass):
    """Collection of templates, e.g. asset templates.
"""
    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    description = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    assetTemplate = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, assetTemplate=None, id=None, name=None, description=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if name is not None:
            self.name = name

        if description is not None:
            self.description = description

        if assetTemplate:
            self.assetTemplate.extend(assetTemplate)


class Address(EObject, metaclass=MetaEClass):
    """The address of a building or building unit."""
    streetName = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    houseNumber = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    houseNumberLetter = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    houseNumberAnnex = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    postalCode = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    city = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    stateOrProvince = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    country = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, streetName=None, houseNumber=None, houseNumberLetter=None, houseNumberAnnex=None, postalCode=None, city=None, stateOrProvince=None, country=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if streetName is not None:
            self.streetName = streetName

        if houseNumber is not None:
            self.houseNumber = houseNumber

        if houseNumberLetter is not None:
            self.houseNumberLetter = houseNumberLetter

        if houseNumberAnnex is not None:
            self.houseNumberAnnex = houseNumberAnnex

        if postalCode is not None:
            self.postalCode = postalCode

        if city is not None:
            self.city = city

        if stateOrProvince is not None:
            self.stateOrProvince = stateOrProvince

        if country is not None:
            self.country = country


class LabelJump(EObject, metaclass=MetaEClass):

    fromLabel = EAttribute(eType=EnergyLabelEnum, unique=True, derived=False, changeable=True)
    toLabel = EAttribute(eType=EnergyLabelEnum, unique=True, derived=False, changeable=True)
    savings = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, fromLabel=None, toLabel=None, savings=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if fromLabel is not None:
            self.fromLabel = fromLabel

        if toLabel is not None:
            self.toLabel = toLabel

        if savings is not None:
            self.savings = savings


@abstract
class BuildingInformation(EObject, metaclass=MetaEClass):
    """Super class of all different kinds of extra information that can be specified for a building"""

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


class Table(EObject, metaclass=MetaEClass):
    """Table class that represents data in a table structure. Current examples are the pump curve table and a table describing the flowCoefficient of a checkvalve (relation between pressure drop and flow rate)"""
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    description = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    row = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    header = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    datasource = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, row=None, header=None, name=None, description=None, datasource=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if description is not None:
            self.description = description

        if row:
            self.row.extend(row)

        if header:
            self.header.extend(header)

        if datasource is not None:
            self.datasource = datasource


class TableRow(EObject, metaclass=MetaEClass):

    value = EAttribute(eType=EDouble, unique=False, derived=False, changeable=True, upper=-1)

    def __init__(self, *, value=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if value:
            self.value.extend(value)


class Notes(EObject, metaclass=MetaEClass):
    """Collection of notes that can be added to the map, like postits (with comments in HTML)"""
    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True, iD=True)
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    description = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    note = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, note=None, id=None, name=None, description=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if name is not None:
            self.name = name

        if description is not None:
            self.description = description

        if note:
            self.note.extend(note)


class Note(EObject, metaclass=MetaEClass):
    """An individual note that can have a location on the map, to document certain decisions"""
    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True, iD=True)
    title = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    author = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    text = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    date = EAttribute(eType=EDate, unique=True, derived=False, changeable=True)
    mapLocation = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, id=None, mapLocation=None, title=None, author=None, text=None, date=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if title is not None:
            self.title = title

        if author is not None:
            self.author = author

        if text is not None:
            self.text = text

        if date is not None:
            self.date = date

        if mapLocation is not None:
            self.mapLocation = mapLocation


class Matters(EObject, metaclass=MetaEClass):

    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True, iD=True)
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    description = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    dataSource = EReference(ordered=True, unique=True, containment=True, derived=False)
    matter = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, id=None, dataSource=None, matter=None, name=None, description=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if name is not None:
            self.name = name

        if description is not None:
            self.description = description

        if dataSource is not None:
            self.dataSource = dataSource

        if matter:
            self.matter.extend(matter)


class EnvironmentalProfiles(EObject, metaclass=MetaEClass):

    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True, iD=True)
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    description = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    outsideTemperatureProfile = EReference(
        ordered=True, unique=True, containment=True, derived=False)
    solarIrradianceProfile = EReference(ordered=True, unique=True, containment=True, derived=False)
    windSpeedProfile = EReference(ordered=True, unique=True, containment=True, derived=False)
    windDirectionProfile = EReference(ordered=True, unique=True, containment=True, derived=False)
    soilTemperatureProfile = EReference(ordered=True, unique=True, containment=True, derived=False)
    relativeHumidityProfile = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, outsideTemperatureProfile=None, solarIrradianceProfile=None, windSpeedProfile=None, windDirectionProfile=None, soilTemperatureProfile=None, relativeHumidityProfile=None, id=None, name=None, description=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if name is not None:
            self.name = name

        if description is not None:
            self.description = description

        if outsideTemperatureProfile is not None:
            self.outsideTemperatureProfile = outsideTemperatureProfile

        if solarIrradianceProfile is not None:
            self.solarIrradianceProfile = solarIrradianceProfile

        if windSpeedProfile is not None:
            self.windSpeedProfile = windSpeedProfile

        if windDirectionProfile is not None:
            self.windDirectionProfile = windDirectionProfile

        if soilTemperatureProfile is not None:
            self.soilTemperatureProfile = soilTemperatureProfile

        if relativeHumidityProfile is not None:
            self.relativeHumidityProfile = relativeHumidityProfile


@abstract
class AbstractBehaviour(EObject, metaclass=MetaEClass):
    """Abstract class for specification of the (dynamic) behaviour of an asset"""
    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, id=None, name=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if name is not None:
            self.name = name


class PortRelation(EObject, metaclass=MetaEClass):
    """Specifies the relation between a port and the main port using a specific ratio."""
    ratio = EAttribute(eType=EDouble, unique=True, derived=False,
                       changeable=True, default_value=0.0)
    port = EReference(ordered=True, unique=True, containment=False, derived=False)
    quantityAndUnit = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, ratio=None, port=None, quantityAndUnit=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if ratio is not None:
            self.ratio = ratio

        if port is not None:
            self.port = port

        if quantityAndUnit is not None:
            self.quantityAndUnit = quantityAndUnit


class BufferDistance(EObject, metaclass=MetaEClass):
    """Buffer distance around an asset that relates to risks, environment, noise, CO2, ..."""
    type = EAttribute(eType=BufferDistanceTypeEnum, unique=True, derived=False, changeable=True)
    distance = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, type=None, distance=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if type is not None:
            self.type = type

        if distance is not None:
            self.distance = distance


class Group(EObject, metaclass=MetaEClass):
    """Logical grouping of elements in an EnergySystem. Can be used to indicate which assets belong to a certain Plan"""
    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    description = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    member = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, id=None, name=None, description=None, member=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if name is not None:
            self.name = name

        if description is not None:
            self.description = description

        if member:
            self.member.extend(member)


@abstract
class AbstractGroupMember(EObject, metaclass=MetaEClass):
    """An abstract class representing a member of a group"""
    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    description = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, id=None, name=None, description=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if name is not None:
            self.name = name

        if description is not None:
            self.description = description


@abstract
class AbstractDataConfiguration(EObject, metaclass=MetaEClass):
    """Defines a data configuration (a file or database configuration) with a name and ID. ID can be used to match or override specific settings of a DatabaseConfiguration in the client."""
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, name=None, id=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if id is not None:
            self.id = id


class DataConfigurations(EObject, metaclass=MetaEClass):
    """Defines a list of configurations to connect to data tables stored in databases or files for retrieving profile information. E.g. when profiles are stored in a relational database, a DatabaseConfiguration can be used to point DataTableProfiles to a specific database or file."""
    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    description = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    configurations = EReference(ordered=True, unique=True,
                                containment=True, derived=False, upper=-1)

    def __init__(self, *, configurations=None, id=None, name=None, description=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if name is not None:
            self.name = name

        if description is not None:
            self.description = description

        if configurations:
            self.configurations.extend(configurations)


class InPort(Port):
    """Represents a port with a positive energy direction into the asset, e.g. for a Consumer. See Port for more details"""
    connectedTo = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, connectedTo=None, **kwargs):

        super().__init__(**kwargs)

        if connectedTo:
            self.connectedTo.extend(connectedTo)


class OutPort(Port):
    """Represents a port with a positive energy direction out of the asset, e.g. for a Producer. See Port for more details"""
    connectedTo = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, connectedTo=None, **kwargs):

        super().__init__(**kwargs)

        if connectedTo:
            self.connectedTo.extend(connectedTo)


@abstract
class Asset(Item):
    """Assets are all physical thing in the EnergySystem. Assets can have a location, a geometry, commissioning and decommissioning dates, cost information (investment, installation and operation and maintenance costs)."""
    surfaceArea = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    commissioningDate = EAttribute(eType=EDate, unique=True, derived=False, changeable=True)
    decommissioningDate = EAttribute(eType=EDate, unique=True, derived=False, changeable=True)
    owner = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    technicalLifetime = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    aggregated = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    aggregationCount = EAttribute(eType=EInt, unique=True, derived=False,
                                  changeable=True, default_value=1)
    installationDuration = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    assetType = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    state = EAttribute(eType=AssetStateEnum, unique=True, derived=False, changeable=True)
    manufacturer = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    area = EReference(ordered=True, unique=True, containment=False, derived=False)
    containingBuilding = EReference(ordered=True, unique=True, containment=False, derived=False)
    geometry = EReference(ordered=True, unique=True, containment=True, derived=False)
    costInformation = EReference(ordered=True, unique=True, containment=True, derived=False)
    KPIs = EReference(ordered=True, unique=True, containment=True, derived=False)
    material = EReference(ordered=True, unique=True, containment=True, derived=False)
    bufferDistance = EReference(ordered=True, unique=True,
                                containment=True, derived=False, upper=-1)
    constraint = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    containingAsset = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, area=None, containingBuilding=None, geometry=None, costInformation=None, technicalLifetime=None, aggregated=None, aggregationCount=None, installationDuration=None, KPIs=None, assetType=None, state=None, material=None, manufacturer=None, bufferDistance=None, constraint=None, containingAsset=None, **kwargs):

        super().__init__(**kwargs)

        if surfaceArea is not None:
            self.surfaceArea = surfaceArea

        if commissioningDate is not None:
            self.commissioningDate = commissioningDate

        if decommissioningDate is not None:
            self.decommissioningDate = decommissioningDate

        if owner is not None:
            self.owner = owner

        if technicalLifetime is not None:
            self.technicalLifetime = technicalLifetime

        if aggregated is not None:
            self.aggregated = aggregated

        if aggregationCount is not None:
            self.aggregationCount = aggregationCount

        if installationDuration is not None:
            self.installationDuration = installationDuration

        if assetType is not None:
            self.assetType = assetType

        if state is not None:
            self.state = state

        if manufacturer is not None:
            self.manufacturer = manufacturer

        if area is not None:
            self.area = area

        if containingBuilding is not None:
            self.containingBuilding = containingBuilding

        if geometry is not None:
            self.geometry = geometry

        if costInformation is not None:
            self.costInformation = costInformation

        if KPIs is not None:
            self.KPIs = KPIs

        if material is not None:
            self.material = material

        if bufferDistance:
            self.bufferDistance.extend(bufferDistance)

        if constraint:
            self.constraint.extend(constraint)

        if containingAsset is not None:
            self.containingAsset = containingAsset


class Point(Geometry):
    """Describes a point geometry, which can be used for giving assets a location on a map"""
    lat = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    lon = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    elevation = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, lat=None, lon=None, elevation=None, **kwargs):

        super().__init__(**kwargs)

        if lat is not None:
            self.lat = lat

        if lon is not None:
            self.lon = lon

        if elevation is not None:
            self.elevation = elevation


class Polygon(Geometry):
    """Describes a polygon geometry, which can be used for defining the shape of an area or building"""
    exterior = EReference(ordered=True, unique=True, containment=True, derived=False)
    interior = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, exterior=None, interior=None, **kwargs):

        super().__init__(**kwargs)

        if exterior is not None:
            self.exterior = exterior

        if interior:
            self.interior.extend(interior)


class Measures(Item):
    """Collection of measures that can be applied to an energy system"""
    measure = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, measure=None, **kwargs):

        super().__init__(**kwargs)

        if measure:
            self.measure.extend(measure)


@abstract
class Service(Item):
    """Abstract class to represent logical entities in the energy system, e.g. demand response services, energy markets, etc."""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class Potential(Item):
    """Abstract class that represents energy potentials in an area, like wind potential, geothermal potential, residual heat source potential, etc."""
    geometryReference = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    aggregated = EAttribute(eType=EBoolean, unique=True, derived=False,
                            changeable=True, default_value=False)
    aggregationCount = EAttribute(eType=EInt, unique=True, derived=False,
                                  changeable=True, default_value=1)
    geometry = EReference(ordered=True, unique=True, containment=True, derived=False)
    quantityAndUnit = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, geometry=None, geometryReference=None, quantityAndUnit=None, aggregated=None, aggregationCount=None, **kwargs):

        super().__init__(**kwargs)

        if geometryReference is not None:
            self.geometryReference = geometryReference

        if aggregated is not None:
            self.aggregated = aggregated

        if aggregationCount is not None:
            self.aggregationCount = aggregationCount

        if geometry is not None:
            self.geometry = geometry

        if quantityAndUnit is not None:
            self.quantityAndUnit = quantityAndUnit


class EnergyCarrier(Carrier):
    """Defines a carrier of energy with its emission and energy content properties"""
    energyContent = EAttribute(eType=EDouble, unique=True, derived=False,
                               changeable=True, default_value=0.0)
    emission = EAttribute(eType=EDouble, unique=True, derived=False,
                          changeable=True, default_value=0.0)
    energyCarrierType = EAttribute(eType=RenewableTypeEnum, unique=True,
                                   derived=False, changeable=True)
    stateOfMatter = EAttribute(eType=StateOfMatterEnum, unique=True, derived=False,
                               changeable=True, default_value=StateOfMatterEnum.UNDEFINED)
    energyContentUnit = EReference(ordered=True, unique=True, containment=True, derived=False)
    emissionUnit = EReference(ordered=True, unique=True, containment=True, derived=False)
    composition = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, energyContent=None, emission=None, energyCarrierType=None, energyContentUnit=None, emissionUnit=None, composition=None, stateOfMatter=None, **kwargs):

        super().__init__(**kwargs)

        if energyContent is not None:
            self.energyContent = energyContent

        if emission is not None:
            self.emission = emission

        if energyCarrierType is not None:
            self.energyCarrierType = energyCarrierType

        if stateOfMatter is not None:
            self.stateOfMatter = stateOfMatter

        if energyContentUnit is not None:
            self.energyContentUnit = energyContentUnit

        if emissionUnit is not None:
            self.emissionUnit = emissionUnit

        if composition is not None:
            self.composition = composition


@abstract
class StaticProfile(GenericProfile):
    """Stores the profile in the ESDL model itself, in contrast with an external profile, which refers to an external source for a profile"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class ExternalProfile(GenericProfile):
    """ExternalProfile allows to refer to an externally defined profile. Common uses are a profile defined in a (timeseries) database such as InfluxDB.
It allows you to specify a multiplier to scale the supplied external profile by a certain factor (e.g. when using NEDU profiles). Default the multiplier is '1'."""
    multiplier = EAttribute(eType=EDouble, unique=True, derived=False,
                            changeable=True, default_value=1.0)
    startDate = EAttribute(eType=EDate, unique=True, derived=False, changeable=True)
    endDate = EAttribute(eType=EDate, unique=True, derived=False, changeable=True)

    def __init__(self, *, multiplier=None, startDate=None, endDate=None, **kwargs):

        super().__init__(**kwargs)

        if multiplier is not None:
            self.multiplier = multiplier

        if startDate is not None:
            self.startDate = startDate

        if endDate is not None:
            self.endDate = endDate


class PercentileDistribution(GenericDistribution):
    """Defines a distribution in terms of percentiles"""
    percentile = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, percentile=None, **kwargs):

        super().__init__(**kwargs)

        if percentile:
            self.percentile.extend(percentile)


@abstract
class SpecificLabelDistribution(GenericDistribution):
    """Abstract class to define a distribution with labels"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class SymmetricVariance(AbstractVariance):
    """(experimental) Used to define statistical information"""
    sigma = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, sigma=None, **kwargs):

        super().__init__(**kwargs)

        if sigma is not None:
            self.sigma = sigma


class AssymmetricVariance(AbstractVariance):
    """(experimental) Used to define statistical information"""
    sigmaMin = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    sigmaPlus = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, sigmaMin=None, sigmaPlus=None, **kwargs):

        super().__init__(**kwargs)

        if sigmaMin is not None:
            self.sigmaMin = sigmaMin

        if sigmaPlus is not None:
            self.sigmaPlus = sigmaPlus


class DoubleAssymmetricVariance(AbstractVariance):
    """(experimental) Used to define statistical information"""
    plus34perc = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    plus48perc = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    min34perc = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    min48perc = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, plus34perc=None, plus48perc=None, min34perc=None, min48perc=None, **kwargs):

        super().__init__(**kwargs)

        if plus34perc is not None:
            self.plus34perc = plus34perc

        if plus48perc is not None:
            self.plus48perc = plus48perc

        if min34perc is not None:
            self.min34perc = min34perc

        if min48perc is not None:
            self.min48perc = min48perc


class Line(Geometry):
    """Describes a line geometry based on a list of points, which can be used to define the shape of pipes and cables"""
    point = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, point=None, **kwargs):

        super().__init__(**kwargs)

        if point:
            self.point.extend(point)


@abstract
class Commodity(Carrier):
    """Abstract class for commodities"""
    emission = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    renewableFactor = EAttribute(eType=EDouble, unique=True,
                                 derived=False, changeable=True, default_value=0.0)
    emissionUnit = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, emission=None, renewableFactor=None, emissionUnit=None, **kwargs):

        super().__init__(**kwargs)

        if emission is not None:
            self.emission = emission

        if renewableFactor is not None:
            self.renewableFactor = renewableFactor

        if emissionUnit is not None:
            self.emissionUnit = emissionUnit


class DataSource(AbstractDataSource):
    """A DataSource describes the source of the piece of information used in the energy system. E.g. a profile from NEDU or typical parameters of an Asset"""
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    description = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    reference = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    attribution = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    releaseDate = EAttribute(eType=EDate, unique=True, derived=False, changeable=True)
    version = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    license = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    author = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    contactDetails = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, name=None, description=None, reference=None, attribution=None, releaseDate=None, version=None, license=None, author=None, contactDetails=None, **kwargs):

        super().__init__(**kwargs)

        if name is not None:
            self.name = name

        if description is not None:
            self.description = description

        if reference is not None:
            self.reference = reference

        if attribution is not None:
            self.attribution = attribution

        if releaseDate is not None:
            self.releaseDate = releaseDate

        if version is not None:
            self.version = version

        if license is not None:
            self.license = license

        if author is not None:
            self.author = author

        if contactDetails is not None:
            self.contactDetails = contactDetails


class MultiPolygon(Geometry):
    """Collection of Polygons"""
    polygon = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, polygon=None, **kwargs):

        super().__init__(**kwargs)

        if polygon:
            self.polygon.extend(polygon)


class QuantityAndUnitType(AbstractQuantityAndUnit):
    """Defines the quantity and its unit for a specific parameter. Used in e.g. profiles and KPIs. For example Energy in Joules or CO2 emission in kton."""
    physicalQuantity = EAttribute(eType=PhysicalQuantityEnum,
                                  unique=True, derived=False, changeable=True)
    multiplier = EAttribute(eType=MultiplierEnum, unique=True, derived=False, changeable=True)
    unit = EAttribute(eType=UnitEnum, unique=True, derived=False, changeable=True)
    perMultiplier = EAttribute(eType=MultiplierEnum, unique=True, derived=False, changeable=True)
    perUnit = EAttribute(eType=UnitEnum, unique=True, derived=False, changeable=True)
    description = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    perTimeUnit = EAttribute(eType=TimeUnitEnum, unique=True, derived=False, changeable=True)
    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True, iD=True)
    perScope = EAttribute(eType=QuantityAndUnitScopeEnum,
                          unique=True, derived=False, changeable=True)

    def __init__(self, *, physicalQuantity=None, multiplier=None, unit=None, perMultiplier=None, perUnit=None, description=None, perTimeUnit=None, id=None, perScope=None, **kwargs):

        super().__init__(**kwargs)

        if physicalQuantity is not None:
            self.physicalQuantity = physicalQuantity

        if multiplier is not None:
            self.multiplier = multiplier

        if unit is not None:
            self.unit = unit

        if perMultiplier is not None:
            self.perMultiplier = perMultiplier

        if perUnit is not None:
            self.perUnit = perUnit

        if description is not None:
            self.description = description

        if perTimeUnit is not None:
            self.perTimeUnit = perTimeUnit

        if id is not None:
            self.id = id

        if perScope is not None:
            self.perScope = perScope


class DataSourceReference(AbstractDataSource):
    """Defines a reference to a datasource, defined in the collection of DataSources (as part of the EnergySystemInformation)"""
    reference = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, reference=None, **kwargs):

        super().__init__(**kwargs)

        if reference is not None:
            self.reference = reference


class QuantityAndUnitReference(AbstractQuantityAndUnit):
    """Defines a reference to a QuantityAndUnitType defined in the collection of QuantityAndUnits (as part of the EnergySystemInformation)"""
    reference = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, reference=None, **kwargs):

        super().__init__(**kwargs)

        if reference is not None:
            self.reference = reference


class StringParameter(Parameters):
    """Defines a parameter of type String"""
    value = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class DoubleParameter(Parameters):
    """Defines a parameter of type Double"""
    value = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class IntegerParameter(Parameters):
    """Defines a parameter of type Integer"""
    value = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class BooleanParameter(Parameters):
    """Defines a parameter of type Boolean"""
    value = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class MultiLine(Geometry):
    """Defines a collection of lines"""
    line = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, line=None, **kwargs):

        super().__init__(**kwargs)

        if line:
            self.line.extend(line)


class InstanceDate(AbstractInstanceDate):
    """Describes the date of the validity of the data that is used in this instance """
    date = EAttribute(eType=EDate, unique=True, derived=False, changeable=True)

    def __init__(self, *, date=None, **kwargs):

        super().__init__(**kwargs)

        if date is not None:
            self.date = date


class InstancePeriod(AbstractInstanceDate):
    """Describes the period of the validity of the data that is used in this instance """
    fromDate = EAttribute(eType=EDate, unique=True, derived=False, changeable=True)
    toDate = EAttribute(eType=EDate, unique=True, derived=False, changeable=True)

    def __init__(self, *, fromDate=None, toDate=None, **kwargs):

        super().__init__(**kwargs)

        if fromDate is not None:
            self.fromDate = fromDate

        if toDate is not None:
            self.toDate = toDate


class WKT(Geometry):
    """Well-Known Text (see https://en.wikipedia.org/wiki/Well-known_text)"""
    value = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class WKB(Geometry):
    """Well-Known Binary (See https://en.wikipedia.org/wiki/Well-known_text#Well-known_binary)"""
    value = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class BuildingUsage(AbstractBuildingUsage):
    """Collection of information about the usage of a building, such as temperature set points and opening hours."""
    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True, iD=True)
    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    coolingSetpoints = EReference(ordered=True, unique=True, containment=True, derived=False)
    heatingSetpoints = EReference(ordered=True, unique=True, containment=True, derived=False)
    openingHours = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, id=None, name=None, coolingSetpoints=None, heatingSetpoints=None, openingHours=None, **kwargs):

        super().__init__(**kwargs)

        if id is not None:
            self.id = id

        if name is not None:
            self.name = name

        if coolingSetpoints is not None:
            self.coolingSetpoints = coolingSetpoints

        if heatingSetpoints is not None:
            self.heatingSetpoints = heatingSetpoints

        if openingHours is not None:
            self.openingHours = openingHours


class BuildingUsageReference(AbstractBuildingUsage):
    """Specifies a reference to building usage (such as opening hours)"""
    reference = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, reference=None, **kwargs):

        super().__init__(**kwargs)

        if reference is not None:
            self.reference = reference


class DoubleKPI(KPI):
    """Specifies a KPI value as a double"""
    value = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    target = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, value=None, target=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value

        if target:
            self.target.extend(target)


class StringKPI(KPI):
    """Specifies a KPI value as a string"""
    value = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    target = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, value=None, target=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value

        if target:
            self.target.extend(target)


class IntKPI(KPI):
    """Specifies a KPI value as an integer"""
    value = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    target = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, value=None, target=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value

        if target:
            self.target.extend(target)


class FromToIntItem(FromToItem):
    """Specifies a percentage range as an integer value, as part of a distribution, e.g. for defining a period of years (1945-1960) in Aggregated Buildings"""
    from_ = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    to = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)

    def __init__(self, *, from_=None, to=None, **kwargs):

        super().__init__(**kwargs)

        if from_ is not None:
            self.from_ = from_

        if to is not None:
            self.to = to


class FromToDoubleItem(FromToItem):
    """Specifies a percentage range as an double value, as part of a distribution, e.g. for defining energy usage (2.5-5.0 GJ of hot tap water) in Aggregated Buildings"""
    from_ = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    to = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, from_=None, to=None, **kwargs):

        super().__init__(**kwargs)

        if from_ is not None:
            self.from_ = from_

        if to is not None:
            self.to = to


@abstract
class Restriction(Item):
    """Allows to specify restrictions to measures"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class AssetTemplate(Item):
    """Template for an asset. Can be used to specify a generic asset type where specific instances can refer to and inherit properties of.
"""
    asset = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, asset=None, **kwargs):

        super().__init__(**kwargs)

        if asset is not None:
            self.asset = asset


@abstract
class GenericLabelDistribution(GenericDistribution):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class DistributionKPI(KPI):

    distribution = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, distribution=None, **kwargs):

        super().__init__(**kwargs)

        if distribution is not None:
            self.distribution = distribution


@abstract
class AbstractMeasure(Item):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class ResidentialBuildingInformation(BuildingInformation):
    """Class that contains extra information that can be specified for a residential building"""
    numberOfInhabitants = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    inhabitantsType = EAttribute(eType=InhabitantsTypeEnum, unique=True, derived=False,
                                 changeable=True, default_value=InhabitantsTypeEnum.UNDEFINED)
    residentialBuildingType = EAttribute(eType=ResidentialBuildingTypeEnum, unique=True,
                                         derived=False, changeable=True, default_value=ResidentialBuildingTypeEnum.UNDEFINED)
    ownershipRentalType = EAttribute(eType=OwnershipRentalTypeEnum, unique=True,
                                     derived=False, changeable=True, default_value=OwnershipRentalTypeEnum.UNDEFINED)

    def __init__(self, *, numberOfInhabitants=None, inhabitantsType=None, residentialBuildingType=None, ownershipRentalType=None, **kwargs):

        super().__init__(**kwargs)

        if numberOfInhabitants is not None:
            self.numberOfInhabitants = numberOfInhabitants

        if inhabitantsType is not None:
            self.inhabitantsType = inhabitantsType

        if residentialBuildingType is not None:
            self.residentialBuildingType = residentialBuildingType

        if ownershipRentalType is not None:
            self.ownershipRentalType = ownershipRentalType


class BuildingStructureInformation(BuildingInformation):

    slantedRoofArea = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    wallArea = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    roofType = EAttribute(eType=RoofTypeEnum, unique=True, derived=False, changeable=True)
    flatRoofArea = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    windowArea = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    glassType = EAttribute(eType=GlazingTypeEnum, unique=True, derived=False, changeable=True)
    height = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    orientation = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    rcWall = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    rcRoof = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    ventilationType = EAttribute(eType=VentilationTypeEnum, unique=True,
                                 derived=False, changeable=True)
    rcFloor = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    uWindow = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    perimeter = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    doorArea = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    uDoor = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, slantedRoofArea=None, wallArea=None, roofType=None, flatRoofArea=None, windowArea=None, glassType=None, height=None, orientation=None, rcWall=None, rcRoof=None, ventilationType=None, rcFloor=None, uWindow=None, perimeter=None, doorArea=None, uDoor=None, **kwargs):

        super().__init__(**kwargs)

        if slantedRoofArea is not None:
            self.slantedRoofArea = slantedRoofArea

        if wallArea is not None:
            self.wallArea = wallArea

        if roofType is not None:
            self.roofType = roofType

        if flatRoofArea is not None:
            self.flatRoofArea = flatRoofArea

        if windowArea is not None:
            self.windowArea = windowArea

        if glassType is not None:
            self.glassType = glassType

        if height is not None:
            self.height = height

        if orientation is not None:
            self.orientation = orientation

        if rcWall is not None:
            self.rcWall = rcWall

        if rcRoof is not None:
            self.rcRoof = rcRoof

        if ventilationType is not None:
            self.ventilationType = ventilationType

        if rcFloor is not None:
            self.rcFloor = rcFloor

        if uWindow is not None:
            self.uWindow = uWindow

        if perimeter is not None:
            self.perimeter = perimeter

        if doorArea is not None:
            self.doorArea = doorArea

        if uDoor is not None:
            self.uDoor = uDoor


@abstract
class AbstractMatter(Carrier):
    """Abstract class for describing Matters, can be instantiated as a subclass of Matter or as a MatterReference."""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class InputOutputRelation(AbstractBehaviour):
    """Describes the relation between one of the ports of an asset (the mainPort) and all other ports using a specific ratio. Can be used for conversion assets to specify how much of the carrier on the InPorts is required to produce an x amount of the carrier on the OutPort. """
    mainPortRelation = EReference(ordered=True, unique=True,
                                  containment=True, derived=False, upper=-1)
    mainPort = EReference(ordered=True, unique=True, containment=False, derived=False)
    mainPortQuantityAndUnit = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, mainPortRelation=None, mainPort=None, mainPortQuantityAndUnit=None, **kwargs):

        super().__init__(**kwargs)

        if mainPortRelation:
            self.mainPortRelation.extend(mainPortRelation)

        if mainPort is not None:
            self.mainPort = mainPort

        if mainPortQuantityAndUnit is not None:
            self.mainPortQuantityAndUnit = mainPortQuantityAndUnit


@abstract
class AbstractTransferFunction(AbstractBehaviour):
    """Abstract class for a TransferFunction for the specification of the behaviour of an asset"""
    type = EAttribute(eType=TransferFunctionTypeEnum, unique=True, derived=False, changeable=True)

    def __init__(self, *, type=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type


@abstract
class Constraint(Item):
    """Allows to specify constraints for asset attributes."""
    attributeReference = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, attributeReference=None, **kwargs):

        super().__init__(**kwargs)

        if attributeReference is not None:
            self.attributeReference = attributeReference


class DataSourceList(AbstractDataSource):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    description = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    dataSource = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, dataSource=None, name=None, description=None, **kwargs):

        super().__init__(**kwargs)

        if name is not None:
            self.name = name

        if description is not None:
            self.description = description

        if dataSource:
            self.dataSource.extend(dataSource)


class InstanceYear(AbstractInstanceDate):
    """Describes the year of the validity of the data that is used in this instance """
    year = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)

    def __init__(self, *, year=None, **kwargs):

        super().__init__(**kwargs)

        if year is not None:
            self.year = year


class Plan(AbstractGroupMember):
    """Plan (e.g. a policy plan) with references to its elements (assets, services, ...)"""
    element = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, element=None, **kwargs):

        super().__init__(**kwargs)

        if element:
            self.element.extend(element)


class DatabaseConfiguration(AbstractDataConfiguration):
    """Defines a configuration to access a database that contains one or more tables that is described by one or more TableBasedProfiles, in terms of the name of the database, its type and host and port. Host an port are optional and can also be defined by the client application and can be looked up by the ID of this database definition. TLS defines if the connection is secured by TLS/SSL.
Username and password required to connect to the database are to be provided by the client application, as it should not be stored in an ESDL."""
    database = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    type = EAttribute(eType=DatabaseTypeEnum, unique=True, derived=False, changeable=True)
    host = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    port = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    tls = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)

    def __init__(self, *, database=None, type=None, host=None, port=None, tls=None, **kwargs):

        super().__init__(**kwargs)

        if database is not None:
            self.database = database

        if type is not None:
            self.type = type

        if host is not None:
            self.host = host

        if port is not None:
            self.port = port

        if tls is not None:
            self.tls = tls


class FileConfiguration(AbstractDataConfiguration):
    """Configures an uri to a file that can be used for one or more TableBasedProfiles. Path can be a file location or an uri that defines how to find this file, e.g. using https:// or s3:// to identify the protocol scheme.
Keep in mind that for portability one should not refer to local files that others cannot access. In those cases a (public) database should be used, e.g. the EDR."""
    uri = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    type = EAttribute(eType=FileTypeEnum, unique=True, derived=False, changeable=True)

    def __init__(self, *, uri=None, type=None, **kwargs):

        super().__init__(**kwargs)

        if uri is not None:
            self.uri = uri

        if type is not None:
            self.type = type


class Insulation(Asset):
    """Describes insulation that can be added to a building. The relation with the heat consumption is not defined and requires manual modelling"""
    thermalInsulation = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, thermalInsulation=None, **kwargs):

        super().__init__(**kwargs)

        if thermalInsulation is not None:
            self.thermalInsulation = thermalInsulation


class LegalArea(Potential):
    """Used to define an area in which its purpose is defined by legal authorities, such as restricted areas. E.g. in areas where water is extracted, it is not allowed to plan new UTES."""
    purpose = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, purpose=None, **kwargs):

        super().__init__(**kwargs)

        if purpose is not None:
            self.purpose = purpose


@abstract
class EnergyService(Service):
    """Abstract class to represent logical entities in the energy system, e.g. demand response services, energy markets, etc."""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class WindPotential(Potential):
    """Defines the potential for wind energy. This class can be used instead of 'SearchAreaWind' in case there is more information available."""
    value = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    fullLoadHours = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    area = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    height = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, value=None, fullLoadHours=None, area=None, height=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value

        if fullLoadHours is not None:
            self.fullLoadHours = fullLoadHours

        if area is not None:
            self.area = area

        if height is not None:
            self.height = height


class DateTimeProfile(StaticProfile):
    """Describes a profile using one or more Profile elements. Each element defines a from- and a to-datetime and a value which is valid for this range. The to-field may be ommitted, meaning this value is valid for all time after the to-date."""
    element = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, element=None, **kwargs):

        super().__init__(**kwargs)

        if element:
            self.element.extend(element)


class SingleValue(StaticProfile):
    """A profile used to define a single value. This should be used when no information is present about the time. E.g. the price of a PV panel as currently known
When a model queries for a value from a certain date (and to a certain date), that information will be ignored and it will always return this value."""
    value = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class StringLabelDistribution(GenericLabelDistribution):
    """Defines a distribution in terms of self-defined labels"""
    stringItem = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, stringItem=None, **kwargs):

        super().__init__(**kwargs)

        if stringItem:
            self.stringItem.extend(stringItem)


class EnergyLabelDistribution(SpecificLabelDistribution):
    """Defines a distribution in terms of energy labels"""
    bin = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, bin=None, **kwargs):

        super().__init__(**kwargs)

        if bin:
            self.bin.extend(bin)


class FromToDistribution(GenericLabelDistribution):
    """Defines a distribution in terms of 'from' and 'to'"""
    fromToItem = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, fromToItem=None, **kwargs):

        super().__init__(**kwargs)

        if fromToItem:
            self.fromToItem.extend(fromToItem)


class URIProfile(ExternalProfile):
    """Describes a reference to a profile in an information system using a URI (e.g. a URI to a profile in Energy Information System (EIS))"""
    URI = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, URI=None, **kwargs):

        super().__init__(**kwargs)

        if URI is not None:
            self.URI = URI


@abstract
class LegacyAbstractDatabaseProfile(ExternalProfile):
    """Describes the fields of a generic database-based profile"""
    host = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    port = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    database = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    filters = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, host=None, port=None, database=None, filters=None, **kwargs):

        super().__init__(**kwargs)

        if host is not None:
            self.host = host

        if port is not None:
            self.port = port

        if database is not None:
            self.database = database

        if filters is not None:
            self.filters = filters


class GasCommodity(Commodity):
    """Defines a gas commodity. This class can be used as an abstract way of modelling gas commodity and can be used in conjunction with electricity commodity and heat commodity. If more detailed modelling is necessary, use energy carriers."""
    pressure = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, pressure=None, **kwargs):

        super().__init__(**kwargs)

        if pressure is not None:
            self.pressure = pressure


class HeatCommodity(Commodity):
    """Defines a heat commodity"""
    supplyTemperature = EAttribute(eType=EDouble, unique=True,
                                   derived=False, changeable=True, default_value=0.0)
    returnTemperature = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, supplyTemperature=None, returnTemperature=None, **kwargs):

        super().__init__(**kwargs)

        if supplyTemperature is not None:
            self.supplyTemperature = supplyTemperature

        if returnTemperature is not None:
            self.returnTemperature = returnTemperature


class ElectricityCommodity(Commodity):
    """Defines an electricity commodity"""
    voltage = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, voltage=None, **kwargs):

        super().__init__(**kwargs)

        if voltage is not None:
            self.voltage = voltage


class Range(StaticProfile):
    """Defines a range between two values. Optionally a mid value can be specified as for example a mean value or most plausible value."""
    minValue = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    maxValue = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    midValue = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, minValue=None, maxValue=None, midValue=None, **kwargs):

        super().__init__(**kwargs)

        if minValue is not None:
            self.minValue = minValue

        if maxValue is not None:
            self.maxValue = maxValue

        if midValue is not None:
            self.midValue = midValue


class SolarPotential(Potential):
    """Defines the potential for solar energy. This class can be used instead of 'SearchAreaSolar' in case there is more information available."""
    value = EAttribute(eType=EDouble, unique=True, derived=False,
                       changeable=True, default_value=0.0)
    solarPotentialType = EAttribute(eType=PVInstallationTypeEnum, unique=True,
                                    derived=False, changeable=True, default_value=PVInstallationTypeEnum.UNDEFINED)
    fullLoadHours = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    area = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    angle = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    orientation = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)

    def __init__(self, *, value=None, solarPotentialType=None, fullLoadHours=None, area=None, angle=None, orientation=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value

        if solarPotentialType is not None:
            self.solarPotentialType = solarPotentialType

        if fullLoadHours is not None:
            self.fullLoadHours = fullLoadHours

        if area is not None:
            self.area = area

        if angle is not None:
            self.angle = angle

        if orientation is not None:
            self.orientation = orientation


class ProfileReference(StaticProfile):
    """Used to refer to profiles defined in the Energy System Information section"""
    multiplier = EAttribute(eType=EDouble, unique=True, derived=False,
                            changeable=True, default_value=1.0)
    reference = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, multiplier=None, reference=None, **kwargs):

        super().__init__(**kwargs)

        if multiplier is not None:
            self.multiplier = multiplier

        if reference is not None:
            self.reference = reference


class ResidualHeatSourcePotential(Potential):
    """Defines the residual heat potential in a specific area."""
    value = EAttribute(eType=EDouble, unique=True, derived=False,
                       changeable=True, default_value=0.0)
    type = EAttribute(eType=ResidualHeatSourceTypeEnum, unique=True, derived=False, changeable=True)
    associatedConversionAsset = EReference(
        ordered=True, unique=True, containment=False, derived=False)
    residualHeatSource = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, value=None, type=None, associatedConversionAsset=None, residualHeatSource=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value

        if type is not None:
            self.type = type

        if associatedConversionAsset is not None:
            self.associatedConversionAsset = associatedConversionAsset

        if residualHeatSource is not None:
            self.residualHeatSource = residualHeatSource


class EnergyCommodity(Commodity):
    """Generic energy commodity, to be used in (national) energy balances (when the type of energy is not important)"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Measure(AbstractMeasure):
    """A single measure or a combination of measures with collective cost information that can be applied to an energy system. An example of a measure-combination would be a combination of insulation and a heat pump."""
    type = EAttribute(eType=MeasureTypeEnum, unique=True, derived=False, changeable=True)
    asset = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    costInformation = EReference(ordered=True, unique=True, containment=True, derived=False)
    restriction = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    labelJump = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, asset=None, costInformation=None, restriction=None, labelJump=None, type=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type

        if asset:
            self.asset.extend(asset)

        if costInformation is not None:
            self.costInformation = costInformation

        if restriction:
            self.restriction.extend(restriction)

        if labelJump is not None:
            self.labelJump = labelJump


@abstract
class AbstractGTPotential(Potential):
    """Abstract class to describe geothermal potential"""
    geothermalSource = EReference(ordered=True, unique=True,
                                  containment=False, derived=False, upper=-1)

    def __init__(self, *, geothermalSource=None, **kwargs):

        super().__init__(**kwargs)

        if geothermalSource:
            self.geothermalSource.extend(geothermalSource)


class UTESPotential(Potential):
    """Defines the potential for underground thermal energy storage (UTES). E.g. ATES or BTES potential"""
    value = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    type = EAttribute(eType=UTESPotentialTypeEnum, unique=True, derived=False, changeable=True)
    UTES = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, value=None, type=None, UTES=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value

        if type is not None:
            self.type = type

        if UTES:
            self.UTES.extend(UTES)


class BiomassPotential(Potential):
    """Defines the biomass potential in a specific area."""
    value = EAttribute(eType=EDouble, unique=True, derived=False,
                       changeable=True, default_value=0.0)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class Glazing(Asset):
    """Allows to specify the glass of a building, e.g. for calculating heat loss"""
    uWindow = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    glazingType = EAttribute(eType=GlazingTypeEnum, unique=True, derived=False,
                             changeable=True, default_value=GlazingTypeEnum.UNDEFINED)

    def __init__(self, *, uWindow=None, glazingType=None, **kwargs):

        super().__init__(**kwargs)

        if uWindow is not None:
            self.uWindow = uWindow

        if glazingType is not None:
            self.glazingType = glazingType


class SearchAreaWind(Potential):
    """Specifies search areas for wind turbines. Search areas are a kind of 'legal' areas that have been appointed by the (local) government as possible areas for wind installations. Further research should give insight in the real potential (in terms of energy)."""
    fullLoadHours = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    area = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    height = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, fullLoadHours=None, area=None, height=None, **kwargs):

        super().__init__(**kwargs)

        if fullLoadHours is not None:
            self.fullLoadHours = fullLoadHours

        if area is not None:
            self.area = area

        if height is not None:
            self.height = height


class SearchAreaSolar(Potential):
    """Specifies search areas for solar installations. Search areas are a kind of 'legal' areas that have been appointed by the (local) government as possible areas for solar installations. Further research should give insight in the real potential (in terms of energy)."""
    fullLoadHours = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    area = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, fullLoadHours=None, area=None, **kwargs):

        super().__init__(**kwargs)

        if fullLoadHours is not None:
            self.fullLoadHours = fullLoadHours

        if area is not None:
            self.area = area


class BuildingTypeDistribution(SpecificLabelDistribution):
    """Specifies the way the building type is distributed in this area (e.g. Utility, Residential), specifing the percentage of buildings per type."""
    bin = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, bin=None, **kwargs):

        super().__init__(**kwargs)

        if bin:
            self.bin.extend(bin)


class ResidentialBuildingTypeDistribution(SpecificLabelDistribution):
    """Specifies the way the residential building type is distributed in this area (e.g. Vrijstaande Woning, Hoekwoning, Flatwoning), specifing the percentage of buildings per residential type."""
    bin = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, bin=None, **kwargs):

        super().__init__(**kwargs)

        if bin:
            self.bin.extend(bin)


class OwnershipRentalTypeDistribution(SpecificLabelDistribution):
    """Specifies the way the housing type is distributed in this area (e.g. Owner occupied, Housing Association, Private Rental), specifing the percentage of buildings per housing type."""
    bin = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, bin=None, **kwargs):

        super().__init__(**kwargs)

        if bin:
            self.bin.extend(bin)


@abstract
class Matter(AbstractMatter):
    """Abstract class for describing matters. There are three subclasses:

- Material: for the materials of which Assets are made, but also for raw materials (e.g. water as an input for an electrolyzer)
- Fuels: for decomposing EnergyCarriers
- CompoundMatter for creating a mixture or a collection of Materials or Fuels"""
    density = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    stateOfMatter = EAttribute(eType=StateOfMatterEnum, unique=True, derived=False, changeable=True)

    def __init__(self, *, density=None, stateOfMatter=None, **kwargs):

        super().__init__(**kwargs)

        if density is not None:
            self.density = density

        if stateOfMatter is not None:
            self.stateOfMatter = stateOfMatter


class BuildingTypeRestriction(Restriction):
    """Defines a restriction on the type of building (the purpose for which the building is used)."""
    type = EAttribute(eType=BuildingTypeEnum, unique=True, derived=False, changeable=True, upper=-1)

    def __init__(self, *, type=None, **kwargs):

        super().__init__(**kwargs)

        if type:
            self.type.extend(type)


class AreaTypeRestriction(Restriction):
    """Defines a restriction on the type of area (road, railway, built, water, ...)"""
    type = EAttribute(eType=AreaTypeEnum, unique=True, derived=False, changeable=True, upper=-1)

    def __init__(self, *, type=None, **kwargs):

        super().__init__(**kwargs)

        if type:
            self.type.extend(type)


class TemplatedAsset(Asset):
    """An instantiated asset that is referring to an asset template and the specific asset. The asset template contains generic information, the specific asset contains specific information about this instance (e.g. geometry)."""
    asset = EReference(ordered=True, unique=True, containment=True, derived=False)
    template = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, asset=None, template=None, **kwargs):

        super().__init__(**kwargs)

        if asset is not None:
            self.asset = asset

        if template is not None:
            self.template = template


class MinimumLabelRestriction(Restriction):
    """Defines a restriction on the minimum label required. Allows to specify for example to only apply a heatpump in a house with energy label B or better."""
    label = EAttribute(eType=EnergyLabelEnum, unique=True, derived=False, changeable=True)

    def __init__(self, *, label=None, **kwargs):

        super().__init__(**kwargs)

        if label is not None:
            self.label = label


class MeasureReference(AbstractMeasure):

    reference = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, reference=None, **kwargs):

        super().__init__(**kwargs)

        if reference is not None:
            self.reference = reference


class InitialValue(StaticProfile):
    """Can be used to explicitely set an initial value of a certain parameter. Used as input for simulation models that calculate this parameter over time, but need a value to initialize the model."""
    value = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class MatterReference(AbstractMatter):
    """can be used to refer to a Matter from the collection of Matters (part of EnergySystemInformation)"""
    reference = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, reference=None, **kwargs):

        super().__init__(**kwargs)

        if reference is not None:
            self.reference = reference


class GenericTransferFunction(AbstractTransferFunction):
    """Generic transfer function with numerator and denominator"""
    numerator = EAttribute(eType=EDouble, unique=False, derived=False, changeable=True, upper=-1)
    denominator = EAttribute(eType=EDouble, unique=False, derived=False, changeable=True, upper=-1)

    def __init__(self, *, numerator=None, denominator=None, **kwargs):

        super().__init__(**kwargs)

        if numerator:
            self.numerator.extend(numerator)

        if denominator:
            self.denominator.extend(denominator)


class DelayTransferFunction(AbstractTransferFunction):
    """Delay transfer function with a time constant"""
    timeConstant = EAttribute(eType=EDouble, unique=True, derived=False,
                              changeable=True, default_value=0.0)

    def __init__(self, *, timeConstant=None, **kwargs):

        super().__init__(**kwargs)

        if timeConstant is not None:
            self.timeConstant = timeConstant


class CombinedTransferFunction(AbstractTransferFunction):
    """Combination of multiple transfer functions by addition of multiplication of individual components"""
    combinationFunction = EAttribute(eType=CombinationFunctionEnum,
                                     unique=True, derived=False, changeable=True)
    component = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, component=None, combinationFunction=None, **kwargs):

        super().__init__(**kwargs)

        if combinationFunction is not None:
            self.combinationFunction = combinationFunction

        if component:
            self.component.extend(component)


class TimeSeriesProfile(StaticProfile):
    """Describes a profile of which the period between the values is constant. The series of values is indexed in time order as a sequence taken at successive equally spaced points in time. It starts at the startDateTime and every next value has intervalBetweenValues seconds between them."""
    startDateTime = EAttribute(eType=EDate, unique=True, derived=False, changeable=True)
    timestep = EAttribute(eType=EInt, unique=True, derived=False,
                          changeable=True, default_value=3600)
    values = EAttribute(eType=EDouble, unique=False, derived=False, changeable=True, upper=-1)

    def __init__(self, *, startDateTime=None, timestep=None, values=None, **kwargs):

        super().__init__(**kwargs)

        if startDateTime is not None:
            self.startDateTime = startDateTime

        if timestep is not None:
            self.timestep = timestep

        if values:
            self.values.extend(values)


class ResidentialBuildingTypeRestriction(Restriction):
    """Defines a restriction on the residential type of the building (terraced, free standing, appartment, ...)."""
    type = EAttribute(eType=ResidentialBuildingTypeEnum, unique=True,
                      derived=False, changeable=True, upper=-1)

    def __init__(self, *, type=None, **kwargs):

        super().__init__(**kwargs)

        if type:
            self.type.extend(type)


class BuildingYearRestriction(Restriction):
    """Defines a restriction on the building year range"""
    range = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, range=None, **kwargs):

        super().__init__(**kwargs)

        if range is not None:
            self.range = range


class RangedConstraint(Constraint):
    """Allow to specify a certain constraint as a range (with min and max values) """
    range = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, range=None, **kwargs):

        super().__init__(**kwargs)

        if range is not None:
            self.range = range


@abstract
class ConnectableAsset(Asset):
    """Abstract class to group sub classes that have exposed ports or ports of its own"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class DataTableProfile(ExternalProfile):
    """Define timeseries data based on a data table structure, such as relational databases or file formats that store data in a table-like structure such as Parquet or Excel files.
The information defined in this data table should be sufficient to build a query using one of the supported database or file types (see AbstractDataConfiguration)."""
    tableName = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    columnName = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    timeColumnName = EAttribute(eType=EString, unique=True, derived=False,
                                changeable=True, default_value='time')
    filter = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    schema = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    configuration = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, tableName=None, columnName=None, timeColumnName=None, filter=None, schema=None, configuration=None, **kwargs):

        super().__init__(**kwargs)

        if tableName is not None:
            self.tableName = tableName

        if columnName is not None:
            self.columnName = columnName

        if timeColumnName is not None:
            self.timeColumnName = timeColumnName

        if filter is not None:
            self.filter = filter

        if schema is not None:
            self.schema = schema

        if configuration is not None:
            self.configuration = configuration


class ProfileConstraint(Constraint):
    """Allow to specify a certain constraint as a profile (varying over time)"""
    minimum = EReference(ordered=True, unique=True, containment=True, derived=False)
    maximum = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, minimum=None, maximum=None, **kwargs):

        super().__init__(**kwargs)

        if minimum is not None:
            self.minimum = minimum

        if maximum is not None:
            self.maximum = maximum


@abstract
class EnergyAsset(ConnectableAsset):
    """An abstract class that describes a connectable Asset using ports. EnergyAssets main subclasses contain the 5 capability type: Producer, Consumer, Storage, Conversion and Transport """
    port = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    controlStrategy = EReference(ordered=True, unique=True, containment=False, derived=False)
    behaviour = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, port=None, controlStrategy=None, behaviour=None, **kwargs):

        super().__init__(**kwargs)

        if port:
            self.port.extend(port)

        if controlStrategy is not None:
            self.controlStrategy = controlStrategy

        if behaviour:
            self.behaviour.extend(behaviour)


class GeothermalPotential(AbstractGTPotential):
    """Defines the geothermal potential in a specific area. This type focusses on temperature and depth of the well. See GeothermalEnergyPotental for class focussing on Energy"""
    temperature = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    depth = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    potential = EAttribute(eType=GeothermalPotentialEnum, unique=True,
                           derived=False, changeable=True)
    powerPerDoublet = EAttribute(eType=GeothermalPowerEnum, unique=True,
                                 derived=False, changeable=True, default_value=GeothermalPowerEnum.UNKNOWN)

    def __init__(self, *, temperature=None, depth=None, potential=None, powerPerDoublet=None, **kwargs):

        super().__init__(**kwargs)

        if temperature is not None:
            self.temperature = temperature

        if depth is not None:
            self.depth = depth

        if potential is not None:
            self.potential = potential

        if powerPerDoublet is not None:
            self.powerPerDoublet = powerPerDoublet


class DemandResponseService(EnergyService):
    """Indicates a service supporting demand response in the energy system"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class AggregatorService(EnergyService):
    """Indicates a aggregator service exploiting flexibility in the energy system"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class InfluxDBProfile(LegacyAbstractDatabaseProfile):
    """Describes a profile based on a measurement and field as part of an InfluxDB timeseries query"""
    measurement = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    field = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, measurement=None, field=None, **kwargs):

        super().__init__(**kwargs)

        if measurement is not None:
            self.measurement = measurement

        if field is not None:
            self.field = field


@abstract
class ControlStrategy(EnergyService):
    """Defines a control strategy for a specific asset"""
    energyAsset = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, energyAsset=None, **kwargs):

        super().__init__(**kwargs)

        if energyAsset is not None:
            self.energyAsset = energyAsset


class EnergyMarket(EnergyService):
    """Defines an EnergyMarket of the energy system. A market is defined by specifying the assets that participate in this market."""
    asset = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    carrier = EReference(ordered=True, unique=True, containment=False, derived=False)
    parameters = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    marketPrice = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, asset=None, carrier=None, parameters=None, marketPrice=None, **kwargs):

        super().__init__(**kwargs)

        if asset:
            self.asset.extend(asset)

        if carrier is not None:
            self.carrier = carrier

        if parameters:
            self.parameters.extend(parameters)

        if marketPrice is not None:
            self.marketPrice = marketPrice


class GeothermalEnergyPotential(AbstractGTPotential):
    """Defines the geothermal potential in a specific area. This type focusses on energy and depth of the well. See GeothermalPotental for class focussing on temperature"""
    depth = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    value = EAttribute(eType=EDouble, unique=True, derived=False,
                       changeable=True, default_value=0.0)

    def __init__(self, *, depth=None, value=None, **kwargs):

        super().__init__(**kwargs)

        if depth is not None:
            self.depth = depth

        if value is not None:
            self.value = value


class CompoundMatter(Matter):
    """Composition of different Matters, either mixed (mix of gasses or liquids) or layered.

Examples of layered Matters
- a construction of a wall, roof, or floor with isolation
- double or triple glazing consisting of multiple layers
- a heatnetwork pipe or electrical cable consisting of multiple layers"""
    compoundType = EAttribute(eType=CompoundTypeEnum, unique=True, derived=False, changeable=True)
    component = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, component=None, compoundType=None, **kwargs):

        super().__init__(**kwargs)

        if compoundType is not None:
            self.compoundType = compoundType

        if component:
            self.component.extend(component)


class Fuel(Matter):
    """a Fuel like wood, oil, gas, and so on."""
    energyContent = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    emission = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    energyContentUnit = EReference(ordered=True, unique=True, containment=True, derived=False)
    emissionUnit = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, energyContent=None, emission=None, energyContentUnit=None, emissionUnit=None, **kwargs):

        super().__init__(**kwargs)

        if energyContent is not None:
            self.energyContent = energyContent

        if emission is not None:
            self.emission = emission

        if energyContentUnit is not None:
            self.energyContentUnit = energyContentUnit

        if emissionUnit is not None:
            self.emissionUnit = emissionUnit


class Material(Matter):
    """a Material like copper, aluminum, wood, stone, concrete, water, styrofoam, plaster"""
    thermalConductivity = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    electricalConductivity = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    youngsModulus = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    specificHeatCapacity = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, thermalConductivity=None, electricalConductivity=None, youngsModulus=None, specificHeatCapacity=None, **kwargs):

        super().__init__(**kwargs)

        if thermalConductivity is not None:
            self.thermalConductivity = thermalConductivity

        if electricalConductivity is not None:
            self.electricalConductivity = electricalConductivity

        if youngsModulus is not None:
            self.youngsModulus = youngsModulus

        if specificHeatCapacity is not None:
            self.specificHeatCapacity = specificHeatCapacity


@abstract
class ExposedPortsAsset(ConnectableAsset):
    """Abstract class with a reference to exposed ports. It's the super class of CompoundAsset and all Buildings"""
    port = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, port=None, **kwargs):

        super().__init__(**kwargs)

        if port:
            self.port.extend(port)


@abstract
class Producer(EnergyAsset):
    """An abstract class that describes EnergyAssets that can produce energy. It is one of the 5 capabilities in ESDL"""
    prodType = EAttribute(eType=RenewableTypeEnum, unique=True, derived=False,
                          changeable=True, default_value=RenewableTypeEnum.RENEWABLE)
    operationalHours = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    fullLoadHours = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    power = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, prodType=None, operationalHours=None, fullLoadHours=None, power=None, **kwargs):

        super().__init__(**kwargs)

        if prodType is not None:
            self.prodType = prodType

        if operationalHours is not None:
            self.operationalHours = operationalHours

        if fullLoadHours is not None:
            self.fullLoadHours = fullLoadHours

        if power is not None:
            self.power = power


@abstract
class Consumer(EnergyAsset):
    """An abstract class that describes EnergyAssets that can consume energy. It is one of the 5 capabilities in ESDL"""
    consType = EAttribute(eType=ConsTypeEnum, unique=True, derived=False,
                          changeable=True, default_value=ConsTypeEnum.PRIMARY)
    power = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    operationalHours = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    fullLoadHours = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)

    def __init__(self, *, consType=None, power=None, operationalHours=None, fullLoadHours=None, **kwargs):

        super().__init__(**kwargs)

        if consType is not None:
            self.consType = consType

        if power is not None:
            self.power = power

        if operationalHours is not None:
            self.operationalHours = operationalHours

        if fullLoadHours is not None:
            self.fullLoadHours = fullLoadHours


@abstract
class Storage(EnergyAsset):
    """An abstract class that describes EnergyAssets that can store energy. It is one of the 5 capabilities in ESDL"""
    capacity = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    chargeEfficiency = EAttribute(eType=EDouble, unique=True,
                                  derived=False, changeable=True, default_value=0.0)
    dischargeEfficiency = EAttribute(eType=EDouble, unique=True,
                                     derived=False, changeable=True, default_value=0.0)
    selfDischargeRate = EAttribute(eType=EDouble, unique=True,
                                   derived=False, changeable=True, default_value=0.0)
    fillLevel = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    maxChargeRate = EAttribute(eType=EDouble, unique=True, derived=False,
                               changeable=True, default_value=0.0)
    maxDischargeRate = EAttribute(eType=EDouble, unique=True,
                                  derived=False, changeable=True, default_value=0.0)
    profile = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, capacity=None, chargeEfficiency=None, profile=None, dischargeEfficiency=None, selfDischargeRate=None, fillLevel=None, maxChargeRate=None, maxDischargeRate=None, **kwargs):

        super().__init__(**kwargs)

        if capacity is not None:
            self.capacity = capacity

        if chargeEfficiency is not None:
            self.chargeEfficiency = chargeEfficiency

        if dischargeEfficiency is not None:
            self.dischargeEfficiency = dischargeEfficiency

        if selfDischargeRate is not None:
            self.selfDischargeRate = selfDischargeRate

        if fillLevel is not None:
            self.fillLevel = fillLevel

        if maxChargeRate is not None:
            self.maxChargeRate = maxChargeRate

        if maxDischargeRate is not None:
            self.maxDischargeRate = maxDischargeRate

        if profile is not None:
            self.profile = profile


@abstract
class Conversion(EnergyAsset):
    """An abstract class that describes EnergyAssets that can convert one energy carrier into another. It is one of the 5 capabilities in ESDL"""
    operationalHours = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    fullLoadHours = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    residualHeatSourcePotential = EReference(
        ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, operationalHours=None, fullLoadHours=None, residualHeatSourcePotential=None, **kwargs):

        super().__init__(**kwargs)

        if operationalHours is not None:
            self.operationalHours = operationalHours

        if fullLoadHours is not None:
            self.fullLoadHours = fullLoadHours

        if residualHeatSourcePotential is not None:
            self.residualHeatSourcePotential = residualHeatSourcePotential


@abstract
class Transport(EnergyAsset):
    """An abstract class that describes EnergyAssets that can transport energy. It is one of the 5 capabilities in ESDL"""
    capacity = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    efficiency = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    operationalHours = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    fullLoadHours = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)

    def __init__(self, *, capacity=None, efficiency=None, operationalHours=None, fullLoadHours=None, **kwargs):

        super().__init__(**kwargs)

        if capacity is not None:
            self.capacity = capacity

        if efficiency is not None:
            self.efficiency = efficiency

        if operationalHours is not None:
            self.operationalHours = operationalHours

        if fullLoadHours is not None:
            self.fullLoadHours = fullLoadHours


@abstract
class AbstractBuilding(ExposedPortsAsset):
    """Describes the shared properties of building, building unit and aggregated building"""
    asset = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    buildingUsage = EReference(ordered=True, unique=True, containment=True, derived=False)
    potential = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    measures = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, asset=None, buildingUsage=None, potential=None, measures=None, **kwargs):

        super().__init__(**kwargs)

        if asset:
            self.asset.extend(asset)

        if buildingUsage is not None:
            self.buildingUsage = buildingUsage

        if potential:
            self.potential.extend(potential)

        if measures is not None:
            self.measures = measures


class DrivenByDemand(ControlStrategy):
    """Control strategy specifying that an asset is driven by the demand of one of the output ports"""
    outPort = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, outPort=None, **kwargs):

        super().__init__(**kwargs)

        if outPort is not None:
            self.outPort = outPort


class DrivenBySupply(ControlStrategy):
    """Control strategy specifying that an asset is driven by the supply of one of the input ports (used in ESDL-based simulation tools)"""
    inPort = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, inPort=None, **kwargs):

        super().__init__(**kwargs)

        if inPort is not None:
            self.inPort = inPort


class DrivenByProfile(ControlStrategy):
    """Control strategy specifying that an asset is driven by a profile specified in one of the ports (used in ESDL-based simulation tools)"""
    profile = EReference(ordered=True, unique=True, containment=True, derived=False)
    port = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, profile=None, port=None, **kwargs):

        super().__init__(**kwargs)

        if profile is not None:
            self.profile = profile

        if port is not None:
            self.port = port


class StorageStrategy(ControlStrategy):
    """Control strategy specifying that a storage asset is driven by two profiles specifying the marginal cost to define its charging and discharging behavior (used in ESDL-based simulation tools)"""
    marginalChargeCosts = EReference(ordered=True, unique=True, containment=True, derived=False)
    marginalDischargeCosts = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, marginalChargeCosts=None, marginalDischargeCosts=None, **kwargs):

        super().__init__(**kwargs)

        if marginalChargeCosts is not None:
            self.marginalChargeCosts = marginalChargeCosts

        if marginalDischargeCosts is not None:
            self.marginalDischargeCosts = marginalDischargeCosts


class CurtailmentStrategy(ControlStrategy):
    """Control strategy that specifies a max power at which the production is curtailed"""
    maxPower = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, maxPower=None, **kwargs):

        super().__init__(**kwargs)

        if maxPower is not None:
            self.maxPower = maxPower


class PIDController(ControlStrategy):
    """Control strategy specifying that an asset is driven by a PID controller (used in ESDL-based simulation tools)"""
    Kp = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    Ki = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    Kd = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    sensor = EReference(ordered=True, unique=True, containment=False, derived=False)
    setPoint = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, Kp=None, Ki=None, Kd=None, sensor=None, setPoint=None, **kwargs):

        super().__init__(**kwargs)

        if Kp is not None:
            self.Kp = Kp

        if Ki is not None:
            self.Ki = Ki

        if Kd is not None:
            self.Kd = Kd

        if sensor is not None:
            self.sensor = sensor

        if setPoint is not None:
            self.setPoint = setPoint


class CompoundAsset(ExposedPortsAsset):
    """Asset that can contain multiple other assets that belong together. Can for example be used for modelling a certain storage technology, that consists of individual processes for charging and discharging, next to the storage capability itself"""
    asset = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, asset=None, **kwargs):

        super().__init__(**kwargs)

        if asset:
            self.asset.extend(asset)


class PriorityStrategy(ControlStrategy):
    """A control strategy to specify a (relative) priority for an asset"""
    priority = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)

    def __init__(self, *, priority=None, **kwargs):

        super().__init__(**kwargs)

        if priority is not None:
            self.priority = priority


class Battery(Storage):
    """A battery can store electrical energy. This is a Storage capability"""
    maxChargeDischargeCycles = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    powerFactor = EAttribute(eType=EDouble, unique=True, derived=False,
                             changeable=True, default_value=0.0)

    def __init__(self, *, maxChargeDischargeCycles=None, powerFactor=None, **kwargs):

        super().__init__(**kwargs)

        if maxChargeDischargeCycles is not None:
            self.maxChargeDischargeCycles = maxChargeDischargeCycles

        if powerFactor is not None:
            self.powerFactor = powerFactor


class AggregatedConsumer(Consumer):
    """Represents an aggregation of multiple consumers as one aggregated consumer. It allows you to reference the consumers it is aggregated of by using the aggregationOf reference. Can be used to aggregate a heterogeneous collection of consumers (e.g. of different types)"""
    aggregationOf = EReference(ordered=True, unique=True,
                               containment=False, derived=False, upper=-1)

    def __init__(self, *, aggregationOf=None, **kwargs):

        super().__init__(**kwargs)

        if aggregationOf:
            self.aggregationOf.extend(aggregationOf)


class AggregatedProducer(Producer):
    """Represents an aggregation of multiple producers as one aggregated producer. It allows you to reference the producers it is aggregated of by using the aggregationOf reference. Can be used to aggregate a heterogeneous collection of producers (e.g. of different types)"""
    aggregationOf = EReference(ordered=True, unique=True,
                               containment=False, derived=False, upper=-1)

    def __init__(self, *, aggregationOf=None, **kwargs):

        super().__init__(**kwargs)

        if aggregationOf:
            self.aggregationOf.extend(aggregationOf)


class GenericConsumer(Consumer):
    """Generic consumer class that can be used in cases that the actual asset type is not important or not supported yet in ESDL"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class GenericProducer(Producer):
    """Generic producer class that can be used in cases that the actual asset type is not important or not supported yet in ESDL"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class GenericStorage(Storage):
    """Generic storage class that can be used in cases that the actual asset type is not important or not supported yet in ESDL"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class GenericTransport(Transport):
    """Generic transport class that can be used in cases that the actual asset type is not important or not supported yet in ESDL"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class AggregatedTransport(Transport):
    """Represents an aggregation of multiple transport assets as one aggregated transport asset. It allows you to reference the transport asset it is aggregated of by using the aggregationOf reference. Can be used to aggregate a heterogeneous collection of transport assets (e.g. of different types)"""
    aggregationOf = EReference(ordered=True, unique=True,
                               containment=False, derived=False, upper=-1)

    def __init__(self, *, aggregationOf=None, **kwargs):

        super().__init__(**kwargs)

        if aggregationOf:
            self.aggregationOf.extend(aggregationOf)


class AggregatedStorage(Storage):
    """Represents an aggregation of multiple storage assets as one aggregated storage asset. It allows you to reference the storage asset it is aggregated of by using the aggregationOf reference. Can be used to aggregate a heterogeneous collection of storage assets (e.g. of different types)"""
    aggregationOf = EReference(ordered=True, unique=True,
                               containment=False, derived=False, upper=-1)

    def __init__(self, *, aggregationOf=None, **kwargs):

        super().__init__(**kwargs)

        if aggregationOf:
            self.aggregationOf.extend(aggregationOf)


@abstract
class GenericBuilding(AbstractBuilding):
    """Represents a physical building"""
    buildingYear = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    type = EAttribute(eType=BuildingTypeEnum, unique=True, derived=False,
                      changeable=True, upper=-1, default_value=BuildingTypeEnum.UNDEFINED)
    floorArea = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    numberOfFloors = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    energyLabel = EAttribute(eType=EnergyLabelEnum, unique=True, derived=False,
                             changeable=True, default_value=EnergyLabelEnum.UNDEFINED)
    energyIndex = EAttribute(eType=EDouble, unique=True, derived=False,
                             changeable=True, default_value=0.0)
    address = EReference(ordered=True, unique=True, containment=True, derived=False)
    buildinginformation = EReference(ordered=True, unique=True,
                                     containment=True, derived=False, upper=-1)

    def __init__(self, *, buildingYear=None, type=None, floorArea=None, numberOfFloors=None, address=None, buildinginformation=None, energyLabel=None, energyIndex=None, **kwargs):

        super().__init__(**kwargs)

        if buildingYear is not None:
            self.buildingYear = buildingYear

        if type:
            self.type.extend(type)

        if floorArea is not None:
            self.floorArea = floorArea

        if numberOfFloors is not None:
            self.numberOfFloors = numberOfFloors

        if energyLabel is not None:
            self.energyLabel = energyLabel

        if energyIndex is not None:
            self.energyIndex = energyIndex

        if address is not None:
            self.address = address

        if buildinginformation:
            self.buildinginformation.extend(buildinginformation)


class HeatStorage(Storage):
    """Generic heat storage asset with min and max temperatures"""
    minStorageTemperature = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    maxStorageTemperature = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    volume = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, minStorageTemperature=None, maxStorageTemperature=None, volume=None, **kwargs):

        super().__init__(**kwargs)

        if minStorageTemperature is not None:
            self.minStorageTemperature = minStorageTemperature

        if maxStorageTemperature is not None:
            self.maxStorageTemperature = maxStorageTemperature

        if volume is not None:
            self.volume = volume


class Import(Producer):
    """Represents a source that delivers imported energy into the current energy system. Used to model the rest of the energy system that is out of the current scope"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Export(Consumer):
    """Represents a consumer that consumes exported energy from the current energy system. Used to model the rest of the energy system that is out of the current scope"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class HeatingDemand(Consumer):
    """Describes the heating demand of e.g. a household, area, etc."""
    type = EAttribute(eType=HeatDemandTypeEnum, unique=True, derived=False, changeable=True)
    deviceType = EAttribute(eType=HeatRadiationDeviceTypeEnum,
                            unique=True, derived=False, changeable=True)
    minTemperature = EAttribute(eType=EDouble, unique=True, derived=False,
                                changeable=True, default_value=0.0)
    maxTemperature = EAttribute(eType=EDouble, unique=True, derived=False,
                                changeable=True, default_value=0.0)

    def __init__(self, *, type=None, deviceType=None, minTemperature=None, maxTemperature=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type

        if deviceType is not None:
            self.deviceType = deviceType

        if minTemperature is not None:
            self.minTemperature = minTemperature

        if maxTemperature is not None:
            self.maxTemperature = maxTemperature


class ElectricityDemand(Consumer):
    """Describes the electricity demand of e.g. a household, area, etc."""
    powerFactor = EAttribute(eType=EDouble, unique=True, derived=False,
                             changeable=True, default_value=0.0)

    def __init__(self, *, powerFactor=None, **kwargs):

        super().__init__(**kwargs)

        if powerFactor is not None:
            self.powerFactor = powerFactor


class GasDemand(Consumer):
    """Describes the gas demand of e.g. a household, area, etc. This can be used for all types of gasses (e.g. CO2, Natural Gas, Hydrogen, etc.)"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class EVChargingStation(Consumer):
    """Represents a charging station for electrical vehicles. Both single private-owned car chargers and public charging spaces can be modelled by this class"""
    powerFactor = EAttribute(eType=EDouble, unique=True, derived=False,
                             changeable=True, default_value=0.0)

    def __init__(self, *, powerFactor=None, **kwargs):

        super().__init__(**kwargs)

        if powerFactor is not None:
            self.powerFactor = powerFactor


class AggregatedBuilding(AbstractBuilding):
    """Represents more than one building aggregated into one entity. It supports different types of aggregation, such as building type, energy label etc."""
    numberOfBuildings = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    floorArea = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    aggregationOf = EReference(ordered=True, unique=True,
                               containment=False, derived=False, upper=-1)
    energyLabelDistribution = EReference(ordered=True, unique=True, containment=True, derived=False)
    buildingYearDistribution = EReference(
        ordered=True, unique=True, containment=True, derived=False)
    buildingTypeDistribution = EReference(
        ordered=True, unique=True, containment=True, derived=False)
    residentialBuildingTypeDistribution = EReference(
        ordered=True, unique=True, containment=True, derived=False)
    ownershipRentalTypeDistribution = EReference(
        ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, aggregationOf=None, numberOfBuildings=None, energyLabelDistribution=None, buildingYearDistribution=None, buildingTypeDistribution=None, residentialBuildingTypeDistribution=None, ownershipRentalTypeDistribution=None, floorArea=None, **kwargs):

        super().__init__(**kwargs)

        if numberOfBuildings is not None:
            self.numberOfBuildings = numberOfBuildings

        if floorArea is not None:
            self.floorArea = floorArea

        if aggregationOf:
            self.aggregationOf.extend(aggregationOf)

        if energyLabelDistribution is not None:
            self.energyLabelDistribution = energyLabelDistribution

        if buildingYearDistribution is not None:
            self.buildingYearDistribution = buildingYearDistribution

        if buildingTypeDistribution is not None:
            self.buildingTypeDistribution = buildingTypeDistribution

        if residentialBuildingTypeDistribution is not None:
            self.residentialBuildingTypeDistribution = residentialBuildingTypeDistribution

        if ownershipRentalTypeDistribution is not None:
            self.ownershipRentalTypeDistribution = ownershipRentalTypeDistribution


class Losses(Consumer):
    """Used to define losses explicitly (as a Consumer capability)"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class CCS(Storage):
    """Represents Carbon Capture and Storage"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class CoolingDemand(Consumer):
    """Describes the cooling demand of e.g. a building"""
    deviceType = EAttribute(eType=CoolingDeviceType, unique=True, derived=False, changeable=True)

    def __init__(self, *, deviceType=None, **kwargs):

        super().__init__(**kwargs)

        if deviceType is not None:
            self.deviceType = deviceType


class EnergyDemand(Consumer):
    """Allows to describe the total energy demand when differentiation between energy carriers is not possible or required, otherwise e.g. ElectricityDemand or HeatingDemand is an alternative"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class MobilityDemand(Consumer):
    """Energy demand of the mobility sector. Allows to specify the vehicle types, fuel types and their efficiency and distance travelled"""
    type = EAttribute(eType=VehicleTypeEnum, unique=True, derived=False, changeable=True, upper=-1)
    fuelType = EAttribute(eType=MobilityFuelTypeEnum, unique=True, derived=False, changeable=True)
    distance = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    efficiency = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, type=None, fuelType=None, distance=None, efficiency=None, **kwargs):

        super().__init__(**kwargs)

        if type:
            self.type.extend(type)

        if fuelType is not None:
            self.fuelType = fuelType

        if distance is not None:
            self.distance = distance

        if efficiency is not None:
            self.efficiency = efficiency


class GasStorage(Storage):
    """Defines a gas storage asset, see also CCS"""
    minStoragePressure = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    maxStoragePressure = EAttribute(eType=EDouble, unique=True,
                                    derived=False, changeable=True, default_value=0.0)
    volume = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    workingVolume = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, minStoragePressure=None, maxStoragePressure=None, volume=None, workingVolume=None, **kwargs):

        super().__init__(**kwargs)

        if minStoragePressure is not None:
            self.minStoragePressure = minStoragePressure

        if maxStoragePressure is not None:
            self.maxStoragePressure = maxStoragePressure

        if volume is not None:
            self.volume = volume

        if workingVolume is not None:
            self.workingVolume = workingVolume


class EnergyNetwork(Transport):
    """Defines an energy network. Used for national energy balances, when the specific energy carrier is not required"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class AbstractConductor(Transport):
    """Abstract class to describe conductors such as cables and pipes and joining them using a joint"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class AbstractSwitch(Transport):
    """Abstract class to describe switches such as valve and a circuit breaker"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class AbstractTransformer(Transport):
    """Abstract class to describe transformers, such as Heat exchangers, transformers and pumps"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class AbstractConnection(Transport):
    """Abstract class to describe connections of a building to a grid. E.g. a heat connection, gas connection and electricity connection"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class PVTInstallation(Producer):
    """Defines an installation that combines PV and thermal energy collection"""
    type = EAttribute(eType=SolarCollectorTypeEnum, unique=True, derived=False,
                      changeable=True, default_value=SolarCollectorTypeEnum.UNDEFINED)
    powerFactor = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, type=None, powerFactor=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type

        if powerFactor is not None:
            self.powerFactor = powerFactor


@abstract
class AbstractSensor(Transport):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class SinkConsumer(Consumer):
    """(Deprecated, will be removed in future ESDL versions) Represents a consumer that consumes exported energy from the current energy system. Used to model the rest of the energy system that is out of the current scope"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class SourceProducer(Producer):
    """(Deprecated, will be removed in future ESDL versions) Represents a source that delivers imported energy into the current energy system. Used to model the rest of the energy system that is out of the current scope"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class AirVessel(Transport):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class ElectricityProducer(Producer):
    """Describes a (generic) electricity producing asset"""
    minPower = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    powerFactor = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, minPower=None, powerFactor=None, **kwargs):

        super().__init__(**kwargs)

        if minPower is not None:
            self.minPower = minPower

        if powerFactor is not None:
            self.powerFactor = powerFactor


class HeatProducer(Producer):
    """Describes a (generic) heat producing asset"""
    minTemperature = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    maxTemperature = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, minTemperature=None, maxTemperature=None, **kwargs):

        super().__init__(**kwargs)

        if minTemperature is not None:
            self.minTemperature = minTemperature

        if maxTemperature is not None:
            self.maxTemperature = maxTemperature


class GasProducer(Producer):
    """Describes a (generic) gas producing asset"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class HybridHeatPump(Conversion):
    """Hybrid heatpump with both an electric heatpump and a gasheater part"""
    gasHeaterThermalPower = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    gasHeaterEfficiency = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    heatPumpThermalPower = EAttribute(eType=EDouble, unique=True,
                                      derived=False, changeable=True, default_value=0.0)
    heatPumpCOP = EAttribute(eType=EDouble, unique=True, derived=False,
                             changeable=True, default_value=0.0)
    heatPumpCoolingPower = EAttribute(eType=EDouble, unique=True,
                                      derived=False, changeable=True, default_value=0.0)
    heatPumpCoolingCOP = EAttribute(eType=EDouble, unique=True,
                                    derived=False, changeable=True, default_value=0.0)
    powerFactor = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, gasHeaterThermalPower=None, gasHeaterEfficiency=None, heatPumpThermalPower=None, heatPumpCOP=None, heatPumpCoolingPower=None, heatPumpCoolingCOP=None, powerFactor=None, **kwargs):

        super().__init__(**kwargs)

        if gasHeaterThermalPower is not None:
            self.gasHeaterThermalPower = gasHeaterThermalPower

        if gasHeaterEfficiency is not None:
            self.gasHeaterEfficiency = gasHeaterEfficiency

        if heatPumpThermalPower is not None:
            self.heatPumpThermalPower = heatPumpThermalPower

        if heatPumpCOP is not None:
            self.heatPumpCOP = heatPumpCOP

        if heatPumpCoolingPower is not None:
            self.heatPumpCoolingPower = heatPumpCoolingPower

        if heatPumpCoolingCOP is not None:
            self.heatPumpCoolingCOP = heatPumpCoolingCOP

        if powerFactor is not None:
            self.powerFactor = powerFactor


@abstract
class AbstractBasicConversion(Conversion):
    """Abstract class for all simple conversion assets that have a power and an efficiency attribute"""
    power = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    efficiency = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, power=None, efficiency=None, **kwargs):

        super().__init__(**kwargs)

        if power is not None:
            self.power = power

        if efficiency is not None:
            self.efficiency = efficiency


class PumpedHydroPower(Storage):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class CAES(Storage):
    """Compressed Air Energy Storage"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class WindTurbine(ElectricityProducer):
    """Describes an individual wind turbine. A wind turbine is a producer capability"""
    rotorDiameter = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    height = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    type = EAttribute(eType=WindTurbineTypeEnum, unique=True, derived=False, changeable=True)
    powerCurveTable = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, rotorDiameter=None, height=None, type=None, powerCurveTable=None, **kwargs):

        super().__init__(**kwargs)

        if rotorDiameter is not None:
            self.rotorDiameter = rotorDiameter

        if height is not None:
            self.height = height

        if type is not None:
            self.type = type

        if powerCurveTable is not None:
            self.powerCurveTable = powerCurveTable


class PVPanel(ElectricityProducer):
    """Describes an individual PV panel. See PVInstallation for multiple PV panels. This is a Producer capability"""
    panelEfficiency = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    inverterEfficiency = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    angle = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    orientation = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)

    def __init__(self, *, panelEfficiency=None, inverterEfficiency=None, angle=None, orientation=None, **kwargs):

        super().__init__(**kwargs)

        if panelEfficiency is not None:
            self.panelEfficiency = panelEfficiency

        if inverterEfficiency is not None:
            self.inverterEfficiency = inverterEfficiency

        if angle is not None:
            self.angle = angle

        if orientation is not None:
            self.orientation = orientation


class ElectricityNetwork(EnergyNetwork):
    """Describes an complete Electricty network, without detailing the complete topology. It is a Transport capability"""
    voltage = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, voltage=None, **kwargs):

        super().__init__(**kwargs)

        if voltage is not None:
            self.voltage = voltage


class ElectricityCable(AbstractConductor):
    """Describes a representation of an electricity cable. When defining the geometry of a cable by means of a line, the first point of the line refers to the first port and the last point of the line refers to the second port."""
    length = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    related = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, length=None, related=None, **kwargs):

        super().__init__(**kwargs)

        if length is not None:
            self.length = length

        if related:
            self.related.extend(related)


class BuildingUnit(GenericBuilding):
    """Describes a physical part of a building. In dutch 'verblijfsobject' in the BAG national building and address registry. This can be used e.g. to model appartments in appartment complexes"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class GenericConversion(AbstractBasicConversion):
    """Generic conversion class that can be used in cases that the actual asset type is not important or not supported yet in ESDL"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class AggregatedConversion(AbstractBasicConversion):
    """Represents an aggregation of multiple conversion assets as one aggregated conversion asset. It allows you to reference the conversion asset it is aggregated of by using the aggregationOf reference. Can be used to aggregate a heterogeneous collection of conversion assets (e.g. of different types)"""
    aggregationOf = EReference(ordered=True, unique=True,
                               containment=False, derived=False, upper=-1)

    def __init__(self, *, aggregationOf=None, **kwargs):

        super().__init__(**kwargs)

        if aggregationOf:
            self.aggregationOf.extend(aggregationOf)


class GasHeater(AbstractBasicConversion):
    """Converts gas to heat, e.g. a gas boiler or gas heater"""
    minimumBurnRate = EAttribute(eType=EDouble, unique=True,
                                 derived=False, changeable=True, default_value=0.0)
    type = EAttribute(eType=GasHeaterTypeEnum, unique=True, derived=False, changeable=True)

    def __init__(self, *, minimumBurnRate=None, type=None, **kwargs):

        super().__init__(**kwargs)

        if minimumBurnRate is not None:
            self.minimumBurnRate = minimumBurnRate

        if type is not None:
            self.type = type


class HeatNetwork(EnergyNetwork):
    """Describes an complete heat network, without detailing the complete topology. It is a Transport capability"""
    temperature = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    temperatureMin = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    temperatureMax = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, temperature=None, temperatureMin=None, temperatureMax=None, **kwargs):

        super().__init__(**kwargs)

        if temperature is not None:
            self.temperature = temperature

        if temperatureMin is not None:
            self.temperatureMin = temperatureMin

        if temperatureMax is not None:
            self.temperatureMax = temperatureMax


class GasNetwork(EnergyNetwork):
    """Describes an complete gas network, without detailing the complete topology. It is a Transport capability"""
    pressure = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, pressure=None, **kwargs):

        super().__init__(**kwargs)

        if pressure is not None:
            self.pressure = pressure


class Pipe(AbstractConductor):
    """Represents a pipe to transport gasses or fluids. When defining the geometry of a pipe by means of a line, the first point of the line refers to the first port and the last point of the line refers to the second port."""
    innerDiameter = EAttribute(eType=EDouble, unique=True, derived=False,
                               changeable=True, default_value=0.0)
    outerDiameter = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    length = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    roughness = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    diameter = EAttribute(eType=PipeDiameterEnum, unique=True, derived=False, changeable=True)
    related = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, innerDiameter=None, outerDiameter=None, length=None, roughness=None, diameter=None, related=None, **kwargs):

        super().__init__(**kwargs)

        if innerDiameter is not None:
            self.innerDiameter = innerDiameter

        if outerDiameter is not None:
            self.outerDiameter = outerDiameter

        if length is not None:
            self.length = length

        if roughness is not None:
            self.roughness = roughness

        if diameter is not None:
            self.diameter = diameter

        if related:
            self.related.extend(related)


class GeothermalSource(HeatProducer):
    """Geothermal source including the installation that connects the source to the network"""
    wellDepth = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    geothermalSourceType = EAttribute(eType=GeothermalSourceTypeEnum,
                                      unique=True, derived=False, changeable=True)
    COP = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    aquiferTemperature = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    flowRate = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    pumpPower = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    powerFactor = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    geothermalPotential = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, wellDepth=None, geothermalSourceType=None, COP=None, aquiferTemperature=None, flowRate=None, pumpPower=None, geothermalPotential=None, powerFactor=None, **kwargs):

        super().__init__(**kwargs)

        if wellDepth is not None:
            self.wellDepth = wellDepth

        if geothermalSourceType is not None:
            self.geothermalSourceType = geothermalSourceType

        if COP is not None:
            self.COP = COP

        if aquiferTemperature is not None:
            self.aquiferTemperature = aquiferTemperature

        if flowRate is not None:
            self.flowRate = flowRate

        if pumpPower is not None:
            self.pumpPower = pumpPower

        if powerFactor is not None:
            self.powerFactor = powerFactor

        if geothermalPotential is not None:
            self.geothermalPotential = geothermalPotential


@abstract
class CoGeneration(AbstractBasicConversion):
    """Abstract asset describing a co-generation plant that produces heat and electricity"""
    heatEfficiency = EAttribute(eType=EDouble, unique=True, derived=False,
                                changeable=True, default_value=0.0)
    electricalEfficiency = EAttribute(eType=EDouble, unique=True,
                                      derived=False, changeable=True, default_value=0.0)
    HERatio = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    fuelType = EAttribute(eType=PowerPlantFuelEnum, unique=True, derived=False, changeable=True)
    leadCommodity = EAttribute(eType=CommodityEnum, unique=True, derived=False, changeable=True)
    powerFactor = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    energyCarrier = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, heatEfficiency=None, electricalEfficiency=None, energyCarrier=None, HERatio=None, fuelType=None, leadCommodity=None, powerFactor=None, **kwargs):

        super().__init__(**kwargs)

        if heatEfficiency is not None:
            self.heatEfficiency = heatEfficiency

        if electricalEfficiency is not None:
            self.electricalEfficiency = electricalEfficiency

        if HERatio is not None:
            self.HERatio = HERatio

        if fuelType is not None:
            self.fuelType = fuelType

        if leadCommodity is not None:
            self.leadCommodity = leadCommodity

        if powerFactor is not None:
            self.powerFactor = powerFactor

        if energyCarrier is not None:
            self.energyCarrier = energyCarrier


class HeatPump(AbstractBasicConversion):
    """Describes a Heat Pump"""
    source = EAttribute(eType=SourceTypeEnum, unique=True, derived=False, changeable=True)
    stages = EAttribute(eType=EInt, unique=True, derived=False, changeable=True, default_value=1)
    COP = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    additionalHeatingSourceType = EAttribute(
        eType=AdditionalHeatingSourceTypeEnum, unique=True, derived=False, changeable=True)
    powerFactor = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, source=None, stages=None, COP=None, additionalHeatingSourceType=None, powerFactor=None, **kwargs):

        super().__init__(**kwargs)

        if source is not None:
            self.source = source

        if stages is not None:
            self.stages = stages

        if COP is not None:
            self.COP = COP

        if additionalHeatingSourceType is not None:
            self.additionalHeatingSourceType = additionalHeatingSourceType

        if powerFactor is not None:
            self.powerFactor = powerFactor


class Transformer(AbstractTransformer):
    """Electrical transformer between different voltage levels"""
    voltagePrimary = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    voltageSecundary = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, voltagePrimary=None, voltageSecundary=None, **kwargs):

        super().__init__(**kwargs)

        if voltagePrimary is not None:
            self.voltagePrimary = voltagePrimary

        if voltageSecundary is not None:
            self.voltageSecundary = voltageSecundary


class HeatExchange(AbstractTransformer):
    """Exchange heat between two circuits"""
    heatTransferCoefficient = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    lengthPrimarySide = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    diameterPrimarySide = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    roughnessPrimarySide = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    lengthSecundarySide = EAttribute(eType=EDouble, unique=True,
                                     derived=False, changeable=True, default_value=0.0)
    diameterSecundarySide = EAttribute(
        eType=EDouble, unique=True, derived=False, changeable=True, default_value=0.0)
    roughnessSecundarySide = EAttribute(
        eType=EDouble, unique=True, derived=False, changeable=True, default_value=0.0)

    def __init__(self, *, heatTransferCoefficient=None, lengthPrimarySide=None, diameterPrimarySide=None, roughnessPrimarySide=None, lengthSecundarySide=None, diameterSecundarySide=None, roughnessSecundarySide=None, **kwargs):

        super().__init__(**kwargs)

        if heatTransferCoefficient is not None:
            self.heatTransferCoefficient = heatTransferCoefficient

        if lengthPrimarySide is not None:
            self.lengthPrimarySide = lengthPrimarySide

        if diameterPrimarySide is not None:
            self.diameterPrimarySide = diameterPrimarySide

        if roughnessPrimarySide is not None:
            self.roughnessPrimarySide = roughnessPrimarySide

        if lengthSecundarySide is not None:
            self.lengthSecundarySide = lengthSecundarySide

        if diameterSecundarySide is not None:
            self.diameterSecundarySide = diameterSecundarySide

        if roughnessSecundarySide is not None:
            self.roughnessSecundarySide = roughnessSecundarySide


class EConnection(AbstractConnection):
    """Electricity connection of a building. Defines the demarcation between the inhouse network and the electricity grid (location where the (smart) meter is located)"""
    EANCode = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, EANCode=None, **kwargs):

        super().__init__(**kwargs)

        if EANCode is not None:
            self.EANCode = EANCode


class HConnection(AbstractConnection):
    """Heat connection of a building. Defines the demarcation between the inhouse network and the heat grid (location where the (smart) meter is located)"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class GConnection(AbstractConnection):
    """Gas connection of a building. Defines the demarcation between the inhouse network and the gas grid (location where the (smart) meter is located)"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class PowerPlant(AbstractBasicConversion):
    """Defines an electricity generating plant"""
    fuel = EAttribute(eType=PowerPlantFuelEnum, unique=True, derived=False, changeable=True)
    maxLoad = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    minLoad = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    effMaxLoad = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    effMinLoad = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    powerFactor = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    type = EAttribute(eType=PowerPlantTypeEnum, unique=True, derived=False, changeable=True)
    energyCarrier = EReference(ordered=True, unique=True, containment=False, derived=False)
    mustRun = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, fuel=None, maxLoad=None, minLoad=None, effMaxLoad=None, effMinLoad=None, energyCarrier=None, mustRun=None, powerFactor=None, type=None, **kwargs):

        super().__init__(**kwargs)

        if fuel is not None:
            self.fuel = fuel

        if maxLoad is not None:
            self.maxLoad = maxLoad

        if minLoad is not None:
            self.minLoad = minLoad

        if effMaxLoad is not None:
            self.effMaxLoad = effMaxLoad

        if effMinLoad is not None:
            self.effMinLoad = effMinLoad

        if powerFactor is not None:
            self.powerFactor = powerFactor

        if type is not None:
            self.type = type

        if energyCarrier is not None:
            self.energyCarrier = energyCarrier

        if mustRun is not None:
            self.mustRun = mustRun


class PowerToX(AbstractBasicConversion):
    """Represents the ability to convert electricity to some other form of energy"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class XToPower(AbstractBasicConversion):
    """Represents the ability to convert some other form of energy to electricity"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Pump(AbstractTransformer):
    """Defines a pump, e.g. in a water or heat network"""
    pumpCapacity = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    pumpEfficiency = EAttribute(eType=EDouble, unique=True, derived=False,
                                changeable=True, default_value=0.0)
    polarMomentOfInertia = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    ratedSpeed = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    powerFactor = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    pumpCurveTable = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, pumpCapacity=None, pumpEfficiency=None, polarMomentOfInertia=None, ratedSpeed=None, pumpCurveTable=None, powerFactor=None, **kwargs):

        super().__init__(**kwargs)

        if pumpCapacity is not None:
            self.pumpCapacity = pumpCapacity

        if pumpEfficiency is not None:
            self.pumpEfficiency = pumpEfficiency

        if polarMomentOfInertia is not None:
            self.polarMomentOfInertia = polarMomentOfInertia

        if ratedSpeed is not None:
            self.ratedSpeed = ratedSpeed

        if powerFactor is not None:
            self.powerFactor = powerFactor

        if pumpCurveTable is not None:
            self.pumpCurveTable = pumpCurveTable


class Airco(AbstractBasicConversion):
    """Represents an air conditioning unit"""
    powerFactor = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, powerFactor=None, **kwargs):

        super().__init__(**kwargs)

        if powerFactor is not None:
            self.powerFactor = powerFactor


class SolarCollector(HeatProducer):
    """Defines a SolarCollector asset"""
    type = EAttribute(eType=SolarCollectorTypeEnum, unique=True, derived=False, changeable=True)

    def __init__(self, *, type=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type


class ResidualHeatSource(HeatProducer):
    """Defines a source of residual heat, e.g. a data center or factory"""
    type = EAttribute(eType=ResidualHeatSourceTypeEnum, unique=True, derived=False, changeable=True)
    residualHeatSourcePotential = EReference(
        ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, type=None, residualHeatSourcePotential=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type

        if residualHeatSourcePotential is not None:
            self.residualHeatSourcePotential = residualHeatSourcePotential


class FermentationPlant(AbstractBasicConversion):
    """Defines a plant fuelled by biomass"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class GasConversion(AbstractBasicConversion):
    """Defines an asset that can convert gas into another form of gas. E.g. SMR or ATR."""
    type = EAttribute(eType=GasConversionTypeEnum, unique=True, derived=False, changeable=True)
    outputPressure = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, type=None, outputPressure=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type

        if outputPressure is not None:
            self.outputPressure = outputPressure


class WaterToPower(ElectricityProducer):
    """Defines an asset that uses water to produce electricity. E.g.  hydro power, tidal power, wave power or osmotic power"""
    type = EAttribute(eType=WaterToPowerTypeEnum, unique=True, derived=False, changeable=True)

    def __init__(self, *, type=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type


class RoomHeater(AbstractBasicConversion):
    """Defines an asset for heating rooms, such as infra red panels, gas stove, etc."""
    type = EAttribute(eType=RoomHeaterTypeEnum, unique=True, derived=False, changeable=True)

    def __init__(self, *, type=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type


class BiomassHeater(AbstractBasicConversion):
    """Converts biomass into heat and/or electricity"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class UTES(HeatStorage):
    """Underground Thermal Energy Storage"""
    type = EAttribute(eType=UTESTypeEnum, unique=True, derived=False,
                      changeable=True, default_value=UTESTypeEnum.UNDEFINED)
    UTESPotential = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, type=None, UTESPotential=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type

        if UTESPotential is not None:
            self.UTESPotential = UTESPotential


class WaterBuffer(HeatStorage):
    """Storage by means of storing energy in water, e.g. a tank."""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Joint(AbstractConductor):
    """A Joint is a means to connect AbstractConductors, such as Pipes and ElectricalCables. This helps when these conductors have opposite Ports."""
    related = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, related=None, **kwargs):

        super().__init__(**kwargs)

        if related:
            self.related.extend(related)


class Bus(AbstractConductor):

    voltage = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    related = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, voltage=None, related=None, **kwargs):

        super().__init__(**kwargs)

        if voltage is not None:
            self.voltage = voltage

        if related:
            self.related.extend(related)


class Sensor(AbstractSensor):

    quantityAndUnit = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, quantityAndUnit=None, **kwargs):

        super().__init__(**kwargs)

        if quantityAndUnit is not None:
            self.quantityAndUnit = quantityAndUnit


class Compressor(AbstractTransformer):

    powerFactor = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, powerFactor=None, **kwargs):

        super().__init__(**kwargs)

        if powerFactor is not None:
            self.powerFactor = powerFactor


class PressureReducingValve(AbstractTransformer):

    valveCoefficient = EAttribute(eType=EDouble, unique=True,
                                  derived=False, changeable=True, default_value=0.0)

    def __init__(self, *, valveCoefficient=None, **kwargs):

        super().__init__(**kwargs)

        if valveCoefficient is not None:
            self.valveCoefficient = valveCoefficient


class Building(GenericBuilding):
    """Represents a physical building"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class AbstractActiveSwitch(AbstractSwitch):

    position = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, position=None, **kwargs):

        super().__init__(**kwargs)

        if position is not None:
            self.position = position


@abstract
class AbstractPassiveSwitch(AbstractSwitch):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class ATES(HeatStorage):
    """Aquifer Thermal Energy Storage"""
    aquiferTopDepth = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    aquiferThickness = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    aquiferMidTemperature = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    aquiferNetToGross = EAttribute(eType=EDouble, unique=True,
                                   derived=False, changeable=True, default_value=0.0)
    aquiferPorosity = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    aquiferPermeability = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    aquiferAnisotropy = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    salinity = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    wellCasingSize = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    wellDistance = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, aquiferTopDepth=None, aquiferThickness=None, aquiferMidTemperature=None, aquiferNetToGross=None, aquiferPorosity=None, aquiferPermeability=None, aquiferAnisotropy=None, salinity=None, wellCasingSize=None, wellDistance=None, **kwargs):

        super().__init__(**kwargs)

        if aquiferTopDepth is not None:
            self.aquiferTopDepth = aquiferTopDepth

        if aquiferThickness is not None:
            self.aquiferThickness = aquiferThickness

        if aquiferMidTemperature is not None:
            self.aquiferMidTemperature = aquiferMidTemperature

        if aquiferNetToGross is not None:
            self.aquiferNetToGross = aquiferNetToGross

        if aquiferPorosity is not None:
            self.aquiferPorosity = aquiferPorosity

        if aquiferPermeability is not None:
            self.aquiferPermeability = aquiferPermeability

        if aquiferAnisotropy is not None:
            self.aquiferAnisotropy = aquiferAnisotropy

        if salinity is not None:
            self.salinity = salinity

        if wellCasingSize is not None:
            self.wellCasingSize = wellCasingSize

        if wellDistance is not None:
            self.wellDistance = wellDistance


class ElectricBoiler(AbstractBasicConversion):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class FuelCell(CoGeneration):
    """Defines a Fuel Cell"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Valve(AbstractActiveSwitch):
    """Defines a valve, e.g. in a water, gas or heat network"""
    type = EAttribute(eType=ValveTypeEnum, unique=True, derived=False, changeable=True)
    innerDiameter = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    flowCoefficient = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, type=None, innerDiameter=None, flowCoefficient=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type

        if innerDiameter is not None:
            self.innerDiameter = innerDiameter

        if flowCoefficient is not None:
            self.flowCoefficient = flowCoefficient


class CHP(CoGeneration):
    """Describes a Combined Heat and Power installation"""
    CHPType = EAttribute(eType=CHPTypeEnum, unique=True, derived=False, changeable=True)

    def __init__(self, *, CHPType=None, **kwargs):

        super().__init__(**kwargs)

        if CHPType is not None:
            self.CHPType = CHPType


class Electrolyzer(PowerToX):
    """Defines an electrolyzer that converts electricity into hydrogen"""
    outputPressure = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    maxLoad = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    minLoad = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    effMaxLoad = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    effMinLoad = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    powerFactor = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, outputPressure=None, maxLoad=None, minLoad=None, effMaxLoad=None, effMinLoad=None, powerFactor=None, **kwargs):

        super().__init__(**kwargs)

        if outputPressure is not None:
            self.outputPressure = outputPressure

        if maxLoad is not None:
            self.maxLoad = maxLoad

        if minLoad is not None:
            self.minLoad = minLoad

        if effMaxLoad is not None:
            self.effMaxLoad = effMaxLoad

        if effMinLoad is not None:
            self.effMinLoad = effMinLoad

        if powerFactor is not None:
            self.powerFactor = powerFactor


class PVInstallation(PVPanel):
    """Defines a Photo Voltaic Installation, e.g. roof top PV, a PV field or parc."""
    type = EAttribute(eType=PVInstallationTypeEnum, unique=True, derived=False, changeable=True)
    numberOfPanels = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)

    def __init__(self, *, type=None, numberOfPanels=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type

        if numberOfPanels is not None:
            self.numberOfPanels = numberOfPanels


class CircuitBreaker(AbstractPassiveSwitch):
    """Defines a circuit breaker in electric transmission or distribution grids"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Switch(AbstractActiveSwitch):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class PVPark(PVPanel):
    """Defines a PV park of multiple panels"""
    numberOfPanels = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)

    def __init__(self, *, numberOfPanels=None, **kwargs):

        super().__init__(**kwargs)

        if numberOfPanels is not None:
            self.numberOfPanels = numberOfPanels


class WindPark(WindTurbine):
    """Defines a wind park of multiple turbines"""
    numberOfTurbines = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    turbinePower = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)

    def __init__(self, *, numberOfTurbines=None, turbinePower=None, **kwargs):

        super().__init__(**kwargs)

        if numberOfTurbines is not None:
            self.numberOfTurbines = numberOfTurbines

        if turbinePower is not None:
            self.turbinePower = turbinePower


class CheckValve(AbstractPassiveSwitch):

    innerDiameter = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    reopenDeltaP = EAttribute(eType=EDouble, unique=True, derived=False, changeable=True)
    flowCoefficient = EAttribute(eType=EDouble, unique=True,
                                 derived=False, changeable=True, default_value=0.0)

    def __init__(self, *, innerDiameter=None, reopenDeltaP=None, flowCoefficient=None, **kwargs):

        super().__init__(**kwargs)

        if innerDiameter is not None:
            self.innerDiameter = innerDiameter

        if reopenDeltaP is not None:
            self.reopenDeltaP = reopenDeltaP

        if flowCoefficient is not None:
            self.flowCoefficient = flowCoefficient
