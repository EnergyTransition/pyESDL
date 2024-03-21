Tutorial 2: Load and manipulate an ESDL
=======================================

This tutorial demonstrates how to load an existing ESDL file, and how to change some of its parameters. In this example, the ESDL created in Tutorial 1 is loaded, and the efficiency of the power plant is changed. The changed ESDL is saved as a new file, for the sake of comparison with the original.

Start with importing the required libraries

.. code-block:: python

    from esdl import esdl
    from esdl.esdl_handler import EnergySystemHandler

.. code-block:: python

    if __name__ == '__main__':

Specify a folder name, a file name to edit, and a file name to save the edited ESDL (not to overwrite the original)

.. code-block:: python

        folder_name = "ESDLs"
        file_name_to_edit = "Tutorial1.esdl"
        file_name_to_save = "Tutorial2.esdl"

Create an EnergySystemHandler - a class that helps a developer to read and write ESDL-files

.. code-block:: python

    energy_system_handler = EnergySystemHandler()

Load an existing energy system from and ESDL file

.. code-block:: python

    energy_system: esdl.EnergySystem = energy_system_handler.load_file(folder_name + "/" + file_name_to_edit)

Iterate through ESDL elements using eAllContents() to find a PowerPlant

.. code-block:: python

    for esdl_element in energy_system.eAllContents():

Check if the element is a PowerPlant (in this ESDL, there is only one PowerPlant)

.. code-block:: python

        if isinstance(esdl_element, esdl.PowerPlant):

Change the PowerPlant's efficiency

.. code-block:: python

            esdl_element.efficiency = 0.7

Save the changes to a new ESDL

.. code-block:: python

    energy_system_handler.save(folder_name + "/" + file_name_to_save)