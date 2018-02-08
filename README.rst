=======
AgavePy
=======

.. image:: https://travis-ci.org/TACC/agavepy.svg?branch=reactors
    :target: https://travis-ci.org/TACC/agavepy

Python2/3 binding for TACC.Cloud `Agave`_ and `Abaco`_ APIs.


Installation
============

Install from PyPI_::

    pip install agavepy


Documentation
=============

A combination of hand-curated code examples, tutorials, and auto-generated API
documentation can be found at AgavePy's ReadTheDocs site.

- http://agavepy.readthedocs.io/en/latest/


Quickstart
==========

If you already have an active installation of the TACC Cloud CLI, AgavePy will
pick up on your existing credential cache, stored in `$HOME/.agave/current`. We
illustrate this usage pattern first, as it's **really** straightforward.

TACC Cloud CLI
--------------

.. code-block:: pycon

   >>> from agavepy.agave import Agave
   >>> ag = Agave.restore()

Voila! You have an active, authenticated API client. AgavePy will use a cached
Oauth2 refresh token to keep the session active. 

Pure Python
-----------

Authentication and authorization to the TACC Cloud APIs uses `OAuth2`_, a 
widely-adopted web standard. Our implementation of Oauth2 is designed to give
you the flexibility you need to script and automate use of TACC Cloud while
keeping your access credentials and digital assets secure. 

This is covered in great detail in our `Developer Documentation`_ but some key
concepts will be highlighted here, interleaved with Python code.

The first step is to create a Python object ``ag`` pointing to an API server.
Your project likely has its own API server, which are discoverable using 
the ``tenants-list --rich`` command in the TACC Cloud CLI. For now, we can
assume ``api.tacc.cloud`` (the default value) will work for you. 

.. code-block:: pycon

   >>> from agavepy.agave import Agave
   >>> ag = Agave(api_server='https://api.tacc.cloud')

Once the object is instantiated, interact with it according to the API 
documentation and your specific usage needs. 

Create a new Oauth client
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: pycon

   >>> ag = Agave(api_server='https://api.tacc.cloud',
   ...            username='your_username',
   ...            password='your_password')
   >>> ag.clients.new()
 

Reuse an existing Oauth client
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ceate a new client with:

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


.. _Agave: http://agaveapi.co/
.. _Abaco: http://useabaco.cloud/
.. _PyPI: https://pypi.python.org/pypi
.. _Developer Documentation: http://developer.tacc.cloud/
.. _Jupyter: http://ipython.org/
.. _Docker: https://docs.docker.com/installation/#installation