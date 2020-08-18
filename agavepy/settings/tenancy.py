import os
from agavepy.constants import (ENV_TENANTS_URL, ENV_TENANT_ID,
                               DEFAULT_TENANTS_URL, DEFAULT_TENANT_ID,
                               ENV_DEFAULT_TENANT_ID, 
                               ENV_DEFAULT_VERIFY_SSL,
                               DEFAULT_VERIFY_SSL)
from .helpers import (ns_os_environ_get, parse_boolean, int_or_none)

__all__ = ['TAPIS_TENANTS_URL', 'TAPIS_DEFAULT_TENANT_ID', 'TAPISPY_VERIFY_SSL']

TAPIS_TENANTS_URL = os.environ.get(ENV_TENANTS_URL, DEFAULT_TENANTS_URL)

TAPIS_DEFAULT_TENANT_ID = os.environ.get(ENV_DEFAULT_TENANT_ID,
                                         DEFAULT_TENANT_ID)

TAPISPY_VERIFY_SSL = parse_boolean(
    os.environ.get(ENV_DEFAULT_VERIFY_SSL, DEFAULT_VERIFY_SSL))

