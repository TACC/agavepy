=======
AgavePy
=======

A simple Python binding for the `Agave API`_.


Installation
============

Install from PyPI_::

    pip install agavepy


Using agavepy in Docker
========================

This repository includes a ``Dockerfile`` and a ``docker-compose.yml``
file, which allows a zero installation version of ``agavepy``.

The only requirement is Docker_ and `docker-compose`_, most likely
already installed in your system.

Then, clone this repository and execute ``docker-compose`` as follows:

.. code-block:: bash

   $ git clone https://github.com/TACC/agavepy.git
   $ cd agavepy
   $ docker-compose build
   $ docker-compose up

(a bug in ``docker-compose`` is preventing to run just ``up``. The steps ``build`` and ``up`` have to be done separately.)
Navigate to http://localhost:9999 and access the Jupyter_ notebook
with password ``agavepy``.  The notebook ``Example.ipynb`` contains a
full example of use.


Quickstart
==========

The first step is to create an ``agave`` Python object pointing to
your tenant:

.. code-block:: pycon

   >>> from agavepy.agave import Agave
   >>> my_agave = Agave(api_server='https://agave.iplantc.org',
   ...                  username='myusername', password='mypassword')

Once the object is instantiated, interact with it according to the
methods in the API documentation.

For example, create a new client with:

.. code-block:: pycon

   >>> my_agave.clients.create(body={'clientName': 'my_client'})

Access any endpoint with:

.. code-block:: pycon

   >>> my_agave.systems.list()
   >>> my_agave.jobs.manage(...)

Once a client is created, it is used by default to access the API.

To make use of an existing client, pass the client's credentials into the Agave constructor:

.. code-block:: pycon

   >>> from agavepy.agave import Agave
   >>> my_agave = Agave(api_server='https://agave.iplantc.org',
   ...                  username='myusername', password='mypassword', client_name='my_client', api_key='123', api_secret='abc')

Alternatively, the SDK will attempt to recover the client credentials from the client name if they are stored
in the user's ``.agavepy`` file, in which case just passing the ``client_name`` will suffice:

.. code-block:: pycon

   >>> from agavepy.agave import Agave
   >>> my_agave = Agave(api_server='https://agave.iplantc.org',
   ...                  username='myusername', password='mypassword', client_name='my_client')


You can also generate client from an access and refresh token to avoid needing end user credentials. By passing the access and refresh tokens, the sdk client will be able to automatically refresh tokens as needed.

.. code-block:: pycon

    >>> ag = Agave(token='76fb5ee42b3e9f25a5ba9069be522', refresh_token='e193fc952954a08b7c8b5766b846d74', 
    ...            api_key='pEN_w4cPMqWpuVFfHblHF6KYniMa', api_secret='', 
    ...            api_server='https://dev.tenants.staging.agaveapi.co', client_name='test', verify=False)


Finally, a client can be generated directly from a JWT in order to bypass the API Gateway and enable direct interaction with the Agave services. Note that the ``api_server`` parameter should point directly at the Agave services, and the ``jwt_header_name`` should reflect the tenant you wish to interact with.

.. code-block:: pycon

    >>> ag = Agave(jwt=jwt, jwt_header_name='X-JWT-Assertion-dev_staging',         
    ...            api_server='https://agave-core-staging.tacc.utexas.edu', verify=False)


.. _Agave API: http://agaveapi.co/
.. _PyPI: https://pypi.python.org/pypi




License
=======

Agavepy is licensed under the BSD license.

Swagger.py is copyright of Digium, Inc., and licensed under BSD 3-Clause License.

.. _Docker: https://docs.docker.com/installation/#installation
.. _docker-compose: https://docs.docker.com/compose/install/
.. _Jupyter: http://ipython.org/
