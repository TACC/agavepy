=======
AgavePy
=======

.. image:: https://badge.fury.io/py/agavepy.svg
    :target: http://badge.fury.io/py/agavepy

.. image:: https://travis-ci.org/TACC/agavepy.svg?branch=develop
    :target: https://travis-ci.org/TACC/agavepy

.. image:: https://readthedocs.org/projects/agavepy/badge/?version=latest
    :target: https://readthedocs.org/projects/agavepy/?badge=latest

.. image:: https://img.shields.io/pypi/l/Django.svg
    :target: https://raw.githubusercontent.com/TACC/agavepy/master/LICENSE

**Python2/3 binding for TACC.Cloud Agave and Abaco APIs**

- Documentation: https://agavepy.readthedocs.io/en/latest/
- GitHub: https://github.com/TACC/agavepy
- PyPI: https://pypi.python.org/pypi/agavepy
- Free software: 3-Clause BSD License


Installation
============

Install from PyPI_::

    pip install agavepy


Install from GitHub checkout::

    cd agavepy
    python setup.py install
    # or #
    make install


Contributing
============
In case you want to contribute, you should read our 
`contributing guidelines`_ and we have a contributor's guide
that explains `setting up a development environment and the contribution process`_.

.. _contributing guidelines: CONTRIBUTING.md
.. _setting up a development environment and the contribution process: docs/contributing/


Quickstart
==========

If you already have an active installation of the TACC Cloud CLI, AgavePy will
pick up on your existing credential cache, stored in `$HOME/.agave/current`. 
We illustrate this usage pattern first, as it's **really** straightforward.

TACC Cloud CLI
--------------

.. code-block:: pycon

   >>> from agavepy.agave import Agave
   >>> ag = Agave.restore()

Voila! You have an active, authenticated API client. AgavePy will use a cached
refresh token to keep this session active as long as the code is running. 

Pure Python
-----------

Authentication and authorization to the TACC Cloud APIs uses OAuth2, a 
widely-adopted web standard. Our implementation of Oauth2 is designed to give
you the flexibility you need to script and automate use of TACC Cloud while
keeping your access credentials and digital assets secure. 

This is covered in great detail in our `Developer Documentation`_ but some key
concepts will be highlighted here, interleaved with Python code.

The first step is to create a Python object ``ag`` which will interact with an
Agave tenant.

.. code-block:: pycon

    >>> from agavepy.agave import Agave
    >>> ag = Agave()
    CODE                 NAME                                     URL
    3dem                 3dem Tenant                              https://api.3dem.org/
    agave.prod           Agave Public Tenant                      https://public.agaveapi.co/
    araport.org          Araport                                  https://api.araport.org/
    designsafe           DesignSafe                               https://agave.designsafe-ci.org/
    iplantc.org          CyVerse Science APIs                     https://agave.iplantc.org/
    irec                 iReceptor                                https://irec.tenants.prod.tacc.cloud/
    sd2e                 SD2E Tenant                              https://api.sd2e.org/
    sgci                 Science Gateways Community Institute     https://sgci.tacc.cloud/
    tacc.prod            TACC                                     https://api.tacc.utexas.edu/
    vdjserver.org        VDJ Server                               https://vdj-agave-api.tacc.utexas.edu/
    
    Please specify the ID of a tenant to interact with: araport.org
    >>> ag.api_server
    'https://api.araport.org/'


If you already now what tenant you want to work with, you can instantiate
``Agave`` as follows:

.. code-block:: pycon

   >>> from agavepy.agave import Agave
   >>> ag = Agave(api_server="https://api.tacc.cloud")

or 

.. code-block:: pycon

    >>> from agavepy.agave import Agave
    >>> ag = Agave(tenant_id="tacc.prod")

Once the object is instantiated, interact with it according to the API 
documentation and your specific usage needs. 

Create a new Oauth client
^^^^^^^^^^^^^^^^^^^^^^^^^
In order to interact with Agave, you'll need to first create an Oauth client so
that later on you can create access tokens to do work.

To create a client you can do the following:

.. code-block:: pycon

    >>> from agavepy.agave import Agave
    >>> ag = Agave(api_server='https://api.tacc.cloud')
    >>> ag.clients_create("client-name", "some description")
    API username: your-username
    API password: 
    >>> ag.api_key
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    >>> ag.api_secret
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

You will use the api key and secret to generate Oauth *tokens*, 
which are temporary credentials that you can use in place of putting your real 
credentials into code that is interacting with TACC APIs.

Reuse an existing Oauth client
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once you generate a client, you can re-use its key and secret. Clients can be
created using the Python-based approach illustrated above, via the TACC Cloud
CLI ``clients-create`` command, or by a direct, correctly-structured ``POST``
to the ``clients`` web service. No matter how you've created a client, setting
AgavePy up to use it works the same way:

.. code-block:: pycon

   >>> from agavepy.agave import Agave
   >>> ag = Agave(api_server='https://api.tacc.cloud',
   ...            username='mwvaughn',
   ...            client_name='my_client',
   ...            api_key='kV4XLPhVBAv9RTf7a2QyBHhQAXca',
   ...            api_secret='5EbjEOcyzzIsAAE3vBS7nspVqHQa')

The Agave object ``ag`` is now configured to talk to all TACC Cloud services.



Generate an Access Token
^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to interact with the TACC cloud services in a more secure and
controlled manner - without constantly using your username and password - we
will use the oauth client, created in the previous step, to generate access
tokens.

The generated tokens will by defualt have a lifetime of 4 hours, or 14400
seconds.

To create a token

.. code-block:: pycon

    >>> ag.get_access_token()
    API password:
    >>> ag.token
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

Keep in mind that you will need to create an oauth client first!



Saving your credentials
^^^^^^^^^^^^^^^^^^^^^^^

To save your process (api key, api secret, access token, refresh token, tenant
information) you can use the method ``Agave.save_configs()``

.. code-block:: pycon

    >>> ag.save_configs()

By default, ``Agave.save_configs`` will store credentials in ``~/.agave``. 
It will save all session in ``~/.agave/config.json`` and, for
backwards-compatibility with other agave tooling, it will save the current
session in ``~/.agave/current``.


The refresh token
^^^^^^^^^^^^^^^^^

Nobody likes to change their password, but they have to if it leaks out into 
the wild. A tragically easy way for that to happen is in committed code or a
Docker container where it's been hard-coded. To get around this, AgavePy works
with the TACC authentication APIs to support using a **refresh token**. 
Basically, as long as you have the apikey, apisecret, and the last refresh 
token for an authenticated session, you can renew the session without sending
a password. Neat, right? Let's build on the ``ag`` object from above to learn
about this.

Let's start by inspecting its ``token`` property, which will also demonstrate 
how you can access token data programmatically for your own purposes. 

.. code-block:: pycon

    >>> ag.token.token_info
    {u'access_token': u'14f0bbd0b334e594e676661bf9ccc136', 'created_at': 
     1518136421, u'expires_in': 13283, 'expires_at': 'Thu Feb  8 22:15:04',
     u'token_type': u'bearer', 'expiration': 1518149704, u'scope': u'default',
     u'refresh_token': u'b138c49040a6f67f80d49a1c112e44b'}
    >>> ag.token.token_info['refresh_token']
    u'b138c49046f67f80d49a1c10a12e44b'


.. _Agave: https://agaveapi.co/
.. _Abaco: http://useabaco.cloud/
.. _PyPI: https://pypi.python.org/pypi
.. _Developer Documentation: http://developer.tacc.cloud/
.. _Docker: https://docs.docker.com/installation/#installation
.. _Jupyter: https://jupyter.org/
