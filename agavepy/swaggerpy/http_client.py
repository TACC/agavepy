#!/usr/bin/env python

#
# Copyright (c) 2013, Digium, Inc.
#
"""HTTP client abstractions.
"""

import logging
import requests
import requests.auth
import urllib.parse
import websocket

log = logging.getLogger(__name__)


class HttpClient(object):
    """Interface for a minimal HTTP client.
    """
    def close(self):
        """Close this client resource.
        """
        raise NotImplementedError("%s: Method not implemented",
                                  self.__class__.__name__)

    def request(self, method, url, params=None, data=None):
        """Issue an HTTP request.

        :param method: HTTP method (GET, POST, DELETE, etc.)
        :type  method: str
        :param url: URL to request
        :type  url: str
        :param params: Query parameters (?key=value)
        :type  params: dict
        :param data: Request body
        :type  data: Dictionary, bytes, or file-like object
        :return: Implementation specific response object
        """
        raise NotImplementedError("%s: Method not implemented",
                                  self.__class__.__name__)

    def ws_connect(self, url, params=None):
        """Create a WebSocket connection.

        :param url: WebSocket URL.
        :type  url: str
        :param params: Query parameters (?key=value)
        :type  params: dict
        :return: Implmentation specific WebSocket connection object
        """
        raise NotImplementedError("%s: Method not implemented",
                                  self.__class__.__name__)

    def set_basic_auth(self, host, username, password):
        """Configures client to use HTTP Basic authentication.

        :param host: Hostname to limit authentication to.
        :param username: Username
        :param password: Password
        """
        raise NotImplementedError("%s: Method not implemented",
                                  self.__class__.__name__)

    def set_api_key(self, host, api_key, param_name='api_key'):
        """Configures client to use api_key authentication.

        The api_key is added to every query parameter sent.

        :param host: Hostname to limit authentication to.
        :param api_key: Value for api_key.
        :param param_name: Parameter name to use in query string.
        """
        raise NotImplementedError("%s: Method not implemented",
                                  self.__class__.__name__)


class Authenticator(object):
    """Authenticates requests.

    :param host: Host to authenticate for.
    """
    def __init__(self, host):
        self.host = host

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, self.host)

    def matches(self, url):
        """Returns true if this authenticator applies to the given url.

        :param url: URL to check.
        :return: True if matches host, port and scheme, False otherwise.
        """
        split = urllib.parse.urlsplit(url)
        return self.host == split.hostname

    def apply(self, request):
        """Apply authentication to a request.

        :param request: Request to add authentication information to.
        """
        raise NotImplementedError("%s: Method not implemented",
                                  self.__class__.__name__)


# noinspection PyDocstring
class BasicAuthenticator(Authenticator):
    """HTTP Basic authenticator.

    :param host: Host to authenticate for.
    :param username: Username.
    :param password: Password
    """
    def __init__(self, host, username, password):
        super(BasicAuthenticator, self).__init__(host)
        self.auth = requests.auth.HTTPBasicAuth(username, password)

    def apply(self, request):
        request.auth = self.auth


# noinspection PyDocstring
class ApiKeyAuthenticator(Authenticator):
    """?api_key authenticator.

    This authenticator adds a query parameter to specify an API key.

    :param host: Host to authenticate for.
    :param api_key: API key.
    :param param_name: Query parameter specifying the API key.
    """
    def __init__(self, host, api_key, param_name='api_key'):
        super(ApiKeyAuthenticator, self).__init__(host)
        self.param_name = param_name
        self.api_key = api_key

    def apply(self, request):
        request.params[self.param_name] = self.api_key


class TokenAuthenticator(Authenticator):
    def __init__(self, host, token):
        super(TokenAuthenticator, self).__init__(host)
        self.token = token

    def apply(self, request):
        request.headers['Authorization'] = 'Bearer {}'.format(self.token)


class NonceAuthenticator(Authenticator):
    """ The NonceAuthenticator can be used when no authentication credentials are present at the time
    of the client instantiation. The assumption is that a nonce or token will be provided at request
    time to authenticate.
    """
    def __init__(self, host):
        super(NonceAuthenticator, self).__init__(host)

    def apply(self, request):
        pass


class JwtAuthenticator(Authenticator):
    def __init__(self, host, header_name, jwt):
        super(JwtAuthenticator, self).__init__(host)
        self.jwt = jwt
        self.header_name = header_name

    def apply(self, request):
        request.headers[self.header_name] = self.jwt
        request.url = request.url.strip('/v2')


# noinspection PyDocstring
class SynchronousHttpClient(HttpClient):
    """Synchronous HTTP client implementation.
    """
    def __init__(self, verify=None):
        self.session = requests.Session()
        self.authenticator = None
        self.websockets = set()
        self.verify = verify

    def close(self):
        self.session.close()
        # There's no WebSocket factory to close; close connections individually

    def set_basic_auth(self, host, username, password):
        self.authenticator = BasicAuthenticator(host=host,
                                                username=username,
                                                password=password)

    def set_api_key(self, host, api_key, param_name='api_key'):
        self.authenticator = ApiKeyAuthenticator(host=host,
                                                 api_key=api_key,
                                                 param_name=param_name)

    def set_token(self, host, token):
        self.authenticator = TokenAuthenticator(host=host, token=token)

    def set_jwt(self, host, header_name, jwt):
        self.authenticator = JwtAuthenticator(host, header_name, jwt)

    def set_nonce(self, host):
        self.authenticator = NonceAuthenticator(host)

    def request(self,
                method,
                url,
                params=None,
                data=None,
                headers=None,
                files=None,
                proxies=None):
        """Requests based implementation.

        :return: Requests response
        :rtype:  requests.Response
        """
        req = requests.Request(method=method,
                               url=url,
                               params=params,
                               data=data,
                               headers=headers,
                               files=files)
        self.apply_authentication(req)
        return self.session.send(self.session.prepare_request(req),
                                 verify=self.verify,
                                 proxies=proxies)

    def ws_connect(self, url, params=None):
        """Websocket-client based implementation.

        :return: WebSocket connection
        :rtype:  websocket.WebSocket
        """
        # Build a prototype request and apply authentication to it
        proto_req = requests.Request('GET', url, params=params)
        self.apply_authentication(proto_req)
        # Prepare the request, so params will be put on the url,
        # and authenticators can manipulate headers
        preped_req = proto_req.prepare()
        # Pull the Authorization header, if needed
        header = [
            "%s: %s" % (k, v) for (k, v) in list(preped_req.headers.items())
            if k == 'Authorization'
        ]
        # Pull the URL, which includes query params
        url = preped_req.url
        return websocket.create_connection(url, header=header)

    def apply_authentication(self, req):
        if self.authenticator and self.authenticator.matches(req.url):
            self.authenticator.apply(req)
