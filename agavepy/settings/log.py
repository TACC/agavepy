import os
from .helpers import (ns_os_environ_get, parse_boolean, int_or_none)

__all__ = ['LOG_LEVEL', 'SWAGGERPY_LOG_LEVEL']

LOG_LEVEL = ns_os_environ_get("LOG_LEVEL", 10)
SWAGGERPY_LOG_LEVEL = ns_os_environ_get("SWAGGERPY_LOG_LEVEL", 20)
