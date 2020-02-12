from __future__ import absolute_import
import dateutil.parser
import logging
import os
import requests
import sys

from agavepy import settings
from agavepy.aloe import EXCEPTION_MODELS
from agavepy.errors import AgaveException, AgaveError
from agavepy.util import AttrDict, with_refresh

sys.path.insert(0, os.path.dirname(__file__))  # noqa
from .swaggerpy.processors import SwaggerProcessor  # noqa
from .swaggerpy.http_client import SynchronousHttpClient  # noqa
from .swaggerpy.client import SwaggerClient  # noqa

HERE = os.path.dirname(os.path.abspath(__file__))
logger = logging.getLogger(__name__)
logging.getLogger(__name__).setLevel(
    os.environ.get('TAPISPY_LOG_LEVEL', logging.WARNING))

__all__ = [
    'AgaveProcessor', 'Operation', 'Resource', 'SwaggerProcessor',
    'SynchronousHttpClient', 'SwaggerClient'
]


class Resource(object):
    def __init__(self, resource, client):
        """

        :param resource:
        :param client: the Agave instance associated with this resource
        :return:
        """
        self.resource = resource
        self.client = client

    def __getattr__(self, attr):
        return Operation(self.resource, attr, client=self.client)

    def __dir__(self):
        if hasattr(self, "clients_resource") and hasattr(
                self.clients_resource, "resources"):
            clients = self.client.clients_resource.resources
            base = list(clients[self.resource].operations.keys())
        else:
            base = []
        if self.client.all is not None:
            base.extend(
                list(self.client.all.resources[
                    self.resource].operations.keys()))
        return base


class Operation(object):

    PRIMITIVE_TYPES = ["array", "string", "integer", "int", "boolean", "dict"]

    def __init__(self, resource, operation, client):
        self.resource = resource
        self.operation = operation
        self.client = client
        self.models = self.get_models()
        self.return_type = self.get_return_type()

    def get_base(self):
        """Get the base ari for this resource."""

        return (self.client.clients_resource
                if self.resource == "clients" else self.client.all)

    def get_operation(self):
        base = self.get_base()
        return getattr(getattr(base, self.resource), self.operation)

    def get_models(self):
        """Get JSON with all the models declarations."""

        base = self.get_base()
        return getattr(base, self.resource).json["api_declaration"]["models"]

    def get_return_type(self):
        """Get JSON with the return type for this operation."""

        return self.get_operation().json

    def __call__(self, *args, **kwargs):
        def operation():
            f = self.get_operation()
            response = f(*args, **kwargs)
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError as h:
                if settings.VERBOSE_ERRORS:
                    # Extract the API JSON message and attach it
                    # to the HTTPError object before raising it
                    code = h.response.status_code
                    reason = h.response.reason + ' for ' + h.response.url
                    try:
                        message = h.response.json().get('message')
                    except Exception:
                        message = h.response.text
                    raise requests.exceptions.HTTPError(code,
                                                        reason,
                                                        message,
                                                        response=h.response,
                                                        request=h.request)
                else:
                    raise h
            return response

        kwargs["proxies"] = self.client.proxies
        logger.debug('Operation.__call__()...')
        resp = with_refresh(self.client, operation)
        if resp.ok:
            # if response is 204 (no content) return none directly
            if resp.status_code == 204 and not resp.content:
                return resp
            # if response is raw file, return it directly
            if self.resource == "files" and (
                    self.operation == "download"
                    or self.operation == "downloadFromDefaultSystem"):
                return resp
            # if response is a result, return it directly as well:
            if self.resource == "actors" and self.operation == "getOneExecutionResult":
                return resp
            # get the version associated with this response; the version is used for post_processing, as
            # some response models depend on the version.
            try:
                version = resp.json().get("version")
            except Exception:
                version = None
            processed = self.post_process(resp.json(), self.return_type,
                                          version)
            result = processed["result"] if "result" in processed else None
            # if operation is clients.create, save name
            if self.resource == "clients" and self.operation == "create":
                self.client.set_client(result["consumerKey"],
                                       result["consumerSecret"])
            return result
        else:
            # if the response is not 2xx return the unprocessed json rather
            # than raising an exception, since the return json contains
            # the error message
            raise AgaveException(resp.json())

    def post_process(self, obj, return_type, version):
        if return_type is None:
            return self.process_untyped(obj)

        type_name = return_type["type"].lower()
        if type_name in self.PRIMITIVE_TYPES:
            f = getattr(self, "process_{}".format(type_name))
            try:
                return f(obj, return_type, version)
            except Exception:
                return self.process_untyped(obj)
        return self.process_model(obj, return_type, version)

    def process_untyped(self, obj, version=None):
        return obj

    def process_dict(self, obj, return_type, version=None):
        return obj

    def process_array(self, obj, return_type, version):
        items = return_type["items"]
        items_type = items.get("type", items.get("$ref"))
        return [
            self.post_process(elem, {"type": items_type}, version)
            for elem in obj
        ]

    def process_string(self, obj, return_type, version=None):
        if obj is None:
            # why is agave returning null for a string type?
            return obj
        if return_type.get("format") == "date-time":
            return dateutil.parser.parse(obj)
        return obj

    def process_integer(self, obj, return_type, version=None):
        return obj

    process_int = process_integer

    def process_boolean(self, obj, return_type, version=None):
        return obj

    def get_model_spec(self, model_name, version):
        """
        Look up the model_spec associated with a model name and check for exceptions based on the version of
         the response.
        :param model_name:
        :return:
        """
        if model_name in EXCEPTION_MODELS:
            version_cutoff = EXCEPTION_MODELS[model_name]["version_cutoff"]
            if version > version_cutoff:
                # the API version of this response was greater than the version cutoff, so we need to look up the
                # the model spec in the exception_resources
                new_model_name = EXCEPTION_MODELS[model_name]["model"]
                return self.client.resource_exceptions[new_model_name][
                    "properties"]
        # if model was not an exception model OR the version was less than the version cutoff, just return the
        # the model in the original models object -
        return self.models[model_name]["properties"]

    def process_model(self, obj, return_type, version):
        model_name = return_type["type"]

        model_spec = self.get_model_spec(model_name, version)
        result = AttrDict({})
        for k in obj:
            try:
                result[k] = self.post_process(obj[k], model_spec.get(k),
                                              version)
            except Exception:
                result[k] = obj
        return result


class AgaveProcessor(SwaggerProcessor):
    def process_property(self, resources, resource, model, prop, context):
        if prop.get("format", None) == "date-time":
            pass

    def process_model(self, resources, resource, model, context):
        pass
