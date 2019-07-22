from __future__ import print_function
from ..constants import BASE_URL


def tenants_url(url=None, base_url=BASE_URL):
    """Returns the URL for tenants operations
    """
    if url is not None:
        return url
    else:
        return base_url + '/tenants'
