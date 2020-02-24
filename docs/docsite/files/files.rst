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
``files.importToDefaultSystem(callbackURL=None, fileName=None, fileToUpload=None, fileType=None, sourcefilePath=<SOURCEFILEPATH>, urlToIngest=None)``

Keyword Args:
-------------
    * **callbackURL**: The URI to notify when the import is complete. This can be an email address or http URL. If a URL is given, a GET will be made to this address. URL templating is supported. Valid template values are: ${NAME}, ${SOURCE_FORMAT}, ${DEST_FORMAT}, ${STATUS} (string)
    * **fileName**: The name of the file after importing. If not specified, the uploaded file name will be used. (string)
    * **fileToUpload**: The file object to import. (void)
    * **fileType**: The file format this file is in. Defaults to raw. This will be used in file transform operations. (string)
    * **sourcefilePath**: The path of the file relative to the user's default storage location. (string)
    * **urlToIngest**: The URL to import the file from. This parameter is used if not file is uploaded with this post. (string)


Response:
---------
    * *A single RemoteFile object*

manageOnDefaultSystem: Perform an action on a file or folder.
=============================================================
``files.manageOnDefaultSystem(body=<BODY>, sourcefilePath=<SOURCEFILEPATH>)``

Keyword Args:
-------------
    * **body**: The operation to perform.  (JSON, FileOperationRequest)
    * **sourcefilePath**: The path of the file relative to the user's default storage location. (string)


Response:
---------
    * *String*

delete: Deletes a file or folder.
=================================
``files.delete(filePath=<FILEPATH>, systemId=<SYSTEMID>)``

Keyword Args:
-------------
    * **filePath**: The path of the file relative to the user's default storage location. (string)
    * **systemId**: The unique id of the system on which the data resides. (string)


Response:
---------
    * *String*

download: Download a file from the user's default storage location.
===================================================================
``files.download(filePath=<FILEPATH>, systemId=<SYSTEMID>)``

Keyword Args:
-------------
    * **filePath**: The path of the file relative to the user's default storage location. (string)
    * **systemId**: The unique id of the system on which the data resides. (string)


Response:
---------
    * *None*

importData: Import a file via direct upload or importing from a url to the user's default storage location.
===========================================================================================================
``files.importData(callbackURL=None, fileName=None, filePath=<FILEPATH>, fileToUpload=None, fileType=None, notifications=[], systemId=<SYSTEMID>, urlToIngest=None)``

Keyword Args:
-------------
    * **callbackURL**: The URI to notify when the import is complete. This can be an email address or http URL. If a URL is given, a GET will be made to this address. URL templating is supported. Valid template values are: ${NAME}, ${SOURCE_FORMAT}, ${DEST_FORMAT}, ${STATUS} (string)
    * **fileName**: The name of the file after importing. If not specified, the uploaded file name will be used. (string)
    * **filePath**: The path of the file relative to the user's default storage location. (string)
    * **fileToUpload**: The file object to import. (void)
    * **fileType**: The file format this file is in. Defaults to raw. This will be used in file transform operations. (string)
    * **notifications**: A list of notification objects to apply to the transfer.  (FileNotificationRequest)
    * **systemId**: The unique id of the system on which the data resides. (string)
    * **urlToIngest**: The URL to import the file from. This parameter is used if not file is uploaded with this post. (string)


Response:
---------
    * *A single RemoteFile object*

manage: Perform an action on a file or folder.
==============================================
``files.manage(body=<BODY>, filePath=<FILEPATH>, systemId=<SYSTEMID>)``

Keyword Args:
-------------
    * **body**: The operation to perform.  (JSON, FileOperationRequest)
    * **filePath**: The path of the file relative to the user's default storage location. (string)
    * **systemId**: The unique id of the system on which the data resides. (string)


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
``files.list(filePath=<FILEPATH>, limit=250, offset=0, systemId=<SYSTEMID>)``

Keyword Args:
-------------
    * **filePath**: The path of the file relative to the user's default storage location. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)
    * **systemId**: The unique id of the system on which the data resides. (string)


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
``files.getHistory(filePath=<FILEPATH>, limit=250, offset=0, systemId=<SYSTEMID>)``

Keyword Args:
-------------
    * **filePath**: The path of the file relative to the given system root location. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)
    * **systemId**: The unique id of the system on which the data resides. (string)


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
    * **body**: The permission add or update.  (JSON, FilePermissionRequest)
    * **filePath**: The path of the file relative to the user's default storage location. (string)


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
``files.listPermissions(filePath=<FILEPATH>, limit=250, offset=0, systemId=<SYSTEMID>)``

Keyword Args:
-------------
    * **filePath**: The path of the file relative to the user's default storage location. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)
    * **systemId**: The unique id of the system on which the data resides. (string)


Response:
---------
    * *Array of FilePermission objects*

updatePermissions: Update permissions for a single user.
========================================================
``files.updatePermissions(body=<BODY>, filePath=<FILEPATH>, systemId=<SYSTEMID>)``

Keyword Args:
-------------
    * **body**: The permission add or update.  (JSON, FilePermissionRequest)
    * **filePath**: The path of the file relative to the user's default storage location. (string)
    * **systemId**: The unique id of the system on which the data resides. (string)


Response:
---------
    * *Array of FilePermission objects*

