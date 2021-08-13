

import importlib
from tendril.utils.versions import get_namespace_package_names
from tendril.utils import log

logger = log.getLogger(__name__, log.DEFAULT)

from tendril.api.core import app

_excluded_prefixes = [
    'tendril.api.server'
]


def build_server(prefix='tendril.api'):
    for p in get_namespace_package_names(prefix):
        if p in _excluded_prefixes:
            continue
        try:
            modname = p
            globals()[modname] = importlib.import_module(modname)
            logger.info("Installing API Endpoints from {0}".format(p))
        except ImportError:
            pass


build_server()
