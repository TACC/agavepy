*****
admin
*****

Summary: Tenant admin services.

addAccount: Register a service account.
=======================================
``admin.addAccount(body=<BODY>)``

Keyword Args:
-------------
    * **body**: The description of the service account to add. (JSON, ServiceAccount)


**ServiceAccount schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/ServiceAccount.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
      "properties": {
        "id": {
          "description": "The unique id of the service account.",
          "type": "string"
        },
        "password": {
          "description": "The password for the service account.",
          "type": "string"
        },
        "roles": {
          "description": "roles occupied by service account.",
          "type": "array"
        }
      },
      "required": [],
      "title": "AgavePy ServiceAccount schema",
      "type": "object"
    }

Response:
---------
    * *A single ServiceAccount object*

listAccounts: List service accounts
===================================
``admin.listAccounts(limit=250, offset=0)``

Keyword Args:
-------------
    * **limit**: The max number of results. (integer, optional)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer, optional)


Response:
---------
    * *Array of ServiceAccountSummary objects*

deleteAccount: Delete a specific service account.
=================================================
``admin.deleteAccount(accountId=<ACCOUNTID>)``

Keyword Args:
-------------
    * **accountId**: The id of the service account. (string)


Response:
---------
    * *A single String object*

getAccount: Retrieve details about a specific service account.
==============================================================
``admin.getAccount(accountId=<ACCOUNTID>)``

Keyword Args:
-------------
    * **accountId**: The id of the service account. (string)


Response:
---------
    * *A single ServiceAccount object*

updateAccount: Update a specific service account.
=================================================
``admin.updateAccount(accountId=<ACCOUNTID>, body=<BODY>)``

Keyword Args:
-------------
    * **accountId**: The id of the service account. (string)
    * **body**: The description of the service account to update. (JSON, ServiceAccount)


**ServiceAccount schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/ServiceAccount.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
      "properties": {
        "id": {
          "description": "The unique id of the service account.",
          "type": "string"
        },
        "password": {
          "description": "The password for the service account.",
          "type": "string"
        },
        "roles": {
          "description": "roles occupied by service account.",
          "type": "array"
        }
      },
      "required": [],
      "title": "AgavePy ServiceAccount schema",
      "type": "object"
    }

Response:
---------
    * *A single ServiceAccount object*

addRoleToAccount: Add a role to a service account.
==================================================
``admin.addRoleToAccount(accountId=<ACCOUNTID>, body=<BODY>)``

Keyword Args:
-------------
    * **accountId**: The id of the service account. (string)
    * **body**: The description of the role to add. (JSON, AddRoleToAccountRequest)


**AddRoleToAccountRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/AddRoleToAccountRequest.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
      "properties": {
        "role_id": {
          "description": "The id of the role to add to the service account.",
          "type": "string"
        }
      },
      "required": [],
      "title": "AgavePy AddRoleToAccountRequest schema",
      "type": "object"
    }

Response:
---------
    * *A single ServiceAccount object*

listAccountRoles: List the roles occupied by a service account.
===============================================================
``admin.listAccountRoles(accountId=<ACCOUNTID>)``

Keyword Args:
-------------
    * **accountId**: The id of the service account. (string)


Response:
---------
    * *A single ServiceAccount object*

deleteRoleFromAccount: Delete a role from the list of occupied roles of a service account.
==========================================================================================
``admin.deleteRoleFromAccount(accountId=<ACCOUNTID>, roleId=<ROLEID>)``

Keyword Args:
-------------
    * **accountId**: The id of the service account. (string)
    * **roleId**: The id of the role. (string)


Response:
---------
    * *A single String object*

addRole: Register a service role.
=================================
``admin.addRole(body=<BODY>)``

Keyword Args:
-------------
    * **body**: The description of the service role to add. (JSON, Role)


**Role schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/Role.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
      "properties": {
        "id": {
          "description": "The unique id of the role.",
          "type": "string"
        }
      },
      "required": [],
      "title": "AgavePy Role schema",
      "type": "object"
    }

Response:
---------
    * *A single RoleDetails object*

listRoles: List service roles.
==============================
``admin.listRoles(limit=250, offset=0)``

Keyword Args:
-------------
    * **limit**: The max number of results. (integer, optional)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer, optional)


Response:
---------
    * *Array of RoleSummary objects*

deleteRole: Delete a specific service role.
===========================================
``admin.deleteRole(roleId=<ROLEID>)``

Keyword Args:
-------------
    * **roleId**: The id of the service role. (string)


Response:
---------
    * *A single String object*

getRole: Retrieve details about a specific service role.
========================================================
``admin.getRole(roleId=<ROLEID>)``

Keyword Args:
-------------
    * **roleId**: The id of the service role. (string)


Response:
---------
    * *A single RoleDetails object*

addAccountToRole: Add a service account to a role.
==================================================
``admin.addAccountToRole(body=<BODY>, roleId=<ROLEID>)``

Keyword Args:
-------------
    * **body**: The description of the service account to add. (JSON, AddServiceAccountToRoleRequest)
    * **roleId**: The id of the service role. (string)


Response:
---------
    * *A single RoleDetails object*

listAccountsInRole: Get the service accounts that occupy a service role.
========================================================================
``admin.listAccountsInRole(roleId=<ROLEID>)``

Keyword Args:
-------------
    * **roleId**: The id of the service role. (string)


Response:
---------
    * *A single RoleDetails object*

deleteAccountFromRole: Delete a service from the list of accounts occupying a service role.
===========================================================================================
``admin.deleteAccountFromRole(accountId=<ACCOUNTID>, roleId=<ROLEID>)``

Keyword Args:
-------------
    * **accountId**: The id of the service account. (string)
    * **roleId**: The id of the service role. (string)


Response:
---------
    * *A single String object*

listClients: List clients.
==========================
``admin.listClients(limit=250, offset=0)``

Keyword Args:
-------------
    * **limit**: The max number of results. (integer, optional)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer, optional)


Response:
---------
    * *Array of Client objects*

addApi: Register an API.
========================
``admin.addApi(body=<BODY>)``

Keyword Args:
-------------
    * **body**: The description of the API to add. (JSON, ApiRequestBody)


**ApiRequestBody schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/ApiRequestBody.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
      "properties": {
        "api_name": {
          "description": "Name of the API, which will also be used to identify the API.",
          "type": "string"
        },
        "auth": {
          "description": "List of quth type per method from (none, oauth). Can also be single string for all methods.",
          "type": "array"
        },
        "context": {
          "description": "Root path (context) for the API, starting with a slash character.",
          "type": "string"
        },
        "methods": {
          "description": "List of allowed methods from (GET, POST, PUT, DELETE, HEAD).",
          "type": "array"
        },
        "roles": {
          "description": "List of required roles to subscribe to API (required when visibility is 'restricted')",
          "type": "array"
        },
        "url": {
          "description": "Fully qualified production URL for the backend service (should include http or https).",
          "type": "string"
        },
        "visibility": {
          "description": "Optionally set the visibility to 'public' or 'restricted' (default is public).",
          "type": "string"
        }
      },
      "required": [],
      "title": "AgavePy ApiRequestBody schema",
      "type": "object"
    }

Response:
---------
    * *A single Api object*

listApis: List APIs.
====================
``admin.listApis(limit=250, offset=0)``

Keyword Args:
-------------
    * **limit**: The max number of results. (integer, optional)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer, optional)


Response:
---------
    * *Array of ApiSummary objects*

deleteApi: Delete a specific API.
=================================
``admin.deleteApi(apiId=<APIID>)``

Keyword Args:
-------------
    * **apiId**: The id of the API. (string)


Response:
---------
    * *A single String object*

getApi: Retrieve details about a specific API.
==============================================
``admin.getApi(apiId=<APIID>)``

Keyword Args:
-------------
    * **apiId**: The id of the API. (string)


Response:
---------
    * *A single Api object*

updateApiStatus: Update a specific API.
=======================================
``admin.updateApiStatus(apiId=<APIID>, body=<BODY>)``

Keyword Args:
-------------
    * **apiId**: The id of the API. (string)
    * **body**: The new status for the API. (JSON, ApiStatus)


**ApiStatus schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/ApiStatus.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
      "properties": {
        "status": {
          "description": "Status of the API: one of (CREATED, PUBLISHED, RETIRED).",
          "type": "string"
        }
      },
      "required": [],
      "title": "AgavePy ApiStatus schema",
      "type": "object"
    }

Response:
---------
    * *A single Api object*

