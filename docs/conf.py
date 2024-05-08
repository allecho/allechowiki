# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'allechowiki'
copyright = '2024, JonLee'
author = 'JonLee'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
        'recommonmark',
        'sphinx_markdown_tables'
]

# added support for .md doc
from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify
source_parsers = {
    '.md': 'recommonmark.parser.CommonMarkParser',
}
source_suffix = ['.rst', '.md']

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# web favicon
html_favicon = '_static/icon/icon.png'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '_static/icon/icon2.png'
