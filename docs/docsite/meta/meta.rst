****
meta
****

Summary: Create and manage metadata

addMetadata: Update or Add new Metadata.
========================================
``meta.addMetadata(body=<BODY>)``

Keyword Args:
-------------
    * **body**: The metadata to add. (JSON, MetadataRequest)


**MetadataRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/MetadataRequest.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
      "properties": {
        "associationIds": {
          "description": "UUIDs of associated Agave entities, including the Data to which this Metadata belongs.",
          "type": "array"
        },
        "name": {
          "description": "The name of this metadata",
          "type": "string"
        },
        "schemaId": {
          "description": "The UUID of the schema that should be used to validate this request.",
          "type": "string"
        },
        "value": {
          "description": "A free text or JSON string containing the metadata stored for the given associationIds",
          "type": "string"
        }
      },
      "required": [
        "name",
        "value"
      ],
      "title": "AgavePy MetadataRequest schema",
      "type": "object"
    }

Response:
---------
    * *A single Metadata object*

listMetadata: List and/or search metadata.
==========================================
``meta.listMetadata(limit=250, offset=0, privileged=True, q=None)``

Keyword Args:
-------------
    * **q**: The query to perform. Traditional MongoDB queries are supported (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)
    * **privileged**: If false, implicit permissions are ignored and only records to which the user has explicit permissions are returned (boolean)


Response:
---------
    * *Array of MetadataResponse objects*

deleteMetadata: Remove Metadata from the system.
================================================
``meta.deleteMetadata(uuid=<UUID>)``

Keyword Args:
-------------
    * **uuid**: The uuid of the metadata item (string)


Response:
---------
    * *A single EmptyMetadata object*

getMetadata: Retrieve Metadata.
===============================
``meta.getMetadata(uuid=<UUID>, limit=250, offset=0)``

Keyword Args:
-------------
    * **uuid**: The uuid of the metadata item (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *A single Metadata object*

updateMetadata: Update or Add new Metadata.
===========================================
``meta.updateMetadata(body=<BODY>, uuid=<UUID>)``

Keyword Args:
-------------
    * **uuid**: The uuid of the metadata item (string)
    * **body**: The metadata to update. (JSON, MetadataRequest)


**MetadataRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/MetadataRequest.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
      "properties": {
        "associationIds": {
          "description": "UUIDs of associated Agave entities, including the Data to which this Metadata belongs.",
          "type": "array"
        },
        "name": {
          "description": "The name of this metadata",
          "type": "string"
        },
        "schemaId": {
          "description": "The UUID of the schema that should be used to validate this request.",
          "type": "string"
        },
        "value": {
          "description": "A free text or JSON string containing the metadata stored for the given associationIds",
          "type": "string"
        }
      },
      "required": [
        "name",
        "value"
      ],
      "title": "AgavePy MetadataRequest schema",
      "type": "object"
    }

Response:
---------
    * *A single Metadata object*

addSchema: Add a new Metadata Schema.
=====================================
``meta.addSchema(body=<BODY>)``

Keyword Args:
-------------
    * **body**: A valid JSON Schema object (JSON, string)


Response:
---------
    * *A single MetadataSchema object*

searchSchema: Retrieve Metadata Schemata.
=========================================
``meta.searchSchema(uuid=<UUID>, limit=250, offset=0)``

Keyword Args:
-------------
    * **uuid**: The uuid of the metadata schema item (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *A single MetadataSchema object*

deleteSchema: Remove Metadata Schema from the system.
=====================================================
``meta.deleteSchema(uuid=<UUID>)``

Keyword Args:
-------------
    * **uuid**: The uuid of the metadata schema item (string)


Response:
---------
    * *A single EmptyMetadata object*

getSchema: Retrieve Metadata Schemata.
======================================
``meta.getSchema(uuid=<UUID>, limit=250, offset=0)``

Keyword Args:
-------------
    * **uuid**: The uuid of the metadata schema item (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *A single MetadataSchema object*

updateSchema: Update or Add a new Metadata Schema.
==================================================
``meta.updateSchema(body=<BODY>, uuid=<UUID>)``

Keyword Args:
-------------
    * **uuid**: The uuid of the metadata schema item (string)
    * **body**: A valid JSON Schema object (JSON, string)


Response:
---------
    * *A single MetadataSchema object*

deleteMetadataPermission: Deletes all permissions on the given metadata.
========================================================================
``meta.deleteMetadataPermission(uuid=<UUID>)``

Keyword Args:
-------------
    * **uuid**: The uuid of the metadata item (string)


Response:
---------
    * *A single EmptyMetadata object*

listMetadataPermissions: Get the permission ACL for this metadata.
==================================================================
``meta.listMetadataPermissions(uuid=<UUID>, limit=250, offset=0)``

Keyword Args:
-------------
    * **uuid**: The uuid of the metadata item (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Array of Permission objects*

updateMetadataPermissions: Add or update a user's permission for the given metadata.
====================================================================================
``meta.updateMetadataPermissions(body=<BODY>, uuid=<UUID>)``

Keyword Args:
-------------
    * **uuid**: The uuid of the metadata item (string)
    * **body**: The metadata permission to update. (JSON, MetadataPermissionRequest)


**MetadataPermissionRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/MetadataPermissionRequest.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
      "properties": {
        "permission": {
          "description": "The permission to set",
          "enum": [
            "READ",
            "WRITE",
            "READ_WRITE",
            "ALL",
            "NONE"
          ],
          "type": "string"
        },
        "username": {
          "description": "The username of the api user whose permission is to be set.",
          "type": "string"
        }
      },
      "required": [
        "username",
        "permission"
      ],
      "title": "AgavePy MetadataPermissionRequest schema",
      "type": "object"
    }

Response:
---------
    * *A single Permission object*

deleteMetadataPermissionsForUser: Deletes all permissions on the given metadata.
================================================================================
``meta.deleteMetadataPermissionsForUser(username=<USERNAME>, uuid=<UUID>)``

Keyword Args:
-------------
    * **uuid**: The uuid of the metadata item (string)
    * **username**: The username of the permission owner (string)


Response:
---------
    * *A single EmptyMetadata object*

listMetadataPermissionsForUser: Get the permission ACL for this metadata.
=========================================================================
``meta.listMetadataPermissionsForUser(username=<USERNAME>, uuid=<UUID>)``

Keyword Args:
-------------
    * **uuid**: The uuid of the metadata item (string)
    * **username**: The username of the permission owner (string)


Response:
---------
    * *A single Permission object*

updateMetadataPermissionsForUser: Add or update a user's permission for the given metadata.
===========================================================================================
``meta.updateMetadataPermissionsForUser(body=<BODY>, username=<USERNAME>, uuid=<UUID>)``

Keyword Args:
-------------
    * **uuid**: The uuid of the metadata item (string)
    * **username**: The username of the permission owner (string)
    * **body**: The metadata permission to update. (JSON, MetadataPermissionRequest)


**MetadataPermissionRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/MetadataPermissionRequest.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
      "properties": {
        "permission": {
          "description": "The permission to set",
          "enum": [
            "READ",
            "WRITE",
            "READ_WRITE",
            "ALL",
            "NONE"
          ],
          "type": "string"
        },
        "username": {
          "description": "The username of the api user whose permission is to be set.",
          "type": "string"
        }
      },
      "required": [
        "username",
        "permission"
      ],
      "title": "AgavePy MetadataPermissionRequest schema",
      "type": "object"
    }

Response:
---------
    * *A single Permission object*

deleteSchemaPermissions: Deletes all permissions on the given schema.
=====================================================================
``meta.deleteSchemaPermissions(uuid=<UUID>)``

Keyword Args:
-------------
    * **uuid**: The uuid of the metadata schema item (string)


Response:
---------
    * *A single EmptyMetadata object*

listSchemaPermissions: Get the permission ACL for this schema.
==============================================================
``meta.listSchemaPermissions(uuid=<UUID>, limit=250, offset=0)``

Keyword Args:
-------------
    * **uuid**: The uuid of the metadata schema item (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Array of Permission objects*

updateSchemaPermissions: Add or update a user's permission for the given schema.
================================================================================
``meta.updateSchemaPermissions(body=<BODY>, uuid=<UUID>)``

Keyword Args:
-------------
    * **uuid**: The uuid of the metadata schema item (string)
    * **body**: The schema permission to update. (JSON, MetadataPermissionRequest)


**MetadataPermissionRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/MetadataPermissionRequest.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
      "properties": {
        "permission": {
          "description": "The permission to set",
          "enum": [
            "READ",
            "WRITE",
            "READ_WRITE",
            "ALL",
            "NONE"
          ],
          "type": "string"
        },
        "username": {
          "description": "The username of the api user whose permission is to be set.",
          "type": "string"
        }
      },
      "required": [
        "username",
        "permission"
      ],
      "title": "AgavePy MetadataPermissionRequest schema",
      "type": "object"
    }

Response:
---------
    * *A single Permission object*

deleteSchemaPermissionsForUser: Deletes all permissions on the given metadata.
==============================================================================
``meta.deleteSchemaPermissionsForUser(username=<USERNAME>, uuid=<UUID>)``

Keyword Args:
-------------
    * **uuid**: The uuid of the metadata schema item (string)
    * **username**: The username of the permission owner (string)


Response:
---------
    * *A single EmptyMetadata object*

listSchemaPermissionsForUser: Get the permission ACL for this schema.
=====================================================================
``meta.listSchemaPermissionsForUser(username=<USERNAME>, uuid=<UUID>)``

Keyword Args:
-------------
    * **uuid**: The uuid of the metadata schema item (string)
    * **username**: The username of the permission owner (string)


Response:
---------
    * *A single Permission object*

updateSchemaPermissionsForUser: Add or update a user's permission for the given metadata schema.
================================================================================================
``meta.updateSchemaPermissionsForUser(body=<BODY>, username=<USERNAME>, uuid=<UUID>)``

Keyword Args:
-------------
    * **uuid**: The uuid of the metadata schema item (string)
    * **username**: The username of the permission owner (string)
    * **body**: The schema permission to update. (JSON, MetadataPermissionRequest)


**MetadataPermissionRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/MetadataPermissionRequest.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
      "properties": {
        "permission": {
          "description": "The permission to set",
          "enum": [
            "READ",
            "WRITE",
            "READ_WRITE",
            "ALL",
            "NONE"
          ],
          "type": "string"
        },
        "username": {
          "description": "The username of the api user whose permission is to be set.",
          "type": "string"
        }
      },
      "required": [
        "username",
        "permission"
      ],
      "title": "AgavePy MetadataPermissionRequest schema",
      "type": "object"
    }

Response:
---------
    * *A single Permission object*

