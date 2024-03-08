Tutorial 2: Load and manipulate an ESDL
===============

<< Introduction text to this tutorial >>

Start with importing the required libraries

.. code-block:: python

    from esdl import esdl
    from esdl.esdl_handler import EnergySystemHandler

.. code-block:: python

    if __name__ == '__main__':
        folder_name = "ESDLs"
        file_name_to_edit = "Tutorial1.esdl"
        file_name_to_save = "Tutorial2.esdl"

Create an EnergySystemHandler - a class that helps a developer to read and write ESDL-files

.. code-block:: python

    energy_system_handler = EnergySystemHandler()

Load an existing energy system from and ESDL file.

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