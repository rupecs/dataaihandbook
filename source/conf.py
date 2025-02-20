# Configuration file for the Sphinx documentation builder.

# -- Project Information -----------------------------------------------------
project = 'Sphinx-with-Github-Pages'
copyright = '2021, Hao Mai'
author = 'Hao Mai'

# -- General Configuration ---------------------------------------------------
extensions = [
    'myst_parser',  # Enable Markdown support
    'sphinx.ext.mathjax',  # Enable MathJax for equations
    'sphinx.ext.autodoc',  # Automatic documentation from docstrings
    'sphinx.ext.napoleon',  # Google-style docstrings support
]

# Define file suffixes that Sphinx should recognize
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Add paths for templates
templates_path = ['_templates']

# List of patterns to exclude from documentation
exclude_patterns = []

# -- HTML Output Options -----------------------------------------------------
html_theme = "press"  # Use Press theme

# Add paths for custom static files
html_static_path = ['_static']
