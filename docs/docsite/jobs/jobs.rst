****
jobs
****

Summary: Run and manage jobs

list: Get a list of jobs the authenticated user had submitted.
==============================================================
``jobs.list(limit=250, offset=0)``

Keyword Args:
-------------
    * **limit**: The max number of results. (integer, optional)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer, optional)


Response:
---------
    * *Array of JobSummary objects*

submit: Submit a new job request.
=================================
``jobs.submit(body=<BODY>)``

Keyword Args:
-------------
    * **body**: The description of the job to submit. This can be either a file upload or json posted to the request body. (JSON, JobRequest)


**JobRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/JobRequest.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
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
      "title": "AgavePy JobRequest schema",
      "type": "object"
    }

Response:
---------
    * *A single Job object*

delete: Deletes a job from the user's history.
==============================================
``jobs.delete(jobId=<JOBID>)``

Keyword Args:
-------------
    * **jobId**: The id of the job. (string)


Response:
---------
    * *String*

get: Get details of the job with the specific job id.
=====================================================
``jobs.get(jobId=<JOBID>)``

Keyword Args:
-------------
    * **jobId**: The id of the job. (string)


Response:
---------
    * *A single Job object*

manage: Perform an action on a job.
===================================
``jobs.manage(body=<BODY>, jobId=<JOBID>)``

Keyword Args:
-------------
    * **body**: The operation to perform. (JSON, JobOperationRequest)
    * **jobId**: The id of the job. (string)


Response:
---------
    * *A single Job object*

getHistory: Get the history of this job.
========================================
``jobs.getHistory(jobId=<JOBID>, limit=250, offset=0)``

Keyword Args:
-------------
    * **jobId**: The id of the job. (string)
    * **limit**: The max number of results. (integer, optional)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer, optional)


Response:
---------
    * *Array of JobHistory objects*

deletePermissions: Deletes all permissions on an job.
=====================================================
``jobs.deletePermissions(jobId=<JOBID>)``

Keyword Args:
-------------
    * **jobId**: The id of the job. (string)


Response:
---------
    * *String*

listPermissions: Get the permission ACL for this job.
=====================================================
``jobs.listPermissions(jobId=<JOBID>, limit=250, offset=0)``

Keyword Args:
-------------
    * **jobId**: The id of the job. (string)
    * **limit**: The max number of results. (integer, optional)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer, optional)


Response:
---------
    * *Array of Permission objects*

updatePermissions: Add or update a user's permission for an application.
========================================================================
``jobs.updatePermissions(body=<BODY>, jobId=<JOBID>)``

Keyword Args:
-------------
    * **body**: The permission add or update.  (JSON, JobPermissionRequest)
    * **jobId**: The id of the job. (string)


Response:
---------
    * *String*

deletePermissionsForUser: Deletes all permissions for the given user on an job.
===============================================================================
``jobs.deletePermissionsForUser(uniqueName=<UNIQUENAME>, username=<USERNAME>)``

Keyword Args:
-------------
    * **uniqueName**: The id of the application. The application id is made up of the name and version separated by a dash. (string)
    * **username**: The username of the api user associated with the permission (string)


Response:
---------
    * *None*

listPermissionsForUser: Get a specific user's permissions for a job.
====================================================================
``jobs.listPermissionsForUser(jobId=<JOBID>, limit=250, offset=0, username=<USERNAME>)``

Keyword Args:
-------------
    * **jobId**: The id of the job. (string)
    * **limit**: The max number of results. (integer, optional)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer, optional)
    * **username**: The username of the api user associated with the permission. (string)


Response:
---------
    * *Array of Permission objects*

updatePermissionsForUser: Add or update a user's permission for an job.
=======================================================================
``jobs.updatePermissionsForUser(body=<BODY>, jobId=<JOBID>, username=<USERNAME>)``

Keyword Args:
-------------
    * **body**: The permission to update.  (JSON, JobPermissionRequest)
    * **jobId**: The id of the job. (string)
    * **username**: The username of the api user associated with the permission (string)


Response:
---------
    * *String*

getStatus: Get the status of the job.
=====================================
``jobs.getStatus(jobId=<JOBID>)``

Keyword Args:
-------------
    * **jobId**: The id of the job. (string)


Response:
---------
    * *A single JobStatus object*

listOutputs: List contents of a job's output directory.
=======================================================
``jobs.listOutputs(filePath=None, jobId=<JOBID>, limit=250, offset=0)``

Keyword Args:
-------------
    * **filePath**: Path to an output file or folder relative to the job output directory. This resource will follow data around as it moves from the execution system to archival storage. (string, optional)
    * **jobId**: The id of the job. (string)
    * **limit**: max number of results. (integer, optional)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer, optional)


Response:
---------
    * *Array of RemoteFile objects*

downloadOutput: Download an output file from a specific job.
============================================================
``jobs.downloadOutput(filePath=<FILEPATH>, jobId=<JOBID>)``

Keyword Args:
-------------
    * **filePath**: Path to an output file relative to the job output directory. (string)
    * **jobId**: The id of the job. (string)


Response:
---------
    * *None*

