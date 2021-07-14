from pyecore.resources import global_registry
from .esdl import getEClassifier, eClassifiers
from .esdl import name, nsURI, nsPrefix, eClass
from .esdl import EnergyAsset, Producer, Consumer, Storage, Conversion, Transport, CommodityEnum, EnergySystem, WindTurbine, PVPanel, Battery, ElectricityNetwork, ElectricityCable, AggregatedConsumer, BuildingUnit, Area, Port, AggregatedProducer, AreaScopeEnum, ProfileTypeEnum, DurationUnitEnum, InPort, OutPort, Asset, GenericConsumer, GenericProducer, GenericStorage, GenericTransport, GenericConversion, AggregatedTransport, AggregatedConversion, AggregatedStorage, BuildingTypeEnum, GenericBuilding, ConsTypeEnum, HeatStorage, GasHeater, HeatNetwork, GasNetwork, Insulation, Import, Export, Pipe, GeothermalSource, CoGeneration, HeatPump, SourceTypeEnum, AggrTypeEnum, AreaTypeEnum, HeatingDemand, HeatDemandTypeEnum, ElectricityDemand, GasDemand, GeothermalPotential, Point, Polygon, OwnershipRentalTypeEnum, EconomicProperties, SocialProperties, LegalArea, RoofTypeEnum, EnergyLabelEnum, EnergyService, DemandResponseService, Transformer, HeatExchange, ResidentialBuildingTypeEnum, Item, Measures, EConnection, HConnection, GConnection, PowerPlant, PowerPlantFuelEnum, AbstractBuilding, Instance, Service, AggregatorService, EVChargingStation, Potential, WindPotential, AggregatedBuilding, SectorEnum, EnergyCarrier, Losses, PowerToX, CCS, RenewableTypeEnum, StateOfMatterEnum, Carriers, FuelCell, XToPower, EnergySystemInformation, Pump, Valve, GenericProfile, StaticProfile, DateTimeProfile, ProfileElement, ExternalProfile, SingleValue, GenericDistribution, Percentile, PercentileDistribution, CoolingDemand, Airco, CostInformation, SpecificLabelDistribution, StringLabelDistribution, EnergyLabelDistribution, StringItem, EnergyLabelPerc, FromToDistribution, FromToItem, PItemStat, AbstractVariance, SymmetricVariance, AssymmetricVariance, DoubleAssymmetricVariance, GeothermalSourceTypeEnum, CHPTypeEnum, CHP, Party, URIProfile, DatabaseProfile, InfluxDBProfile, Line, Geometry, GlazingTypeEnum, VentilationTypeEnum, GasHeaterTypeEnum, InhabitantsTypeEnum, AdditionalHeatingSourceTypeEnum, GeothermalPotentialEnum, GeothermalPowerEnum, Commodity, GasCommodity, HeatCommodity, ElectricityCommodity, Carrier, Range, SolarPotential, Duration, ProfileReference, Profiles, Parties, DataSources, DataSource, EnergyDemand, SolarCollector, ResidualHeatSource, ResidualHeatSourceTypeEnum, FermentationPlant, ResidualHeatSourcePotential, SubPolygon, MultiPolygon, EnergyCommodity, MobilityDemand, MobilityFuelTypeEnum, VehicleTypeEnum, MobilityFuelInformation, VehicleFuelEfficiency, MobilityProperties, NumberOfVehicles, VehicleCount, Electrolyzer, GasStorage, Services, ControlStrategy, DrivenByDemand, QuantityAndUnitType, MultiplierEnum, PhysicalQuantityEnum, UnitEnum, AbstractDataSource, DataSourceReference, TimeUnitEnum, KPIs, KPI, QuantityAndUnits, AbstractQuantityAndUnit, QuantityAndUnitReference, EnergyMarket, GasConversion, GasConversionTypeEnum, Parameters, StringParameter, DoubleParameter, IntegerParameter, BooleanParameter, DrivenBySupply, DrivenByProfile, PVInstallation, PVInstallationTypeEnum, WindTurbineTypeEnum, CircuitBreaker, Measure, WaterToPower, WaterToPowerTypeEnum, Sectors, Sector, EnergyNetwork, AbstractConductor, AbstractSwitch, AbstractTransformer, AbstractConnection, MultiLine, SolarCollectorTypeEnum, HeatRadiationDeviceTypeEnum, CoolingDeviceType, GeothermalEnergyPotential, AbstractGTPotential, UTESPotential, AbstractInstanceDate, InstanceDate, InstancePeriod, RoomHeater, RoomHeaterTypeEnum, BiomassPotential, BiomassHeater, BiomassHeaterTypeEnum, UTESPotentialTypeEnum, UTES, WaterBuffer, UTESTypeEnum, Glazing, InterpolationMethodEnum, WKT, WKB, SearchAreaWind, SearchAreaSolar, Joint, StorageStrategy, CurtailmentStrategy, PVTInstallation, BuildingUsage, WeekSchedule, DaySchedule, Event, AbstractBuildingUsage, BuildingUsageReference, BuildingUsageInformation, BuildingTypeDistribution, BuildingTypePercentage, ResidentialBuildingTypeDistribution, ResidentialBuildingTypePercentage, OwnershipRentalTypeDistribution, OwnershipRentalTypePercentage, DoubleKPI, StringKPI, IntKPI, FromToIntItem, FromToDoubleItem, Matter, PipeDiameterEnum, Bus, AbstractSensor, Sensor, Switch, Compressor, PressureReducingValve, CompoundMatter, CompoundMatterComponent, PIDController, PVPark, WindPark, IntTargetKPI, DoubleTargetKPI, StringTargetKPI, AssetStateEnum, Restriction, BuildingTypeRestriction, AreaTypeRestriction, Templates, AssetTemplate, TemplatedAsset, Address, QuantityAndUnitScopeEnum, GenericLabelDistribution, DistributionKPI, SinkConsumer, SourceProducer, MinimumLabelRestriction, LabelJump, AbstractMeasure, MeasureReference, Building, BuildingInformation, ResidentialBuildingInformation, BuildingStructureInformation, CompoundAsset, InitialValue, Table, TableRow, ValveTypeEnum, AbstractActiveSwitch, AbstractPassiveSwitch, CheckValve, AirVessel, Notes, Note, Fuel, Material, Matters, AbstractMatter, MatterReference, CompoundTypeEnum, EnvironmentalProfiles, AbstractBehaviour, GenericTransferFunction, InputOutputRelation, DelayTransferFunction, AbstractTransferFunction, CombinedTransferFunction, CombinationFunctionEnum, TransferFunctionTypeEnum, ElectricityProducer, HeatProducer, GasProducer, MeasureTypeEnum, TimeSeriesProfile, PortRelation, BufferDistance, BufferDistanceTypeEnum, ATES


from . import esdl

__all__ = ['EnergyAsset', 'Producer', 'Consumer', 'Storage', 'Conversion', 'Transport', 'CommodityEnum', 'EnergySystem', 'WindTurbine', 'PVPanel', 'Battery', 'ElectricityNetwork', 'ElectricityCable', 'AggregatedConsumer', 'BuildingUnit', 'Area', 'Port', 'AggregatedProducer', 'AreaScopeEnum', 'ProfileTypeEnum', 'DurationUnitEnum', 'InPort', 'OutPort', 'Asset', 'GenericConsumer', 'GenericProducer', 'GenericStorage', 'GenericTransport', 'GenericConversion', 'AggregatedTransport', 'AggregatedConversion', 'AggregatedStorage', 'BuildingTypeEnum', 'GenericBuilding', 'ConsTypeEnum', 'HeatStorage', 'GasHeater', 'HeatNetwork', 'GasNetwork', 'Insulation', 'Import', 'Export', 'Pipe', 'GeothermalSource', 'CoGeneration', 'HeatPump', 'SourceTypeEnum', 'AggrTypeEnum', 'AreaTypeEnum', 'HeatingDemand', 'HeatDemandTypeEnum', 'ElectricityDemand', 'GasDemand', 'GeothermalPotential', 'Point', 'Polygon', 'OwnershipRentalTypeEnum', 'EconomicProperties', 'SocialProperties', 'LegalArea', 'RoofTypeEnum', 'EnergyLabelEnum', 'EnergyService', 'DemandResponseService', 'Transformer', 'HeatExchange', 'ResidentialBuildingTypeEnum', 'Item', 'Measures', 'EConnection', 'HConnection', 'GConnection', 'PowerPlant', 'PowerPlantFuelEnum', 'AbstractBuilding', 'Instance', 'Service', 'AggregatorService', 'EVChargingStation', 'Potential', 'WindPotential', 'AggregatedBuilding', 'SectorEnum', 'EnergyCarrier', 'Losses', 'PowerToX', 'CCS', 'RenewableTypeEnum', 'StateOfMatterEnum', 'Carriers', 'FuelCell', 'XToPower', 'EnergySystemInformation', 'Pump', 'Valve', 'GenericProfile', 'StaticProfile', 'DateTimeProfile', 'ProfileElement', 'ExternalProfile', 'SingleValue', 'GenericDistribution', 'Percentile', 'PercentileDistribution', 'CoolingDemand', 'Airco', 'CostInformation', 'SpecificLabelDistribution', 'StringLabelDistribution', 'EnergyLabelDistribution', 'StringItem', 'EnergyLabelPerc', 'FromToDistribution', 'FromToItem', 'PItemStat', 'AbstractVariance', 'SymmetricVariance', 'AssymmetricVariance', 'DoubleAssymmetricVariance', 'GeothermalSourceTypeEnum', 'CHPTypeEnum', 'CHP', 'Party', 'URIProfile', 'DatabaseProfile', 'InfluxDBProfile', 'Line', 'Geometry', 'GlazingTypeEnum', 'VentilationTypeEnum', 'GasHeaterTypeEnum', 'InhabitantsTypeEnum', 'AdditionalHeatingSourceTypeEnum', 'GeothermalPotentialEnum', 'GeothermalPowerEnum', 'Commodity', 'GasCommodity', 'HeatCommodity', 'ElectricityCommodity', 'Carrier', 'Range', 'SolarPotential', 'Duration', 'ProfileReference', 'Profiles', 'Parties', 'DataSources', 'DataSource', 'EnergyDemand', 'SolarCollector', 'ResidualHeatSource', 'ResidualHeatSourceTypeEnum', 'FermentationPlant', 'ResidualHeatSourcePotential', 'SubPolygon', 'MultiPolygon', 'EnergyCommodity', 'MobilityDemand', 'MobilityFuelTypeEnum', 'VehicleTypeEnum', 'MobilityFuelInformation', 'VehicleFuelEfficiency', 'MobilityProperties', 'NumberOfVehicles', 'VehicleCount', 'Electrolyzer', 'GasStorage', 'Services', 'ControlStrategy', 'DrivenByDemand',
           'QuantityAndUnitType', 'MultiplierEnum', 'PhysicalQuantityEnum', 'UnitEnum', 'AbstractDataSource', 'DataSourceReference', 'TimeUnitEnum', 'KPIs', 'KPI', 'QuantityAndUnits', 'AbstractQuantityAndUnit', 'QuantityAndUnitReference', 'EnergyMarket', 'GasConversion', 'GasConversionTypeEnum', 'Parameters', 'StringParameter', 'DoubleParameter', 'IntegerParameter', 'BooleanParameter', 'DrivenBySupply', 'DrivenByProfile', 'PVInstallation', 'PVInstallationTypeEnum', 'WindTurbineTypeEnum', 'CircuitBreaker', 'Measure', 'WaterToPower', 'WaterToPowerTypeEnum', 'Sectors', 'Sector', 'EnergyNetwork', 'AbstractConductor', 'AbstractSwitch', 'AbstractTransformer', 'AbstractConnection', 'MultiLine', 'SolarCollectorTypeEnum', 'HeatRadiationDeviceTypeEnum', 'CoolingDeviceType', 'GeothermalEnergyPotential', 'AbstractGTPotential', 'UTESPotential', 'AbstractInstanceDate', 'InstanceDate', 'InstancePeriod', 'RoomHeater', 'RoomHeaterTypeEnum', 'BiomassPotential', 'BiomassHeater', 'BiomassHeaterTypeEnum', 'UTESPotentialTypeEnum', 'UTES', 'WaterBuffer', 'UTESTypeEnum', 'Glazing', 'InterpolationMethodEnum', 'WKT', 'WKB', 'SearchAreaWind', 'SearchAreaSolar', 'Joint', 'StorageStrategy', 'CurtailmentStrategy', 'PVTInstallation', 'BuildingUsage', 'WeekSchedule', 'DaySchedule', 'Event', 'AbstractBuildingUsage', 'BuildingUsageReference', 'BuildingUsageInformation', 'BuildingTypeDistribution', 'BuildingTypePercentage', 'ResidentialBuildingTypeDistribution', 'ResidentialBuildingTypePercentage', 'OwnershipRentalTypeDistribution', 'OwnershipRentalTypePercentage', 'DoubleKPI', 'StringKPI', 'IntKPI', 'FromToIntItem', 'FromToDoubleItem', 'Matter', 'PipeDiameterEnum', 'Bus', 'AbstractSensor', 'Sensor', 'Switch', 'Compressor', 'PressureReducingValve', 'CompoundMatter', 'CompoundMatterComponent', 'PIDController', 'PVPark', 'WindPark', 'IntTargetKPI', 'DoubleTargetKPI', 'StringTargetKPI', 'AssetStateEnum', 'Restriction', 'BuildingTypeRestriction', 'AreaTypeRestriction', 'Templates', 'AssetTemplate', 'TemplatedAsset', 'Address', 'QuantityAndUnitScopeEnum', 'GenericLabelDistribution', 'DistributionKPI', 'SinkConsumer', 'SourceProducer', 'MinimumLabelRestriction', 'LabelJump', 'AbstractMeasure', 'MeasureReference', 'Building', 'BuildingInformation', 'ResidentialBuildingInformation', 'BuildingStructureInformation', 'CompoundAsset', 'InitialValue', 'Table', 'TableRow', 'ValveTypeEnum', 'AbstractActiveSwitch', 'AbstractPassiveSwitch', 'CheckValve', 'AirVessel', 'Notes', 'Note', 'Fuel', 'Material', 'Matters', 'AbstractMatter', 'MatterReference', 'CompoundTypeEnum', 'EnvironmentalProfiles', 'AbstractBehaviour', 'GenericTransferFunction', 'InputOutputRelation', 'DelayTransferFunction', 'AbstractTransferFunction', 'CombinedTransferFunction', 'CombinationFunctionEnum', 'TransferFunctionTypeEnum', 'ElectricityProducer', 'HeatProducer', 'GasProducer', 'MeasureTypeEnum', 'TimeSeriesProfile', 'PortRelation', 'BufferDistance', 'BufferDistanceTypeEnum', 'ATES']

eSubpackages = []
eSuperPackage = None
esdl.eSubpackages = eSubpackages
esdl.eSuperPackage = eSuperPackage

EnergyAsset.behaviour.eType = AbstractBehaviour
Storage.profile.eType = GenericProfile
EnergySystem.measures.eType = Measures
EnergySystem.instance.eType = Instance
EnergySystem.energySystemInformation.eType = EnergySystemInformation
EnergySystem.parties.eType = Parties
EnergySystem.services.eType = Services
EnergySystem.templates.eType = Templates
AggregatedConsumer.aggregationOf.eType = Consumer
Area.socialProperties.eType = SocialProperties
Area.economicProperties.eType = EconomicProperties
Area.mobilityProperties.eType = MobilityProperties
Area.KPIs.eType = KPIs
Area.potential.eType = Potential
Area.geometry.eType = Geometry
Area.measures.eType = Measures
Area.sector.eType = Sector
Port.profile.eType = GenericProfile
Port.carrier.eType = Carrier
AggregatedProducer.aggregationOf.eType = Producer
Asset.geometry.eType = Geometry
Asset.costInformation.eType = CostInformation
Asset.KPIs.eType = KPIs
Asset.material.eType = AbstractMatter
Asset.bufferDistance.eType = BufferDistance
AggregatedTransport.aggregationOf.eType = Transport
AggregatedConversion.aggregationOf.eType = Conversion
AggregatedStorage.aggregationOf.eType = Storage
GenericBuilding.address.eType = Address
GenericBuilding.buildinginformation.eType = BuildingInformation
CoGeneration.energyCarrier.eType = EnergyCarrier
Polygon.exterior.eType = SubPolygon
Polygon.interior.eType = SubPolygon
Item.dataSource.eType = AbstractDataSource
Item.sector.eType = Sector
Measures.measure.eType = AbstractMeasure
PowerPlant.energyCarrier.eType = EnergyCarrier
PowerPlant.mustRun.eType = GenericProfile
AbstractBuilding.buildingUsage.eType = AbstractBuildingUsage
AbstractBuilding.potential.eType = Potential
Instance.area.eType = Area
Instance.date.eType = AbstractInstanceDate
Potential.geometry.eType = Geometry
Potential.quantityAndUnit.eType = AbstractQuantityAndUnit
AggregatedBuilding.aggregationOf.eType = AbstractBuilding
AggregatedBuilding.energyLabelDistribution.eType = EnergyLabelDistribution
AggregatedBuilding.buildingYearDistribution.eType = FromToDistribution
AggregatedBuilding.buildingTypeDistribution.eType = BuildingTypeDistribution
AggregatedBuilding.residentialBuildingTypeDistribution.eType = ResidentialBuildingTypeDistribution
AggregatedBuilding.ownershipRentalTypeDistribution.eType = OwnershipRentalTypeDistribution
EnergyCarrier.energyContentUnit.eType = AbstractQuantityAndUnit
EnergyCarrier.emissionUnit.eType = AbstractQuantityAndUnit
EnergyCarrier.composition.eType = AbstractMatter
Carriers.carrier.eType = Carrier
Carriers.dataSource.eType = AbstractDataSource
EnergySystemInformation.carriers.eType = Carriers
EnergySystemInformation.profiles.eType = Profiles
EnergySystemInformation.dataSources.eType = DataSources
EnergySystemInformation.mobilityFuelInformation.eType = MobilityFuelInformation
EnergySystemInformation.quantityAndUnits.eType = QuantityAndUnits
EnergySystemInformation.sectors.eType = Sectors
EnergySystemInformation.buildingUsageInformation.eType = BuildingUsageInformation
EnergySystemInformation.notes.eType = Notes
EnergySystemInformation.matters.eType = Matters
EnergySystemInformation.environmentalProfiles.eType = EnvironmentalProfiles
Pump.pumpCurveTable.eType = Table
Valve.flowCoefficient.eType = Table
GenericProfile.dataSource.eType = AbstractDataSource
GenericProfile.profileQuantityAndUnit.eType = AbstractQuantityAndUnit
DateTimeProfile.element.eType = ProfileElement
PercentileDistribution.percentile.eType = Percentile
CostInformation.investmentCosts.eType = GenericProfile
CostInformation.installationCosts.eType = GenericProfile
CostInformation.fixedOperationalAndMaintenanceCosts.eType = GenericProfile
CostInformation.marginalCosts.eType = GenericProfile
CostInformation.variableOperationalAndMaintenanceCosts.eType = GenericProfile
CostInformation.discountRate.eType = GenericProfile
CostInformation.variableOperationalCosts.eType = GenericProfile
CostInformation.fixedMaintenanceCosts.eType = GenericProfile
CostInformation.fixedOperationalCosts.eType = GenericProfile
CostInformation.variableMaintenanceCosts.eType = GenericProfile
StringLabelDistribution.stringItem.eType = StringItem
EnergyLabelDistribution.labelPerc.eType = EnergyLabelPerc
FromToDistribution.fromToItem.eType = FromToItem
Party.sector.eType = Sector
Line.point.eType = Point
Carrier.cost.eType = GenericProfile
Carrier.dataSource.eType = AbstractDataSource
ProfileReference.reference.eType = GenericProfile
Profiles.profile.eType = GenericProfile
Parties.party.eType = Party
DataSources.dataSource.eType = DataSource
SubPolygon.point.eType = Point
MultiPolygon.polygon.eType = Polygon
MobilityFuelInformation.vehicleFuelEfficiency.eType = VehicleFuelEfficiency
MobilityFuelInformation.dataSource.eType = AbstractDataSource
MobilityProperties.numberOfVehicles.eType = NumberOfVehicles
NumberOfVehicles.vehicleCount.eType = VehicleCount
Services.service.eType = Service
DrivenByDemand.outPort.eType = OutPort
DataSourceReference.reference.eType = DataSource
KPIs.kpi.eType = KPI
KPI.quantityAndUnit.eType = AbstractQuantityAndUnit
QuantityAndUnits.quantityAndUnit.eType = QuantityAndUnitType
QuantityAndUnitReference.reference.eType = QuantityAndUnitType
EnergyMarket.asset.eType = Asset
EnergyMarket.carrier.eType = Carrier
EnergyMarket.parameters.eType = Parameters
EnergyMarket.marketPrice.eType = GenericProfile
Parameters.parameterUnit.eType = AbstractQuantityAndUnit
DrivenBySupply.inPort.eType = InPort
DrivenByProfile.profile.eType = GenericProfile
DrivenByProfile.port.eType = Port
Measure.asset.eType = Asset
Measure.costInformation.eType = CostInformation
Measure.restriction.eType = Restriction
Measure.labelJump.eType = LabelJump
Sectors.sector.eType = Sector
Sectors.dataSource.eType = AbstractDataSource
Sector.dataSource.eType = AbstractDataSource
MultiLine.line.eType = Line
StorageStrategy.marginalChargeCosts.eType = GenericProfile
StorageStrategy.marginalDischargeCosts.eType = GenericProfile
BuildingUsage.coolingSetpoints.eType = WeekSchedule
BuildingUsage.heatingSetpoints.eType = WeekSchedule
BuildingUsage.openingHours.eType = WeekSchedule
WeekSchedule.mon.eType = DaySchedule
WeekSchedule.tue.eType = DaySchedule
WeekSchedule.wed.eType = DaySchedule
WeekSchedule.thu.eType = DaySchedule
WeekSchedule.fri.eType = DaySchedule
WeekSchedule.sat.eType = DaySchedule
WeekSchedule.sun.eType = DaySchedule
WeekSchedule.weekdays.eType = DaySchedule
WeekSchedule.weekenddays.eType = DaySchedule
DaySchedule.event.eType = Event
BuildingUsageReference.reference.eType = BuildingUsage
BuildingUsageInformation.buildingUsage.eType = BuildingUsage
BuildingTypeDistribution.buildingTypePercentage.eType = BuildingTypePercentage
ResidentialBuildingTypeDistribution.residentialBuildingTypePercentage.eType = ResidentialBuildingTypePercentage
OwnershipRentalTypeDistribution.ownershipRentalTypePercentage.eType = OwnershipRentalTypePercentage
DoubleKPI.target.eType = DoubleTargetKPI
StringKPI.target.eType = StringTargetKPI
IntKPI.target.eType = IntTargetKPI
Sensor.quantityAndUnit.eType = AbstractQuantityAndUnit
CompoundMatter.component.eType = CompoundMatterComponent
CompoundMatterComponent.matter.eType = AbstractMatter
PIDController.sensor.eType = Sensor
PIDController.setPoint.eType = GenericProfile
Templates.assetTemplate.eType = AssetTemplate
AssetTemplate.asset.eType = Asset
TemplatedAsset.asset.eType = Asset
TemplatedAsset.template.eType = AssetTemplate
DistributionKPI.distribution.eType = GenericLabelDistribution
LabelJump.buildingYearRange.eType = Range
MeasureReference.reference.eType = Measure
CompoundAsset.asset.eType = Asset
Table.row.eType = TableRow
Table.header.eType = AbstractQuantityAndUnit
Table.datasource.eType = AbstractDataSource
Notes.note.eType = Note
Note.mapLocation.eType = Point
Fuel.energyContentUnit.eType = AbstractQuantityAndUnit
Fuel.emissionUnit.eType = AbstractQuantityAndUnit
Matters.dataSource.eType = AbstractDataSource
Matters.matter.eType = Matter
MatterReference.reference.eType = Matter
EnvironmentalProfiles.outsideTemperatureProfile.eType = GenericProfile
EnvironmentalProfiles.solarIrradianceProfile.eType = GenericProfile
EnvironmentalProfiles.windSpeedProfile.eType = GenericProfile
EnvironmentalProfiles.windDirectionProfile.eType = GenericProfile
EnvironmentalProfiles.soilTemperatureProfile.eType = GenericProfile
EnvironmentalProfiles.relativeHumidityProfile.eType = GenericProfile
InputOutputRelation.mainPortRelation.eType = PortRelation
InputOutputRelation.mainPort.eType = Port
CombinedTransferFunction.component.eType = AbstractTransferFunction
PortRelation.port.eType = Port
EnergyAsset.port.eType = Port
EnergyAsset.controlStrategy.eType = ControlStrategy
Conversion.residualHeatSourcePotential.eType = ResidualHeatSourcePotential
Area.asset.eType = Asset
Area.area.eType = Area
Area.containingArea.eType = Area
Area.containingArea.eOpposite = Area.area
Area.isOwnedBy.eType = Party
Port.energyasset.eType = EnergyAsset
Port.energyasset.eOpposite = EnergyAsset.port
InPort.connectedTo.eType = OutPort
OutPort.connectedTo.eType = InPort
OutPort.connectedTo.eOpposite = InPort.connectedTo
Asset.area.eType = Area
Asset.area.eOpposite = Area.asset
Asset.containingBuilding.eType = AbstractBuilding
GeothermalSource.geothermalPotential.eType = AbstractGTPotential
Item.isOwnedBy.eType = Party
AbstractBuilding.asset.eType = Asset
AbstractBuilding.asset.eOpposite = Asset.containingBuilding
Party.owns.eType = Item
Party.owns.eOpposite = Item.isOwnedBy
Party.ownsArea.eType = Area
Party.ownsArea.eOpposite = Area.isOwnedBy
ResidualHeatSource.residualHeatSourcePotential.eType = ResidualHeatSourcePotential
ResidualHeatSourcePotential.associatedConversionAsset.eType = Conversion
ResidualHeatSourcePotential.associatedConversionAsset.eOpposite = Conversion.residualHeatSourcePotential
ResidualHeatSourcePotential.residualHeatSource.eType = ResidualHeatSource
ResidualHeatSourcePotential.residualHeatSource.eOpposite = ResidualHeatSource.residualHeatSourcePotential
ControlStrategy.energyAsset.eType = EnergyAsset
ControlStrategy.energyAsset.eOpposite = EnergyAsset.controlStrategy
AbstractGTPotential.geothermalSource.eType = GeothermalSource
AbstractGTPotential.geothermalSource.eOpposite = GeothermalSource.geothermalPotential
UTESPotential.UTES.eType = UTES
UTES.UTESPotential.eType = UTESPotential
UTES.UTESPotential.eOpposite = UTESPotential.UTES

otherClassifiers = [CommodityEnum, AreaScopeEnum, ProfileTypeEnum, DurationUnitEnum, BuildingTypeEnum, ConsTypeEnum, SourceTypeEnum, AggrTypeEnum, AreaTypeEnum, HeatDemandTypeEnum, OwnershipRentalTypeEnum, RoofTypeEnum, EnergyLabelEnum, ResidentialBuildingTypeEnum, PowerPlantFuelEnum, SectorEnum, RenewableTypeEnum, StateOfMatterEnum, GeothermalSourceTypeEnum, CHPTypeEnum, GlazingTypeEnum, VentilationTypeEnum, GasHeaterTypeEnum, InhabitantsTypeEnum, AdditionalHeatingSourceTypeEnum, GeothermalPotentialEnum, GeothermalPowerEnum, ResidualHeatSourceTypeEnum,
                    MobilityFuelTypeEnum, VehicleTypeEnum, MultiplierEnum, PhysicalQuantityEnum, UnitEnum, TimeUnitEnum, GasConversionTypeEnum, PVInstallationTypeEnum, WindTurbineTypeEnum, WaterToPowerTypeEnum, SolarCollectorTypeEnum, HeatRadiationDeviceTypeEnum, CoolingDeviceType, RoomHeaterTypeEnum, BiomassHeaterTypeEnum, UTESPotentialTypeEnum, UTESTypeEnum, InterpolationMethodEnum, PipeDiameterEnum, AssetStateEnum, QuantityAndUnitScopeEnum, ValveTypeEnum, CompoundTypeEnum, CombinationFunctionEnum, TransferFunctionTypeEnum, MeasureTypeEnum, BufferDistanceTypeEnum]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [esdl] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack
