# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

"""Base widget class for widgets provided in Core"""

from .widget import Widget
from .._version import __jupyter_widget_version__

from traitlets import Unicode

class CoreWidget(Widget):

    _model_module = Unicode('jupyter-js-widgets').tag(sync=True)
    _model_module_version = Unicode(__jupyter_widget_version__).tag(sync=True)
    _view_module = Unicode('jupyter-js-widgets').tag(sync=True)
    _view_module_version = Unicode(__jupyter_widget_version__).tag(sync=True)
