Tutorial 4: Exporting ESDL parameters to Excel
==============================================

This tutorial shows how to export ESDL parameters to an Excel file (in CSV format). For that purpose, the ESDL from Tutorial 3 is loaded, and energy asset parameters such as type, ID, name, power, and efficiency are written to an Excel file.

Start with importing the required libraries

.. code-block:: python

    from esdl import esdl
    from esdl.esdl_handler import EnergySystemHandler
    import pandas as pd

Define constants such as ESDL file name and the folder it is located in.

.. code-block:: python

    if __name__ == '__main__':
        folder_name = "ESDLs"
        file_name = "Tutorial3_pyESDL.esdl"

Create an EnergySystemHandler - a class that helps a developer to read and write ESDL-files

.. code-block:: python

        energy_system_handler = EnergySystemHandler()

Load the ESDL file whose energy asset parameters will be written to a CSV file.

.. code-block:: python

        energy_system: esdl.EnergySystem = energy_system_handler.load_file(folder_name + "/" + file_name)

Define lists where different asset parameters will be written to (this will later be added to a DataFrame which is converted to a CSV file.

.. code-block:: python

        asset_types_list = []
        asset_names_list = []
        asset_ids_list = []
        asset_powers_list = []
        asset_efficiencies_list = []

Define a DataFrame which will contain asset parameters, and which will be converted to a CSV file.

.. code-block:: python

        asset_parameters = pd.DataFrame()

Iterate through all ESDL elements

.. code-block:: python

        # get_all_instances_of_type
        for esdl_element in energy_system.eAllContents():

Check if the element is an EnegyAsset

.. code-block:: python

            if isinstance(esdl_element, esdl.EnergyAsset):

If it is, write its type (using eClass.name), ID, and name to a corresponding list
.. code-block:: python

                asset_types_list.append(esdl_element.eClass.name)
                asset_ids_list.append(esdl_element.id)
                asset_names_list.append(esdl_element.name)

If an element is a Producer, a Consumer or a Conversion, write its power

.. code-block:: python

                if isinstance(esdl_element, esdl.Producer) or isinstance(esdl_element, esdl.Consumer) or isinstance(
                        esdl_element, esdl.Conversion):
                    asset_powers_list.append(esdl_element.power)
                else:
                    asset_powers_list.append("")

If an element is a PowerPlant, write its efficiency

.. code-block:: python

                if isinstance(esdl_element, esdl.PowerPlant):
                    asset_efficiencies_list.append(esdl_element.efficiency)
                else:
                    asset_efficiencies_list.append("")

Add the lists to the DataFrame

.. code-block:: python

        asset_parameters["Type"] = asset_types_list
        asset_parameters["ID"] = asset_ids_list
        asset_parameters["Name"] = asset_names_list
        asset_parameters["Power"] = asset_powers_list
        asset_parameters["Efficiency"] = asset_efficiencies_list

Define the name of the CSV, and convert the DataFrame to that CSV

.. code-block:: python

        filename = 'asset_parameters.csv'
        asset_parameters.to_csv(filename,
                                index=False,
                                sep=';')
