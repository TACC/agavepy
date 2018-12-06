***********************
Other methods available
***********************

Summary: Move and manage data

deleteFromDefaultSystem: Deletes a file or folder.
==================================================
``agavepy.files.deleteFromDefaultSystem(sourcefilePath)``

Parameters:
-----------
    * **sourcefilePath**: The path of the file relative to the user's default storage location. (string)


Response:
---------
    * *String*

downloadFromDefaultSystem: Download a file from the user's default storage location.
====================================================================================
``agavepy.files.downloadFromDefaultSystem(sourcefilePath)``

Parameters:
-----------
    * **sourcefilePath**: The path of the file relative to the user's default storage location. (string)


Response:
---------
    * *None*

importToDefaultSystem: Import a file via direct upload or importing from a url to the user's default storage location.
======================================================================================================================
``agavepy.files.importToDefaultSystem(sourcefilePath, callbackURL=None, fileName=None, fileToUpload=None, fileType=None, urlToIngest=None)``

Parameters:
-----------
    * **sourcefilePath**: The path of the file relative to the user's default storage location. (string)
    * **fileType**: The file format this file is in. Defaults to raw. This will be used in file transform operations. (string)
    * **callbackURL**: The URI to notify when the import is complete. This can be an email address or http URL. If a URL is given, a GET will be made to this address. URL templating is supported. Valid template values are: ${NAME}, ${SOURCE_FORMAT}, ${DEST_FORMAT}, ${STATUS} (string)
    * **fileName**: The name of the file after importing. If not specified, the uploaded file name will be used. (string)
    * **urlToIngest**: The URL to import the file from. This parameter is used if not file is uploaded with this post. (string)
    * **fileToUpload**: The file object to import. (void)


Response:
---------
    * *A single RemoteFile object*

**RemoteFile schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/RemoteFile.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "format": {
          "description": "The file type of the file.", 
          "type": "string"
        }, 
        "lastModified": {
          "description": "The date this file was last modified in ISO 8601 format.", 
          "type": "string"
        }, 
        "length": {
          "description": "The length of the file/folder.", 
          "type": "integer"
        }, 
        "mimeType": {
          "description": "The mime type of the file/folder. If unknown, it defaults to application/binary.", 
          "type": "string"
        }, 
        "name": {
          "description": "The name of the file/folder.", 
          "type": "string"
        }, 
        "path": {
          "description": "The absolute path to the file/folder.", 
          "type": "string"
        }, 
        "permissions": {
          "description": "The system permission of the invoking user on the file/folder.", 
          "type": "string"
        }, 
        "system": {
          "description": "The systemId of the system where this file lives.", 
          "type": "string"
        }, 
        "type": {
          "description": "Whether it is a file or folder.", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy RemoteFile schema", 
      "type": "object"
    }

manageOnDefaultSystem: Perform an action on a file or folder.
=============================================================
``agavepy.files.manageOnDefaultSystem(body, sourcefilePath)``

Parameters:
-----------
    * **sourcefilePath**: The path of the file relative to the user's default storage location. (string)
    * **body**: The operation to perform.  (JSON, FileOperationRequest)


**FileOperationRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/FileOperationRequest.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "action": {
          "description": "Action to perform on the file or folder.", 
          "enum": [
            "mkdir", 
            "rename", 
            "copy", 
            "move"
          ], 
          "type": "string"
        }, 
        "path": {
          "description": "Destination file or folder.", 
          "type": "string"
        }
      }, 
      "required": [
        "action"
      ], 
      "title": "AgavePy FileOperationRequest schema", 
      "type": "object"
    }

Response:
---------
    * *String*

delete: Deletes a file or folder.
=================================
``agavepy.files.delete(filePath, systemId)``

Parameters:
-----------
    * **systemId**: The unique id of the system on which the data resides. (string)
    * **filePath**: The path of the file relative to the user's default storage location. (string)


Response:
---------
    * *String*

download: Download a file from the user's default storage location.
===================================================================
``agavepy.files.download(filePath, systemId)``

Parameters:
-----------
    * **systemId**: The unique id of the system on which the data resides. (string)
    * **filePath**: The path of the file relative to the user's default storage location. (string)


Response:
---------
    * *None*

importData: Import a file via direct upload or importing from a url to the user's default storage location.
===========================================================================================================
``agavepy.files.importData(filePath, systemId, callbackURL=None, fileName=None, fileToUpload=None, fileType=None, notifications=[], urlToIngest=None)``

Parameters:
-----------
    * **systemId**: The unique id of the system on which the data resides. (string)
    * **filePath**: The path of the file relative to the user's default storage location. (string)
    * **fileType**: The file format this file is in. Defaults to raw. This will be used in file transform operations. (string)
    * **callbackURL**: The URI to notify when the import is complete. This can be an email address or http URL. If a URL is given, a GET will be made to this address. URL templating is supported. Valid template values are: ${NAME}, ${SOURCE_FORMAT}, ${DEST_FORMAT}, ${STATUS} (string)
    * **fileName**: The name of the file after importing. If not specified, the uploaded file name will be used. (string)
    * **urlToIngest**: The URL to import the file from. This parameter is used if not file is uploaded with this post. (string)
    * **fileToUpload**: The file object to import. (void)
    * **notifications**: A list of notification objects to apply to the transfer.  (FileNotificationRequest)


Response:
---------
    * *A single RemoteFile object*

**RemoteFile schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/RemoteFile.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "format": {
          "description": "The file type of the file.", 
          "type": "string"
        }, 
        "lastModified": {
          "description": "The date this file was last modified in ISO 8601 format.", 
          "type": "string"
        }, 
        "length": {
          "description": "The length of the file/folder.", 
          "type": "integer"
        }, 
        "mimeType": {
          "description": "The mime type of the file/folder. If unknown, it defaults to application/binary.", 
          "type": "string"
        }, 
        "name": {
          "description": "The name of the file/folder.", 
          "type": "string"
        }, 
        "path": {
          "description": "The absolute path to the file/folder.", 
          "type": "string"
        }, 
        "permissions": {
          "description": "The system permission of the invoking user on the file/folder.", 
          "type": "string"
        }, 
        "system": {
          "description": "The systemId of the system where this file lives.", 
          "type": "string"
        }, 
        "type": {
          "description": "Whether it is a file or folder.", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy RemoteFile schema", 
      "type": "object"
    }

manage: Perform an action on a file or folder.
==============================================
``agavepy.files.manage(body, filePath, systemId)``

Parameters:
-----------
    * **systemId**: The unique id of the system on which the data resides. (string)
    * **filePath**: The path of the file relative to the user's default storage location. (string)
    * **body**: The operation to perform.  (JSON, FileOperationRequest)


**FileOperationRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/FileOperationRequest.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "action": {
          "description": "Action to perform on the file or folder.", 
          "enum": [
            "mkdir", 
            "rename", 
            "copy", 
            "move"
          ], 
          "type": "string"
        }, 
        "path": {
          "description": "Destination file or folder.", 
          "type": "string"
        }
      }, 
      "required": [
        "action"
      ], 
      "title": "AgavePy FileOperationRequest schema", 
      "type": "object"
    }

Response:
---------
    * *String*

listOnDefaultSystem: Get a remote directory listing.
====================================================
``agavepy.files.listOnDefaultSystem(filePath, limit=250, offset=0)``

Parameters:
-----------
    * **filePath**: The path of the file relative to the user's default storage location. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Array of RemoteFile objects*

**RemoteFile schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/RemoteFile.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "format": {
          "description": "The file type of the file.", 
          "type": "string"
        }, 
        "lastModified": {
          "description": "The date this file was last modified in ISO 8601 format.", 
          "type": "string"
        }, 
        "length": {
          "description": "The length of the file/folder.", 
          "type": "integer"
        }, 
        "mimeType": {
          "description": "The mime type of the file/folder. If unknown, it defaults to application/binary.", 
          "type": "string"
        }, 
        "name": {
          "description": "The name of the file/folder.", 
          "type": "string"
        }, 
        "path": {
          "description": "The absolute path to the file/folder.", 
          "type": "string"
        }, 
        "permissions": {
          "description": "The system permission of the invoking user on the file/folder.", 
          "type": "string"
        }, 
        "system": {
          "description": "The systemId of the system where this file lives.", 
          "type": "string"
        }, 
        "type": {
          "description": "Whether it is a file or folder.", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy RemoteFile schema", 
      "type": "object"
    }

list: Get a remote directory listing on a specific system.
==========================================================
``agavepy.files.list(filePath, systemId, limit=250, offset=0)``

Parameters:
-----------
    * **systemId**: The unique id of the system on which the data resides. (string)
    * **filePath**: The path of the file relative to the user's default storage location. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Array of RemoteFile objects*

**RemoteFile schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/RemoteFile.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "format": {
          "description": "The file type of the file.", 
          "type": "string"
        }, 
        "lastModified": {
          "description": "The date this file was last modified in ISO 8601 format.", 
          "type": "string"
        }, 
        "length": {
          "description": "The length of the file/folder.", 
          "type": "integer"
        }, 
        "mimeType": {
          "description": "The mime type of the file/folder. If unknown, it defaults to application/binary.", 
          "type": "string"
        }, 
        "name": {
          "description": "The name of the file/folder.", 
          "type": "string"
        }, 
        "path": {
          "description": "The absolute path to the file/folder.", 
          "type": "string"
        }, 
        "permissions": {
          "description": "The system permission of the invoking user on the file/folder.", 
          "type": "string"
        }, 
        "system": {
          "description": "The systemId of the system where this file lives.", 
          "type": "string"
        }, 
        "type": {
          "description": "Whether it is a file or folder.", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy RemoteFile schema", 
      "type": "object"
    }

getHistoryOnDefaultSystem: Download a file from the user's default storage location.
====================================================================================
``agavepy.files.getHistoryOnDefaultSystem(filePath, limit=250, offset=0)``

Parameters:
-----------
    * **filePath**: The path of the file relative to the user's default storage location. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Array of FileHistory objects*

**FileHistory schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/FileHistory.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "created": {
          "description": "The date of the event.", 
          "type": "string"
        }, 
        "description": {
          "description": "A brief description of the event details.", 
          "type": "String"
        }, 
        "status": {
          "description": "The status of the file/folder after this event.", 
          "type": "String"
        }
      }, 
      "required": [], 
      "title": "AgavePy FileHistory schema", 
      "type": "object"
    }

getHistory: Return history of api actions.
==========================================
``agavepy.files.getHistory(filePath, systemId, limit=250, offset=0)``

Parameters:
-----------
    * **systemId**: The unique id of the system on which the data resides. (string)
    * **filePath**: The path of the file relative to the given system root location. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Array of FileHistory objects*

**FileHistory schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/FileHistory.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "created": {
          "description": "The date of the event.", 
          "type": "string"
        }, 
        "description": {
          "description": "A brief description of the event details.", 
          "type": "String"
        }, 
        "status": {
          "description": "The status of the file/folder after this event.", 
          "type": "String"
        }
      }, 
      "required": [], 
      "title": "AgavePy FileHistory schema", 
      "type": "object"
    }

listPermissionsOnDefaultSystem: List all the share permissions for a file or folder.
====================================================================================
``agavepy.files.listPermissionsOnDefaultSystem(filePath, limit=250, offset=0)``

Parameters:
-----------
    * **filePath**: The path of the file relative to the user's default storage location. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Array of FilePermission objects*

**FilePermission schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/FilePermission.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "name": {
          "description": "The name of the file/folder.", 
          "type": "string"
        }, 
        "owner": {
          "description": "Local username of the owner.", 
          "type": "string"
        }, 
        "permissions": {
          "description": "One or more permission objects", 
          "type": "array"
        }
      }, 
      "required": [], 
      "title": "AgavePy FilePermission schema", 
      "type": "object"
    }

updatePermissionsOnDefaultSystem: Update permissions for a single user.
=======================================================================
``agavepy.files.updatePermissionsOnDefaultSystem(body, filePath)``

Parameters:
-----------
    * **filePath**: The path of the file relative to the user's default storage location. (string)
    * **body**: The permission add or update.  (JSON, FilePermissionRequest)


**FilePermissionRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/FilePermissionRequest.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "permission": {
          "description": "The permission to set", 
          "enum": [
            "READ", 
            "WRITE", 
            "EXECUTE", 
            "READ_WRITE", 
            "READ_EXECUTE", 
            "WRITE_EXECUTE", 
            "ALL", 
            "NONE"
          ], 
          "type": "string"
        }, 
        "recursive": {
          "description": "Should updated permissions be applied recursively. Defaults to false.", 
          "type": "boolean"
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
      "title": "AgavePy FilePermissionRequest schema", 
      "type": "object"
    }

Response:
---------
    * *String*

deletePermissions: Deletes all permissions on a file except those of the owner.
===============================================================================
``agavepy.files.deletePermissions(filePath, systemId)``

Parameters:
-----------
    * **filePath**: The path of the file relative to the user's default storage location. (string)
    * **systemId**: The unique id of the system on which the data resides. (string)


Response:
---------
    * *String*

listPermissions: List all the share permissions for a file or folder.
=====================================================================
``agavepy.files.listPermissions(filePath, systemId, limit=250, offset=0)``

Parameters:
-----------
    * **filePath**: The path of the file relative to the user's default storage location. (string)
    * **limit**: The max number of results. (integer)
    * **systemId**: The unique id of the system on which the data resides. (string)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Array of FilePermission objects*

**FilePermission schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/FilePermission.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "name": {
          "description": "The name of the file/folder.", 
          "type": "string"
        }, 
        "owner": {
          "description": "Local username of the owner.", 
          "type": "string"
        }, 
        "permissions": {
          "description": "One or more permission objects", 
          "type": "array"
        }
      }, 
      "required": [], 
      "title": "AgavePy FilePermission schema", 
      "type": "object"
    }

updatePermissions: Update permissions for a single user.
========================================================
``agavepy.files.updatePermissions(body, filePath, systemId)``

Parameters:
-----------
    * **filePath**: The path of the file relative to the user's default storage location. (string)
    * **systemId**: The unique id of the system on which the data resides. (string)
    * **body**: The permission add or update.  (JSON, FilePermissionRequest)


**FilePermissionRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/FilePermissionRequest.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "permission": {
          "description": "The permission to set", 
          "enum": [
            "READ", 
            "WRITE", 
            "EXECUTE", 
            "READ_WRITE", 
            "READ_EXECUTE", 
            "WRITE_EXECUTE", 
            "ALL", 
            "NONE"
          ], 
          "type": "string"
        }, 
        "recursive": {
          "description": "Should updated permissions be applied recursively. Defaults to false.", 
          "type": "boolean"
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
      "title": "AgavePy FilePermissionRequest schema", 
      "type": "object"
    }

Response:
---------
    * *Array of FilePermission objects*

**FilePermission schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/FilePermission.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "name": {
          "description": "The name of the file/folder.", 
          "type": "string"
        }, 
        "owner": {
          "description": "Local username of the owner.", 
          "type": "string"
        }, 
        "permissions": {
          "description": "One or more permission objects", 
          "type": "array"
        }
      }, 
      "required": [], 
      "title": "AgavePy FilePermission schema", 
      "type": "object"
    }

