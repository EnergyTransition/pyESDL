Installation
============

PyESDL now comes with a lot of support functions for handling profiles, geometries and quantity and units. This requires
additional dependencies. As not all users might need all functionalities, there are several ways to install pyESDL.

Use the following command to install the pyESDL python module including all dependencies from the PyPi registry:

``pip install pyESDL[all]``

To install the minimal version of pyESDL:

``pip install pyESDL``

To install the dependencies for additional profile functionalities (only required for support for Excel and InfluxDB):

``pip install pyESDL[profiles]``

To install the dependencies for handling geometries:

``pip install pyESDL[geometry]``
