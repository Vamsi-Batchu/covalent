# Copyright 2021 Agnostiq Inc.
#
# This file is part of Covalent.
#
# Licensed under the GNU Affero General Public License 3.0 (the "License").
# A copy of the License may be obtained with this software package or at
#
#      https://www.gnu.org/licenses/agpl-3.0.en.html
#
# Use of this file is prohibited except in compliance with the License. Any
# modifications or derivative works of this file must retain this copyright
# notice, and modified files must contain a notice indicating that they have
# been altered from the originals.
#
# Covalent is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the License for more details.
#
# Relief from the License may be granted by purchasing a commercial license.

"""Configuration file for the Sphinx documentation builder."""

import os
import sys

# Project information
project = ""
copyright = "2021 Agnostiq Inc."
author = "Agnostiq"

html_static_path = ["_static"]


# Sphinx Extensions
sys.path.append(os.path.abspath("./extensions"))

extensions = [
    "sphinx.ext.autodoc",
    "sphinx_panels",
    "sphinx.ext.napoleon",
    "sphinx_automodapi.automodapi",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
    "sphinx_design",
    "autodocsumm",
    "nbsphinx",
    "sphinx_autodoc_typehints",
    "sphinx-prompt",
    "sphinx_inline_tabs",
    "sphinx_execute_code",
    "sphinx_click.ext",
    "sphinx_autodoc_typehints",
    "myst_parser",
    'sphinx_reredirects'
]

# Sphinx variables
numpydoc_show_class_members = False
autosummary_generate = True
autodoc_default_options = {
    "autosummary": True,
}
exclude_patterns = ["_build", "**.ipynb_checkpoints"]
nbsphinx_execute = "never"
highlight_language = "python"
html_scaled_image_link = False
add_module_names = True

templates_path = ["_templates"]

# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# Options for HTML output
html_static_path = ["_static"]
templates_path = ["_templates"]
html_theme = "furo"

html_title = ""
html_favicon = "_static/covalent-logo-blue-favicon.png"
html_theme_options = {
    "light_logo": "covalent-logo-horizontal-blue.png",
    "dark_logo": "covalent-logo-horizontal-light.png",
    "light_css_variables": {
        "color-brand-primary": "#5552FF",
        "color-brand-content": "#6D7CFF",
    },
    "dark_css_variables": {
        "color-brand-primary": "#5552FF",
        "color-brand-secondary": "#AEB6FF",
        "color-brand-ternary": "#6E33ED",
        "color-brand-content": "#6D7CFF",
    },
}

# Options for Markdown files
myst_enable_extensions = [
    "colon_fence",
    "deflist",
]
myst_heading_anchors = 3

baseurl="https://develop.d19pvbre9ckryz.amplifyapp.com"

redirects = {
    "troubleshooting": baseurl + "/docs/user-documentation/troubleshooting",
    # "tutorials/tutorials":  baseurl + "/docs/user-documentation/tutorials",
    "credentials":  baseurl + "/docs/user-documentation/credentials/",
    "plugins":  baseurl + "/docs/features/executor-plugins/exe",
    "about/why_covalent":  baseurl + "/docs/why-covalent",
    "api/executors/index":  baseurl + "/docs/features/executor-plugins/exe",
    # "how_to/index":  baseurl + "/docs/user-documentation/how-to/how-to-guide",
    "features/triggers":  baseurl + "/docs/features/triggers",
    "api/executors/dask":  baseurl + "/docs/user-documentation/api-reference/executors/dask/",
    "api/executors/ssh":  baseurl + "/docs/user-documentation/api-reference/executors/ssh",
    "api/executors/slurm":  baseurl + "/docs/user-documentation/api-reference/executors/slurm",
    "api/executors/awsplugins":  baseurl + "/docs/features/executor-plugins/aws-plugins",
    "api/executors/awsec2":  baseurl + "/docs/user-documentation/api-reference/executors/awsec2",
    "api/executors/awsecs":  baseurl + "/docs/user-documentation/api-reference/executors/awsecs",
    "glossary/index":  baseurl + "/docs/glossary",
    "features/cancel":  baseurl + "/docs/features/cancellation",
    "webapp_ui/index":  baseurl + "/docs/user-documentation/user-interface/the-ui",
    "webapp_ui/dashboard/index":  baseurl + "/docs/user-documentation/user-interface/dashboard",
    "webapp_ui/dashboard/summary":  baseurl + "/docs/user-documentation/user-interface/dispatch-summary",
    "webapp_ui/dashboard/dispatch_list":  baseurl + "/docs/user-documentation/user-interface/workflow-dispatch-list",
    "webapp_ui/dashboard/navigation/pagination":  baseurl + "/docs/user-documentation/user-interface/pagination",
    "webapp_ui/dashboard/navigation/search":  baseurl + "/docs/user-documentation/user-interface/search",
    "webapp_ui/dashboard/navigation/sort":  baseurl + "/docs/user-documentation/user-interface/sort",
    "webapp_ui/dashboard/navigation/filter":  baseurl + "/docs/user-documentation/user-interface/filter",
    "webapp_ui/dashboard/navigation/delete_dispatches":  baseurl + "/docs/user-documentation/user-interface/workflow-dispatch-deletetion",
    "webapp_ui/graph_view/index":  baseurl + "/docs/user-documentation/user-interface/graph-view",
    "webapp_ui/graph_view/graphs":  baseurl + "/docs/user-documentation/user-interface/transport-graph",
    "webapp_ui/graph_view/lattice":  baseurl + "/docs/user-documentation/user-interface/lattice-sidebar",
    "webapp_ui/graph_view/electron":  baseurl + "/docs/user-documentation/user-interface/electron-sidebar",
    # "index":  baseurl + "/docs/", 
    # remove this when you are pushing the code again
    "getting_started/quick_start/index":  baseurl + "/docs/get-started/quick-start",
    "getting_started/first_experiment/index":  baseurl + "/docs/get-started/first-experiment",
    "concepts/concepts":  baseurl + "/docs/user-documentation/credentials/",
    "concepts/basics":  baseurl + "/docs/user-documentation/concepts/covalent-basics",
    "concepts/architecture":  baseurl + "/docs/user-documentation/concepts/covalent-arch/covalent-architecture",
    "concepts/api_concepts":  baseurl + "/docs/user-documentation/concepts/covalent-arch/covalent-sdk",
    "concepts/server_concepts":  baseurl + "/docs/user-documentation/concepts/covalent-arch/covalent-services",
    "concepts/ui_concepts":  baseurl + "/docs/user-documentation/concepts/covalent-arch/covalent-gui",
    "tutorials/0_ClassicalMachineLearning/mnist_images/source":  baseurl + "/docs/user-documentation/tutorials/mnist/",
    "tutorials/1_QuantumMachineLearning/pennylane_hybrid/source":  baseurl + "/docs/user-documentation/tutorials/hybrid/",
    "tutorials/0_ClassicalMachineLearning/autoencoders/source":  baseurl + "/docs/user-documentation/tutorials/autoencoders/",
    "tutorials/5_QPUAccessIBM/source":  baseurl + "/docs/user-documentation/tutorials/qpuaccessibm/",
    "tutorials/1_QuantumMachineLearning/pennylane_iris_classification/source":  baseurl + "/docs/user-documentation/tutorials/iris/",
    "tutorials/1_QuantumMachineLearning/pennylane_parity_classifier/source":  baseurl + "/docs/user-documentation/tutorials/parityclassify/",
    "tutorials/machine_learning/dnn_comparison":  baseurl + "/docs/user-documentation/tutorials/dnn_comparison/"
}