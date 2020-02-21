import os
from .helpers import (ns_os_environ_get, parse_boolean, int_or_none)

__all__ = [
    'LOG_LEVEL', 'TAPISPY_LOG_LEVEL', 'SWAGGERPY_LOG_LEVEL', 'SHOW_CURL',
    'VERBOSE_ERRORS'
]

DEFAULT_LOG_LEVEL = 'WARNING'
LOG_LEVEL = ns_os_environ_get('LOG_LEVEL', DEFAULT_LOG_LEVEL)
TAPISPY_LOG_LEVEL = ns_os_environ_get('TAPISPY_LOG_LEVEL', LOG_LEVEL)
SWAGGERPY_LOG_LEVEL = ns_os_environ_get('SWAGGERPY_LOG_LEVEL',
                                        TAPISPY_LOG_LEVEL)
SHOW_CURL = parse_boolean(ns_os_environ_get('SHOW_CURL', '0'))
VERBOSE_ERRORS = parse_boolean(ns_os_environ_get('VERBOSE_ERRORS', '1'))
