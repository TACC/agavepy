#########################
Authenticating with Tapis
#########################

To interact with the Tapis APIs, you will need an Tapis platform account, 
an Oauth API client (created using your account credentials), and an 
access/refresh token pair (created using your Oauth client). 

***************
Oauth2 Overview
***************

Tapis uses Oauth2_ for authentication, which is a scheme to avoid sending your private 
username and password over the Internet. Without getting deeply into the details, 
here's how it works. You provide your actual username and password once and get 
back a substitute set of credentials called an **API Key and Secret**. You then 
use those credentials to get a temporary (expires in a short time) **access token** 
which is used in place of the username, password, key, and secret to access APIs. 
If a hostile actor were to get access to your token, they will only have a brief 
window where it is valid, which is much more secure than having static credentials 
floating around on the Internet. 

Getting a new token is simple: the **access_token** is returned with a 
**refresh token**, which can be redeemed **once** to get another 
**access token**. This can be done automatically (AgavePy does it for you) 
when the **access token** expires, or **on-demand** by you or your agent. 

***************
Create a Client
***************

Create a Tapis API client using the following code.

.. code-block:: pycon

   >>> from agavepy import Agave
   >>> ag = Agave(api_server='https://api.tacc.utexas.edu', 
                  username='tacobot',
                  password='$uch9oOdT@coS')
   >>> ag.clients_create()
   {'api_key': 'fybMWk8H4ROzk0aBKCC3VeCvCE5V', 
    'api_secret': 'XFsHQ8Vt7Wc37oQtyBLfa', 
    'client_name': 'cariad-major-puma'}

Write down the API key and secret, as you will need them to configure 
AgavePy to use this client in the future. Also note the client name, 
as you can use it to refer to the client when performing management 
actions like changing its subscriptions or deleting it. 

************************
Generate an Access Token
************************

Issuing your first access and refresh token requires you to specify api key and secret 
plus a username and password. This provides extra validation and protection since 
the resulting token pair can be chain-refreshed indefinitely until revoked. An AgavePy 
client automatically requests a token pair when initialized with valid 
credentials and API client details.

.. code-block:: pycon

   >>> from agavepy import Agave
   >>> ag = Agave(api_server='https://api.tacc.utexas.edu', 
                  username='tacobot',
                  password='$uch9oOdT@coS',
                  api_key='fybMWk8H4ROzk0aBKCC3VeCvCE5V',
                  api_secret='XFsHQ8Vt7Wc37oQtyBLfa')

You can confirm that the client ``ag`` is active by making an API query. 
Try ``ag.profiles.get()``. Alternatively, you can view the current token pair with 
``ag.tokens()``. 

Refreshing the Token
====================

The ``Agave.refresh()`` function will attempt to regenerate the access token, 
returning it as a string. If you need to discover the value of the refresh token, 
``tokens()`` will do the trick. 

.. code-block:: pycon

    >>> ag.refresh()
    'b9ffb4ed6c3c3412d2e09de3b3defa33'
    >>> ag.tokens()
    {'access_token': 'b9ffb4ed6c3c3412d2e09de3b3defa33', 
     'refresh_token': 'd941cc474ed4a2fcf93672b65f76195'}

.. note:: A properly initialized Agave client will attempt to refresh its own token 
          automatically whenever the token appears to have expired. Thus, you do 
          not generally need to worry about token management while working with 
          AgavePy functions.  

**********************
Local Credential Cache
**********************

Once a complete AgavePy client has been initialized, it stores a small plaintext file 
containing api key and secret, access token, and refresh token on the local file 
system. The default location for this cache file is in the directory 
``$HOME/.agave/`` but this can be overridden by setting the environment variable 
``TAPIS_CACHE_DIR``. This comes in handy because AgavePy has a built-in function for 
reading from the cache file. In a fresh Python REPL, try the following:

.. code-block:: pycon

   >>> from agavepy import Agave
   >>> ag = Agave.restore()

Like we did earlier, you can confirm that the client ``ag`` is active by making 
an API query. Try ``ag.profiles.get()``. Alternatively, you can view the 
current token pair with ``ag.tokens()``.

*************
Special Cases
*************

AgavePy's standard workflow is optimized to support interactive scripting on systems 
where you have write access to the local filesystem, and where you are comfortable 
storing your API key and secret. Some environments, like Docker containers or public 
web services, don't fit that mold. Thus, there are a couple of alternative paths to 
configure AgavePy for use by your application. 

Access-Only Client
==================

AgavePy can be set up as a **access-only client** using just an access token. This is 
helpful for short-term usage, but does require the access token be generated using 
another means. Also, the token will be active no more than an hour. Keep these 
limitations in mind when designing an implementation that relies on an access-only 
API client.  

.. code-block:: pycon

   >>> from agavepy import Agave
   >>> ag = Agave(api_server='https://api.tacc.utexas.edu', 
   ...            token='b9ffb4ed6c3c3412d2e09de3b3defa33')
   >>> ag.profiles.get()
   {'first_name': 'Taco', 'last_name': 'Bot', 'full_name': 'tacobot', 
    'email': 'tacobot@tacc.cloud', 
    'phone': '', 'mobile_phone': '', 'status': '', 'create_time': '20140515180317Z', 
    'uid': 806444, 'username': 'tacobot'}


Environment Variables
=====================

By setting various configurations of environment variables, AgavePy can be initialized 
directly from the environment with no cache file required via ``Agave.restore()``. The 
capabilities of the client will be based on which variables were set. For example, a 
*Standard* client can issue and re-issue access tokens indefinitely, while an 
*Access-Only** client can access Tapis APIs only for the active duration of the token 
passed as ``TAPIS_API_TOKEN``.

+-----------------------------+------------+---------------+---------------+--------------+----------------+-----------------+
| **Variable**                | *Standard* | *Access-Only* | Token-Refresh | Bare-Refresh | Client-Manager | Token-Generator |
+-----------------------------+------------+---------------+---------------+--------------+----------------+-----------------+
| ``TAPIS_BASE_URL``          | X          | X             | X             | X            | X              | X               |
+-----------------------------+------------+---------------+---------------+--------------+----------------+-----------------+
| ``TAPIS_API_KEY``           | X          |               | X             |              |                | X               |
+-----------------------------+------------+---------------+---------------+--------------+----------------+-----------------+
| ``TAPIS_API_SECRET``        | X          |               | X             |              |                | X               |
+-----------------------------+------------+---------------+---------------+--------------+----------------+-----------------+
| ``TAPIS_API_TOKEN``         |            | X             | X             | X            |                |                 |
+-----------------------------+------------+---------------+---------------+--------------+----------------+-----------------+
| ``TAPIS_API_REFRESH_TOKEN`` |            |               | X             | X            |                |                 |
+-----------------------------+------------+---------------+---------------+--------------+----------------+-----------------+
| ``TAPIS_API_USERNAME``      | X          |               |               |              | X              | X               |
+-----------------------------+------------+---------------+---------------+--------------+----------------+-----------------+
| ``TAPIS_API_PASSWORD``      | X          |               |               |              | X              | X               |
+-----------------------------+------------+---------------+---------------+--------------+----------------+-----------------+

.. note:: Environment variables are not updated by the AgavePy library. For example, if ``TAPIS_API_TOKEN`` expires, the 
          client will no longer have access to Tapis APIs. Or, if a *Token-Refresh* client is created, it must track any 
          new values for the access and refresh tokens after ``Agave.refresh()`` is invoked, since the environment variable 
          values will no longer be valid. 

.. Links

.. _Docker: https://docs.docker.com/installation/#installation
.. _Jupyter: https://jupyter.org/
.. _Oauth2: https://auth0.com/docs/protocols/oauth2
.. _PyPI: https://pypi.python.org/pypi
.. |TapisCLI| replace:: Tapis CLI docs
.. _TapisCLI: https://tapis-cli.readthedocs.io/en/latest/
.. |TapisAPI| replace:: Tapis API docs
.. _TapisAPI: https://tacc-cloud.readthedocs.io/projects/agave/en/latest/
.. |AbacoAPI| replace:: Abaco API docs
.. _AbacoAPI: https://tacc-cloud.readthedocs.io/projects/abaco/en/latest/
.. |TUP| replace:: TACC User Portal
.. _TUP: https://portal.tacc.utexas.edu/account-request
