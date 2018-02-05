************
agavepy.meta
************

Summary: Create and manage metadata

listMetadata
============
``agavepy.meta.listMetadata(limit=250, offset=0, privileged=True, q=None)``

List and/or search metadata.

Parameters:
-----------
    * **q**: The query to perform. Traditional MongoDB queries are supported (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)
    * **privileged**: If false, implicit permissions are ignored and only records to which the user has explicit permissions are returned (boolean)


Response:
---------
    * *Coming soon*

addMetadata
===========
``agavepy.meta.addMetadata(body)``

Update or Add new Metadata.

Parameters:
-----------
    * **body**: The metadata to add. (JSON, MetadataRequest)


**MetadataRequest:**

.. code-block:: javascript

    {
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
      "title": "MetadataRequest", 
      "type": "object"
    }

Response:
---------
    * *Coming soon*

getMetadata
===========
``agavepy.meta.getMetadata(uuid, limit=250, offset=0)``

Retrieve Metadata.

Parameters:
-----------
    * **uuid**: The uuid of the metadata item (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Coming soon*

updateMetadata
==============
``agavepy.meta.updateMetadata(body, uuid)``

Update or Add new Metadata.

Parameters:
-----------
    * **uuid**: The uuid of the metadata item (string)
    * **body**: The metadata to update. (JSON, MetadataRequest)


**MetadataRequest:**

.. code-block:: javascript

    {
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
      "title": "MetadataRequest", 
      "type": "object"
    }

Response:
---------
    * *Coming soon*

deleteMetadata
==============
``agavepy.meta.deleteMetadata(uuid)``

Remove Metadata from the system.

Parameters:
-----------
    * **uuid**: The uuid of the metadata item (string)


Response:
---------
    * *Coming soon*

searchSchema
============
``agavepy.meta.searchSchema(uuid, limit=250, offset=0)``

Retrieve Metadata Schemata.

Parameters:
-----------
    * **uuid**: The uuid of the metadata schema item (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Coming soon*

addSchema
=========
``agavepy.meta.addSchema(body)``

Add a new Metadata Schema.

Parameters:
-----------
    * **body**: A valid JSON Schema object (JSON, string)


Response:
---------
    * *Coming soon*

getSchema
=========
``agavepy.meta.getSchema(uuid, limit=250, offset=0)``

Retrieve Metadata Schemata.

Parameters:
-----------
    * **uuid**: The uuid of the metadata schema item (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Coming soon*

updateSchema
============
``agavepy.meta.updateSchema(body, uuid)``

Update or Add a new Metadata Schema.

Parameters:
-----------
    * **uuid**: The uuid of the metadata schema item (string)
    * **body**: A valid JSON Schema object (JSON, string)


Response:
---------
    * *Coming soon*

deleteSchema
============
``agavepy.meta.deleteSchema(uuid)``

Remove Metadata Schema from the system.

Parameters:
-----------
    * **uuid**: The uuid of the metadata schema item (string)


Response:
---------
    * *Coming soon*

listMetadataPermissions
=======================
``agavepy.meta.listMetadataPermissions(uuid, limit=250, offset=0)``

Get the permission ACL for this metadata.

Parameters:
-----------
    * **uuid**: The uuid of the metadata item (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Coming soon*

updateMetadataPermissions
=========================
``agavepy.meta.updateMetadataPermissions(body, uuid)``

Add or update a user's permission for the given metadata.

Parameters:
-----------
    * **uuid**: The uuid of the metadata item (string)
    * **body**: The metadata permission to update. (JSON, MetadataPermissionRequest)


**MetadataPermissionRequest:**

.. code-block:: javascript

    {
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
      "title": "MetadataPermissionRequest", 
      "type": "object"
    }

Response:
---------
    * *Coming soon*

deleteMetadataPermission
========================
``agavepy.meta.deleteMetadataPermission(uuid)``

Deletes all permissions on the given metadata.

Parameters:
-----------
    * **uuid**: The uuid of the metadata item (string)


Response:
---------
    * *Coming soon*

listMetadataPermissionsForUser
==============================
``agavepy.meta.listMetadataPermissionsForUser(username, uuid)``

Get the permission ACL for this metadata.

Parameters:
-----------
    * **uuid**: The uuid of the metadata item (string)
    * **username**: The username of the permission owner (string)


Response:
---------
    * *Coming soon*

updateMetadataPermissionsForUser
================================
``agavepy.meta.updateMetadataPermissionsForUser(body, username, uuid)``

Add or update a user's permission for the given metadata.

Parameters:
-----------
    * **uuid**: The uuid of the metadata item (string)
    * **username**: The username of the permission owner (string)
    * **body**: The metadata permission to update. (JSON, MetadataPermissionRequest)


**MetadataPermissionRequest:**

.. code-block:: javascript

    {
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
      "title": "MetadataPermissionRequest", 
      "type": "object"
    }

Response:
---------
    * *Coming soon*

deleteMetadataPermissionsForUser
================================
``agavepy.meta.deleteMetadataPermissionsForUser(username, uuid)``

Deletes all permissions on the given metadata.

Parameters:
-----------
    * **uuid**: The uuid of the metadata item (string)
    * **username**: The username of the permission owner (string)


Response:
---------
    * *Coming soon*

listSchemaPermissions
=====================
``agavepy.meta.listSchemaPermissions(uuid, limit=250, offset=0)``

Get the permission ACL for this schema.

Parameters:
-----------
    * **uuid**: The uuid of the metadata schema item (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Coming soon*

updateSchemaPermissions
=======================
``agavepy.meta.updateSchemaPermissions(body, uuid)``

Add or update a user's permission for the given schema.

Parameters:
-----------
    * **uuid**: The uuid of the metadata schema item (string)
    * **body**: The schema permission to update. (JSON, MetadataPermissionRequest)


**MetadataPermissionRequest:**

.. code-block:: javascript

    {
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
      "title": "MetadataPermissionRequest", 
      "type": "object"
    }

Response:
---------
    * *Coming soon*

deleteSchemaPermissions
=======================
``agavepy.meta.deleteSchemaPermissions(uuid)``

Deletes all permissions on the given schema.

Parameters:
-----------
    * **uuid**: The uuid of the metadata schema item (string)


Response:
---------
    * *Coming soon*

listSchemaPermissionsForUser
============================
``agavepy.meta.listSchemaPermissionsForUser(username, uuid)``

Get the permission ACL for this schema.

Parameters:
-----------
    * **uuid**: The uuid of the metadata schema item (string)
    * **username**: The username of the permission owner (string)


Response:
---------
    * *Coming soon*

updateSchemaPermissionsForUser
==============================
``agavepy.meta.updateSchemaPermissionsForUser(body, username, uuid)``

Add or update a user's permission for the given metadata schema.

Parameters:
-----------
    * **uuid**: The uuid of the metadata schema item (string)
    * **username**: The username of the permission owner (string)
    * **body**: The schema permission to update. (JSON, MetadataPermissionRequest)


**MetadataPermissionRequest:**

.. code-block:: javascript

    {
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
      "title": "MetadataPermissionRequest", 
      "type": "object"
    }

Response:
---------
    * *Coming soon*

deleteSchemaPermissionsForUser
==============================
``agavepy.meta.deleteSchemaPermissionsForUser(username, uuid)``

Deletes all permissions on the given metadata.

Parameters:
-----------
    * **uuid**: The uuid of the metadata schema item (string)
    * **username**: The username of the permission owner (string)


Response:
---------
    * *Coming soon*

