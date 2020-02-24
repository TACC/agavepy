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
    * **limit**: The max number of results. (integer, optional)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer, optional)
    * **privileged**: If false, implicit permissions are ignored and only records to which the user has explicit permissions are returned (boolean, optional)
    * **q**: The query to perform. Traditional MongoDB queries are supported (string, optional)


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
``meta.getMetadata(limit=250, offset=0, uuid=<UUID>)``

Keyword Args:
-------------
    * **limit**: The max number of results. (integer, optional)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer, optional)
    * **uuid**: The uuid of the metadata item (string)


Response:
---------
    * *A single Metadata object*

updateMetadata: Update or Add new Metadata.
===========================================
``meta.updateMetadata(body=<BODY>, uuid=<UUID>)``

Keyword Args:
-------------
    * **body**: The metadata to update. (JSON, MetadataRequest)
    * **uuid**: The uuid of the metadata item (string)


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
``meta.searchSchema(limit=250, offset=0, uuid=<UUID>)``

Keyword Args:
-------------
    * **limit**: The max number of results. (integer, optional)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer, optional)
    * **uuid**: The uuid of the metadata schema item (string)


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
``meta.getSchema(limit=250, offset=0, uuid=<UUID>)``

Keyword Args:
-------------
    * **limit**: The max number of results. (integer, optional)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer, optional)
    * **uuid**: The uuid of the metadata schema item (string)


Response:
---------
    * *A single MetadataSchema object*

updateSchema: Update or Add a new Metadata Schema.
==================================================
``meta.updateSchema(body=<BODY>, uuid=<UUID>)``

Keyword Args:
-------------
    * **body**: A valid JSON Schema object (JSON, string)
    * **uuid**: The uuid of the metadata schema item (string)


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
``meta.listMetadataPermissions(limit=250, offset=0, uuid=<UUID>)``

Keyword Args:
-------------
    * **limit**: The max number of results. (integer, optional)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer, optional)
    * **uuid**: The uuid of the metadata item (string)


Response:
---------
    * *Array of Permission objects*

updateMetadataPermissions: Add or update a user's permission for the given metadata.
====================================================================================
``meta.updateMetadataPermissions(body=<BODY>, uuid=<UUID>)``

Keyword Args:
-------------
    * **body**: The metadata permission to update. (JSON, MetadataPermissionRequest)
    * **uuid**: The uuid of the metadata item (string)


Response:
---------
    * *A single Permission object*

deleteMetadataPermissionsForUser: Deletes all permissions on the given metadata.
================================================================================
``meta.deleteMetadataPermissionsForUser(username=<USERNAME>, uuid=<UUID>)``

Keyword Args:
-------------
    * **username**: The username of the permission owner (string)
    * **uuid**: The uuid of the metadata item (string)


Response:
---------
    * *A single EmptyMetadata object*

listMetadataPermissionsForUser: Get the permission ACL for this metadata.
=========================================================================
``meta.listMetadataPermissionsForUser(username=<USERNAME>, uuid=<UUID>)``

Keyword Args:
-------------
    * **username**: The username of the permission owner (string)
    * **uuid**: The uuid of the metadata item (string)


Response:
---------
    * *A single Permission object*

updateMetadataPermissionsForUser: Add or update a user's permission for the given metadata.
===========================================================================================
``meta.updateMetadataPermissionsForUser(body=<BODY>, username=<USERNAME>, uuid=<UUID>)``

Keyword Args:
-------------
    * **body**: The metadata permission to update. (JSON, MetadataPermissionRequest)
    * **username**: The username of the permission owner (string)
    * **uuid**: The uuid of the metadata item (string)


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
``meta.listSchemaPermissions(limit=250, offset=0, uuid=<UUID>)``

Keyword Args:
-------------
    * **limit**: The max number of results. (integer, optional)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer, optional)
    * **uuid**: The uuid of the metadata schema item (string)


Response:
---------
    * *Array of Permission objects*

updateSchemaPermissions: Add or update a user's permission for the given schema.
================================================================================
``meta.updateSchemaPermissions(body=<BODY>, uuid=<UUID>)``

Keyword Args:
-------------
    * **body**: The schema permission to update. (JSON, MetadataPermissionRequest)
    * **uuid**: The uuid of the metadata schema item (string)


Response:
---------
    * *A single Permission object*

deleteSchemaPermissionsForUser: Deletes all permissions on the given metadata.
==============================================================================
``meta.deleteSchemaPermissionsForUser(username=<USERNAME>, uuid=<UUID>)``

Keyword Args:
-------------
    * **username**: The username of the permission owner (string)
    * **uuid**: The uuid of the metadata schema item (string)


Response:
---------
    * *A single EmptyMetadata object*

listSchemaPermissionsForUser: Get the permission ACL for this schema.
=====================================================================
``meta.listSchemaPermissionsForUser(username=<USERNAME>, uuid=<UUID>)``

Keyword Args:
-------------
    * **username**: The username of the permission owner (string)
    * **uuid**: The uuid of the metadata schema item (string)


Response:
---------
    * *A single Permission object*

updateSchemaPermissionsForUser: Add or update a user's permission for the given metadata schema.
================================================================================================
``meta.updateSchemaPermissionsForUser(body=<BODY>, username=<USERNAME>, uuid=<UUID>)``

Keyword Args:
-------------
    * **body**: The schema permission to update. (JSON, MetadataPermissionRequest)
    * **username**: The username of the permission owner (string)
    * **uuid**: The uuid of the metadata schema item (string)


Response:
---------
    * *A single Permission object*

