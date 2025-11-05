# Including specific path.

import sys
from pathlib import Path

# Define list stores the paths to add.
paths_to_add= [
    'chapter_10',
    'chapter_9_sort',
    'chapter_8',
    'chapter_7',
    'chapter_7_ex',
    'chapter_6',
    'chapter_5',
    'chapter_4',
    'chapter_3',
    'chapter_2',
    'chapter_1',
]

# Define new root of source files.
src_root = Path(__file__).resolve().parents[1] / 'pysource'

# Define the variable used by jinja2
pysrc = str(src_root)

# Insertion of the paths.
for paths in paths_to_add:
    sys.path.insert(0, str(src_root/paths))


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Pydsadoc"
copyright = '2025, Aina'
author = 'Aina'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx_copybutton',
    'sphinx_inline_tabs',
]

templates_path = [
    '_templates', 
    '_templates/furo',
]

exclude_patterns = []

# -- Options for the Python domain -------------------------------------------
add_module_names = False


# -- Options for sphinx.ext.autodoc ------------------------------------------

autodoc_default_options = {
    'member-order': 'bysource',
    'undoc-members': True,
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

html_theme_options = {
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/Enec0De/pydsadoc",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
            "class": "",
        },
    ],
    "source_repository": "https://github.com/Enec0De/pydsadoc",
    "source_branch": "main",
    "source_directory": "sphinx/pydsadoc/source",
}

# html_logo = "_static/hammer.svg"
html_favicon = "_static/hammer.svg"

# Set to '' to prevent appending "documentation" to the site title
html_title = ""
