"""
Module to facilitate writing actor containers for the abaco platform. See https://github.com/TACC/abaco

"""

import ast
import os
import requests

from .agave import Agave, AttrDict


def get_client():
    """Returns a pre-authenticated Agave client using the abaco environment variables."""
    # if we have an access token, use that:
    if os.environ.get('_abaco_access_token'):
        ag = Agave(api_server=os.environ.get('_abaco_api_server'),
                   token=os.environ.get('_abaco_access_token'))
    else:
        # otherwise, create a client with a fake JWT. this will only work in testing scenarios.
        ag = Agave(api_server=os.environ.get('_abaco_api_server'),
                   jwt='123',
                   jwt_header_name='X-JWT-Assertion-dev_sandbox')

    return ag


def get_context():
    """Returns a context dictionary with message and metadata about the message."""
    context = AttrDict({
        'raw_message': os.environ.get('MSG'),
        'content_type': os.environ.get('_abaco_Content-Type'),
        'execution_id': os.environ.get('_abaco_execution_id'),
        'username': os.environ.get('_abaco_username'),
        'state': os.environ.get('_abaco_actor_state'),
        'actor_dbid': os.environ.get('_abaco_actor_dbid'),
        'actor_id': os.environ.get('_abaco_actor_id'),
    })
    try:
        context['message_dict'] = ast.literal_eval(context['raw_message'])
    except ValueError:
        context['message_dict'] = None
    context.update(os.environ)
    context.update(os.environ)
    return context

def update_state(state):
    """Update the actor's state with the new value of `state`. The `state` variable should be a dictionary."""
    base = os.environ.get('_abaco_api_server')
    token = os.environ.get('_abaco_access_token')
    if 'localhost' in base:
        base = 'http://172.17.0.1:8000'
    url = '{}/actors/{}/state'.format(base,
                                      os.environ.get('_abaco_actor_id'))
    headers = {'Authorization': 'Bearer {}'.format(token)}
    print(("update_state() using URL: {}".format(url)))
    requests.post(url, headers=headers, json={'state':state})