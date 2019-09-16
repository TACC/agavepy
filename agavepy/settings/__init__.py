"""Provides environment variable-driven runtime configuration
"""
PKG_NAME = 'tapis_py'

from attrdict import AttrDict  # noqa
from .helpers import ENV_PREFIX  # noqa
from .log import *  # noqa
from .tenancy import *  # noqa


def all_settings():
    """Returns name and value of all settings
    """
    from types import ModuleType

    settings = {}
    for name, item in globals().items():
        # Ignore callables and private properties
        if not callable(item) and not name.startswith("__") \
                and not isinstance(item, ModuleType):
            settings[name] = item
    return AttrDict(settings)
