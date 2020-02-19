.. _configs:

####################
Saving your sesssion
####################

If you are here, hopefully you were able to specify a tenant, :ref:`tenants`,
create an oauth client, :ref:`clients`, and get an access token :ref:`tokens`.

To store your session, you can use ``save_configs``.

.. code-block:: pycon

    >>> agave.save_configs()

``save_configs`` takes an optional argument, ``cache_dir`` which tells
``Agave`` the directory where you want to store your configurations otherwise
it will default to ``~/.agave``.

``save_configs`` will store your configurations in a file named
``config.json``.
If you use default parameters, this file will be in ``~/.agave/config.json``.
``save_configs`` also writes a ``current`` file for backward-compatibility with
other Agave tools.

The configuration file will look something like this:

.. code-block:: json

    {
        "current": {
            "my_super_cool_client": {
                "tenantid": "sd2e",
                "baseurl": "https://api.sd2e.org",
                "devurl": "",
                "apisecret": "some-secret",
                "apikey": "some-key",
                "username": "your-username",
                "access_token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                "refresh_token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                "created_at": "1539708516",
                "expires_in": 14400,
                "expires_at": "Tue Oct 16 20:48:36 UTC 2018"
            }
        },
        "sessions": {
            "sd2e": {
                "your-username": {
                    "my_super_cool_client": {
                        "tenantid": "sd2e",
                        "baseurl": "https://api.sd2e.org/",
                        "devurl": "",
                        "apisecret": "some-secret",
                        "apikey": "some-key",
                        "username": "your-username",
                        "access_token": "xxxxxxxxxxxxxxxxxxxxxxxxx",
                        "refresh_token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                        "created_at": "1539706810",
                        "expires_in": 14400,
                        "expires_at": "Tue Oct 16 20:20:10 UTC 2018"
                    }
                }
            }
        }
    }
