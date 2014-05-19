import json
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
        print(args, kwargs)
        print(self.operation)
    

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