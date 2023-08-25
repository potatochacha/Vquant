# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import os
import sys
sys.path.insert(0, os.path.abspath('../../../maincode'))
sys.path.insert(0, os.path.abspath('../../../maincode/vquant\_kernel'))
from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify
# import pydata_sphinxsphinx_theme

# -- Project information -----------------------------------------------------

project = 'Vquants'
copyright = '2023, Huanning Dong'
author = 'Huanning Dong'

# The full version, including alpha/beta/rc tags
release = '1.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
  'sphinx.ext.autodoc',
  'sphinx.ext.doctest',
  'sphinx.ext.intersphinx',
  'sphinx_rtd_theme',
  'sphinx.ext.todo',
  'sphinx.ext.coverage',
  'sphinx.ext.mathjax',
  'sphinx.ext.ifconfig',
  'sphinx.ext.viewcode',
  'sphinx.ext.githubpages',
  'sphinx.ext.imgmath',
  'sphinx.ext.napoleon',
  'sphinx.ext.autosectionlabel',
  'sphinx.ext.coverage',
  'sphinx.ext.mathjax',
  'recommonmark',
  'sphinx_markdown_tables',
  'sphinx.ext.napoleon',
  'sphinx.ext.inheritance_diagram',
]
autoapi_dirs = ['../../../maincode']
autoapi_options = ['members', 'undoc-members', 'private-members', 'show-inheritance', 'show-module-summary', 'special-members', 'imported-members']
autoapi_type = 'python'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
todo_include_todos = True
# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
source_suffix = ['.rst', '.md', '.MD']

def setup(app):
    github_doc_root = 'https://github.com/potatochacha'
    app.add_config_value('recommonmark_config', {
        # 'url_resolver': lambda url: github_doc_root + url,
        "enable_auto_toc_tree": True,
        "auto_toc_tree_section": "目录",
        'auto_toc_maxdepth': 2,
        "enable_math": True,
        'enable_eval_rst': True
    }, True)

    app.add_transform(AutoStructify)

# html_theme = 'alabaster'
html_theme = 'pydata_sphinx_theme'
# html_theme = 'sphinx_book_theme'
html_theme_options = {
    "footer_start": ["copyright"],
    'navigation_depth': 2,
    'navbar_align': 'content',
    "icon_links": [
    {
        "name": "GitHub",
        "url": "https://github.com/potatochacha",
        "icon": "fa-brands fa-square-github",
        "type": "fontawesome",
    },
],
  }
html_static_path = ['./maincode/Vquant_docs/introd/_static']
html_logo = "./_static/duck3.png"
html_favicon = "./_static/duck3.png"
html_css_files = ['./_static/custom.css']

html_sidebars = {
    "<page_pattern>": ["list", "of", "templates"]
}

# favicons = [
#     {
#         "sizes": "16x16",
#         "href": "https://profile-avatar.csdnimg.cn/334f3ec1c2484587b63913c30e39182b_qq_33039859.jpg",
#     },
#     {
#         "sizes": "32x32",
#         "href": "https://profile-avatar.csdnimg.cn/334f3ec1c2484587b63913c30e39182b_qq_33039859.jpg",
#     },
#     {
#         "rel": "apple-touch-icon",
#         "sizes": "180x180",
#         "href": "like_me.jpeg",  # use a local file in _static
#     },
# ]

source_parsers = {
    '.md': CommonMarkParser,
    '.MD': CommonMarkParser,
}
source_encoding = 'utf-8-sig'
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
