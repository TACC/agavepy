************
agavepy.jobs
************

Summary: Run and manage jobs

list
====
``agavepy.jobs.list(limit=250, offset=0)``

Get a list of jobs the authenticated user had submitted.

Parameters:
-----------
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Coming soon*

submit
======
``agavepy.jobs.submit(body)``

Submit a new job request.

Parameters:
-----------
    * **body**: The description of the job to submit. This can be either a file upload or json posted to the request body. (JSON, JobRequest)


**JobRequest:**

.. code-block:: javascript

    {
      "properties": {
        "appId": {
          "description": "The unique name of the application being run by this job. This must be a valid application that the calling user has permission to run.", 
          "type": "string"
        }, 
        "archive": {
          "description": "Whether the output from this job should be archived. If true, all new files created by this application's execution will be archived to the archivePath in the user's default storage system.", 
          "type": "boolean"
        }, 
        "archivePath": {
          "description": "The path of the archive folder for this job on the user's default storage sytem.", 
          "type": "string"
        }, 
        "archiveSystem": {
          "description": "The unique id of the storage system on which this job's output will be staged.", 
          "type": "string"
        }, 
        "batchQueue": {
          "description": "The queue to which this job should be submitted. This is optional and only applies when the execution system has a batch scheduler.", 
          "type": "string"
        }, 
        "inputs": {
          "description": "The application specific input files needed for this job. These vary from application to application and should be entered as multiple individual parameters in the form. Inputs may be given as relative paths in the user's default storage system or as URI. If a URI is given, the data will be staged in by the IO service and made avaialble to the application at run time.", 
          "type": "JobInputs"
        }, 
        "maxRunTime": {
          "description": "The requested compute time needed for this application to complete given in HH:mm:ss format.", 
          "type": "string"
        }, 
        "memoryPerNode": {
          "description": "The requested memory for this application to run given in GB.", 
          "type": "string"
        }, 
        "name": {
          "description": "The name of the job.", 
          "type": "string"
        }, 
        "nodeCount": {
          "description": "The number of processors this application should utilize while running. If the application is not of executionType PARALLEL, this should be 1.", 
          "type": "integer"
        }, 
        "notifications": {
          "description": "An array of notifications you wish to receive.", 
          "type": "array"
        }, 
        "parameters": {
          "description": "The application specific parameters needed for this job. These vary from application to application and should be entered as multiple individual parameters in the form. The actual dataType will be determined by the application description.", 
          "type": "JobParameters"
        }, 
        "processorsPerNode": {
          "description": "The number of processors this application should utilize while running. If the application is not of executionType PARALLEL, this should be 1.", 
          "type": "integer"
        }
      }, 
      "required": [
        "inputs", 
        "name", 
        "parameters", 
        "appId", 
        "archive"
      ], 
      "title": "JobRequest", 
      "type": "object"
    }

Response:
---------
    * *Coming soon*

get
===
``agavepy.jobs.get(jobId)``

Get details of the job with the specific job id.

Parameters:
-----------
    * **jobId**: The id of the job. (string)


Response:
---------
    * *Coming soon*

manage
======
``agavepy.jobs.manage(body, jobId)``

Perform an action on a job.

Parameters:
-----------
    * **jobId**: The id of the job. (string)
    * **body**: The operation to perform. (JSON, JobOperationRequest)


**JobOperationRequest:**

.. code-block:: javascript

    {
      "properties": {
        "action": {
          "description": "Action to perform on the job.", 
          "enum": [
            "resubmit", 
            "stop"
          ], 
          "type": "string"
        }
      }, 
      "required": [
        "action"
      ], 
      "title": "JobOperationRequest", 
      "type": "object"
    }

Response:
---------
    * *Coming soon*

delete
======
``agavepy.jobs.delete(jobId)``

Deletes a job from the user's history.

Parameters:
-----------
    * **jobId**: The id of the job. (string)


Response:
---------
    * *Coming soon*

getHistory
==========
``agavepy.jobs.getHistory(jobId, limit=250, offset=0)``

Get the history of this job.

Parameters:
-----------
    * **jobId**: The id of the job. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Coming soon*

listPermissions
===============
``agavepy.jobs.listPermissions(jobId, limit=250, offset=0)``

Get the permission ACL for this job.

Parameters:
-----------
    * **jobId**: The id of the job. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Coming soon*

updatePermissions
=================
``agavepy.jobs.updatePermissions(body, jobId)``

Add or update a user's permission for an application.

Parameters:
-----------
    * **jobId**: The id of the job. (string)
    * **body**: The permission add or update.  (JSON, JobPermissionRequest)


**JobPermissionRequest:**

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
        "username": {
          "description": "The username of the api user whose permission is to be set.", 
          "type": "string"
        }
      }, 
      "required": [
        "username", 
        "permission"
      ], 
      "title": "JobPermissionRequest", 
      "type": "object"
    }

Response:
---------
    * *Coming soon*

deletePermissions
=================
``agavepy.jobs.deletePermissions(jobId)``

Deletes all permissions on an job.

Parameters:
-----------
    * **jobId**: The id of the job. (string)


Response:
---------
    * *Coming soon*

listPermissionsForUser
======================
``agavepy.jobs.listPermissionsForUser(jobId, username, limit=250, offset=0)``

Get a specific user's permissions for a job.

Parameters:
-----------
    * **jobId**: The id of the job. (string)
    * **username**: The username of the api user associated with the permission. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Coming soon*

updatePermissionsForUser
========================
``agavepy.jobs.updatePermissionsForUser(body, jobId, username)``

Add or update a user's permission for an job.

Parameters:
-----------
    * **jobId**: The id of the job. (string)
    * **username**: The username of the api user associated with the permission (string)
    * **body**: The permission to update.  (JSON, JobPermissionRequest)


**JobPermissionRequest:**

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
        "username": {
          "description": "The username of the api user whose permission is to be set.", 
          "type": "string"
        }
      }, 
      "required": [
        "username", 
        "permission"
      ], 
      "title": "JobPermissionRequest", 
      "type": "object"
    }

Response:
---------
    * *Coming soon*

deletePermissionsForUser
========================
``agavepy.jobs.deletePermissionsForUser(uniqueName, username)``

Deletes all permissions for the given user on an job.

Parameters:
-----------
    * **uniqueName**: The id of the application. The application id is made up of the name and version separated by a dash. (string)
    * **username**: The username of the api user associated with the permission (string)


Response:
---------
    * *Coming soon*

getStatus
=========
``agavepy.jobs.getStatus(jobId)``

Get the status of the job.

Parameters:
-----------
    * **jobId**: The id of the job. (string)


Response:
---------
    * *Coming soon*

listOutputs
===========
``agavepy.jobs.listOutputs(jobId, filePath=None, limit=250, offset=0)``

List contents of a job's output directory.

Parameters:
-----------
    * **jobId**: The id of the job. (string)
    * **filePath**: Path to an output file or folder relative to the job output directory. This resource will follow data around as it moves from the execution system to archival storage. (string)
    * **limit**: max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Coming soon*

downloadOutput
==============
``agavepy.jobs.downloadOutput(filePath, jobId)``

Download an output file from a specific job.

Parameters:
-----------
    * **jobId**: The id of the job. (string)
    * **filePath**: Path to an output file relative to the job output directory. (string)


Response:
---------
    * *Coming soon*

search
======
``agavepy.jobs.search(attribute, value, limit=250, offset=0)``

Find jobs matching the given attribute/value combination(s).

Parameters:
-----------
    * **attribute**: The attribute to query by. This can be any job field. (string)
    * **value**: The value of the attribute to query for. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Coming soon*

