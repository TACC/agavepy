"""
Module to facilitate writing actor containers for the abaco platform. See https://github.com/TACC/abaco

"""

import ast
import cloudpickle
import os
import requests
import socket

from .agave import Agave, AgaveError, AttrDict


def get_client():
    """Returns a pre-authenticated Agave client using the abaco environment variables."""
    # if we have an access token, use that:
    if os.environ.get('_abaco_access_token'):
        ag = Agave(api_server=os.environ.get('_abaco_api_server'),
                   token=os.environ.get('_abaco_access_token'))
    elif os.environ.get('_abaco_api_server'):
        # otherwise, create a client with a fake JWT. this will only work in testing scenarios.
        ag = Agave(api_server=os.environ.get('_abaco_api_server'),
                   jwt='123',
                   jwt_header_name='X-JWT-Assertion-dev_sandbox')
    else:
        # try to use ~/.agave/current to support purely local testing
        try:
            ag = Agave.restore()
        except Exception as e:
            raise AgaveError(
                "Unable to instantiate an Agave client: {}".format(e))

    return ag


def get_context():
    """
    Returns a context dictionary with message and metadata about the message
    """
    context = AttrDict({
        'raw_message': os.environ.get('MSG'),
        'content_type': os.environ.get('_abaco_Content-Type'),
        'execution_id': os.environ.get('_abaco_execution_id'),
        'username': os.environ.get('_abaco_username'),
        'state': os.environ.get('_abaco_actor_state'),
        'actor_dbid': os.environ.get('_abaco_actor_dbid'),
        'actor_id': os.environ.get('_abaco_actor_id'),
        'raw_message_parse_log': ''
    })

    # Set up message_dict and error log preemptively
    # message_dict is actually an AttrDict so users can use
    # dot notation when programming against it
    context['message_dict'] = AttrDict()
    context['raw_message_parse_log'] = ''
    try:
        temp_dict = ast.literal_eval(context['raw_message'])
        if isinstance(temp_dict, dict):
            context['message_dict'] = AttrDict(temp_dict)
    except Exception as e:
        context['raw_message_parse_log'] = \
            "Error parsing message: {}".format(e)
        pass

    context.update(os.environ)
    return context

def get_binary_message():
    """Read the full binary message sent via the abaco named pipe."""
    fd = os.open('/_abaco_binary_data', os.O_RDONLY | os.O_NONBLOCK)
    msg = b''
    while True:
        frame = _read_bytes(fd)
        if frame:
            msg += frame
        else:
            return msg

def _read_bytes(fifo, n=4069):
    """Read at most n bytes from a pipe at path `fifo`."""
    try:
        return os.read(fifo, n)
    except OSError:
        # an empty fifo will return a Resource temporarily unavailable OSError (Errno 11)
        # since we explicitly support a single message protocol, this means we are done
        return None

def update_state(state):
    """Update the actor's state with the new value of `state`. The `state` variable should be JSON serializable."""
    ag = get_client()
    actor_id = get_context()['actor_id']
    ag.actors.updateState(actorId=actor_id, body=state)


def send_python_result(obj):
    """
    Send an arbitrary python object, `obj` 
    :param obj: a python object to return as a result.
    :return: 
    """
    try:
        b = cloudpickle.dumps(obj)
    except Exception as e:
        msg = "Could not serialize {}; got exception: {}".format(obj, e)
        print(msg)
        raise AgaveError(msg)
    send_bytes_result(b)

def send_bytes_result(b):
    """
    Send a result `b` which should be a bytes object to the Abaco system.
    `b` must be shorter than MAX_RESULT_LENGTH configured for the Abaco instance
    or else 
    """
    if not isinstance(b, bytes):
        msg = "send_bytes_result did not receive bytes, got: {}".format(b)
        print(msg)
        raise AgaveError(msg)
    sock = _get_results_socket()
    try:
        sock.send(b)
    except Exception as e:
        msg = "Got exception sending bytes over results socket: {}".format(e)
        print(msg)
        raise AgaveError(msg)

def _get_results_socket():
    """Instantiate the results socket for sending binary results."""
    client = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    sock = '/_abaco_results.sock'
    try:
        client.connect(sock)
    except (FileNotFoundError, ConnectionError) as e:
        msg = "Exception connecting to results socket: {}".format(e)
        print(msg)
        raise AgaveError(msg)
    return client
