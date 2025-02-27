# Configuration file for the Sphinx documentation builder.

# -- Project Information -----------------------------------------------------
project = 'Data and AI Handbook'
copyright = '2025, iSigma'
author = 'Chanaka S. Rupasinghe and Dinesh S. Gamage'

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
html_theme = "sphinx_book_theme"

# Enable collapsible sidebar & proper navigation
html_theme_options = {
    "repository_url": "https://github.com/iSigma/dataaihandbook",  # Replace with actual repo
    "repository_branch": "main",  # Adjust if needed
    "use_repository_button": True,  # GitHub button
    "use_edit_page_button": True,  # Edit button
    "use_issues_button": True,  # Report issues button
    "use_fullscreen_button": True,  # Enables fullscreen button
    "collapse_navigation": True,  # ✅ Enables collapsible sidebar
    "show_navbar_depth": 2,  # ✅ Controls sidebar depth
    "home_page_in_toc": True,  # ✅ Include homepage in ToC
}



# Ensure `_static` is linked properly
html_static_path = ['_static']
#html_css_files = ["custom.css"]
#html_js_files = ["sidebar_toggle.js"]
