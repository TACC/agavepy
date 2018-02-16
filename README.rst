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
   ...            username='mwvaughn',
   ...            password='PaZ$w0r6!')
   >>> ag.clients.create(body={'clientName': 'my_client'})
   {u'consumerKey': u'kV4XLPhVBAv9RTf7a2QyBHhQAXca', u'_links': {u'subscriber':
   {u'href': u'https://api.tacc.cloud/profiles/v2/mwvaughn'}, u'self': {u'href':
    u'https://api.tacc.cloud/clients/v2/my_client'}, u'subscriptions': {u'href':
    u'https://api.tacc.cloud/clients/v2/my_client/subscriptions/'}},
    u'description': u'', u'tier': u'Unlimited', u'callbackUrl': u'',
    u'consumerSecret': u'5EbjEOcyzzIsAAE3vBS7nspVqHQa', u'name': u'my_client'}

You use the **consumerKey** and **consumerSecret** to generate Oauth *tokens*, 
which are temporary credentials that you can use in place of putting your real 
credentials into code that is scripting against the TACC APIs.

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
   ...            username='mwvaughn', password='PaZ$w0r6!',
   ...            client_name='my_client',
   ...            api_key='kV4XLPhVBAv9RTf7a2QyBHhQAXca',
   ...            api_secret='5EbjEOcyzzIsAAE3vBS7nspVqHQa')

The Agave object ``ag`` is now configured to talk to all TACC Cloud services.
Here's an example: Let's retrieve a the curent user's **profile**.

.. code-block:: pycon

   >>> ag.profiles.get()
   {u'status': u'', u'username': u'mwvaughn', u'first_name': u'Matthew', 
    u'last_name': u'Vaughn', u'phone': u'867-5309', u'mobile_phone': u'', 
    u'create_time': u'20140515180317Z', u'full_name': u'vaughn', 
    u'email': u'mwvaughn@devnull.com'}

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

**To be continued**

.. _Agave: https://agaveapi.co/
.. _Abaco: http://useabaco.cloud/
.. _PyPI: https://pypi.python.org/pypi
.. _Developer Documentation: http://developer.tacc.cloud/
.. _Docker: https://docs.docker.com/installation/#installation
.. _Jupyter: https://jupyter.org/
