.. _clients:

#############
OAuth Clients
#############


Creating a client
#################


Once you have specified the tenant you wish to interact with :ref:`tenants`
we can go ahead and create an oauth client, which in turn we will use to obtain
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


Deleting a client
#################

If you want to delete an oauth client, you can do as such:

.. code-block:: pycon

    >>> ag.clients_delete("some-client-name")
    API password:

If you don't pass a client name to ``clients_delete``, then the ``Agave``
object will try to delete the oauth client in its current session.


Subscribing to an API
#####################

If you want to subscribe an oauth client to a TACC api, then you can do so as
follows:

.. code-block:: pycon

    >>> ag.clients_subscribe("PublicKeys", "v2", "admin", client_name="client")

If you don't set the ``client_name`` argument then the ``ag`` object will try
to use the oauth client stored in your current session.
