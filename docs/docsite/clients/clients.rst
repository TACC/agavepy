#############
OAuth Clients
#############


Creating a client
#################

We will start by generating a set of Agave client keys, OAuth credentials.

Generating OAuth credentials uses HTTP Basic authentication 
(requires username and password).

Agave has a full OAuth provider server and supports 4 major grant types:

1. `password`
2. `authorization_code`
3. `refresh_token`
4. `implicit`

For more information, see `supported authorization flows <http://developer.agaveapi.co/#supported-authorization-flows>`_.

The OAuth client will have access to all basic Agave APIs.

To create a client, simply make a POST reuest to the clients endpoint. 
The request must include the `clientName`.
If successful, the response should include a 201 HTTP code.

We can use ``agavepy`` to create an oauth client:

.. code-block:: pycon

    >>> from agavepy.agave import Agave
    >>> ag = Agave(tenant_id="sd2e")
    >>> ag.init()
    >>> ag.clients_create("client-name", "some description")
    API username: your-username
    API password:


Two important fields in the response are the `consumerKey` and
`consumerSecret`.
We will need these two values to interact with theAgave OAuth token service to
generate access tokens.
The ``Agave`` object will store this two field and make them available for you.

.. code-block:: pycon

    >>> ag.api_key
    'some-api-key'
    >>> ag.api_secret
    'some-api-secret'


Listing all clients
###################

To list all agave oauth clients registered for a given user, one can use the
`clients_list()` method.

.. code-block:: pycon

    >>> ag.clients_list()
    API username: your-username
    API password:
    NAME                           DESCRIPTION
    client-name                    some description
    >>>
