"""
Module to facilitate writing actor containers for the abaco platform. See https://github.com/TACC/abaco

"""

import ast
from concurrent.futures import TimeoutError
import cloudpickle
import getpass
import os
import socket
import time

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


def is_tapis_notebook():
    """
    Determine whether this code is running from within a Tapis notebook. This can be used for automatically
    determining the image to use for the asynchronous executor.
    """
    # are we running as the jupyter user
    if not getpass.getuser() == 'jupyter':
        return False
    # do we have a MyData:
    try:
        os.listdir('/home/jupyter/MyData')
    except:
        try:
            os.listdir('/home/jupyter/mydata')
        except:
            return False
    return True


def get_tapis_abaco_image(base_url):
    """
    Determine the docker image name for a tapis notebook associated with a base_url.
    """
    # designsafe tenant:
    if 'agave.designsafe-ci.org' in base_url:
        return 'taccsciapps/jupyteruser-ds-abaco:1.2.14'
    return None


class AbacoExecutor(object):
    """Executor class that leverages an Abaco actor for executions"""
    def __init__(
            self,
            # the agave oauth client to use to connect to the abaco instance
            ag,
            # use an existing actor; it must have been defined with an allowable image.
            actor_id=None,
            # specify an image to use for the abaco actor. it must be able to accept a message that contains a
            # callable and parameters and execute the callable.
            image=None,
            # if not specifying an image, one of a pre-defined set of strings that determines the image to use for the actor
            context=None,
            # the number of abaco workers to use for the actor
            num_workers=1,
            # timeout (in seconds) to wait for actor to be READY; for very large images, may need to increase this
            # to allow for longer download times on the abaco side.
            timeout=60):
        self.ag = ag
        self.timeout = timeout
        if actor_id:
            # make sure it exists:
            rsp = ag.actors.get(actorId=actor_id)
            self.actor_id = actor_id
            self.status = rsp.get('status')
            self.image = rsp.get('image')
        else:
            # first, determine the image that should be used:
            if not image:
                # if no image provided, check to see if we are running from within a Tapis jupyter notebook:
                if is_tapis_notebook():
                    image = get_tapis_abaco_image(ag.api_server)

            # next, check if a user already has an agpy_abaco_executor for the correct image:
            actors = ag.actors.list()
            for a in actors:
                if a.get('name') == 'agpy_abaco_executor':
                    # check fot the image:
                    if not image or image == a.get('image'):
                        self.actor_id = a.get('id')
            if not self.actor_id:
                # this is a new actor:
                self.image = None
                if image:
                    self.image = image
                elif context and hasattr(context, 'lower'):
                    # basic py3 image:
                    if context.lower() == 'py3':
                        self.image = 'abacosamples/py3_func:dev'
                    # docker image with many scientific libraries pre-installed
                    elif context.lower() == 'py3-scipy':
                        self.image = 'abacosamples/py3_sci_base_func'
                    # docker image used for the sd2e jupyter hub
                    elif context.lower() == 'sd2e-jupyter':
                        self.image = 'sd2e/jupyteruser_func'
                    # add support for other contexts as needed...
                # provide a sensible default image
                if not self.image:
                    self.image = 'abacosamples/py3_func:dev'
                # register an Abaco actor with the appropriate image:
                try:
                    rsp = ag.actors.add(
                        body={
                            'image': self.image,
                            'stateless': True,
                            'name': 'agpy_abaco_executor'
                        })
                except Exception as e:
                    raise AgaveError(
                        "Unable to register the actor; exception: {}".format(
                            e))
                self.actor_id = rsp['id']
                self.status = 'SUBMITTED'

                self.wait_until_ready()
        self.num_workers = num_workers
        if self.num_workers <= 1:
            return
        # register the workers:
        try:
            ag.actors.addWorker(actorId=self.actor_id,
                                body={'num': self.num_workers})
        except TypeError:
            # this is an issue in agavepy; swallow these for now until it is fixed
            pass
        except Exception as e:
            raise AgaveError(
                "Unable to add workers for actor. Exceptoion: {}".format(e))

    def _update_status(self):
        status = self.ag.actors.get(actorId=self.actor_id).get('status')
        self.status = status
        return status

    def _is_ready(self):
        return self.status == 'READY'

    def wait_until_ready(self, timeout=None):
        now = time.time()
        if timeout:
            future = now + timeout
        else:
            future = float("inf")
        while not self._is_ready() and time.time() < future:
            self._update_status()
            time.sleep(2)

    def submit(self, fn, *args, **kwargs):
        """Schedule the callable fn to run as fn(*args, **kwargs) and returns a
        AbacoAsyncReponse Future object representing the execution of the callable."""

        if not args:
            args = []
        if not kwargs:
            kwargs = {}
        message = cloudpickle.dumps({
            'func': fn,
            'args': args,
            'kwargs': kwargs
        })
        headers = {'Content-Type': 'application/octet-stream'}
        rsp = self.ag.actors.sendBinaryMessage(actorId=self.actor_id,
                                               message=message,
                                               headers=headers)
        execution_id = rsp.get('executionId')
        if not execution_id:
            raise AgaveError(
                "Error submitting function call. Did not get an execution id; response: {}"
                .format(rsp))
        return AbacoAsyncResponse(
            self.ag,
            self.actor_id,
            execution_id,
        )

    def map(self, fn, args_list=[], kwargs_list=None):
        """
        Map a function, fn, over input data args_list and kwargs_list. If kwargs_list is provided,
        it must have the same length as args list.
        """
        if not kwargs_list:
            kwargs_list = [{} for i in args_list]
        if not len(args_list) == len(kwargs_list):
            raise AgaveError("map requires lists of equal length")
        return [
            self.submit(fn, *args, **kwargs)
            for args, kwargs in zip(args_list, kwargs_list)
        ]

    def delete(self):
        """ Delete this executor completely."""
        self.ag.actors.delete(actorId=self.actor_id)

    def blocking_call(self, fn, *args, **kwargs):
        """Execute fn(*args, **kwargs) and block until the result completes. """
        arsp = self.submit(fn, *args, **kwargs)
        return arsp.result()


# max time, in seconds, to sleep between status check calls for an execution
MAX_SLEEP = 60


def exp_backoff(prev, count):
    # exponentially increase the sleep amount via the equation 2^(0.2*prev) every 10th time:
    next = prev
    if (count % 10) == 0:
        next = 2.0**(prev * 0.2)
    if next > MAX_SLEEP:
        return MAX_SLEEP
    return next


class AbacoAsyncResponse(object):
    """
    Future class encapsulating an asynchronous execution performed via an Abaco actor.
    """
    def __init__(self, ag, actor_id, execution_id):
        self.ag = ag
        self.actor_id = actor_id
        self.execution_id = execution_id
        self.status = 'SUBMITTED'

    def _update_status(self):
        status = self.ag.actors.getExecution(
            actorId=self.actor_id, executionId=self.execution_id).get('status')
        self.status = status
        return status

    def _is_done(self):
        return self.status == 'COMPLETE'

    def done(self):
        """Return True if the call was successfully cancelled or finished running."""
        self._update_status()
        return self._is_done()

    def running(self):
        self._update_status()
        return not self._is_done()

    def result(self, timeout=None):
        """
        :param timeout: int,
        :return:
        """
        now = time.time()
        sleep = 0.5
        count = 0
        if timeout:
            future = now + timeout
        else:
            future = float("inf")
        while not self._is_done() and time.time() < future:
            self._update_status()
            count += 1
            time.sleep(exp_backoff(sleep, count))
        if time.time() > future and not self._is_done():
            raise TimeoutError()
        # result should be ready:
        results = []
        while True:
            result = self.ag.actors.getOneExecutionResult(
                actorId=self.actor_id, executionId=self.execution_id).content
            if not result:
                break
            results.append(cloudpickle.loads(result))
        return results
