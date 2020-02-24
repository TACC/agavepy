.. AgavePy documentation master file, created by
   sphinx-quickstart on Mon Feb  5 11:08:11 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

#####################
AgavePy Documentation
#####################

AgavePy is an open-source Python SDK that lets you to use Tapis_ (v2) 
services to manage data, perform computational analysis workflows, 
build automations, and more, all from within Python scripts or 
the Python interactive REPL. 

You can view and fork the source code for AgavePy on 
`GitHub <https://github.com/TACC/agavepy>`_. Join our 
community of users to provide feedback, request features, 
and submit your own contributions. 

***********
About Tapis
***********

Tapis is an open source *Science-as-a-Service* API that powers 
research computing and data management workflows. Tapis unites high-performance 
computing (HPC), high-throughput computing (HTC), Cloud, and Big Data resources under a 
single, web-friendly REST API featuring fine-grained access control, detailed 
provenance, reproducibility, and scalability. 

Example: List contents of a Tapis storageSystem path
====================================================

To illustrate how one can use AgavePy, consider this example. Here, the 
``Agave.files.list()`` function is used to return a Python list of the 
contents of a directory on a Tapis storage system.

.. code-block:: pycon

   >>> from agavepy import Agave
   >>> ag = Agave.restore()
   >>> files = ag.files.list(storageSystem='tacc-public-demo', filePath='/examples')

This same function can be accomplished by making an authenticated HTTP GET to 
the files API:

.. code-block:: shell

   curl -XGET -H "Authentication: Bearer 24cace8cea8cd541012a323d9ebd2b6" \
   'https://api.tacc.utexas.edu/files/v2/listings/system/files/v2/listings/system/tacc-public-demo/examples'

It could also be done using the Tapis CLI:

.. code-block:: shell

    tapis files list agave://tacc-public-demo/examples

Making a direct API call requires more experience working with web services, 
but is extremely flexible. Using the CLI is very accessible, though it is 
a bit more opinionated and is also suited to interactive or script usage. AgavePy 
aims for the middle ground, providing an expressive, embeddable interface to Tapis 
that is closely aligned with the platform API's syntax and usage. 

Ultimately, your use case informs your choice of tooling - If you are interested in
these other paths for working with Tapis, they are amply documented:

  * |TapisAPI|_ : Research computing web services
  * |AbacoAPI|_ : Functions-as-a-Service for orchestration and integration
  * |TapisCLI|_ : Shell environment for Tapis and Abaco

.. toctree::
    :maxdepth: 1
    :caption: Install & Configure AgavePy

    install/installation
    account
    authentication

.. toctree::
   :maxdepth: 1
   :caption: Using AgavePy

   use_agavepy

.. toctree::
   :maxdepth: 1
   :caption: Use AgavePy with Tapis APIs

   docsite/systems/index
   docsite/files/index
   docsite/apps/index
   docsite/jobs/index
   docsite/meta/index
   docsite/notifications/index
   docsite/postits/index
   docsite/profiles/index
   docsite/actors/index

.. toctree::
   :maxdepth: 1
   :caption: Advanced Topics

   docsite/querying/index
   docsite/admin/index
   docsite/clients/index

.. toctree::
   :maxdepth: 1
   :caption: Contribute to AgavePy

.. Links

.. _Docker: https://docs.docker.com/installation/#installation
.. _Jupyter: https://jupyter.org/
.. _Oauth2: https://auth0.com/docs/protocols/oauth2
.. _PyPI: https://pypi.python.org/pypi
.. _Tapis: https://www.tacc.utexas.edu/tapis
.. |TapisCLI| replace:: Tapis CLI docs
.. _TapisCLI: https://tapis-cli.readthedocs.io/en/latest/
.. |TapisAPI| replace:: Tapis API docs
.. _TapisAPI: https://tacc-cloud.readthedocs.io/projects/agave/en/latest/
.. |AbacoAPI| replace:: Abaco API docs
.. _AbacoAPI: https://tacc-cloud.readthedocs.io/projects/abaco/en/latest/
.. |TUP| replace:: TACC User Portal
.. _TUP: https://portal.tacc.utexas.edu/account-request
