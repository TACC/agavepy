"""Provides environment variable-driven runtime configuration
"""
PKG_NAME = 'tapis_py'
import os
import warnings
from dotenv import load_dotenv, find_dotenv

with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    if not load_dotenv(find_dotenv()):
        if not load_dotenv(find_dotenv(usecwd=True)):
            load_dotenv(os.path.join(os.path.expanduser('~'), '.env'))

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
