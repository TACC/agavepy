##################
Tapis User Account
##################

Tapis is a "multi-tenant" web service platform, which means it provides 
and manages logically-isolated resources. The main source for such 
isolation is how a user's identity is confirmed. As a Tapis user, you need 
to know which **tenant** you wish to use. For most people, and for the 
purposes of this documentation, the **TACC** tenant (``tacc.prod``) will 
be the default and correct choice. 

Thus, you will need an active TACC account. Go to the TUP_ and 
create an account, or, if you have a TACC account already, please confirm that 
you are able log into the TUP_ with your TACC username and password.

.. note:: New TACC accounts must be confirmed via an email-based workflow before 
          they are active, so please check your email and follow any validation 
          instructions you find there. 

*************
Other Tenants
*************

Documentation on account policy and management for other tenants 
(and Tapis sites) can be found here.

+----------+------------+---------------------------+-------------------------------------------------+
| **Site** | **Tenant** | **Credentials**           | **Account Page**                                |
+----------+------------+---------------------------+-------------------------------------------------+
| TACC     | CyVerse    | Cyverse username/password | https://user.cyverse.org/                       |
+----------+------------+---------------------------+-------------------------------------------------+
| TACC     | DesignSafe | TACC username/password    | https://www.designsafe-ci.org/account/register/ |
+----------+------------+---------------------------+-------------------------------------------------+
| TACC     | SGCI       | TACC username/password    | TBD                                             |
+----------+------------+---------------------------+-------------------------------------------------+
| TACC     | TACC       | TACC username/password    | https://portal.tacc.utexas.edu/account-request  |
+----------+------------+---------------------------+-------------------------------------------------+
| TACC     | 3DEM       | TACC username/password    | https://3dem.org/help/portal-users-guide/       |
+----------+------------+---------------------------+-------------------------------------------------+
| CDC      | TBD        | TBD                       | TBD                                             |
+----------+------------+---------------------------+-------------------------------------------------+

You may also consult the Tapis platform point of contact for each tenant directly. 

.. Links

.. _Docker: https://docs.docker.com/installation/#installation
.. _Jupyter: https://jupyter.org/
.. _Oauth2: https://auth0.com/docs/protocols/oauth2
.. _PyPI: https://pypi.python.org/pypi
.. |TapisCLI| replace:: Tapis CLI docs
.. _TapisCLI: https://tapis-cli.readthedocs.io/en/latest/
.. |TapisAPI| replace:: Tapis API docs
.. _TapisAPI: https://tacc-cloud.readthedocs.io/projects/agave/en/latest/
.. |AbacoAPI| replace:: Abaco API docs
.. _AbacoAPI: https://tacc-cloud.readthedocs.io/projects/abaco/en/latest/
.. |TUP| replace:: TACC User Portal
.. _TUP: https://portal.tacc.utexas.edu/account-request
