"""
Module to facilitate writing actor containers for the abaco platform. See https://github.com/TACC/abaco

"""

import ast
import os

from agave import Agave, AttrDict


def get_client():
    """Returns a pre-authenticated Agave client using the abaco environment variables."""
    ag = Agave(api_server=os.environ.get('_abaco_api_server'),
               token=os.environ.get('_abaco_access_token'))
    return ag


def get_context():
    """Returns a context dictionary with message and metadata about the message."""
    context = AttrDict({
        'raw_message': os.environ.get('MSG'),
        'content_type': os.environ.get('_abaco_Content-Type'),
        'execution_id': os.environ.get('_abaco_execution_id'),
        'username': os.environ.get('_abaco_username')
    })
    try:
        context['message_dict'] = ast.literal_eval(context['raw_message'])
    except ValueError:
        context['message_dict'] = None
    context.update(os.environ)
    context.update(os.environ)
    return context
