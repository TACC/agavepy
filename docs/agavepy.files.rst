*************
agavepy.files
*************

Summary: Move and manage data

downloadFromDefaultSystem
=========================
``agavepy.files.downloadFromDefaultSystem(sourcefilePath)``

Download a file from the user's default storage location.

Parameters:
-----------
    * **sourcefilePath**: The path of the file relative to the user's default storage location. (string)


Response:
---------
    * *Coming soon*

importToDefaultSystem
=====================
``agavepy.files.importToDefaultSystem(sourcefilePath, callbackURL=None, fileName=None, fileToUpload=None, fileType=None, urlToIngest=None)``

Import a file via direct upload or importing from a url to the user's default storage location.

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
    * *Coming soon*

manageOnDefaultSystem
=====================
``agavepy.files.manageOnDefaultSystem(body, sourcefilePath)``

Perform an action on a file or folder.

Parameters:
-----------
    * **sourcefilePath**: The path of the file relative to the user's default storage location. (string)
    * **body**: The operation to perform.  (JSON, FileOperationRequest)


**FileOperationRequest:**

.. code-block:: javascript

    {
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
      "title": "FileOperationRequest", 
      "type": "object"
    }

Response:
---------
    * *Coming soon*

deleteFromDefaultSystem
=======================
``agavepy.files.deleteFromDefaultSystem(sourcefilePath)``

Deletes a file or folder.

Parameters:
-----------
    * **sourcefilePath**: The path of the file relative to the user's default storage location. (string)


Response:
---------
    * *Coming soon*

download
========
``agavepy.files.download(filePath, systemId)``

Download a file from the user's default storage location.

Parameters:
-----------
    * **systemId**: The unique id of the system on which the data resides. (string)
    * **filePath**: The path of the file relative to the user's default storage location. (string)


Response:
---------
    * *Coming soon*

importData
==========
``agavepy.files.importData(filePath, systemId, callbackURL=None, fileName=None, fileToUpload=None, fileType=None, notifications=[], urlToIngest=None)``

Import a file via direct upload or importing from a url to the user's default storage location.

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
    * *Coming soon*

manage
======
``agavepy.files.manage(body, filePath, systemId)``

Perform an action on a file or folder.

Parameters:
-----------
    * **systemId**: The unique id of the system on which the data resides. (string)
    * **filePath**: The path of the file relative to the user's default storage location. (string)
    * **body**: The operation to perform.  (JSON, FileOperationRequest)


**FileOperationRequest:**

.. code-block:: javascript

    {
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
      "title": "FileOperationRequest", 
      "type": "object"
    }

Response:
---------
    * *Coming soon*

delete
======
``agavepy.files.delete(filePath, systemId)``

Deletes a file or folder.

Parameters:
-----------
    * **systemId**: The unique id of the system on which the data resides. (string)
    * **filePath**: The path of the file relative to the user's default storage location. (string)


Response:
---------
    * *Coming soon*

listOnDefaultSystem
===================
``agavepy.files.listOnDefaultSystem(filePath, limit=250, offset=0)``

Get a remote directory listing.

Parameters:
-----------
    * **filePath**: The path of the file relative to the user's default storage location. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Coming soon*

list
====
``agavepy.files.list(filePath, systemId, limit=250, offset=0)``

Get a remote directory listing on a specific system.

Parameters:
-----------
    * **systemId**: The unique id of the system on which the data resides. (string)
    * **filePath**: The path of the file relative to the user's default storage location. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Coming soon*

getHistoryOnDefaultSystem
=========================
``agavepy.files.getHistoryOnDefaultSystem(filePath, limit=250, offset=0)``

Download a file from the user's default storage location.

Parameters:
-----------
    * **filePath**: The path of the file relative to the user's default storage location. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Coming soon*

getHistory
==========
``agavepy.files.getHistory(filePath, systemId, limit=250, offset=0)``

Return history of api actions.

Parameters:
-----------
    * **systemId**: The unique id of the system on which the data resides. (string)
    * **filePath**: The path of the file relative to the given system root location. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Coming soon*

listPermissionsOnDefaultSystem
==============================
``agavepy.files.listPermissionsOnDefaultSystem(filePath, limit=250, offset=0)``

List all the share permissions for a file or folder.

Parameters:
-----------
    * **filePath**: The path of the file relative to the user's default storage location. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Coming soon*

updatePermissionsOnDefaultSystem
================================
``agavepy.files.updatePermissionsOnDefaultSystem(body, filePath)``

Update permissions for a single user.

Parameters:
-----------
    * **filePath**: The path of the file relative to the user's default storage location. (string)
    * **body**: The permission add or update.  (JSON, FilePermissionRequest)


**FilePermissionRequest:**

.. code-block:: javascript

    {
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
      "title": "FilePermissionRequest", 
      "type": "object"
    }

Response:
---------
    * *Coming soon*

listPermissions
===============
``agavepy.files.listPermissions(filePath, systemId, limit=250, offset=0)``

List all the share permissions for a file or folder.

Parameters:
-----------
    * **filePath**: The path of the file relative to the user's default storage location. (string)
    * **limit**: The max number of results. (integer)
    * **systemId**: The unique id of the system on which the data resides. (string)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Coming soon*

updatePermissions
=================
``agavepy.files.updatePermissions(body, filePath, systemId)``

Update permissions for a single user.

Parameters:
-----------
    * **filePath**: The path of the file relative to the user's default storage location. (string)
    * **systemId**: The unique id of the system on which the data resides. (string)
    * **body**: The permission add or update.  (JSON, FilePermissionRequest)


**FilePermissionRequest:**

.. code-block:: javascript

    {
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
      "title": "FilePermissionRequest", 
      "type": "object"
    }

Response:
---------
    * *Coming soon*

deletePermissions
=================
``agavepy.files.deletePermissions(filePath, systemId)``

Deletes all permissions on a file except those of the owner.

Parameters:
-----------
    * **filePath**: The path of the file relative to the user's default storage location. (string)
    * **systemId**: The unique id of the system on which the data resides. (string)


Response:
---------
    * *Coming soon*

