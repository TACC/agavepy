import os
from agavepy.constants import (ENV_TENANTS_URL, ENV_TENANT_ID,
                               DEFAULT_TENANTS_URL, DEFAULT_TENANT_ID,
                               ENV_DEFAULT_TENANT_ID)

__all__ = ['TAPIS_TENANTS_URL', 'TAPIS_DEFAULT_TENANT_ID']

TAPIS_TENANTS_URL = os.environ.get(ENV_TENANTS_URL, DEFAULT_TENANTS_URL)

TAPIS_DEFAULT_TENANT_ID = os.environ.get(ENV_DEFAULT_TENANT_ID,
                                         DEFAULT_TENANT_ID)
