.. _authentication:

==============                                          
Authentication
==============

In order to use ``AgavePy`` a user or program needs to be authenticated with
the API.
The Agave services use the Oauth protocol to manage user authentication.

The authentication process involves specifying the tenant one wishes to
interact with, the creation of an Oauth client that will create and refresh
access tokens for the rest of the Agave services, and the request for the
creation of an access token and refresh token pair or the use of a refresh
token to obtain a new token pair after the tokens have expired.
We will refer to the specfication fo a tenant, client configurations, and
tokens as a session.

In this section we descrie how ``AgavePy`` enables us to go through the process
of initiating and managing a session.

                                                                                
.. toctree::
    :maxdepth: 2

    tenants
    clients
    tokens
    configs

.. only::  subproject and html                                                  
                                                                                
   Indices                                                                      
   =======                                                                      
                                                                                
   * :ref:`genindex`
