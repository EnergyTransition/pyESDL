# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath("../../esdl/"))
sys.path.insert(0, os.path.abspath("../../"))
print(sys.path)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
from esdl import _version

project = 'pyESDL'
copyright = 'Ewoud Werkman, Edwin Matthijssen, Selma Causevic'
author = 'Ewoud Werkman, Edwin Matthijssen, Selma Causevic'
#release = '2023'
version = _version.get_versions()['version']
if '+' in version:
    version = version.split('+')[0]  # remove any 'dirty' state information

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_rtd_theme",
    # "sphinx.ext.autosectionlabel",
    "sphinx.ext.autodoc",
    # "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.napoleon"
]

templates_path = ['_templates']
exclude_patterns = []

autodoc_member_order = 'bysource'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
