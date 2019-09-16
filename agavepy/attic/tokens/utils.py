__all__ = ['tokens_url']


def tokens_url(tenant_url):
    """Returns the tokens API endpoint
    """
    return '{0}/token'.format(tenant_url)
