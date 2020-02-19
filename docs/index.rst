.. AgavePy documentation master file, created by
   sphinx-quickstart on Mon Feb  5 11:08:11 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

#####################
AgavePy Documentation
#####################

****************
What is AgavePy?
****************

AgavePy is an open source Python SDK that enables you to interact 
with Tapis_ (v2) services using functions in your Python scripts and REPL. 

With minimal configuration, AgavePy lets you to start running commands 
that implement functions equivalent to those provided by browser-based 
Tapis web applications or the Tapis CLI.

All Tapis PaaS (platform as a service) administration, management, and access 
functions are available via AgavePy. AgavePy provides direct access to all  
public Tapis APIs - You can explore a service's capabilities 
with AgavePy, and develop Python scripts to manage resources, perform 
computation or analysis workflows, build automations, and more. 

Example: List contents of a Tapis storageSystem path
====================================================

The ``Agave.files.list()`` function returns the directory contents of a 
Tapis storage system (similar to an S3 bucket) and path.

.. code-block:: pycon

   >>> from agavepy import Agave
   >>> ag = Agave.restore()
   >>> files = ag.files.list(storageSystem='tacc-public-demo', filePath='/examples')

The same function could be performed via authenticated HTTP GET to 
``/files/v2/listings/system/tacc-public-demo/examples`` or using the 
Tapis CLI ``tapis files list agave://tacc-public-demo/examples``. The former 
requires more sophisticated knowledge of working with web services, while 
the latter is more suited to interactive or shell script usage. 

Your use case informs your choice of tooling - If you are interested in these 
other mechanisms for working with Tapis, please consult the appropriate resources:

  * |TapisAPI|_ : Research computing web services
  * |AbacoAPI|_ : Functions-as-a-Service for orchestration and integration
  * |TapisCLI|_ : Shell environment for Tapis and Abaco

You can view *and fork* the source code for Tapis, AgavePy, and Tapis CLI on 
GitHub. Join the community of users on GitHub to provide feedback, request features, 
and submit your own contributions. 

************************
About the Tapis Platform
************************

Tapis is an open source *Science-as-a-Service* API platform for powering  
research computing and data management workflows. Tapis unites high-performance 
computing (HPC), high-throughput computing (HTC), Cloud, and Big Data resources under a 
single, web-friendly REST API featuring fine-grained access control, detailed 
provenance, reproducibility, and scalability. 

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
