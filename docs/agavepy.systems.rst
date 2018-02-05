***************
agavepy.systems
***************

Summary: Register and manage systems

list
====
``agavepy.systems.list(default=None, limit=250, offset=0, public=None, type=None)``

Show all systems available to the user.

Parameters:
-----------
    * **type**: The type of system to return (string)
    * **default**: Should only default systems be returned (boolean)
    * **public**: Should only publicly available systems be returned (boolean)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Coming soon*

add
===
``agavepy.systems.add(body)``

Add or update a system.

Parameters:
-----------
    * **body**: The description of the system to add or update. (JSON, SystemRequest)


**SystemRequest:**

.. code-block:: javascript

    {
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
        "scheduler", 
        "name", 
        "queues", 
        "storage", 
        "executionType", 
        "login", 
        "type"
      ], 
      "title": "SystemRequest", 
      "type": "object"
    }

Response:
---------
    * *Coming soon*

get
===
``agavepy.systems.get(systemId)``

Find information about an individual system.

Parameters:
-----------
    * **systemId**: The unique id of the system (string)


Response:
---------
    * *Coming soon*

update
======
``agavepy.systems.update(body, systemId)``

Find information about an individual system.

Parameters:
-----------
    * **systemId**: The unique id of the system (string)
    * **body**: The description of the system to update. (JSON, SystemRequest)


**SystemRequest:**

.. code-block:: javascript

    {
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
        "scheduler", 
        "name", 
        "queues", 
        "storage", 
        "executionType", 
        "login", 
        "type"
      ], 
      "title": "SystemRequest", 
      "type": "object"
    }

Response:
---------
    * *Coming soon*

manage
======
``agavepy.systems.manage(body, systemId)``

Perform a management action on the system.

Parameters:
-----------
    * **systemId**: The unique id of the system (string)
    * **body**: The description of the system to update. (JSON, SystemOperationRequest)


**SystemOperationRequest:**

.. code-block:: javascript

    {
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
      "title": "SystemOperationRequest", 
      "type": "object"
    }

Response:
---------
    * *Coming soon*

delete
======
``agavepy.systems.delete(systemId)``

Delete a system.

Parameters:
-----------
    * **systemId**: The unique id of the system (string)


Response:
---------
    * *Coming soon*

listRoles
=========
``agavepy.systems.listRoles(systemId, limit=250, offset=0)``

Get a list of all users and their roles on this system.

Parameters:
-----------
    * **systemId**: The id of the system. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Coming soon*

updateRole
==========
``agavepy.systems.updateRole(body, systemId)``

Add or update a user's role on a system.

Parameters:
-----------
    * **systemId**: The id of the system. (string)
    * **body**: The role to update. (JSON, SystemRole)


**SystemRole:**

.. code-block:: javascript

    {
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
      "title": "SystemRole", 
      "type": "object"
    }

Response:
---------
    * *Coming soon*

deleteRoles
===========
``agavepy.systems.deleteRoles(systemId)``

Deletes all roles on a system.

Parameters:
-----------
    * **systemId**: The id of the system. (string)


Response:
---------
    * *Coming soon*

getRoleForUser
==============
``agavepy.systems.getRoleForUser(systemId, username, limit=250, offset=0)``

Get a specific user's roles on this system.

Parameters:
-----------
    * **systemId**: The id of the system. (string)
    * **username**: The username of the user about whose role you are inquiring. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Coming soon*

updateRoleForUser
=================
``agavepy.systems.updateRoleForUser(body, systemId, username)``

Add or update a user's role on a system.

Parameters:
-----------
    * **systemId**: The id of the system. (string)
    * **username**: The username of the api user associated with the role (string)
    * **body**: The role to update. (JSON, SystemRole)


**SystemRole:**

.. code-block:: javascript

    {
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
      "title": "SystemRole", 
      "type": "object"
    }

Response:
---------
    * *Coming soon*

deleteRoleForUser
=================
``agavepy.systems.deleteRoleForUser(systemId, username)``

Deletes all roles on a system.

Parameters:
-----------
    * **systemId**: The id of the system. (string)
    * **username**: The username of the api user associated with the role (string)


Response:
---------
    * *Coming soon*

listCredentials
===============
``agavepy.systems.listCredentials(systemId, limit=250, offset=0)``

Get a list of all internal users and their credentials on this system.

Parameters:
-----------
    * **systemId**: The id of the system. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Coming soon*

updateCredentials
=================
``agavepy.systems.updateCredentials(body, systemId)``

Add or update a user's credential on a system. This applies both to data and, if applicable, login credenitals.

Parameters:
-----------
    * **systemId**: The id of the system. (string)
    * **body**: The description of the internal user credential to add or update. (JSON, UserCredential)


**UserCredential:**

.. code-block:: javascript

    {
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
      "title": "UserCredential", 
      "type": "object"
    }

Response:
---------
    * *Coming soon*

deleteCredentials
=================
``agavepy.systems.deleteCredentials(systemId)``

Deletes all credentials registered to a system.

Parameters:
-----------
    * **systemId**: The id of the system. (string)


Response:
---------
    * *Coming soon*

listCredentialsForInternalUser
==============================
``agavepy.systems.listCredentialsForInternalUser(internalUsername, systemId, limit=250, offset=0)``

Get a list of all internal users and their credentials on this system.

Parameters:
-----------
    * **systemId**: The id of the system. (string)
    * **internalUsername**: The username of a internal user on this system. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Coming soon*

updateCredentialsForInternalUser
================================
``agavepy.systems.updateCredentialsForInternalUser(body, internalUsername, systemId)``

Add or update a user's credentials on a system.

Parameters:
-----------
    * **systemId**: The id of the system. (string)
    * **internalUsername**: The username of a internal user on this system. (string)
    * **body**: The description of the internal user credential to add or update. (JSON, UserCredential)


**UserCredential:**

.. code-block:: javascript

    {
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
      "title": "UserCredential", 
      "type": "object"
    }

Response:
---------
    * *Coming soon*

deleteCredentialsForInternalUser
================================
``agavepy.systems.deleteCredentialsForInternalUser(internalUsername, systemId)``

Deletes all credentials registered to a system.

Parameters:
-----------
    * **systemId**: The id of the system. (string)
    * **internalUsername**: The username of a internal user on this system. (string)


Response:
---------
    * *Coming soon*

listCredentialsForInternalUserByType
====================================
``agavepy.systems.listCredentialsForInternalUserByType(credentialType, internalUsername, systemId, limit=250, offset=0)``

Get the internal user credential of the given type on the system.

Parameters:
-----------
    * **systemId**: The id of the system. (string)
    * **internalUsername**: The username of a internal user on this system. (string)
    * **credentialType**: The configuration type to which to apply this credential. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Coming soon*

updateCredentialsForInternalUserByType
======================================
``agavepy.systems.updateCredentialsForInternalUserByType(body, credentialType, internalUsername, systemId)``

Add or update a credential of the given type on a system.

Parameters:
-----------
    * **systemId**: The id of the system. (string)
    * **internalUsername**: The username of a internal user on this system. (string)
    * **credentialType**: The configuration type to which to apply this credential. (string)
    * **body**: The description of the internal user credential to add or update. (JSON, UserCredential)


**UserCredential:**

.. code-block:: javascript

    {
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
      "title": "UserCredential", 
      "type": "object"
    }

Response:
---------
    * *Coming soon*

deleteCredentialsForInternalUserByType
======================================
``agavepy.systems.deleteCredentialsForInternalUserByType(credentialType, internalUsername, systemId)``

Deletes the internal user credentials for the given credential type on a system.

Parameters:
-----------
    * **systemId**: The id of the system. (string)
    * **internalUsername**: The username of a internal user on this system. (string)
    * **credentialType**: The configuration type to which to apply this credential. (string)


Response:
---------
    * *Coming soon*

