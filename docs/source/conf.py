# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

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
from unittest.mock import MagicMock, Mock

sys.path.insert(0, os.path.abspath('../../choirbot'))

html_theme = "sphinx_rtd_theme"


# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.mathjax',
              'sphinx.ext.viewcode',
              'sphinx.ext.napoleon',
              'sphinx.ext.intersphinx',
              'sphinx_autodoc_typehints',
              ]
napoleon_use_param = True

# mock modules
MOCK_MODULES = ['rclpy', 'rclpy.node', 'rclpy.guard_condition', 'rclpy.qos', 'rclpy.callback_groups',
    'rclpy.task', 'rclpy.duration', 'rclpy.executors', 'visualization_msgs', 'visualization_msgs.msg',
    'std_msgs', 'std_msgs.msg', 'geometry_msgs', 'geometry_msgs.msg']

class RecursiveMagicMock(MagicMock):
    @classmethod
    def __getattr__(cls, name):
        return MagicMock()

for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = RecursiveMagicMock()

# special mock classes
sys.modules['rclpy.node'].Node = object
sys.modules['rclpy.guard_condition'].GuardCondition = object

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']


# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# -- Project information -----------------------------------------------------

project = 'ChoiRbot'
copyright = '2020, Andrea Testa, Andrea Camisa, Giuseppe Notarstefano'
author = 'Andrea Testa, Andrea Camisa, Giuseppe Notarstefano'

# The full version, including alpha/beta/rc tags
release = '0.0.1'

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'rclpy': ('http://docs.ros2.org/dashing/api/rclpy/', None),
}

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# the following two functions serve enable automatic documentation of __init__ methods
def skip(app, what, name, obj, would_skip, options):
    if name == "__init__":
        return False
    return would_skip

def setup(app):
    app.connect("autodoc-skip-member", skip)


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']
html_static_path = []


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'examplecodedoc'