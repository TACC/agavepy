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

Install latest release from PyPI_::

    pip install agavepy


Install latest release from GitHub::

    cd agavepy
    git checkout master
    python setup.py install

Developing or testing
=====================

Install latest development code from GitHub::

    cd agavepy
    git checkout develop
    python setup.py install

Configure a testing client, either by writing a `tests/configuration.json` file
or by setting environment variables as documented in the [auth fixture](https://github.com/TACC/agavepy/blob/cli/tests/fixtures/auth.py#L13)

Run unit tests with ``python -m pytest tests``

Quickstart
==========

If you already have an active installation of the TACC Cloud CLI or have worked
with AgavePy in the past, AgavePy can load credentials from a local cache. The
cache directory defaults to ``$HOME/.agave/`` but this can be overridden by
setting the ``TAPIS_CACHE_DIR`` or ``AGAVE_CACHE_DIR`` environment variables.

If this is the first time you are setting up AgavePy on the current host, you
will need to provide initial configuration details. In the future, AgavePy will
leverage the credential cache.

Pre-existing Tapis Auth Cache
-----------------------------

Load a cached client as follows:

.. code-block:: pycon

   >>> from agavepy.agave import Agave
   >>> ag = Agave.restore()

AgavePy will attempt to use the ``refresh_token`` Oauth2 workflow to maintain
an active access token, allowing for uninterrupted use of the Tapis APIs.

Configure a new Auth Cache
--------------------------

.. code-block:: pycon

   >>> from agavepy.agave import Agave
   >>> ag = Agave(tenant_id=<tenant_id>, username=<username>, password=<password>, api_key=<api_key>, api_secret=<api_secret>, api_server=<api_server>)

Advanced: Client from Environment
---------------------------------

There are many cases where it is not feasible or acceptable to load or save
cached credentials. Examples include public Docker container images, source
code repositories, or continuous integration jobs.

Handily, AgavePy supports loading an active client from the environment. To
take advantage of this, set the following environment variables:

.. code-block::

   TAPIS_BASE_URL=https://<api_server>
   TAPIS_TENANT_ID=<api_secret>
   TAPIS_USERNAME=<username>
   TAPIS_PASSWORD=<password>
   TAPIS_API_KEY=<api_key>
   TAPIS_API_SECRET=<api_secret>

With these variable set, the standard ``restore()`` method will load a client

.. code-block:: pycon

   >>> from agavepy.agave import Agave
   >>> ag = Agave.restore()
   >>> ag.token.api_key
   <api_key>

Advanced: Manually Refresh a Token
----------------------------------

.. code-block:: pycon

   >>> from agavepy.agave import Agave
   >>> ag = Agave.restore()
   >>> ag.refresh_token()
   '8776fba39858957ce72110135947af9f'

.. _Agave: https://agaveapi.co/
.. _Abaco: http://useabaco.cloud/
.. _PyPI: https://pypi.python.org/pypi
.. _Developer Documentation: http://developer.tacc.cloud/
.. _Docker: https://docs.docker.com/installation/#installation
.. _Jupyter: https://jupyter.org/
