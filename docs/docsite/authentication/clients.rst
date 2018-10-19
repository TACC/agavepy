.. _clients:

#############
OAuth Clients
#############


Creating a client
#################


Once you have soecified the tenant you wish to interact with :ref:`tenants`
we can go ahead and create an oauth client, which in turn we will use to biant
and refresh tokens.

To create a client use the method ``clients_create``.
This method takes two arguments, the client's name and a description, both
strings.

.. code-block:: pycon

    >>> from agavepy.agave import Agave
    >>> ag = Agave(tenant_id="sd2e")
    >>> ag.init()
    >>> agave.clients_create("my_super_cool_client", "my client's desciption")
    API username: your-username
    API password:
    >>> agave.api_key, agave.api_secret
    ('some-weird-looking-string', 'of-characters-that-agave-needs')


We will need the ``api_key`` and ``api_secret`` down the road to generate 
access tokens.


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
