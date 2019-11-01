*******
systems
*******

Summary: Register and manage systems

add: Add or update a system.
============================
``systems.add(body=<BODY>)``

Keyword Args:
-------------
    * **body**: The description of the system to add or update. (JSON, SystemRequest)


**SystemRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/SystemRequest.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
      "properties": {
        "description": {
          "description": "Verbose description of this system.",
          "type": "string"
        },
        "environment": {
          "description": "Environment variables to set upon login prior to job submission.",
          "type": "string"
        },
        "executionType": {
          "description": "The execution paradigm used to run jobs on this system.",
          "enum": [
            "HPC",
            "CONDOR",
            "CLI"
          ],
          "type": "string"
        },
        "id": {
          "description": "Unique identifier for this system.",
          "type": "string"
        },
        "login": {
          "description": "The login config defining how to connect to this system for job submission.",
          "type": "LoginConfig"
        },
        "maxSystemJobs": {
          "description": "The maximum number of jobs that can be simultaneously run on the system across all queues.",
          "type": "int"
        },
        "maxSystemJobsPerUser": {
          "description": "The maximum number of jobs that can be simultaneously run on the system across all queues by a single user.",
          "type": "int"
        },
        "name": {
          "description": "Common name for this system.",
          "type": "string"
        },
        "queues": {
          "description": "The execution paradigm used to run jobs on this system.",
          "type": "array"
        },
        "scheduler": {
          "description": "The type of scheduled used to run jobs.",
          "enum": [
            "COBALT",
            "CONDOR",
            "FORK",
            "LOADLEVELER",
            "LSF",
            "MOAB",
            "PBS",
            "SGE",
            "SLURM",
            "TORQUE",
            "UNKNOWN"
          ],
          "type": "string"
        },
        "scratchDir": {
          "description": "The scratch directory where job execution directories will be created at runtime. The workDir is used if this is not specified.",
          "type": "string"
        },
        "site": {
          "description": "The site associated with this system.",
          "type": "string"
        },
        "startupScript": {
          "description": "Script to be run after login and prior to execution.",
          "type": "string"
        },
        "status": {
          "description": "The status of this system. Systems must be in UP status to be used.",
          "enum": [
            "UP",
            "DOWN",
            "UNKNOWN"
          ],
          "type": "string"
        },
        "storage": {
          "description": "The storage config defining how to connect to this system for data staging.",
          "type": "StorageConfig"
        },
        "type": {
          "description": "The type of this system.",
          "enum": [
            "EXECUTION",
            "STORAGE"
          ],
          "type": "string"
        },
        "workDir": {
          "description": "The work directory where job execution directories will be created at runtime. This is used if scratchDir is not specified. If neither are specified, the job directory will be created in the system homeDir.",
          "type": "string"
        }
      },
      "required": [
        "status",
        "queues",
        "storage",
        "executionType",
        "scheduler",
        "login",
        "type",
        "name"
      ],
      "title": "AgavePy SystemRequest schema",
      "type": "object"
    }

Response:
---------
    * *A single System object*

list: Show all systems available to the user.
=============================================
``systems.list(default=None, limit=250, offset=0, public=None, type=None)``

Keyword Args:
-------------
    * **type**: The type of system to return (string)
    * **default**: Should only default systems be returned (boolean)
    * **public**: Should only publicly available systems be returned (boolean)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Array of SystemSummary objects*

delete: Delete a system.
========================
``systems.delete(systemId=<SYSTEMID>)``

Keyword Args:
-------------
    * **systemId**: The unique id of the system (string)


Response:
---------
    * *String*

get: Find information about an individual system.
=================================================
``systems.get(systemId=<SYSTEMID>)``

Keyword Args:
-------------
    * **systemId**: The unique id of the system (string)


Response:
---------
    * *A single System object*

manage: Perform a management action on the system.
==================================================
``systems.manage(body=<BODY>, systemId=<SYSTEMID>)``

Keyword Args:
-------------
    * **systemId**: The unique id of the system (string)
    * **body**: The description of the system to update. (JSON, SystemOperationRequest)


**SystemOperationRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/SystemOperationRequest.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
      "properties": {
        "action": {
          "description": "Action to perform on the system.",
          "enum": [
            "ENABLE",
            "DISABLE",
            "PUBLISH",
            "UNPUBLISH",
            "SETDEFAULT",
            "UNSETDEFAULT",
            "SETGLOBALDEFAULT",
            "UNSETGLOBALDEFAULT",
            "CLONE"
          ],
          "type": "string"
        },
        "id": {
          "description": "The new system id of the cloned system",
          "type": "string"
        }
      },
      "required": [
        "action"
      ],
      "title": "AgavePy SystemOperationRequest schema",
      "type": "object"
    }

Response:
---------
    * *String*

update: Find information about an individual system.
====================================================
``systems.update(body=<BODY>, systemId=<SYSTEMID>)``

Keyword Args:
-------------
    * **systemId**: The unique id of the system (string)
    * **body**: The description of the system to update. (JSON, SystemRequest)


**SystemRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/SystemRequest.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
      "properties": {
        "description": {
          "description": "Verbose description of this system.",
          "type": "string"
        },
        "environment": {
          "description": "Environment variables to set upon login prior to job submission.",
          "type": "string"
        },
        "executionType": {
          "description": "The execution paradigm used to run jobs on this system.",
          "enum": [
            "HPC",
            "CONDOR",
            "CLI"
          ],
          "type": "string"
        },
        "id": {
          "description": "Unique identifier for this system.",
          "type": "string"
        },
        "login": {
          "description": "The login config defining how to connect to this system for job submission.",
          "type": "LoginConfig"
        },
        "maxSystemJobs": {
          "description": "The maximum number of jobs that can be simultaneously run on the system across all queues.",
          "type": "int"
        },
        "maxSystemJobsPerUser": {
          "description": "The maximum number of jobs that can be simultaneously run on the system across all queues by a single user.",
          "type": "int"
        },
        "name": {
          "description": "Common name for this system.",
          "type": "string"
        },
        "queues": {
          "description": "The execution paradigm used to run jobs on this system.",
          "type": "array"
        },
        "scheduler": {
          "description": "The type of scheduled used to run jobs.",
          "enum": [
            "COBALT",
            "CONDOR",
            "FORK",
            "LOADLEVELER",
            "LSF",
            "MOAB",
            "PBS",
            "SGE",
            "SLURM",
            "TORQUE",
            "UNKNOWN"
          ],
          "type": "string"
        },
        "scratchDir": {
          "description": "The scratch directory where job execution directories will be created at runtime. The workDir is used if this is not specified.",
          "type": "string"
        },
        "site": {
          "description": "The site associated with this system.",
          "type": "string"
        },
        "startupScript": {
          "description": "Script to be run after login and prior to execution.",
          "type": "string"
        },
        "status": {
          "description": "The status of this system. Systems must be in UP status to be used.",
          "enum": [
            "UP",
            "DOWN",
            "UNKNOWN"
          ],
          "type": "string"
        },
        "storage": {
          "description": "The storage config defining how to connect to this system for data staging.",
          "type": "StorageConfig"
        },
        "type": {
          "description": "The type of this system.",
          "enum": [
            "EXECUTION",
            "STORAGE"
          ],
          "type": "string"
        },
        "workDir": {
          "description": "The work directory where job execution directories will be created at runtime. This is used if scratchDir is not specified. If neither are specified, the job directory will be created in the system homeDir.",
          "type": "string"
        }
      },
      "required": [
        "status",
        "queues",
        "storage",
        "executionType",
        "scheduler",
        "login",
        "type",
        "name"
      ],
      "title": "AgavePy SystemRequest schema",
      "type": "object"
    }

Response:
---------
    * *A single System object*

deleteRoles: Deletes all roles on a system.
===========================================
``systems.deleteRoles(systemId=<SYSTEMID>)``

Keyword Args:
-------------
    * **systemId**: The id of the system. (string)


Response:
---------
    * *String*

listRoles: Get a list of all users and their roles on this system.
==================================================================
``systems.listRoles(systemId=<SYSTEMID>, limit=250, offset=0)``

Keyword Args:
-------------
    * **systemId**: The id of the system. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Array of SystemRole objects*

updateRole: Add or update a user's role on a system.
====================================================
``systems.updateRole(body=<BODY>, systemId=<SYSTEMID>)``

Keyword Args:
-------------
    * **systemId**: The id of the system. (string)
    * **body**: The role to update. (JSON, SystemRole)


**SystemRole schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/SystemRole.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
      "properties": {
        "role": {
          "description": "The role granted this user.",
          "enum": [
            "USER",
            "PUBLISHER",
            "ADMIN",
            "OWNER"
          ],
          "type": "string"
        },
        "username": {
          "description": "The username of the api user granted this role.",
          "type": "string"
        }
      },
      "required": [],
      "title": "AgavePy SystemRole schema",
      "type": "object"
    }

Response:
---------
    * *String*

deleteRoleForUser: Deletes all roles on a system.
=================================================
``systems.deleteRoleForUser(systemId=<SYSTEMID>, username=<USERNAME>)``

Keyword Args:
-------------
    * **systemId**: The id of the system. (string)
    * **username**: The username of the api user associated with the role (string)


Response:
---------
    * *String*

getRoleForUser: Get a specific user's roles on this system.
===========================================================
``systems.getRoleForUser(systemId=<SYSTEMID>, username=<USERNAME>, limit=250, offset=0)``

Keyword Args:
-------------
    * **systemId**: The id of the system. (string)
    * **username**: The username of the user about whose role you are inquiring. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *A single SystemRole object*

updateRoleForUser: Add or update a user's role on a system.
===========================================================
``systems.updateRoleForUser(body=<BODY>, systemId=<SYSTEMID>, username=<USERNAME>)``

Keyword Args:
-------------
    * **systemId**: The id of the system. (string)
    * **username**: The username of the api user associated with the role (string)
    * **body**: The role to update. (JSON, SystemRole)


**SystemRole schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/SystemRole.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
      "properties": {
        "role": {
          "description": "The role granted this user.",
          "enum": [
            "USER",
            "PUBLISHER",
            "ADMIN",
            "OWNER"
          ],
          "type": "string"
        },
        "username": {
          "description": "The username of the api user granted this role.",
          "type": "string"
        }
      },
      "required": [],
      "title": "AgavePy SystemRole schema",
      "type": "object"
    }

Response:
---------
    * *String*

deleteCredentials: Deletes all credentials registered to a system.
==================================================================
``systems.deleteCredentials(systemId=<SYSTEMID>)``

Keyword Args:
-------------
    * **systemId**: The id of the system. (string)


Response:
---------
    * *String*

listCredentials: Get a list of all internal users and their credentials on this system.
=======================================================================================
``systems.listCredentials(systemId=<SYSTEMID>, limit=250, offset=0)``

Keyword Args:
-------------
    * **systemId**: The id of the system. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *A single StoredCredential object*

updateCredentials: Add or update a user's credential on a system. This applies both to data and, if applicable, login credenitals.
==================================================================================================================================
``systems.updateCredentials(body=<BODY>, systemId=<SYSTEMID>)``

Keyword Args:
-------------
    * **systemId**: The id of the system. (string)
    * **body**: The description of the internal user credential to add or update. (JSON, UserCredential)


**UserCredential schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/UserCredential.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
      "properties": {
        "credential": {
          "description": "The credential used to authenticate to the remote system. Depending on the authentication protocol of the remote system, this could be an OAuth Token, X.509 certificate, Kerberose token, or an private key..",
          "type": "string"
        },
        "internalUsername": {
          "description": "The username of the internal user associated with this credential.",
          "type": "string"
        },
        "password": {
          "description": "The password on the remote system used to authenticate.",
          "type": "string"
        },
        "privateKey": {
          "description": "The public ssh key used to authenticate to the remote system..",
          "type": "string"
        },
        "publicKey": {
          "description": "The public ssh key used to authenticate to the remote system.",
          "type": "string"
        },
        "server": {
          "description": "The server from which a credential may be obtained.",
          "type": "UserCredentialServer"
        },
        "type": {
          "description": "The authentication type.",
          "enum": [
            "LOCAL",
            "PAM",
            "PASSWORD",
            "SSHKEYS",
            "TOKEN",
            "X509"
          ],
          "type": "string"
        },
        "username": {
          "description": "The local username on the remote system used to authenticate.",
          "type": "string"
        }
      },
      "required": [
        "type"
      ],
      "title": "AgavePy UserCredential schema",
      "type": "object"
    }

Response:
---------
    * *String*

deleteCredentialsForInternalUser: Deletes all credentials registered to a system.
=================================================================================
``systems.deleteCredentialsForInternalUser(internalUsername=<INTERNALUSERNAME>, systemId=<SYSTEMID>)``

Keyword Args:
-------------
    * **systemId**: The id of the system. (string)
    * **internalUsername**: The username of a internal user on this system. (string)


Response:
---------
    * *String*

listCredentialsForInternalUser: Get a list of all internal users and their credentials on this system.
======================================================================================================
``systems.listCredentialsForInternalUser(internalUsername=<INTERNALUSERNAME>, systemId=<SYSTEMID>, limit=250, offset=0)``

Keyword Args:
-------------
    * **systemId**: The id of the system. (string)
    * **internalUsername**: The username of a internal user on this system. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *A single StoredCredential object*

updateCredentialsForInternalUser: Add or update a user's credentials on a system.
=================================================================================
``systems.updateCredentialsForInternalUser(body=<BODY>, internalUsername=<INTERNALUSERNAME>, systemId=<SYSTEMID>)``

Keyword Args:
-------------
    * **systemId**: The id of the system. (string)
    * **internalUsername**: The username of a internal user on this system. (string)
    * **body**: The description of the internal user credential to add or update. (JSON, UserCredential)


**UserCredential schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/UserCredential.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
      "properties": {
        "credential": {
          "description": "The credential used to authenticate to the remote system. Depending on the authentication protocol of the remote system, this could be an OAuth Token, X.509 certificate, Kerberose token, or an private key..",
          "type": "string"
        },
        "internalUsername": {
          "description": "The username of the internal user associated with this credential.",
          "type": "string"
        },
        "password": {
          "description": "The password on the remote system used to authenticate.",
          "type": "string"
        },
        "privateKey": {
          "description": "The public ssh key used to authenticate to the remote system..",
          "type": "string"
        },
        "publicKey": {
          "description": "The public ssh key used to authenticate to the remote system.",
          "type": "string"
        },
        "server": {
          "description": "The server from which a credential may be obtained.",
          "type": "UserCredentialServer"
        },
        "type": {
          "description": "The authentication type.",
          "enum": [
            "LOCAL",
            "PAM",
            "PASSWORD",
            "SSHKEYS",
            "TOKEN",
            "X509"
          ],
          "type": "string"
        },
        "username": {
          "description": "The local username on the remote system used to authenticate.",
          "type": "string"
        }
      },
      "required": [
        "type"
      ],
      "title": "AgavePy UserCredential schema",
      "type": "object"
    }

Response:
---------
    * *String*

deleteCredentialsForInternalUserByType: Deletes the internal user credentials for the given credential type on a system.
========================================================================================================================
``systems.deleteCredentialsForInternalUserByType(credentialType=<CREDENTIALTYPE>, internalUsername=<INTERNALUSERNAME>, systemId=<SYSTEMID>)``

Keyword Args:
-------------
    * **systemId**: The id of the system. (string)
    * **internalUsername**: The username of a internal user on this system. (string)
    * **credentialType**: The configuration type to which to apply this credential. (string)


Response:
---------
    * *String*

listCredentialsForInternalUserByType: Get the internal user credential of the given type on the system.
=======================================================================================================
``systems.listCredentialsForInternalUserByType(credentialType=<CREDENTIALTYPE>, internalUsername=<INTERNALUSERNAME>, systemId=<SYSTEMID>, limit=250, offset=0)``

Keyword Args:
-------------
    * **systemId**: The id of the system. (string)
    * **internalUsername**: The username of a internal user on this system. (string)
    * **credentialType**: The configuration type to which to apply this credential. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *A single StoredCredential object*

updateCredentialsForInternalUserByType: Add or update a credential of the given type on a system.
=================================================================================================
``systems.updateCredentialsForInternalUserByType(body=<BODY>, credentialType=<CREDENTIALTYPE>, internalUsername=<INTERNALUSERNAME>, systemId=<SYSTEMID>)``

Keyword Args:
-------------
    * **systemId**: The id of the system. (string)
    * **internalUsername**: The username of a internal user on this system. (string)
    * **credentialType**: The configuration type to which to apply this credential. (string)
    * **body**: The description of the internal user credential to add or update. (JSON, UserCredential)


**UserCredential schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/UserCredential.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
      "properties": {
        "credential": {
          "description": "The credential used to authenticate to the remote system. Depending on the authentication protocol of the remote system, this could be an OAuth Token, X.509 certificate, Kerberose token, or an private key..",
          "type": "string"
        },
        "internalUsername": {
          "description": "The username of the internal user associated with this credential.",
          "type": "string"
        },
        "password": {
          "description": "The password on the remote system used to authenticate.",
          "type": "string"
        },
        "privateKey": {
          "description": "The public ssh key used to authenticate to the remote system..",
          "type": "string"
        },
        "publicKey": {
          "description": "The public ssh key used to authenticate to the remote system.",
          "type": "string"
        },
        "server": {
          "description": "The server from which a credential may be obtained.",
          "type": "UserCredentialServer"
        },
        "type": {
          "description": "The authentication type.",
          "enum": [
            "LOCAL",
            "PAM",
            "PASSWORD",
            "SSHKEYS",
            "TOKEN",
            "X509"
          ],
          "type": "string"
        },
        "username": {
          "description": "The local username on the remote system used to authenticate.",
          "type": "string"
        }
      },
      "required": [
        "type"
      ],
      "title": "AgavePy UserCredential schema",
      "type": "object"
    }

Response:
---------
    * *String*

