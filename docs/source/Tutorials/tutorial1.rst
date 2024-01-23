Tutorial 1: Create a simple EnergySystem
========================================

<< Introduction text to this tutorial >>

Start with importing the required libraries

.. code-block:: python

    from esdl import esdl
    from esdl.edr.client import EDRClient
    from esdl.esdl_handler import EnergySystemHandler
    import pandas as pd
    from esdl.profiles.influxdbprofilemanager import InfluxDBProfileManager

Define some constants

.. code-block:: python

    if __name__ == '__main__':
        folder_name = "ESDLs"
        file_name = "Tutorial1.esdl"

Create an EnergySystemHandler - a class that helps a developer to read and write ESDL-files

.. code-block:: python

    energy_system_handler = EnergySystemHandler()

First, create an empty EnergySystem with a name, a description, and an Instance

.. code-block:: python

    energy_system = energy_system_handler.create_empty_energy_system(name="Training_EnergySystem",
                                                                     es_description="Hello pyESDL training Energy System",
                                                                     inst_title="Tutorial1_Instance",
                                                                     area_title="Tutorial1_Area")

Get the energy system area to be able to append assets later on

.. code-block:: python

    tutorial1_area = energy_system.instance[0].area

Create carriers and commodities. Carriers and commodities are a part of energy system information

.. code-block:: python

    energy_system_information = esdl.EnergySystemInformation(id="es_information-ID")
    natural_gas_commodity = esdl.GasCommodity(id="natural-gas-commodity-ID", name="NaturalGas")
    electricity_commodity = esdl.ElectricityCommodity(id="electricity-commodity-ID", name="Electricity")

    energy_carriers = esdl.Carriers(id="energy-carriers-ID")
    energy_carriers.carrier.append(natural_gas_commodity)
    energy_carriers.carrier.append(electricity_commodity)

    energy_system_information.carriers = energy_carriers
    energy_system.energySystemInformation = energy_system_information


Create an EnergySystem with an Import, a PowerPlant and an ElectricityDemand

Create an Import with 1TW power

.. code-block:: python

    natural_gas_import = esdl.Import(name="NaturalGas_Import", id="natural-gas-import-ID", prodType="FOSSIL",
                                     power=1000000000000.0)

Create a location for the Import

.. code-block:: python

    natural_gas_import_location = esdl.Point(lat=52.044, lon=4.3004)
    natural_gas_import.geometry = natural_gas_import_location

OutPort that connects to other assets

.. code-block:: python

    natural_gas_import_out_port = esdl.OutPort(id="natural-gas-import-out-port-ID")

 Assign the commodity to he port

 .. code-block:: python

    natural_gas_import_out_port.carrier = natural_gas_commodity
    natural_gas_import.port.append(natural_gas_import_out_port)

Add the NaturalGas Import to the area

.. code-block:: python

    tutorial1_area.asset.append(natural_gas_import)

Create a gas-powered PowerPlant

.. code-block:: python

    power_plant = esdl.PowerPlant(name="GasPowered_PowerPlant", id="gas-powered-power-plant-ID", power=2000000000.0,
                                  efficiency=0.6)

Create a location for the PowerPlant

.. code-block:: python

    power_plant_location = esdl.Point(lat=52.044, lon=4.3008)
    power_plant.geometry = power_plant_location

Create PowerPlant's InPort

.. code-block:: python

    power_plant_in_port = esdl.InPort(id="power-plant-in-port-ID", connectedTo=[natural_gas_import_out_port])
    power_plant_in_port.carrier = natural_gas_commodity
    power_plant.port.append(power_plant_in_port)

Create PowerPlant's OutPot

.. code-block:: python

    power_plant_out_port = esdl.OutPort(id="power-plant-out-port-ID")

Create and append electricity commodity

.. code-block:: python

    power_plant_out_port.carrier = electricity_commodity
    power_plant.port.append(power_plant_out_port)

Add the PowerPlant to the area

.. code-block:: python

    tutorial1_area.asset.append(power_plant)

Create an ElectricityDemand with a 800 MWh flat profile

.. code-block:: python

    electricity_demand = esdl.ElectricityDemand(name="ElectricityDemand", id="electricity-demand-ID")

Create a location for the ElectricityDemand, create a port and assign carrier

.. code-block:: python

    electricity_demand_location = esdl.Point(lat=52.044, lon=4.3012)
    electricity_demand.geometry = electricity_demand_location

    electricity_demand_in_port = esdl.InPort(id="electricity-demand-in-port-ID", connectedTo=[power_plant_out_port])
    electricity_demand_in_port.carrier = electricity_commodity
    electricity_demand.port.append(electricity_demand_in_port)

Do not set quantity and unit now

.. code-block:: python

    electricity_demand_profile = esdl.SingleValue(id="electricity-demand-profile-ID", value=800.0)

Create QuantityAndUnitReference

.. code-block:: python

    electricity_demand_qty_unit = esdl.QuantityAndUnitType(id='ed-megawatthour-ID', physicalQuantity='ENERGY',
                                                           unit='WATTHOUR', multiplier='MEGA',
                                                           description='Energy in MWh')
    electricity_demand_profile.profileQuantityAndUnit = electricity_demand_qty_unit
    electricity_demand_in_port.profile.append(electricity_demand_profile)

Add the ElectricityDemand to the area

.. code-block:: python

    tutorial1_area.asset.append(electricity_demand)

Save the ESDL

.. code-block:: python

    energy_system_handler.save(folder_name + "/" + file_name)