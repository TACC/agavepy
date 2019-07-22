import petname
import socket
__all__ = ['clients_url', 'random_client_name']


def clients_url(tenant_url):
    """Returns the clients API endpoint for a given tenant
    """
    return '{0}/clients/v2'.format(tenant_url)


def random_client_name(words=3, letters=6, hostname=False):
    """Generate a pseudorandom but human-readable Oauth client name
    """
    client_name = petname.generate(words=words, letters=letters)
    if hostname:
        client_name = socket.gethostname().lower() + '-' + client_name
    return client_name
