import collections.abc
import json
import numbers
import os.path
import urllib.parse

import requests


class Agave(object):

    def __init__(self, base, token, swagger):
        self.base = base
        self.token = token
        self.swagger = Swagger(swagger)

    def __getattr__(self, endpoint):
        return Endpoint(endpoint, agave=self)


class Endpoint(object):

    def __init__(self, endpoint, agave):
        self.endpoint = endpoint
        self.agave = agave

    def __getattr__(self, attr):
        return Operation(attr, endpoint=self)


class Operation(object):

    def __init__(self, nickname, endpoint):
        self.nickname = nickname
        self.endpoint = endpoint
        self.swagger = self.endpoint.agave.swagger
        self.operation = self.swagger.get_nickname(self.nickname,
                                                   self.endpoint.endpoint)
        self.token = self.endpoint.agave.token
        self.bearer = {'Authorization': 'Bearer {}'.format(self.token)}

    def __call__(self, *args, **kwargs):
        operation = self.operation['operation']
        method = operation['method']
        path = self.operation['path']
        url = urllib.parse.urljoin(self.endpoint.agave.base, path)
        parameters = operation['parameters']

        params = {}             # query parameters
        data_form = {}          # form parameters
        data_body = {}          # body parameter
        paths = {}              # path parameters
        for parameter in parameters:
            name = parameter['name']
            param_type = parameter['paramType']
            try:
                param = kwargs.pop(name)
            except KeyError:
                try:
                    param = parameter['defaultValue']
                except KeyError:
                    if parameter['required']:
                        raise Exception('parameter required: {}'.format(name))
                    continue
            param = serialize(param)
            if param_type == 'query':
                params[name] = param
            if param_type == 'form':
                data_form[name] = param
            if param_type == 'body':
                data_body = param if isinstance(param, str) else str(param)
            if param_type == 'path':
                paths[name] = param
        if kwargs:
            raise Exception('unknown parameters: {}'
                            .format(list(kwargs.keys())))
        req = self.build_request(method, url, paths,
                                 data_form, data_body, params)
        if req.ok:
            response_model = self.swagger.get_model(
                self.operation['operation']['type'], self.endpoint.endpoint)
            return_type = response_model['properties']['result']
            return self.deserialize(req.json()['result'],
                                    return_type=return_type)
        else:
            raise Exception(req.text)

    def build_request(self, method, url, paths, data_form, data_body, params):
        data = data_form or data_body
        url = url.format(**paths)
        meth = getattr(requests, method.lower())
        return meth(url, data=data, params=params, headers=self.bearer)

    def deserialize(self, dic, return_type):
        """dict -> Model"""

        if return_type['type'] == 'array':
            items = return_type['items']
            items_type = items.get('type', items.get('$ref'))
            return [self.deserialize(elem, {'type': items_type})
                    for elem in dic]
        if return_type['type'] == 'string':
            assert isinstance(dic, str) or dic is None
            return dic
        if return_type['type'] == 'integer':
            assert isinstance(dic, numbers.Number)
            return dic
        if return_type['type'] == 'boolean':
            assert isinstance(dic, bool)
            return dic
        else:
            try:
                del dic['_links']
            except KeyError:
                pass
            model_spec = self.swagger.get_model(
                return_type['type'], self.endpoint.endpoint)['properties']
            deserialized_dic = {k: self.deserialize(dic[k], model_spec[k])
                                for k in dic}
            return ModelGenerator(model_spec)(**deserialized_dic)


def serialize(obj):
    """Model -> dict"""

    if isinstance(obj, Model):
        return {k: serialize(v)
                for k, v in obj.__dict__.items() if not k.startswith('_')}
    if isinstance(obj, str):
        return obj
    if isinstance(obj, collections.abc.Sequence):
        return [serialize(v) for v in obj]
    return obj


class Swagger(object):

    def __init__(self, url):
        self.url = url
        self.parsed_url = urllib.parse.urlparse(url)
        self.get = (self.file_get if self.parsed_url.scheme == 'file'
                    else self.requests_get)
        index = self.get('index.html')
        self.apis = {}
        for api in index['apis']:
            path = api['path']
            name = os.path.basename(path)
            self.apis[name] = self.get(name)
        self.generate_models()

    def file_get(self, path):
        f = open(os.path.join(self.parsed_url.path, path))
        return json.load(f)

    def requests_get(self, path):
        resp = requests.get(urllib.parse.urljoin(self.url, path))
        if resp.ok:
            return resp.json()

    def get_nickname(self, nickname, endpoint):
        apis = self.apis[endpoint]['apis']
        for api in apis:
            url_path = api['path']
            for operation in api['operations']:
                if operation['nickname'] == nickname:
                    return {'path': url_path,
                            'operation': operation}
        raise Exception('nickname "{}" not found'.format(nickname))

    def get_parameter(self, name, nickname, endpoint):
        parameters = self.get_nickname(
            nickname, endpoint)['operation']['parameters']
        for parameter in parameters:
            if parameter['name'] == name:
                return parameter
        raise Exception('parameter "{}" not found'.format(name))

    def generate_models(self):
        for endpoint in self.apis:
            self.generate_model(endpoint)

    def generate_model(self, endpoint):
        models = self.apis[endpoint]['models']
        global_dict = globals()
        for model_name, spec in models.items():
            global_dict[model_name] = ModelGenerator(spec['properties'])

    def get_model(self, name, endpoint):
        return self.apis[endpoint]['models'][name]


class Model(object):
    pass


class ModelGenerator(object):

    def __init__(self, spec):
        self._spec = spec

    def __call__(self, *args, **kwargs):
        model = Model()
        model._spec = self._spec
        for key, param_spec in self._spec.items():
            try:
                param = kwargs.pop(key)
            except KeyError:
                if param_spec.get('required', False):
                    raise
                continue
            self._check(param, param_spec)
            setattr(model, key, param)
        if kwargs:
            raise Exception('unknown parameter(s): {}'
                            .format(list(kwargs.keys())))
        return model

    def _check(self, param, param_spec):
        """Check that `param` satisfies the spec `param_spec`."""

        param_type = param_spec['type']
        if param_type == 'string' and 'enum' in param_spec:
            assert param in param_spec['enum']
        elif param_type == 'string':
            assert isinstance(param, str) or param is None
        elif param_type == 'boolean':
            assert isinstance(param, bool)
        elif param_type in ('integer', 'number'):
            assert isinstance(param, numbers.Number)
        elif param_type == 'array':
            assert isinstance(param, collections.abc.Sequence)
        else:
            raise Exception('wrong parameter type: {}'.format(param))
