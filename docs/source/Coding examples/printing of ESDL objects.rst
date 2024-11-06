Printing of ESDL Objects
========================

Sometimes it is convenient to print ESDL objects, but they all look the same: the class name and
then a hexadecimal memory location, e.g. :code:`<esdl.esdl.WindTurbine object at 0x00000215AF0EE590>`.
This snippet makes them more useful, using the repr() functionality of Python:


.. code-block:: python

    esdl.InfluxDBProfile.__repr__ = lambda x: f"<{x.eClass.name} name={x.name}, measurement={x.measurement}, field={x.field}>"
    esdl.Consumer.__repr__ = lambda x: f"<{x.eClass.name} name={x.name}, id={x.id}>"

As a :code:`Consumer` is a super class, all subclasses (like :code:`HeatingDemand`) will also be printed using this `repr`.
Output will be like:

.. code-block::

    <InfluxDBProfile name=Profile1, measurement=profiles, field=profile1>
    <HeatingDemand name=HeatDemand1, id=id1>

More advanced :code:`__repr__` is useful for Ports:

.. code-block:: python

    esdl.Port.__repr__ = lambda x: f'<{x.eClass.name}[{x.name}] of {x.eContainer().name if x.eContainer() else None}, id={x.id}>'

This will print also the name of the container object, e.g.:

.. code-block::

     <OutPort[Out] of WindTurbine_c53e, id=2040dfa0-bb51-4d57-9b11-9b0001429b71>


