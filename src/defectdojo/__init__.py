from .finding import DojoFinding

from sphinx.application import Sphinx

def setup(app: Sphinx):
    """
    Extension setup, called by Sphinx
    """

    app.add_directive('dojofinding', DojoFinding)