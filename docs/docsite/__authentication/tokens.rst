.. _tokens:

#############
Access Tokens
#############

Getting an access token
#######################

Now that you have a tenant to interact with, :ref:`tenants`, and you have
created an oauth client, :ref:`clients`, creating an access and refresh tokens
is one method away: ``get_access_token``.

.. code-block:: pycon

    >>> agave.get_access_token()
    API password:
    >>> agave.token, agave.refresh_token
    ('imageine-an-access-token-here', 'and-a-refresh-token-here')


Refreshing an access token
##########################

You can use the ``refresh_tokens`` method to manually refresh your tokens.

.. code-block:: pycon

    >>> agave.refresh_tokens()
    >>> agave.token, agave.refresh_token
    ('new-access-token-goes-here', 'new-refresh-token')
