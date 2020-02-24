##################
The AgavePy client
##################

The core aspect of an initialized AgavePy client is a submodule 
and function structure that mirrors the Swagger 1.2 specification 
for the Tapis APIs. 

.. code-block:: pycon

   >>> from agavepy import Agave
   >>> ag = Agave.restore()
   >>> # find available APIs
   >>> dir(ag)
   ['actors', 'admin', 'apps', 'clients', 'files', 'jobs', 'meta', 'monitors', 
   'notifications', 'postits', 'profiles', 'systems', 'transforms']
   >>> # inspect functions available for the 'apps' API
   >>> dir(ag.apps)
   ['add', 'delete', 'deletePermissions', 'deletePermissionsForUser', 'get', 
   'getJobSubmissionForm', 'list', 'listByName', 'listByOntologyTerm', 'listBySystemId', 
   'listByTag', 'listPermissions', 'listPermissionsForUser', 'manage', 'update', 
   'updateApplicationPermissions', 'updatePermissionsForUser']

Unfortunately, because AgavePy is metaprogrammed from the Swagger specification, 
the help text for the individual functions is not available. As an alternative, 
you can look up the function help here in the AgavePy docs in the section 
**Use AgavePy with Tapis APIs**. 

#####################
Specifying Parameters
#####################

In the table below are some common parameters, a list of services that accept them 
for at least one command, and a description of what they are. Usage examples are shown 
below the table. 

+--------------------------------+-------------------------------+---------------------------------+
| **Keyword Argument**           | **Service(s)**                | **Description**                 |
+--------------------------------+-------------------------------+---------------------------------+
| ``actorId``, ``executionId``,  | actors                        | String hashed identifier        |
| ``nonceId``, ``workerId``      |                               |                                 |
+--------------------------------+-------------------------------+---------------------------------+
| ``appId``, ``systemId``        | apps, jobs, systems           | String distinct identifier      |
+--------------------------------+-------------------------------+---------------------------------+
| ``jobId``, ``uuid``            | jobs, metadata, notifications | String UUID                     |
+--------------------------------+-------------------------------+---------------------------------+
| ``filePath``                   | apps, jobs, notifications     | String path relative to ``/``   |
|                                |                               | on a storage system             |
+--------------------------------+-------------------------------+---------------------------------+
| ``body``                       | actors, apps, jobs,           | JSON document conforming to an  |
|                                | notifications, metadata,      | API+function schema             |
|                                | systems                       |                                 |
+--------------------------------+-------------------------------+---------------------------------+
| ``limit``                      | apps, jobs, notifications,    | integer <= 300                  |
|                                | metadata, systems             |                                 |
+--------------------------------+-------------------------------+---------------------------------+
| ``offset``                     | apps, jobs, notifications,    | integer >= 0                    |
|                                | metadata, systems             |                                 |
+--------------------------------+-------------------------------+---------------------------------+

.. note:: All values must be passed as keyword arguments in AgavePy. A common coding 
          convention is that Python keyword arguments can be passed positionally. 
          This isn't a safe assumption when using AgavePy due to some low-level details 
          of how the library is implemented.

.. code-block:: pycon
   :caption: Refer to a specific Tapis entity by its identifier

   >>> # show a specific app
   >>> ag.apps.get(appId='prodigal-2.6.3u3')
   {'id': 'prodigal-2.6.3u3', ..., 'outputs': []}
   >>> #
   >>> # show a specific system
   >>> ag.systems.get(systemId='data.iplantcollaborative.org')
   {'owner': 'cyverse', ..., 'status': 'UP'}
   >>> #
   >>> # inspect a job
   >>> ag.jobs.getStatus(jobId='6632084267285418471-242ac113-0001-007')
   {'id': '6632084267285418471-242ac113-0001-007', 'status': 'FINISHED'}

.. code-block:: pycon
   :caption: Call a function requiring a body parameter

   >>> # disable an app using its 'manage' function
   >>> ag.apps.manage(appId='prodigal-2.6.3', body={'action': 'disable'})
   {'id': 'prodigal-2.6.3', ..., 'available': False}

##################
Pagination Options
##################

Any Tapis API operations (save for the Abaco API) that implement a ``list`` operation accept 
pagination options ``limit`` and ``offset``. 

.. code-block:: pycon

   >>> # show applications 51-100
   >>> ag.apps.list(limit=50, offset=50)

#####################
Reponses from AgavePy
#####################

All AgavePy commands return a Python dictionary, deserialized from a JSON response sent 
by the relevant Tapis API. This dictionary corresponds to the ``result`` key in the 
API JSON response. 

Interpreting Errors
===================

TBD
