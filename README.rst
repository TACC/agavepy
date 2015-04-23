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
   ...                  username='myusername', password='mypassword')

Once the object is instantiated, interact with it according to the
methods in the API documentation.

For example, create a new client with:

.. code-block:: pycon

   >>> my_agave.clients.create(body={'clientName': 'my_client'})

Access any endpoint with:

.. code-block:: pycon

   >>> my_agave.systems.list()
   >>> my_agave.jobs.manage(...)

Once a client is created, it is used by default to access the API.

To make use of an existing client, pass the client's credentials into the Agave constructor:

.. code-block:: pycon

   >>> from agavepy.agave import Agave
   >>> my_agave = Agave(api_server='https://agave.iplantc.org',
   ...                  username='myusername', password='mypassword', client_name='my_client', api_key='123', api_secret='abc')

Alternatively, the SDK will attempt to recover the client credentials from the client name if they are stored
in the user's ``.agavepy`` file, in which case just passing the ``client_name`` will suffice:

.. code-block:: pycon

   >>> from agavepy.agave import Agave
   >>> my_agave = Agave(api_server='https://agave.iplantc.org',
   ...                  username='myusername', password='mypassword', client_name='my_client')



.. _Agave API: http://agaveapi.co/
.. _PyPI: https://pypi.python.org/pypi


Using agavepy in Docker
========================

This repository includes a ``Dockerfile`` and a ``docker-compose.yml``
file, which allows a zero installation version of ``agavepy``.

The only requirement is Docker_ and `docker-compose`_, most likely
already installed in your system.

Then, clone this repository and execute ``docker-compose`` as follows:

.. code-block:: bash

   $ cd agavepy
   $ docker-compose up

Navigate to http://localhost:8888 and access the Jupyter_ notebook
with password ``agavepy``.  The notebook ``Example.ipynb`` contains a
full example of use.


License
=======

Agavepy is licensed under the MIT license.

Swagger.py is copyright of Digium, Inc., and licensed under BSD 3-Clause License.
