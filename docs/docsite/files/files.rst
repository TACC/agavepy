*****
files
*****

Summary: Move and manage data

deleteFromDefaultSystem: Deletes a file or folder.
==================================================
``files.deleteFromDefaultSystem(sourcefilePath=<SOURCEFILEPATH>)``

Keyword Args:
-------------
    * **sourcefilePath**: The path of the file relative to the user's default storage location. (string)


Response:
---------
    * *String*

downloadFromDefaultSystem: Download a file from the user's default storage location.
====================================================================================
``files.downloadFromDefaultSystem(sourcefilePath=<SOURCEFILEPATH>)``

Keyword Args:
-------------
    * **sourcefilePath**: The path of the file relative to the user's default storage location. (string)


Response:
---------
    * *None*

importToDefaultSystem: Import a file via direct upload or importing from a url to the user's default storage location.
======================================================================================================================
``files.importToDefaultSystem(sourcefilePath=<SOURCEFILEPATH>, callbackURL=None, fileName=None, fileToUpload=None, fileType=None, urlToIngest=None)``

Keyword Args:
-------------
    * **sourcefilePath**: The path of the file relative to the user's default storage location. (string)
    * **fileType**: The file format this file is in. Defaults to raw. This will be used in file transform operations. (string)
    * **callbackURL**: The URI to notify when the import is complete. This can be an email address or http URL. If a URL is given, a GET will be made to this address. URL templating is supported. Valid template values are: ${NAME}, ${SOURCE_FORMAT}, ${DEST_FORMAT}, ${STATUS} (string)
    * **fileName**: The name of the file after importing. If not specified, the uploaded file name will be used. (string)
    * **urlToIngest**: The URL to import the file from. This parameter is used if not file is uploaded with this post. (string)
    * **fileToUpload**: The file object to import. (void)


Response:
---------
    * *A single RemoteFile object*

manageOnDefaultSystem: Perform an action on a file or folder.
=============================================================
``files.manageOnDefaultSystem(body=<BODY>, sourcefilePath=<SOURCEFILEPATH>)``

Keyword Args:
-------------
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
``files.delete(filePath=<FILEPATH>, systemId=<SYSTEMID>)``

Keyword Args:
-------------
    * **systemId**: The unique id of the system on which the data resides. (string)
    * **filePath**: The path of the file relative to the user's default storage location. (string)


Response:
---------
    * *String*

download: Download a file from the user's default storage location.
===================================================================
``files.download(filePath=<FILEPATH>, systemId=<SYSTEMID>)``

Keyword Args:
-------------
    * **systemId**: The unique id of the system on which the data resides. (string)
    * **filePath**: The path of the file relative to the user's default storage location. (string)


Response:
---------
    * *None*

importData: Import a file via direct upload or importing from a url to the user's default storage location.
===========================================================================================================
``files.importData(filePath=<FILEPATH>, systemId=<SYSTEMID>, callbackURL=None, fileName=None, fileToUpload=None, fileType=None, notifications=[], urlToIngest=None)``

Keyword Args:
-------------
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

manage: Perform an action on a file or folder.
==============================================
``files.manage(body=<BODY>, filePath=<FILEPATH>, systemId=<SYSTEMID>)``

Keyword Args:
-------------
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
``files.listOnDefaultSystem(filePath=<FILEPATH>, limit=250, offset=0)``

Keyword Args:
-------------
    * **filePath**: The path of the file relative to the user's default storage location. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Array of RemoteFile objects*

list: Get a remote directory listing on a specific system.
==========================================================
``files.list(filePath=<FILEPATH>, systemId=<SYSTEMID>, limit=250, offset=0)``

Keyword Args:
-------------
    * **systemId**: The unique id of the system on which the data resides. (string)
    * **filePath**: The path of the file relative to the user's default storage location. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Array of RemoteFile objects*

getHistoryOnDefaultSystem: Download a file from the user's default storage location.
====================================================================================
``files.getHistoryOnDefaultSystem(filePath=<FILEPATH>, limit=250, offset=0)``

Keyword Args:
-------------
    * **filePath**: The path of the file relative to the user's default storage location. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Array of FileHistory objects*

getHistory: Return history of api actions.
==========================================
``files.getHistory(filePath=<FILEPATH>, systemId=<SYSTEMID>, limit=250, offset=0)``

Keyword Args:
-------------
    * **systemId**: The unique id of the system on which the data resides. (string)
    * **filePath**: The path of the file relative to the given system root location. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Array of FileHistory objects*

listPermissionsOnDefaultSystem: List all the share permissions for a file or folder.
====================================================================================
``files.listPermissionsOnDefaultSystem(filePath=<FILEPATH>, limit=250, offset=0)``

Keyword Args:
-------------
    * **filePath**: The path of the file relative to the user's default storage location. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Array of FilePermission objects*

updatePermissionsOnDefaultSystem: Update permissions for a single user.
=======================================================================
``files.updatePermissionsOnDefaultSystem(body=<BODY>, filePath=<FILEPATH>)``

Keyword Args:
-------------
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
``files.deletePermissions(filePath=<FILEPATH>, systemId=<SYSTEMID>)``

Keyword Args:
-------------
    * **filePath**: The path of the file relative to the user's default storage location. (string)
    * **systemId**: The unique id of the system on which the data resides. (string)


Response:
---------
    * *String*

listPermissions: List all the share permissions for a file or folder.
=====================================================================
``files.listPermissions(filePath=<FILEPATH>, systemId=<SYSTEMID>, limit=250, offset=0)``

Keyword Args:
-------------
    * **filePath**: The path of the file relative to the user's default storage location. (string)
    * **limit**: The max number of results. (integer)
    * **systemId**: The unique id of the system on which the data resides. (string)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Array of FilePermission objects*

updatePermissions: Update permissions for a single user.
========================================================
``files.updatePermissions(body=<BODY>, filePath=<FILEPATH>, systemId=<SYSTEMID>)``

Keyword Args:
-------------
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

