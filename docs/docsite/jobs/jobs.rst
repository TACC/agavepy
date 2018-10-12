****
Jobs
****

Summary: Run and manage jobs

list: Get a list of jobs the authenticated user had submitted.
==============================================================
``agavepy.jobs.list(limit=250, offset=0)``

Parameters:
-----------
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Array of JobSummary objects*

**JobSummary schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/JobSummary.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "appId": {
          "description": "The unique name of the application being run by this job. This must be a valid application that the calling user has permission to run.", 
          "type": "string"
        }, 
        "endTime": {
          "description": "The date the job ended in ISO 8601 format.", 
          "type": "string"
        }, 
        "executionSystem": {
          "description": "The system id of the execution system.", 
          "type": "string"
        }, 
        "id": {
          "description": "The unique id of the job.", 
          "type": "string"
        }, 
        "name": {
          "description": "The name of the job.", 
          "type": "string"
        }, 
        "owner": {
          "description": "The job owner.", 
          "type": "string"
        }, 
        "startTime": {
          "description": "The date the job started in ISO 8601 format.", 
          "type": "string"
        }, 
        "status": {
          "description": "The status of the job. Possible values are: PENDING, STAGING_INPUTS, CLEANING_UP, ARCHIVING, STAGING_JOB, FINISHED, KILLED, FAILED, STOPPED, RUNNING, PAUSED, QUEUED, SUBMITTING, STAGED, PROCESSING_INPUTS, ARCHIVING_FINISHED, ARCHIVING_FAILED", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy JobSummary schema", 
      "type": "object"
    }

submit: Submit a new job request.
=================================
``agavepy.jobs.submit(body)``

Parameters:
-----------
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

**Job schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/Job.json", 
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
        "endTime": {
          "description": "The date the job stopped running due to termination, completion, or error in ISO 8601 format.", 
          "type": "string"
        }, 
        "executionSystem": {
          "description": "The system id of the execution system.", 
          "type": "string"
        }, 
        "id": {
          "description": "The unique id of the job.", 
          "type": "string"
        }, 
        "inputs": {
          "description": "The application specific input files needed for this job. These vary from application to application and should be entered as multiple individual parameters in the form. Inputs may be given as relative paths in the user's default storage system or as URI. If a URI is given, the data will be staged in by the IO service and made avaialble to the application at run time.", 
          "type": "JobInputs"
        }, 
        "localId": {
          "description": "The process or local job id of the job on the remote execution system.", 
          "type": "string"
        }, 
        "maxRunTime": {
          "description": "The requested compute time needed for this application to complete given in HH:mm:ss format.", 
          "type": "string"
        }, 
        "memoryPerNode": {
          "description": "The requested memory for this application to run given in GB.", 
          "type": "string"
        }, 
        "message": {
          "description": "The error message incurred when the job failed.", 
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
        "outputPath": {
          "description": "Relative path of the job's output data.", 
          "type": "String"
        }, 
        "owner": {
          "description": "The job owner.", 
          "type": "string"
        }, 
        "parameters": {
          "description": "The application specific parameters needed for this job. These vary from application to application and should be entered as multiple individual parameters in the form. The actual dataType will be determined by the application description.", 
          "type": "JobParameters"
        }, 
        "processorsPerNode": {
          "description": "The number of processors this application should utilize while running. If the application is not of executionType PARALLEL, this should be 1.", 
          "type": "integer"
        }, 
        "retries": {
          "description": "The number of retires it took to submit this job.", 
          "type": "integer"
        }, 
        "startTime": {
          "description": "The date the job started in ISO 8601 format.", 
          "type": "string"
        }, 
        "status": {
          "description": "The status of the job. Possible values are: PENDING, STAGING_INPUTS, CLEANING_UP, ARCHIVING, STAGING_JOB, FINISHED, KILLED, FAILED, STOPPED, RUNNING, PAUSED, QUEUED, SUBMITTING, STAGED, PROCESSING_INPUTS, ARCHIVING_FINISHED, ARCHIVING_FAILED", 
          "type": "string"
        }, 
        "submitTime": {
          "description": "The date the job was submitted in ISO 8601 format.", 
          "type": "string"
        }, 
        "workPath": {
          "description": "The directory on the remote execution system from which the job is running.", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy Job schema", 
      "type": "object"
    }

delete: Deletes a job from the user's history.
==============================================
``agavepy.jobs.delete(jobId)``

Parameters:
-----------
    * **jobId**: The id of the job. (string)


Response:
---------
    * *String*

get: Get details of the job with the specific job id.
=====================================================
``agavepy.jobs.get(jobId)``

Parameters:
-----------
    * **jobId**: The id of the job. (string)


Response:
---------
    * *A single Job object*

**Job schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/Job.json", 
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
        "endTime": {
          "description": "The date the job stopped running due to termination, completion, or error in ISO 8601 format.", 
          "type": "string"
        }, 
        "executionSystem": {
          "description": "The system id of the execution system.", 
          "type": "string"
        }, 
        "id": {
          "description": "The unique id of the job.", 
          "type": "string"
        }, 
        "inputs": {
          "description": "The application specific input files needed for this job. These vary from application to application and should be entered as multiple individual parameters in the form. Inputs may be given as relative paths in the user's default storage system or as URI. If a URI is given, the data will be staged in by the IO service and made avaialble to the application at run time.", 
          "type": "JobInputs"
        }, 
        "localId": {
          "description": "The process or local job id of the job on the remote execution system.", 
          "type": "string"
        }, 
        "maxRunTime": {
          "description": "The requested compute time needed for this application to complete given in HH:mm:ss format.", 
          "type": "string"
        }, 
        "memoryPerNode": {
          "description": "The requested memory for this application to run given in GB.", 
          "type": "string"
        }, 
        "message": {
          "description": "The error message incurred when the job failed.", 
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
        "outputPath": {
          "description": "Relative path of the job's output data.", 
          "type": "String"
        }, 
        "owner": {
          "description": "The job owner.", 
          "type": "string"
        }, 
        "parameters": {
          "description": "The application specific parameters needed for this job. These vary from application to application and should be entered as multiple individual parameters in the form. The actual dataType will be determined by the application description.", 
          "type": "JobParameters"
        }, 
        "processorsPerNode": {
          "description": "The number of processors this application should utilize while running. If the application is not of executionType PARALLEL, this should be 1.", 
          "type": "integer"
        }, 
        "retries": {
          "description": "The number of retires it took to submit this job.", 
          "type": "integer"
        }, 
        "startTime": {
          "description": "The date the job started in ISO 8601 format.", 
          "type": "string"
        }, 
        "status": {
          "description": "The status of the job. Possible values are: PENDING, STAGING_INPUTS, CLEANING_UP, ARCHIVING, STAGING_JOB, FINISHED, KILLED, FAILED, STOPPED, RUNNING, PAUSED, QUEUED, SUBMITTING, STAGED, PROCESSING_INPUTS, ARCHIVING_FINISHED, ARCHIVING_FAILED", 
          "type": "string"
        }, 
        "submitTime": {
          "description": "The date the job was submitted in ISO 8601 format.", 
          "type": "string"
        }, 
        "workPath": {
          "description": "The directory on the remote execution system from which the job is running.", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy Job schema", 
      "type": "object"
    }

manage: Perform an action on a job.
===================================
``agavepy.jobs.manage(body, jobId)``

Parameters:
-----------
    * **jobId**: The id of the job. (string)
    * **body**: The operation to perform. (JSON, JobOperationRequest)


**JobOperationRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/JobOperationRequest.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
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
      "title": "AgavePy JobOperationRequest schema", 
      "type": "object"
    }

Response:
---------
    * *A single Job object*

**Job schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/Job.json", 
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
        "endTime": {
          "description": "The date the job stopped running due to termination, completion, or error in ISO 8601 format.", 
          "type": "string"
        }, 
        "executionSystem": {
          "description": "The system id of the execution system.", 
          "type": "string"
        }, 
        "id": {
          "description": "The unique id of the job.", 
          "type": "string"
        }, 
        "inputs": {
          "description": "The application specific input files needed for this job. These vary from application to application and should be entered as multiple individual parameters in the form. Inputs may be given as relative paths in the user's default storage system or as URI. If a URI is given, the data will be staged in by the IO service and made avaialble to the application at run time.", 
          "type": "JobInputs"
        }, 
        "localId": {
          "description": "The process or local job id of the job on the remote execution system.", 
          "type": "string"
        }, 
        "maxRunTime": {
          "description": "The requested compute time needed for this application to complete given in HH:mm:ss format.", 
          "type": "string"
        }, 
        "memoryPerNode": {
          "description": "The requested memory for this application to run given in GB.", 
          "type": "string"
        }, 
        "message": {
          "description": "The error message incurred when the job failed.", 
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
        "outputPath": {
          "description": "Relative path of the job's output data.", 
          "type": "String"
        }, 
        "owner": {
          "description": "The job owner.", 
          "type": "string"
        }, 
        "parameters": {
          "description": "The application specific parameters needed for this job. These vary from application to application and should be entered as multiple individual parameters in the form. The actual dataType will be determined by the application description.", 
          "type": "JobParameters"
        }, 
        "processorsPerNode": {
          "description": "The number of processors this application should utilize while running. If the application is not of executionType PARALLEL, this should be 1.", 
          "type": "integer"
        }, 
        "retries": {
          "description": "The number of retires it took to submit this job.", 
          "type": "integer"
        }, 
        "startTime": {
          "description": "The date the job started in ISO 8601 format.", 
          "type": "string"
        }, 
        "status": {
          "description": "The status of the job. Possible values are: PENDING, STAGING_INPUTS, CLEANING_UP, ARCHIVING, STAGING_JOB, FINISHED, KILLED, FAILED, STOPPED, RUNNING, PAUSED, QUEUED, SUBMITTING, STAGED, PROCESSING_INPUTS, ARCHIVING_FINISHED, ARCHIVING_FAILED", 
          "type": "string"
        }, 
        "submitTime": {
          "description": "The date the job was submitted in ISO 8601 format.", 
          "type": "string"
        }, 
        "workPath": {
          "description": "The directory on the remote execution system from which the job is running.", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy Job schema", 
      "type": "object"
    }

getHistory: Get the history of this job.
========================================
``agavepy.jobs.getHistory(jobId, limit=250, offset=0)``

Parameters:
-----------
    * **jobId**: The id of the job. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Array of JobHistory objects*

**JobHistory schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/JobHistory.json", 
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
          "description": "The status of the job after this event.", 
          "type": "String"
        }
      }, 
      "required": [], 
      "title": "AgavePy JobHistory schema", 
      "type": "object"
    }

deletePermissions: Deletes all permissions on an job.
=====================================================
``agavepy.jobs.deletePermissions(jobId)``

Parameters:
-----------
    * **jobId**: The id of the job. (string)


Response:
---------
    * *String*

listPermissions: Get the permission ACL for this job.
=====================================================
``agavepy.jobs.listPermissions(jobId, limit=250, offset=0)``

Parameters:
-----------
    * **jobId**: The id of the job. (string)
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

updatePermissions: Add or update a user's permission for an application.
========================================================================
``agavepy.jobs.updatePermissions(body, jobId)``

Parameters:
-----------
    * **jobId**: The id of the job. (string)
    * **body**: The permission add or update.  (JSON, JobPermissionRequest)


**JobPermissionRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/JobPermissionRequest.json", 
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
        "username": {
          "description": "The username of the api user whose permission is to be set.", 
          "type": "string"
        }
      }, 
      "required": [
        "username", 
        "permission"
      ], 
      "title": "AgavePy JobPermissionRequest schema", 
      "type": "object"
    }

Response:
---------
    * *String*

deletePermissionsForUser: Deletes all permissions for the given user on an job.
===============================================================================
``agavepy.jobs.deletePermissionsForUser(uniqueName, username)``

Parameters:
-----------
    * **uniqueName**: The id of the application. The application id is made up of the name and version separated by a dash. (string)
    * **username**: The username of the api user associated with the permission (string)


Response:
---------
    * *None*

listPermissionsForUser: Get a specific user's permissions for a job.
====================================================================
``agavepy.jobs.listPermissionsForUser(jobId, username, limit=250, offset=0)``

Parameters:
-----------
    * **jobId**: The id of the job. (string)
    * **username**: The username of the api user associated with the permission. (string)
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

updatePermissionsForUser: Add or update a user's permission for an job.
=======================================================================
``agavepy.jobs.updatePermissionsForUser(body, jobId, username)``

Parameters:
-----------
    * **jobId**: The id of the job. (string)
    * **username**: The username of the api user associated with the permission (string)
    * **body**: The permission to update.  (JSON, JobPermissionRequest)


**JobPermissionRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/JobPermissionRequest.json", 
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
        "username": {
          "description": "The username of the api user whose permission is to be set.", 
          "type": "string"
        }
      }, 
      "required": [
        "username", 
        "permission"
      ], 
      "title": "AgavePy JobPermissionRequest schema", 
      "type": "object"
    }

Response:
---------
    * *String*

getStatus: Get the status of the job.
=====================================
``agavepy.jobs.getStatus(jobId)``

Parameters:
-----------
    * **jobId**: The id of the job. (string)


Response:
---------
    * *A single JobStatus object*

**JobStatus schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/JobStatus.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "id": {
          "description": "The unique id of the job.", 
          "type": "string"
        }, 
        "status": {
          "description": "The status of the job. Possible values are: PENDING, STAGING_INPUTS, CLEANING_UP, ARCHIVING, STAGING_JOB, FINISHED, KILLED, FAILED, STOPPED, RUNNING, PAUSED, QUEUED, SUBMITTING, STAGED, PROCESSING_INPUTS, ARCHIVING_FINISHED, ARCHIVING_FAILED", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy JobStatus schema", 
      "type": "object"
    }

listOutputs: List contents of a job's output directory.
=======================================================
``agavepy.jobs.listOutputs(jobId, filePath=None, limit=250, offset=0)``

Parameters:
-----------
    * **jobId**: The id of the job. (string)
    * **filePath**: Path to an output file or folder relative to the job output directory. This resource will follow data around as it moves from the execution system to archival storage. (string)
    * **limit**: max number of results. (integer)
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

downloadOutput: Download an output file from a specific job.
============================================================
``agavepy.jobs.downloadOutput(filePath, jobId)``

Parameters:
-----------
    * **jobId**: The id of the job. (string)
    * **filePath**: Path to an output file relative to the job output directory. (string)


Response:
---------
    * *None*

search: Find jobs matching the given attribute/value combination(s).
====================================================================
``agavepy.jobs.search(attribute, value, limit=250, offset=0)``

Parameters:
-----------
    * **attribute**: The attribute to query by. This can be any job field. (string)
    * **value**: The value of the attribute to query for. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Array of JobSummary objects*

**JobSummary schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/JobSummary.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "appId": {
          "description": "The unique name of the application being run by this job. This must be a valid application that the calling user has permission to run.", 
          "type": "string"
        }, 
        "endTime": {
          "description": "The date the job ended in ISO 8601 format.", 
          "type": "string"
        }, 
        "executionSystem": {
          "description": "The system id of the execution system.", 
          "type": "string"
        }, 
        "id": {
          "description": "The unique id of the job.", 
          "type": "string"
        }, 
        "name": {
          "description": "The name of the job.", 
          "type": "string"
        }, 
        "owner": {
          "description": "The job owner.", 
          "type": "string"
        }, 
        "startTime": {
          "description": "The date the job started in ISO 8601 format.", 
          "type": "string"
        }, 
        "status": {
          "description": "The status of the job. Possible values are: PENDING, STAGING_INPUTS, CLEANING_UP, ARCHIVING, STAGING_JOB, FINISHED, KILLED, FAILED, STOPPED, RUNNING, PAUSED, QUEUED, SUBMITTING, STAGED, PROCESSING_INPUTS, ARCHIVING_FINISHED, ARCHIVING_FAILED", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy JobSummary schema", 
      "type": "object"
    }

