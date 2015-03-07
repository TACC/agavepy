=======
AgavePy
=======

A simple Python binding for the `Agave API`_.


Installation
------------

Install from PyPI_::

    pip install agavepy


Quickstart
----------

The first step is to create an ``agave`` Python object pointing to
your tenant:

.. code-block:: pycon

   >>> from agavepy.agave import Agave
   >>> my_agave = Agave(api_server='https://agave.iplantc.org',
   ...                  resources='https://agave.iplantc.org/docs/v2/resources/',
   ...                  username='myusername', password='mypassword')

Once the object is instantiated, interact with it according to the
methods in the API documentation.

For example, create a new client with:

.. code-block:: pycon

   >>> my_client = my_agave.clients.create(...)

Create a token with:

.. code-block:: pycon

   >>> my_agave.token.create()

Access any endpoint with:

.. code-block:: pycon

   >>> my_agave.systems.list()
   >>> my_agave.jobs.manage(...)


.. _Agave API: http://agaveapi.co/
.. _PyPI: https://pypi.python.org/pypi


License
=======

MIT
