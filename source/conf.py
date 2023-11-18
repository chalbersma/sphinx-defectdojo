# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# Make Local Deve Work
import sys
import os

sys.path.append(os.path.abspath('../src/'))

project = 'sphinx-defectdojo'
copyright = '2023, Chris Halbersma'
author = 'Chris Halbersma'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["defectdojo"]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
