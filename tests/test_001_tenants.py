import pytest
from . import TESTS_DATA


def test_tenants_list(test_tenant_id):
    """Tenants can be listed and contain the test tenant ID
    """
    from agavepy.tenants import list_tenants
    tenants = list_tenants()
    tenant_ids = [t.get('code') for t in tenants]
    assert len(tenant_ids) > 0, 'No tenants returned'
    assert test_tenant_id in tenant_ids, '{} not found in list'.format(
        test_tenant_id)


def test_api_server_from_id(test_tenant_id, test_api_server):
    """Test tenant ID resolves to test API server
    """
    from agavepy.tenants import api_server_by_id
    assert test_api_server == api_server_by_id(
        test_tenant_id), 'Tenant API servers do not match'
