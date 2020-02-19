import requests
from agavepy.util import clients_url, random_client_name

__all__ = ['ClientCommands']


class ClientCommands(object):
    def clients_create(self,
                       client_name=None,
                       description=None,
                       tenant_url=None,
                       username=None,
                       password=None,
                       quiet=False):
        """ Create an Oauth client

        Make a request to the API to create an Oauth client. Returns the client
        API key and secret as a tuple.

        KEYWORD ARGUMENTS
        -----------------
        client_name: string
            Name for Oauth2 client.
        description: string
            Description of the Oauth2 client
        tenant_url: string
            URL of the API tenant to interact with
        username: string
            The user's username.
        password: string
            The user's password

        RETURNS
        -------
        api_key: string
        api_secret: string
        """

        # Set request endpoint.
        if tenant_url is None:
            tenant_url = getattr(self, 'api_server')
        endpoint = clients_url(tenant_url)

        # User credentials
        if username is None:
            username = getattr(self, 'username')
        if password is None:
            password = getattr(self, 'password')

        # Make sure client_name is not empty
        if client_name == '' or client_name is None:
            client_name = random_client_name(words=2, hostname=True)

        # Make request.
        try:
            data = {
                'clientName': client_name,
                'description': description,
                'tier': 'Unlimited',
                'callbackUrl': '',
            }
            response = requests.post(endpoint,
                                     data=data,
                                     auth=(username, password))
            del password
        except Exception:
            del password
            raise

        # Parse the request's response and return api key and secret.
        result = response.json().get('result', {})
        api_key = result.get('consumerKey')
        api_secret = result.get('consumerSecret')
        if api_key == '' or api_secret == '':
            raise requests.exceptions.HTTPError(
                'Failed to create client {0}'.format(client_name))

        return {
            'api_key': api_key,
            'api_secret': api_secret,
            'client_name': client_name
        }
