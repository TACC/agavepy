import collections.abc
import json
import numbers
import os.path
import urllib.parse

import requests


class Agave(object):

    def __init__(self, base, swagger):
        self.base = base
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

    def __call__(self, *args, **kwargs):
        operation = self.operation['operation']
        method = operation['method']
        path = self.operation['path']
        url = urllib.parse.urljoin(self.endpoint.agave.base, path)
        parameters = operation['parameters']
        for parameter in parameters:
            print('processing', parameter)
            try:
                param = kwargs.pop(parameter['name'])
            except KeyError:
                try:
                    param = parameter['defaultValue']
                except KeyError:
                    if parameter['required']:
                        raise Exception('parameter required: {}'.format(parameter['name']))
                    continue
            print('param', param)

        if kwargs:
            raise Exception('unknown parameters: {}'.format(list(kwargs.keys())))
        req = requests.Request(method, url)


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
        raise Exception('nickname "{}" not found'.format(nickame))

    def get_parameter(self, name, nickname, endpoint):
        parameters = self.get_nickname(
            nickname, endpoint)['operation']['parameters']
        for parameter in parameters:
            if parameter['name'] == name:
                return parameter
        raise Exception('parameter "{}" not found'.format(name))

    def generate_models(self, endpoint):
        models = self.apis[endpoint]['models']
        global_dict = globals()
        for model_name, model in models.items():
            global_dict[model_name] = Model(model)


class Model(object):

    def __init__(self, spec):
        self.spec = spec

    def __call__(self, *args, **kwargs):
        class _model(object):
            pass
        model = _model()
        for key, param_spec in self.spec['properties'].items():
            try:
                param = kwargs.pop(key)
            except KeyError:
                if param_spec.get('required', False):
                    raise
                continue
            self.check(param, param_spec)
            setattr(model, key, param)
        if kwargs:
            raise Exception('unknown parameter(s): {}'.format(list(kwargs.keys())))
        return model

    def check(self, param, param_spec):
        """Check that `param` satisfies the spec `param_spec`."""

        param_type = param_spec['type']
        if param_type == 'string' and 'enum' in param_spec:
            assert param in param_spec['enum']
        elif param_type == 'string':
            assert isinstance(param, str)
        elif param_type == 'boolean':
            assert isinstance(param, bool)
        elif param_type in ('integer', 'number'):
            assert isinstance(param, numbers.Number)
        elif param_type == 'array':
            assert isinstance(param, collections.abc.Sequence)
        else:
            raise Exception('wrong parameter type: {}'.format(param))
