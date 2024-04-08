Ecore functionality in pyESDL
=============================

As described in :doc:`/Technical foundation/index`, pyESDL and ESDL are build upon ECore.
This offers some extra functionality that is usually not available in other data structure libraries.

Tips & Tricks
-------------

The ESDL ECore model describes the classes that are available in the ESDL language. Classes, such
as ``esdl.GenericProdcuer`` are the specification of the objects present in the language,
while objects are the instantiation of the classes at runtime (``gp = esdl.GenericProducer()``).

All Ecore related methods/attributes start with the letter 'e'.

.. The following raw html is necessary to fix long line wrapping
   with the sphinx theme and the vertical alignment of the table


.. raw:: html

   <style>
   .wy-table-responsive table td,.wy-table-responsive table th{white-space:normal}
   .rst-content table.docutils td { vertical-align: top }
   </style>

.. list-table:: ECore functionality examples
   :widths: 45 50
   :header-rows: 1

   * - Code
     - Explanation
   * - ``esdl_object.eClass``
     - Refers to the Class it belongs to (name, references, attributes).
       Both references and attributes are called `features` in Ecore terminology

   * - ``esdl_object.eAllContents()``
     - Lists all objects contained in an object in ESDL.
       When you use the energySystem object here, it will iterate over all objects in the ESDL. It returns an iterator.
   * - ``esdl_object.eContainer()``
     - Returns the container this object belongs to, e.g. its parent.
   * - ``esdl_object.eGet('attribute_name')``
     - Gets the value of the attribute (same as ``esdl_object.attribute_name``)
   * - ``esdl_object.eSet('attribute_name', value)``
     - Sets the value of the attribute (same as ``esdl_object.attribute_name = value``)
   * - ``esdl_object.eIsSet('attribute_name')``
     - Checks if the attribute is set in the model
       (otherwise it will return the default value)



As shown above, each runtime object has a reference to its EClass.
To get the name of the class of an ESDL object you can do the following:

.. code-block:: python

  import esdl

  gp = esdl.GenericProducer()
  class_name = gp.eClass.name
  print(class_name)

  >> GenericProducer

