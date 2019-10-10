import os
from agavepy.constants import (ENV_TENANTS_URL,
                               ENV_TENANT_ID,
                               DEFAULT_TENANTS_URL,
                               DEFAULT_TENANT_ID)

__all__ = ['TENANTS_URL', 'TENANT_ID']

TENANTS_URL = os.environ.get(
    ENV_TENANTS_URL, DEFAULT_TENANTS_URL)

TENANT_ID = os.environ.get(
    ENV_TENANT_ID, DEFAULT_TENANT_ID)
