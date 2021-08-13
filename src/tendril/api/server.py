

import importlib
from tendril.utils.versions import get_namespace_package_names
from tendril.api.core import app


_excluded_prefixes = []


def build_server(prefix='tendril.api'):
    for p in get_namespace_package_names(prefix):
        if p in _excluded_prefixes:
            continue
        try:
            modname = p
            globals()[modname] = importlib.import_module(modname)
            logger.info("Installed API Endpoints from {0}".format(p))
        except ImportError:
            pass
