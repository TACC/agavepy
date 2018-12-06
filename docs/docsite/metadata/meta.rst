********
Metadata
********

Summary: Create and manage metadata

addMetadata: Update or Add new Metadata.
========================================
``agavepy.meta.addMetadata(body)``

Parameters:
-----------
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

**Metadata schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/Metadata.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "associationIds": {
          "description": "UUIDs of associated Agave entities, including the Data to which this Metadata belongs.", 
          "type": "array"
        }, 
        "created": {
          "description": "A timestamp indicating when this Metadata was created in the metadata store.", 
          "type": "string"
        }, 
        "internalUsername": {
          "description": "The name of the Internal User, if any, who owns this metadata.", 
          "type": "string"
        }, 
        "lastUpdated": {
          "description": "A timestamp indicating when this Metadata was last updated in the metadata store.", 
          "type": "string"
        }, 
        "name": {
          "description": "The name of this metadata", 
          "type": "string"
        }, 
        "owner": {
          "description": "The API user who owns this Metadata.", 
          "type": "string"
        }, 
        "uuid": {
          "description": "The UUID for this Metadata.", 
          "type": "string"
        }, 
        "value": {
          "description": "A free text or JSON string containing the metadata stored for the given associationIds", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy Metadata schema", 
      "type": "object"
    }

listMetadata: List and/or search metadata.
==========================================
``agavepy.meta.listMetadata(limit=250, offset=0, privileged=True, q=None)``

Parameters:
-----------
    * **q**: The query to perform. Traditional MongoDB queries are supported (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)
    * **privileged**: If false, implicit permissions are ignored and only records to which the user has explicit permissions are returned (boolean)


Response:
---------
    * *Array of MetadataResponse objects*

deleteMetadata: Remove Metadata from the system.
================================================
``agavepy.meta.deleteMetadata(uuid)``

Parameters:
-----------
    * **uuid**: The uuid of the metadata item (string)


Response:
---------
    * *A single EmptyMetadata object*

**EmptyMetadata schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/EmptyMetadata.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {}, 
      "required": [], 
      "title": "AgavePy EmptyMetadata schema", 
      "type": "object"
    }

getMetadata: Retrieve Metadata.
===============================
``agavepy.meta.getMetadata(uuid, limit=250, offset=0)``

Parameters:
-----------
    * **uuid**: The uuid of the metadata item (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *A single Metadata object*

**Metadata schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/Metadata.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "associationIds": {
          "description": "UUIDs of associated Agave entities, including the Data to which this Metadata belongs.", 
          "type": "array"
        }, 
        "created": {
          "description": "A timestamp indicating when this Metadata was created in the metadata store.", 
          "type": "string"
        }, 
        "internalUsername": {
          "description": "The name of the Internal User, if any, who owns this metadata.", 
          "type": "string"
        }, 
        "lastUpdated": {
          "description": "A timestamp indicating when this Metadata was last updated in the metadata store.", 
          "type": "string"
        }, 
        "name": {
          "description": "The name of this metadata", 
          "type": "string"
        }, 
        "owner": {
          "description": "The API user who owns this Metadata.", 
          "type": "string"
        }, 
        "uuid": {
          "description": "The UUID for this Metadata.", 
          "type": "string"
        }, 
        "value": {
          "description": "A free text or JSON string containing the metadata stored for the given associationIds", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy Metadata schema", 
      "type": "object"
    }

updateMetadata: Update or Add new Metadata.
===========================================
``agavepy.meta.updateMetadata(body, uuid)``

Parameters:
-----------
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

**Metadata schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/Metadata.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "associationIds": {
          "description": "UUIDs of associated Agave entities, including the Data to which this Metadata belongs.", 
          "type": "array"
        }, 
        "created": {
          "description": "A timestamp indicating when this Metadata was created in the metadata store.", 
          "type": "string"
        }, 
        "internalUsername": {
          "description": "The name of the Internal User, if any, who owns this metadata.", 
          "type": "string"
        }, 
        "lastUpdated": {
          "description": "A timestamp indicating when this Metadata was last updated in the metadata store.", 
          "type": "string"
        }, 
        "name": {
          "description": "The name of this metadata", 
          "type": "string"
        }, 
        "owner": {
          "description": "The API user who owns this Metadata.", 
          "type": "string"
        }, 
        "uuid": {
          "description": "The UUID for this Metadata.", 
          "type": "string"
        }, 
        "value": {
          "description": "A free text or JSON string containing the metadata stored for the given associationIds", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy Metadata schema", 
      "type": "object"
    }

addSchema: Add a new Metadata Schema.
=====================================
``agavepy.meta.addSchema(body)``

Parameters:
-----------
    * **body**: A valid JSON Schema object (JSON, string)


Response:
---------
    * *A single MetadataSchema object*

**MetadataSchema schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/MetadataSchema.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "created": {
          "description": "A timestamp indicating when this Metadata was created in the metadata schema store.", 
          "type": "string"
        }, 
        "internalUsername": {
          "description": "The name of the Internal User, if any, who owns this schema.", 
          "type": "string"
        }, 
        "lastUpdated": {
          "description": "A timestamp indicating when this Metadata was last updated in the metadata schema store.", 
          "type": "string"
        }, 
        "owner": {
          "description": "The API user who owns this Schema.", 
          "type": "string"
        }, 
        "schema": {
          "description": "A JSON Schema", 
          "type": "string"
        }, 
        "uuid": {
          "description": "The UUID for this Schema.", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy MetadataSchema schema", 
      "type": "object"
    }

searchSchema: Retrieve Metadata Schemata.
=========================================
``agavepy.meta.searchSchema(uuid, limit=250, offset=0)``

Parameters:
-----------
    * **uuid**: The uuid of the metadata schema item (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *A single MetadataSchema object*

**MetadataSchema schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/MetadataSchema.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "created": {
          "description": "A timestamp indicating when this Metadata was created in the metadata schema store.", 
          "type": "string"
        }, 
        "internalUsername": {
          "description": "The name of the Internal User, if any, who owns this schema.", 
          "type": "string"
        }, 
        "lastUpdated": {
          "description": "A timestamp indicating when this Metadata was last updated in the metadata schema store.", 
          "type": "string"
        }, 
        "owner": {
          "description": "The API user who owns this Schema.", 
          "type": "string"
        }, 
        "schema": {
          "description": "A JSON Schema", 
          "type": "string"
        }, 
        "uuid": {
          "description": "The UUID for this Schema.", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy MetadataSchema schema", 
      "type": "object"
    }

deleteSchema: Remove Metadata Schema from the system.
=====================================================
``agavepy.meta.deleteSchema(uuid)``

Parameters:
-----------
    * **uuid**: The uuid of the metadata schema item (string)


Response:
---------
    * *A single EmptyMetadata object*

**EmptyMetadata schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/EmptyMetadata.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {}, 
      "required": [], 
      "title": "AgavePy EmptyMetadata schema", 
      "type": "object"
    }

getSchema: Retrieve Metadata Schemata.
======================================
``agavepy.meta.getSchema(uuid, limit=250, offset=0)``

Parameters:
-----------
    * **uuid**: The uuid of the metadata schema item (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *A single MetadataSchema object*

**MetadataSchema schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/MetadataSchema.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "created": {
          "description": "A timestamp indicating when this Metadata was created in the metadata schema store.", 
          "type": "string"
        }, 
        "internalUsername": {
          "description": "The name of the Internal User, if any, who owns this schema.", 
          "type": "string"
        }, 
        "lastUpdated": {
          "description": "A timestamp indicating when this Metadata was last updated in the metadata schema store.", 
          "type": "string"
        }, 
        "owner": {
          "description": "The API user who owns this Schema.", 
          "type": "string"
        }, 
        "schema": {
          "description": "A JSON Schema", 
          "type": "string"
        }, 
        "uuid": {
          "description": "The UUID for this Schema.", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy MetadataSchema schema", 
      "type": "object"
    }

updateSchema: Update or Add a new Metadata Schema.
==================================================
``agavepy.meta.updateSchema(body, uuid)``

Parameters:
-----------
    * **uuid**: The uuid of the metadata schema item (string)
    * **body**: A valid JSON Schema object (JSON, string)


Response:
---------
    * *A single MetadataSchema object*

**MetadataSchema schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/MetadataSchema.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "created": {
          "description": "A timestamp indicating when this Metadata was created in the metadata schema store.", 
          "type": "string"
        }, 
        "internalUsername": {
          "description": "The name of the Internal User, if any, who owns this schema.", 
          "type": "string"
        }, 
        "lastUpdated": {
          "description": "A timestamp indicating when this Metadata was last updated in the metadata schema store.", 
          "type": "string"
        }, 
        "owner": {
          "description": "The API user who owns this Schema.", 
          "type": "string"
        }, 
        "schema": {
          "description": "A JSON Schema", 
          "type": "string"
        }, 
        "uuid": {
          "description": "The UUID for this Schema.", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy MetadataSchema schema", 
      "type": "object"
    }

deleteMetadataPermission: Deletes all permissions on the given metadata.
========================================================================
``agavepy.meta.deleteMetadataPermission(uuid)``

Parameters:
-----------
    * **uuid**: The uuid of the metadata item (string)


Response:
---------
    * *A single EmptyMetadata object*

**EmptyMetadata schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/EmptyMetadata.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {}, 
      "required": [], 
      "title": "AgavePy EmptyMetadata schema", 
      "type": "object"
    }

listMetadataPermissions: Get the permission ACL for this metadata.
==================================================================
``agavepy.meta.listMetadataPermissions(uuid, limit=250, offset=0)``

Parameters:
-----------
    * **uuid**: The uuid of the metadata item (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Array of Permission objects*

**Permission schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/Permission.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "permission": {
          "description": "", 
          "type": "ACL"
        }, 
        "username": {
          "description": "Username associate with this permission", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy Permission schema", 
      "type": "object"
    }

updateMetadataPermissions: Add or update a user's permission for the given metadata.
====================================================================================
``agavepy.meta.updateMetadataPermissions(body, uuid)``

Parameters:
-----------
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

**Permission schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/Permission.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "permission": {
          "description": "", 
          "type": "ACL"
        }, 
        "username": {
          "description": "Username associate with this permission", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy Permission schema", 
      "type": "object"
    }

deleteMetadataPermissionsForUser: Deletes all permissions on the given metadata.
================================================================================
``agavepy.meta.deleteMetadataPermissionsForUser(username, uuid)``

Parameters:
-----------
    * **uuid**: The uuid of the metadata item (string)
    * **username**: The username of the permission owner (string)


Response:
---------
    * *A single EmptyMetadata object*

**EmptyMetadata schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/EmptyMetadata.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {}, 
      "required": [], 
      "title": "AgavePy EmptyMetadata schema", 
      "type": "object"
    }

listMetadataPermissionsForUser: Get the permission ACL for this metadata.
=========================================================================
``agavepy.meta.listMetadataPermissionsForUser(username, uuid)``

Parameters:
-----------
    * **uuid**: The uuid of the metadata item (string)
    * **username**: The username of the permission owner (string)


Response:
---------
    * *A single Permission object*

**Permission schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/Permission.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "permission": {
          "description": "", 
          "type": "ACL"
        }, 
        "username": {
          "description": "Username associate with this permission", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy Permission schema", 
      "type": "object"
    }

updateMetadataPermissionsForUser: Add or update a user's permission for the given metadata.
===========================================================================================
``agavepy.meta.updateMetadataPermissionsForUser(body, username, uuid)``

Parameters:
-----------
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

**Permission schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/Permission.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "permission": {
          "description": "", 
          "type": "ACL"
        }, 
        "username": {
          "description": "Username associate with this permission", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy Permission schema", 
      "type": "object"
    }

deleteSchemaPermissions: Deletes all permissions on the given schema.
=====================================================================
``agavepy.meta.deleteSchemaPermissions(uuid)``

Parameters:
-----------
    * **uuid**: The uuid of the metadata schema item (string)


Response:
---------
    * *A single EmptyMetadata object*

**EmptyMetadata schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/EmptyMetadata.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {}, 
      "required": [], 
      "title": "AgavePy EmptyMetadata schema", 
      "type": "object"
    }

listSchemaPermissions: Get the permission ACL for this schema.
==============================================================
``agavepy.meta.listSchemaPermissions(uuid, limit=250, offset=0)``

Parameters:
-----------
    * **uuid**: The uuid of the metadata schema item (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Array of Permission objects*

**Permission schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/Permission.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "permission": {
          "description": "", 
          "type": "ACL"
        }, 
        "username": {
          "description": "Username associate with this permission", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy Permission schema", 
      "type": "object"
    }

updateSchemaPermissions: Add or update a user's permission for the given schema.
================================================================================
``agavepy.meta.updateSchemaPermissions(body, uuid)``

Parameters:
-----------
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

**Permission schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/Permission.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "permission": {
          "description": "", 
          "type": "ACL"
        }, 
        "username": {
          "description": "Username associate with this permission", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy Permission schema", 
      "type": "object"
    }

deleteSchemaPermissionsForUser: Deletes all permissions on the given metadata.
==============================================================================
``agavepy.meta.deleteSchemaPermissionsForUser(username, uuid)``

Parameters:
-----------
    * **uuid**: The uuid of the metadata schema item (string)
    * **username**: The username of the permission owner (string)


Response:
---------
    * *A single EmptyMetadata object*

**EmptyMetadata schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/EmptyMetadata.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {}, 
      "required": [], 
      "title": "AgavePy EmptyMetadata schema", 
      "type": "object"
    }

listSchemaPermissionsForUser: Get the permission ACL for this schema.
=====================================================================
``agavepy.meta.listSchemaPermissionsForUser(username, uuid)``

Parameters:
-----------
    * **uuid**: The uuid of the metadata schema item (string)
    * **username**: The username of the permission owner (string)


Response:
---------
    * *A single Permission object*

**Permission schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/Permission.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "permission": {
          "description": "", 
          "type": "ACL"
        }, 
        "username": {
          "description": "Username associate with this permission", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy Permission schema", 
      "type": "object"
    }

updateSchemaPermissionsForUser: Add or update a user's permission for the given metadata schema.
================================================================================================
``agavepy.meta.updateSchemaPermissionsForUser(body, username, uuid)``

Parameters:
-----------
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

**Permission schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/Permission.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "permission": {
          "description": "", 
          "type": "ACL"
        }, 
        "username": {
          "description": "Username associate with this permission", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy Permission schema", 
      "type": "object"
    }

