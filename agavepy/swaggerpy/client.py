#
# Copyright (c) 2013, Digium, Inc.
#

"""Swagger client library.
"""

import json
import logging
import os.path
import re
import urllib.request, urllib.parse, urllib.error
import swaggerpy
from numbers import Real

from requests_toolbelt import MultipartEncoder

from swaggerpy.http_client import SynchronousHttpClient
from swaggerpy.processors import WebsocketProcessor, SwaggerProcessor

log = logging.getLogger(__name__)


class ClientProcessor(SwaggerProcessor):
    """Enriches swagger models for client processing.
    """

    def process_resource_listing_api(self, resources, listing_api, context):
        """Add name to listing_api.

        :param resources: Resource listing object
        :param listing_api: ResourceApi object.
        :type context: ParsingContext
        :param context: Current context in the API.
        """
        name, ext = os.path.splitext(os.path.basename(listing_api['path']))
        listing_api['name'] = name


class Operation(object):
    """Operation object.
    """

    def __init__(self, uri, operation, http_client):
        self.uri = uri
        self.json = operation
        self.http_client = http_client

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, self.json['nickname'])

    def file_like(self, obj):
        """Try to decide if we should put this object in multipart."""

        primitives = (str, Real)
        return not isinstance(obj, primitives)

    def __call__(self, **kwargs):
        """Invoke ARI operation.

        :param kwargs: ARI operation arguments.
        :return: Implementation specific response or WebSocket connection
        """
        log.info("%s?%r" % (self.json['nickname'], urllib.parse.urlencode(kwargs)))
        # http method must be native string (for Python 2.x, bytes). This must be done to prevent errors when trying to
        # upload binary data because when unicode is passed, the concatenated request string gets decoded using the
        # default encoding (ASCII) and that breaks on binary data. See the bottom of this thread:
        # https://github.com/kennethreitz/requests/issues/1252
        method = str(self.json['method'])
        uri = self.uri
        params = {}
        data = {}
        headers = {}
        files = {}
        proxies = kwargs.pop('proxies')
        # allow passing custom headers
        if kwargs.get('headers'):
            try:
                headers.update(kwargs.pop('headers'))
            except ValueError:
                raise AssertionError("Parameter headers must be of type dict.")
        # allow passing a custom query dict
        if kwargs.get('query'):
            try:
                params.update(kwargs.pop('query'))
            except ValueError:
                raise AssertionError("Parameter query must be of type dict.")
        accepts_multipart = ('multipart/form-data' in
                             self.json.get('consumes', []))
        # allow passing an `x-nonce`
        if kwargs.get('nonce'):
            nonce = kwargs.get('nonce')
            params['x-nonce'] = nonce
            del kwargs['nonce']

        for param in self.json.get('parameters', []):
            pname = param['name']
            ptype = param['type']
            value = kwargs.get(pname)
            if ptype == 'dict':
                if value and param['paramType'] == 'query':
                    try:
                        params.update(value)
                    except ValueError:
                        raise AssertionError("Parameter {} must be of type dict.".format(pname))
            # Turn list params into comma separated values
            if isinstance(value, list):
                value = ",".join(value)
            if value is not None:
                param_type = param['paramType']
                if param_type == 'path':
                    uri = uri.replace('{%s}' % pname, str(value))
                elif param_type == 'query':
                    params[pname] = value
                elif param_type == 'form':
                    if accepts_multipart and self.file_like(value):
                        # AD-1345 : issue uploading large files (see ticket).
                        try:
                            file_name = os.path.basename(value.name)
                        except AttributeError:
                            raise TypeError("File upload object must have a name attribute.")
                        m = MultipartEncoder(fields = {pname: (file_name, value, 'text/plain')})
                        headers['Content-type'] = m.content_type
                        data = m
                    else:
                        data[pname] = value
                elif param_type == 'body':
                    isjson = True
                    if isinstance(value, str):
                        data = value
                    else:
                        try:
                            data = json.dumps(value)
                        except TypeError:
                            data = value
                            if not headers.get('Content-type') \
                                or headers.get('Content-type') == 'application/octet-stream':
                                isjson = False
                                headers['Content-type'] = 'application/octet-stream'
                    if isjson:
                        headers['Content-type'] = 'application/json'
                else:
                    raise AssertionError(
                        "Unsupported paramType %s" %
                        param_type)
                del kwargs[pname]
            else:
                if param['required']:
                    raise TypeError(
                        "Missing required parameter '%s' for '%s'" %
                        (pname, self.json['nickname']))
        if method.lower() == 'get':
            # look for the search dictionary on GET requests:
            value = kwargs.get('search')
            if value:
                if not isinstance(value, dict):
                    raise TypeError("search parameter must be of type dict")
                for k, v in list(value.items()):
                    params[k] = v
                kwargs.pop('search')
            value = kwargs.get('filter')
            if value:
                if not isinstance(value, str):
                    raise TypeError("filter parameter must be of type str")
                params['filter'] = value
                kwargs.pop('filter')

        if kwargs:
            raise TypeError("'%s' does not have parameters %r" %
                            (self.json['nickname'], list(kwargs.keys())))

        log.info("%s %s(%r)", method, uri, params)
        if self.json['is_websocket']:
            # Fix up http: URLs
            uri = re.sub('^http', "ws", uri)
            return self.http_client.ws_connect(uri, params=params)
        else:
            return self.http_client.request(
                method, uri, params=params,
                data=data, headers=headers, files=files, proxies=proxies)


class Resource(object):
    """Swagger resource, described in an API declaration.

    :param resource: Resource model
    :param http_client: HTTP client API
    """

    def __init__(self, resource, http_client):
        log.debug("Building resource '%s'" % resource['name'])
        self.json = resource
        decl = resource['api_declaration']
        self.http_client = http_client
        self.operations = {
            oper['nickname']: self._build_operation(decl, api, oper)
            for api in decl['apis']
            for oper in api['operations']}

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, self.json['name'])

    def __getattr__(self, item):
        """Promote operations to be object fields.

        :param item: Name of the attribute to get.
        :rtype: Resource
        :return: Resource object.
        """
        op = self.get_operation(item)
        if not op:
            raise AttributeError("Resource '%s' has no operation '%s'" %
                                 (self.get_name(), item))
        return op

    def get_operation(self, name):
        """Gets the operation with the given nickname.

        :param name: Nickname of the operation.
        :rtype:  Operation
        :return: Operation, or None if not found.
        """
        return self.operations.get(name)

    def get_name(self):
        """Returns the name of this resource.

        Name is derived from the filename of the API declaration.

        :return: Resource name.
        """
        return self.json.get('name')

    def _build_operation(self, decl, api, operation):
        """Build an operation object

        :param decl: API declaration.
        :param api: API entry.
        :param operation: Operation.
        """
        log.debug("Building operation %s.%s" % (
            self.get_name(), operation['nickname']))
        uri = decl['basePath'] + api['path']
        return Operation(uri, operation, self.http_client)


class SwaggerClient(object):
    """Client object for accessing a Swagger-documented RESTful service.

    :param url_or_resource: Either the parsed resource listing+API decls, or
                            its URL.
    :type url_or_resource: dict or str
    :param http_client: HTTP client API
    :type  http_client: HttpClient
    """

    def __init__(self, url_or_resource,
                 http_client=None, extra_processors=None):
        if not http_client:
            http_client = SynchronousHttpClient()
        self.http_client = http_client

        processors = [WebsocketProcessor(), ClientProcessor()]
        if extra_processors is not None:
            processors.extend(extra_processors)
        loader = swaggerpy.Loader(http_client, processors)

        if isinstance(url_or_resource, str):
            log.debug("Loading from %s" % url_or_resource)
            self.api_docs = loader.load_resource_listing(url_or_resource)
        else:
            log.debug("Loading from %s" % url_or_resource.get('basePath'))
            self.api_docs = url_or_resource
            loader.process_resource_listing(self.api_docs)

        self.resources = {
            resource['name']: Resource(resource, http_client)
            for resource in self.api_docs['apis']}

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, self.api_docs['basePath'])

    def __getattr__(self, item):
        """Promote resource objects to be client fields.

        :param item: Name of the attribute to get.
        :return: Resource object.
        """
        resource = self.get_resource(item)
        if not resource:
            raise AttributeError("API has no resource '%s'" % item)
        return resource

    def close(self):
        """Close the SwaggerClient, and underlying resources.
        """
        self.http_client.close()

    def get_resource(self, name):
        """Gets a Swagger resource by name.

        :param name: Name of the resource to get
        :rtype: Resource
        :return: Resource, or None if not found.
        """
        return self.resources.get(name)
