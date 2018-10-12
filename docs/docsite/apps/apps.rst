****
Apps
****

Summary: Register and manage apps

add: Register and update new applications.
==========================================
``agavepy.apps.add(body)``

Parameters:
-----------
    * **body**: The description of the app to add or update.  (JSON, ApplicationRequest)


**ApplicationRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/ApplicationRequest.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "available": {
          "description": "Whether the application is available.", 
          "type": "boolean"
        }, 
        "checkpointable": {
          "description": "Whether the application supports checkpointing.", 
          "type": "boolean"
        }, 
        "defaultMaxRunTime": {
          "description": "The max execution time that should be used if none is given in a job description. Ignore if the system does not support schedulers.", 
          "type": "int"
        }, 
        "defaultMemory": {
          "description": "The default memory in GB to pass to the scheduler if none is given in the job description. This must be less than the max memory parameter in the target queue definition.", 
          "type": "string"
        }, 
        "defaultNodeCount": {
          "description": "The number of nodes that should be used if none is given in a job description. Ignore if the system does not support schedulers.", 
          "type": "string"
        }, 
        "defaultProcessors": {
          "description": "The number of processors to pass to the scheduler if none are given in the job description. This must be 1 if the app is serial.", 
          "type": "int"
        }, 
        "defaultQueue": {
          "description": "The queue on the execution system that should be used if none is given in a job description. Ignore if the system does not support schedulers.", 
          "type": "string"
        }, 
        "deploymentPath": {
          "description": "The location in the user's default storage system containing the application wrapper and dependencies.", 
          "type": "string"
        }, 
        "deploymentSystem": {
          "description": "The system id of the storage system where this app should run.", 
          "type": "string"
        }, 
        "executionSystem": {
          "description": "The system id of the execution system where this app should run.", 
          "type": "string"
        }, 
        "executionType": {
          "description": "The execution type of the application. If you're unsure, it's probably HPC.", 
          "enum": [
            "ATMOSPHERE", 
            "HPC", 
            "CONDOR", 
            "CLI"
          ], 
          "type": "string"
        }, 
        "helpURI": {
          "description": "The URL where users can go for more information about the app.", 
          "type": "string"
        }, 
        "icon": {
          "description": "The icon to associate with this app.", 
          "type": "string"
        }, 
        "inputs": {
          "description": "The inputs files for this application. ", 
          "type": "array"
        }, 
        "label": {
          "description": "The label to use when generating forms.", 
          "type": "string"
        }, 
        "longDescription": {
          "description": "The full text description of this input to use when generating forms.", 
          "type": "string"
        }, 
        "modules": {
          "description": "An array of modules to load prior to the execution of the application.", 
          "type": "array"
        }, 
        "name": {
          "description": "The name of the application. The name does not have to be unique, but the combination of name and version does.", 
          "type": "string"
        }, 
        "ontology": {
          "description": "An array of ontology values describing this application.", 
          "type": "array"
        }, 
        "outputs": {
          "description": "The outputs files for this application. ", 
          "type": "array"
        }, 
        "parallelism": {
          "description": "The parallelism type of the application. If you're unsure, it's probably SERIAL.", 
          "enum": [
            "SERIAL", 
            "PARALLEL", 
            "PTHREAD"
          ], 
          "type": "string"
        }, 
        "parameters": {
          "description": "The inputs parameters for this application. ", 
          "type": "array"
        }, 
        "shortDescription": {
          "description": "The short description of this application.", 
          "type": "string"
        }, 
        "tags": {
          "description": "An array of tags related to this application.", 
          "type": "array"
        }, 
        "templatePath": {
          "description": "The path to the wrapper script relative to the deploymentPath.", 
          "type": "string"
        }, 
        "testPath": {
          "description": "The path to the test script relative to the deploymentPath.", 
          "type": "string"
        }, 
        "version": {
          "description": "The version of the application in #.#.# format. While the version does not need to be unique, the combination of name and version does have to be unique.", 
          "type": "string"
        }
      }, 
      "required": [
        "available", 
        "inputs", 
        "executionSystem", 
        "testPath", 
        "deploymentPath", 
        "templatePath", 
        "deploymentSystem", 
        "name", 
        "parameters", 
        "executionType", 
        "version"
      ], 
      "title": "AgavePy ApplicationRequest schema", 
      "type": "object"
    }

Response:
---------
    * *A single Application object*

**Application schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/Application.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "available": {
          "description": "Whether the application is available.", 
          "type": "boolean"
        }, 
        "checkpointable": {
          "description": "Whether the application supports checkpointing.", 
          "type": "boolean"
        }, 
        "defaultMaxRunTime": {
          "description": "The max execution time that should be used if none is given in a job description. Ignore if the system does not support schedulers.", 
          "type": "string"
        }, 
        "defaultMemoryPerNode": {
          "description": "The default memory in GB to pass to the scheduler if none is given in the job description. This must be less than the max memory parameter in the target queue definition.", 
          "type": "string"
        }, 
        "defaultNodeCount": {
          "description": "The number of nodes that should be used if none is given in a job description. Ignore if the system does not support schedulers.", 
          "type": "string"
        }, 
        "defaultProcessorsPerNode": {
          "description": "The number of processors to pass to the scheduler if none are given in the job description. This must be 1 if the app is serial.", 
          "type": "string"
        }, 
        "defaultQueue": {
          "description": "The queue on the execution system that should be used if none is given in a job description. Ignore if the system does not support schedulers.", 
          "type": "string"
        }, 
        "deploymentPath": {
          "description": "The location in the user's default storage system containing the application wrapper and dependencies.", 
          "type": "string"
        }, 
        "deploymentSystem": {
          "description": "The system id of the storage system where this app should run.", 
          "type": "string"
        }, 
        "executionSystem": {
          "description": "The system id of the execution system where this app should run.", 
          "type": "string"
        }, 
        "executionType": {
          "description": "The execution type of the application. If you're unsure, it's probably HPC.", 
          "enum": [
            "ATMOSPHERE", 
            "HPC", 
            "CONDOR", 
            "CLI"
          ], 
          "type": "string"
        }, 
        "helpURI": {
          "description": "The URL where users can go for more information about the app.", 
          "type": "string"
        }, 
        "icon": {
          "description": "The icon to associate with this app.", 
          "type": "string"
        }, 
        "id": {
          "description": "Unique id of this app. Comprised of the app name-version.", 
          "type": "string"
        }, 
        "inputs": {
          "description": "The inputs files for this application. ", 
          "type": "array"
        }, 
        "isPublic": {
          "description": "Whether the application is public or private.", 
          "type": "boolean"
        }, 
        "label": {
          "description": "The label to use when generating forms.", 
          "type": "string"
        }, 
        "lastModified": {
          "description": "The date this application was last modified in ISO 8601 format.", 
          "type": "string"
        }, 
        "longDescription": {
          "description": "The full text description of this input to use when generating forms.", 
          "type": "string"
        }, 
        "modules": {
          "description": "An array of modules to load prior to the execution of the application.", 
          "type": "array"
        }, 
        "name": {
          "description": "The name of the application. The name does not have to be unique, but the combination of name and version does.", 
          "type": "string"
        }, 
        "ontology": {
          "description": "An array of ontology values describing this application.", 
          "type": "array"
        }, 
        "outputs": {
          "description": "The outputs files for this application. ", 
          "type": "array"
        }, 
        "parallelism": {
          "description": "The parallelism type of the application. If you're unsure, it's probably SERIAL.", 
          "enum": [
            "SERIAL", 
            "PARALLEL", 
            "PTHREAD"
          ], 
          "type": "string"
        }, 
        "parameters": {
          "description": "The inputs parameters for this application. ", 
          "type": "array"
        }, 
        "revision": {
          "description": "The number of times this application has been revised.", 
          "type": "integer"
        }, 
        "shortDescription": {
          "description": "The short description of this application.", 
          "type": "string"
        }, 
        "tags": {
          "description": "An array of tags related to this application.", 
          "type": "array"
        }, 
        "templatePath": {
          "description": "The path to the wrapper script relative to the deploymentPath.", 
          "type": "string"
        }, 
        "testPath": {
          "description": "The path to the test script relative to the deploymentPath.", 
          "type": "string"
        }, 
        "uuid": {
          "description": "The UUID of this application. UUID are 36 alphanumeric string.", 
          "type": "string"
        }, 
        "version": {
          "description": "The version of the application in #.#.# format. While the version does not need to be unique, the combination of name and version does have to be unique.", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy Application schema", 
      "type": "object"
    }

list: Get a list of available applications.
===========================================
``agavepy.apps.list(limit=250, offset=0, privateOnly=None, publicOnly=None)``

Parameters:
-----------
    * **publicOnly**: Whether to return only public apps. (boolean)
    * **privateOnly**: Whether to return only private apps. (boolean)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Array of ApplicationSummary objects*

**ApplicationSummary schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/ApplicationSummary.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "executionSystem": {
          "description": "The system id of the execution system where this app should run.", 
          "type": "string"
        }, 
        "id": {
          "description": "Unique id of this app. Comprised of the app name-version.", 
          "type": "string"
        }, 
        "isPublic": {
          "description": "Whether the application is public or private.", 
          "type": "boolean"
        }, 
        "lastModified": {
          "description": "The date this application was last modified in ISO 8601 format.", 
          "type": "string"
        }, 
        "name": {
          "description": "The name of the application. The name does not have to be unique, but the combination of name and version does.", 
          "type": "string"
        }, 
        "revision": {
          "description": "The number of times this application has been revised.", 
          "type": "integer"
        }, 
        "shortDescription": {
          "description": "The short description of this application.", 
          "type": "string"
        }, 
        "version": {
          "description": "The version of the application in #.#.# format. While the version does not need to be unique, the combination of name and version does have to be unique.", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy ApplicationSummary schema", 
      "type": "object"
    }

delete: Deletes an application.
===============================
``agavepy.apps.delete(appId)``

Parameters:
-----------
    * **appId**: The id of the application. The application id is made up of the name and version separated by a dash. (string)


Response:
---------
    * *String*

get: Get details of an application by it's unique id.
=====================================================
``agavepy.apps.get(appId)``

Parameters:
-----------
    * **appId**: The id of the application. The application id is made up of the name and version separated by a dash. (string)


Response:
---------
    * *A single Application object*

**Application schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/Application.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "available": {
          "description": "Whether the application is available.", 
          "type": "boolean"
        }, 
        "checkpointable": {
          "description": "Whether the application supports checkpointing.", 
          "type": "boolean"
        }, 
        "defaultMaxRunTime": {
          "description": "The max execution time that should be used if none is given in a job description. Ignore if the system does not support schedulers.", 
          "type": "string"
        }, 
        "defaultMemoryPerNode": {
          "description": "The default memory in GB to pass to the scheduler if none is given in the job description. This must be less than the max memory parameter in the target queue definition.", 
          "type": "string"
        }, 
        "defaultNodeCount": {
          "description": "The number of nodes that should be used if none is given in a job description. Ignore if the system does not support schedulers.", 
          "type": "string"
        }, 
        "defaultProcessorsPerNode": {
          "description": "The number of processors to pass to the scheduler if none are given in the job description. This must be 1 if the app is serial.", 
          "type": "string"
        }, 
        "defaultQueue": {
          "description": "The queue on the execution system that should be used if none is given in a job description. Ignore if the system does not support schedulers.", 
          "type": "string"
        }, 
        "deploymentPath": {
          "description": "The location in the user's default storage system containing the application wrapper and dependencies.", 
          "type": "string"
        }, 
        "deploymentSystem": {
          "description": "The system id of the storage system where this app should run.", 
          "type": "string"
        }, 
        "executionSystem": {
          "description": "The system id of the execution system where this app should run.", 
          "type": "string"
        }, 
        "executionType": {
          "description": "The execution type of the application. If you're unsure, it's probably HPC.", 
          "enum": [
            "ATMOSPHERE", 
            "HPC", 
            "CONDOR", 
            "CLI"
          ], 
          "type": "string"
        }, 
        "helpURI": {
          "description": "The URL where users can go for more information about the app.", 
          "type": "string"
        }, 
        "icon": {
          "description": "The icon to associate with this app.", 
          "type": "string"
        }, 
        "id": {
          "description": "Unique id of this app. Comprised of the app name-version.", 
          "type": "string"
        }, 
        "inputs": {
          "description": "The inputs files for this application. ", 
          "type": "array"
        }, 
        "isPublic": {
          "description": "Whether the application is public or private.", 
          "type": "boolean"
        }, 
        "label": {
          "description": "The label to use when generating forms.", 
          "type": "string"
        }, 
        "lastModified": {
          "description": "The date this application was last modified in ISO 8601 format.", 
          "type": "string"
        }, 
        "longDescription": {
          "description": "The full text description of this input to use when generating forms.", 
          "type": "string"
        }, 
        "modules": {
          "description": "An array of modules to load prior to the execution of the application.", 
          "type": "array"
        }, 
        "name": {
          "description": "The name of the application. The name does not have to be unique, but the combination of name and version does.", 
          "type": "string"
        }, 
        "ontology": {
          "description": "An array of ontology values describing this application.", 
          "type": "array"
        }, 
        "outputs": {
          "description": "The outputs files for this application. ", 
          "type": "array"
        }, 
        "parallelism": {
          "description": "The parallelism type of the application. If you're unsure, it's probably SERIAL.", 
          "enum": [
            "SERIAL", 
            "PARALLEL", 
            "PTHREAD"
          ], 
          "type": "string"
        }, 
        "parameters": {
          "description": "The inputs parameters for this application. ", 
          "type": "array"
        }, 
        "revision": {
          "description": "The number of times this application has been revised.", 
          "type": "integer"
        }, 
        "shortDescription": {
          "description": "The short description of this application.", 
          "type": "string"
        }, 
        "tags": {
          "description": "An array of tags related to this application.", 
          "type": "array"
        }, 
        "templatePath": {
          "description": "The path to the wrapper script relative to the deploymentPath.", 
          "type": "string"
        }, 
        "testPath": {
          "description": "The path to the test script relative to the deploymentPath.", 
          "type": "string"
        }, 
        "uuid": {
          "description": "The UUID of this application. UUID are 36 alphanumeric string.", 
          "type": "string"
        }, 
        "version": {
          "description": "The version of the application in #.#.# format. While the version does not need to be unique, the combination of name and version does have to be unique.", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy Application schema", 
      "type": "object"
    }

manage: Edit an application.
============================
``agavepy.apps.manage(appId, body)``

Parameters:
-----------
    * **appId**: The id of the application. The application id is made up of the name and version separated by a dash. (string)
    * **body**: The operation to perform. (JSON, ApplicationOperationRequest)


**ApplicationOperationRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/ApplicationOperationRequest.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "action": {
          "description": "Action to perform on the file or folder.", 
          "enum": [
            "publish", 
            "clone"
          ], 
          "type": "string"
        }, 
        "deploymentPath": {
          "description": "Path to the on cloned app's deployment folder on its storage system. Only used with the clone action.", 
          "type": "string"
        }, 
        "executionSystem": {
          "description": "System on which the clone apps should run. Only used with the clone action.", 
          "type": "string"
        }, 
        "name": {
          "description": "Name of cloned app. Only used with the clone action.", 
          "type": "string"
        }, 
        "storageSystem": {
          "description": "Storage system on which the cloned app's assets resides. Only used with the clone action.", 
          "type": "string"
        }, 
        "version": {
          "description": "Version of the cloned app. Only used with the clone action.", 
          "type": "string"
        }
      }, 
      "required": [
        "action"
      ], 
      "title": "AgavePy ApplicationOperationRequest schema", 
      "type": "object"
    }

Response:
---------
    * *A single Application object*

**Application schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/Application.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "available": {
          "description": "Whether the application is available.", 
          "type": "boolean"
        }, 
        "checkpointable": {
          "description": "Whether the application supports checkpointing.", 
          "type": "boolean"
        }, 
        "defaultMaxRunTime": {
          "description": "The max execution time that should be used if none is given in a job description. Ignore if the system does not support schedulers.", 
          "type": "string"
        }, 
        "defaultMemoryPerNode": {
          "description": "The default memory in GB to pass to the scheduler if none is given in the job description. This must be less than the max memory parameter in the target queue definition.", 
          "type": "string"
        }, 
        "defaultNodeCount": {
          "description": "The number of nodes that should be used if none is given in a job description. Ignore if the system does not support schedulers.", 
          "type": "string"
        }, 
        "defaultProcessorsPerNode": {
          "description": "The number of processors to pass to the scheduler if none are given in the job description. This must be 1 if the app is serial.", 
          "type": "string"
        }, 
        "defaultQueue": {
          "description": "The queue on the execution system that should be used if none is given in a job description. Ignore if the system does not support schedulers.", 
          "type": "string"
        }, 
        "deploymentPath": {
          "description": "The location in the user's default storage system containing the application wrapper and dependencies.", 
          "type": "string"
        }, 
        "deploymentSystem": {
          "description": "The system id of the storage system where this app should run.", 
          "type": "string"
        }, 
        "executionSystem": {
          "description": "The system id of the execution system where this app should run.", 
          "type": "string"
        }, 
        "executionType": {
          "description": "The execution type of the application. If you're unsure, it's probably HPC.", 
          "enum": [
            "ATMOSPHERE", 
            "HPC", 
            "CONDOR", 
            "CLI"
          ], 
          "type": "string"
        }, 
        "helpURI": {
          "description": "The URL where users can go for more information about the app.", 
          "type": "string"
        }, 
        "icon": {
          "description": "The icon to associate with this app.", 
          "type": "string"
        }, 
        "id": {
          "description": "Unique id of this app. Comprised of the app name-version.", 
          "type": "string"
        }, 
        "inputs": {
          "description": "The inputs files for this application. ", 
          "type": "array"
        }, 
        "isPublic": {
          "description": "Whether the application is public or private.", 
          "type": "boolean"
        }, 
        "label": {
          "description": "The label to use when generating forms.", 
          "type": "string"
        }, 
        "lastModified": {
          "description": "The date this application was last modified in ISO 8601 format.", 
          "type": "string"
        }, 
        "longDescription": {
          "description": "The full text description of this input to use when generating forms.", 
          "type": "string"
        }, 
        "modules": {
          "description": "An array of modules to load prior to the execution of the application.", 
          "type": "array"
        }, 
        "name": {
          "description": "The name of the application. The name does not have to be unique, but the combination of name and version does.", 
          "type": "string"
        }, 
        "ontology": {
          "description": "An array of ontology values describing this application.", 
          "type": "array"
        }, 
        "outputs": {
          "description": "The outputs files for this application. ", 
          "type": "array"
        }, 
        "parallelism": {
          "description": "The parallelism type of the application. If you're unsure, it's probably SERIAL.", 
          "enum": [
            "SERIAL", 
            "PARALLEL", 
            "PTHREAD"
          ], 
          "type": "string"
        }, 
        "parameters": {
          "description": "The inputs parameters for this application. ", 
          "type": "array"
        }, 
        "revision": {
          "description": "The number of times this application has been revised.", 
          "type": "integer"
        }, 
        "shortDescription": {
          "description": "The short description of this application.", 
          "type": "string"
        }, 
        "tags": {
          "description": "An array of tags related to this application.", 
          "type": "array"
        }, 
        "templatePath": {
          "description": "The path to the wrapper script relative to the deploymentPath.", 
          "type": "string"
        }, 
        "testPath": {
          "description": "The path to the test script relative to the deploymentPath.", 
          "type": "string"
        }, 
        "uuid": {
          "description": "The UUID of this application. UUID are 36 alphanumeric string.", 
          "type": "string"
        }, 
        "version": {
          "description": "The version of the application in #.#.# format. While the version does not need to be unique, the combination of name and version does have to be unique.", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy Application schema", 
      "type": "object"
    }

update: Update an application.
==============================
``agavepy.apps.update(appId, body)``

Parameters:
-----------
    * **appId**: The id of the application. The application id is made up of the name and version separated by a dash. (string)
    * **body**: The description of the app to add or update.  (JSON, ApplicationRequest)


**ApplicationRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/ApplicationRequest.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "available": {
          "description": "Whether the application is available.", 
          "type": "boolean"
        }, 
        "checkpointable": {
          "description": "Whether the application supports checkpointing.", 
          "type": "boolean"
        }, 
        "defaultMaxRunTime": {
          "description": "The max execution time that should be used if none is given in a job description. Ignore if the system does not support schedulers.", 
          "type": "int"
        }, 
        "defaultMemory": {
          "description": "The default memory in GB to pass to the scheduler if none is given in the job description. This must be less than the max memory parameter in the target queue definition.", 
          "type": "string"
        }, 
        "defaultNodeCount": {
          "description": "The number of nodes that should be used if none is given in a job description. Ignore if the system does not support schedulers.", 
          "type": "string"
        }, 
        "defaultProcessors": {
          "description": "The number of processors to pass to the scheduler if none are given in the job description. This must be 1 if the app is serial.", 
          "type": "int"
        }, 
        "defaultQueue": {
          "description": "The queue on the execution system that should be used if none is given in a job description. Ignore if the system does not support schedulers.", 
          "type": "string"
        }, 
        "deploymentPath": {
          "description": "The location in the user's default storage system containing the application wrapper and dependencies.", 
          "type": "string"
        }, 
        "deploymentSystem": {
          "description": "The system id of the storage system where this app should run.", 
          "type": "string"
        }, 
        "executionSystem": {
          "description": "The system id of the execution system where this app should run.", 
          "type": "string"
        }, 
        "executionType": {
          "description": "The execution type of the application. If you're unsure, it's probably HPC.", 
          "enum": [
            "ATMOSPHERE", 
            "HPC", 
            "CONDOR", 
            "CLI"
          ], 
          "type": "string"
        }, 
        "helpURI": {
          "description": "The URL where users can go for more information about the app.", 
          "type": "string"
        }, 
        "icon": {
          "description": "The icon to associate with this app.", 
          "type": "string"
        }, 
        "inputs": {
          "description": "The inputs files for this application. ", 
          "type": "array"
        }, 
        "label": {
          "description": "The label to use when generating forms.", 
          "type": "string"
        }, 
        "longDescription": {
          "description": "The full text description of this input to use when generating forms.", 
          "type": "string"
        }, 
        "modules": {
          "description": "An array of modules to load prior to the execution of the application.", 
          "type": "array"
        }, 
        "name": {
          "description": "The name of the application. The name does not have to be unique, but the combination of name and version does.", 
          "type": "string"
        }, 
        "ontology": {
          "description": "An array of ontology values describing this application.", 
          "type": "array"
        }, 
        "outputs": {
          "description": "The outputs files for this application. ", 
          "type": "array"
        }, 
        "parallelism": {
          "description": "The parallelism type of the application. If you're unsure, it's probably SERIAL.", 
          "enum": [
            "SERIAL", 
            "PARALLEL", 
            "PTHREAD"
          ], 
          "type": "string"
        }, 
        "parameters": {
          "description": "The inputs parameters for this application. ", 
          "type": "array"
        }, 
        "shortDescription": {
          "description": "The short description of this application.", 
          "type": "string"
        }, 
        "tags": {
          "description": "An array of tags related to this application.", 
          "type": "array"
        }, 
        "templatePath": {
          "description": "The path to the wrapper script relative to the deploymentPath.", 
          "type": "string"
        }, 
        "testPath": {
          "description": "The path to the test script relative to the deploymentPath.", 
          "type": "string"
        }, 
        "version": {
          "description": "The version of the application in #.#.# format. While the version does not need to be unique, the combination of name and version does have to be unique.", 
          "type": "string"
        }
      }, 
      "required": [
        "available", 
        "inputs", 
        "executionSystem", 
        "testPath", 
        "deploymentPath", 
        "templatePath", 
        "deploymentSystem", 
        "name", 
        "parameters", 
        "executionType", 
        "version"
      ], 
      "title": "AgavePy ApplicationRequest schema", 
      "type": "object"
    }

Response:
---------
    * *A single Application object*

**Application schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/Application.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "available": {
          "description": "Whether the application is available.", 
          "type": "boolean"
        }, 
        "checkpointable": {
          "description": "Whether the application supports checkpointing.", 
          "type": "boolean"
        }, 
        "defaultMaxRunTime": {
          "description": "The max execution time that should be used if none is given in a job description. Ignore if the system does not support schedulers.", 
          "type": "string"
        }, 
        "defaultMemoryPerNode": {
          "description": "The default memory in GB to pass to the scheduler if none is given in the job description. This must be less than the max memory parameter in the target queue definition.", 
          "type": "string"
        }, 
        "defaultNodeCount": {
          "description": "The number of nodes that should be used if none is given in a job description. Ignore if the system does not support schedulers.", 
          "type": "string"
        }, 
        "defaultProcessorsPerNode": {
          "description": "The number of processors to pass to the scheduler if none are given in the job description. This must be 1 if the app is serial.", 
          "type": "string"
        }, 
        "defaultQueue": {
          "description": "The queue on the execution system that should be used if none is given in a job description. Ignore if the system does not support schedulers.", 
          "type": "string"
        }, 
        "deploymentPath": {
          "description": "The location in the user's default storage system containing the application wrapper and dependencies.", 
          "type": "string"
        }, 
        "deploymentSystem": {
          "description": "The system id of the storage system where this app should run.", 
          "type": "string"
        }, 
        "executionSystem": {
          "description": "The system id of the execution system where this app should run.", 
          "type": "string"
        }, 
        "executionType": {
          "description": "The execution type of the application. If you're unsure, it's probably HPC.", 
          "enum": [
            "ATMOSPHERE", 
            "HPC", 
            "CONDOR", 
            "CLI"
          ], 
          "type": "string"
        }, 
        "helpURI": {
          "description": "The URL where users can go for more information about the app.", 
          "type": "string"
        }, 
        "icon": {
          "description": "The icon to associate with this app.", 
          "type": "string"
        }, 
        "id": {
          "description": "Unique id of this app. Comprised of the app name-version.", 
          "type": "string"
        }, 
        "inputs": {
          "description": "The inputs files for this application. ", 
          "type": "array"
        }, 
        "isPublic": {
          "description": "Whether the application is public or private.", 
          "type": "boolean"
        }, 
        "label": {
          "description": "The label to use when generating forms.", 
          "type": "string"
        }, 
        "lastModified": {
          "description": "The date this application was last modified in ISO 8601 format.", 
          "type": "string"
        }, 
        "longDescription": {
          "description": "The full text description of this input to use when generating forms.", 
          "type": "string"
        }, 
        "modules": {
          "description": "An array of modules to load prior to the execution of the application.", 
          "type": "array"
        }, 
        "name": {
          "description": "The name of the application. The name does not have to be unique, but the combination of name and version does.", 
          "type": "string"
        }, 
        "ontology": {
          "description": "An array of ontology values describing this application.", 
          "type": "array"
        }, 
        "outputs": {
          "description": "The outputs files for this application. ", 
          "type": "array"
        }, 
        "parallelism": {
          "description": "The parallelism type of the application. If you're unsure, it's probably SERIAL.", 
          "enum": [
            "SERIAL", 
            "PARALLEL", 
            "PTHREAD"
          ], 
          "type": "string"
        }, 
        "parameters": {
          "description": "The inputs parameters for this application. ", 
          "type": "array"
        }, 
        "revision": {
          "description": "The number of times this application has been revised.", 
          "type": "integer"
        }, 
        "shortDescription": {
          "description": "The short description of this application.", 
          "type": "string"
        }, 
        "tags": {
          "description": "An array of tags related to this application.", 
          "type": "array"
        }, 
        "templatePath": {
          "description": "The path to the wrapper script relative to the deploymentPath.", 
          "type": "string"
        }, 
        "testPath": {
          "description": "The path to the test script relative to the deploymentPath.", 
          "type": "string"
        }, 
        "uuid": {
          "description": "The UUID of this application. UUID are 36 alphanumeric string.", 
          "type": "string"
        }, 
        "version": {
          "description": "The version of the application in #.#.# format. While the version does not need to be unique, the combination of name and version does have to be unique.", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy Application schema", 
      "type": "object"
    }

deletePermissions: Deletes all permissions on an application.
=============================================================
``agavepy.apps.deletePermissions(appId)``

Parameters:
-----------
    * **appId**: The id of the application. The application id is made up of the name and version separated by a dash. (string)


Response:
---------
    * *String*

listPermissions: Get the permission ACL for this application.
=============================================================
``agavepy.apps.listPermissions(appId, limit=250, offset=0)``

Parameters:
-----------
    * **appId**: The id of the application. The application id is made up of the name and version separated by a dash. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Array of ApplicationPermission objects*

**ApplicationPermission schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/ApplicationPermission.json", 
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
      "title": "AgavePy ApplicationPermission schema", 
      "type": "object"
    }

updateApplicationPermissions: Add or update a user's permission for an application.
===================================================================================
``agavepy.apps.updateApplicationPermissions(appId, body)``

Parameters:
-----------
    * **appId**: The id of the application. The application id is made up of the name and version separated by a dash. (string)
    * **body**: The permission add or update.  (JSON, ApplicationPermissionRequest)


**ApplicationPermissionRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/ApplicationPermissionRequest.json", 
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
      "title": "AgavePy ApplicationPermissionRequest schema", 
      "type": "object"
    }

Response:
---------
    * *String*

deletePermissionsForUser: Deletes all permissions for the given user on an application.
=======================================================================================
``agavepy.apps.deletePermissionsForUser(appId, username)``

Parameters:
-----------
    * **appId**: The id of the application. The application id is made up of the name and version separated by a dash. (string)
    * **username**: The username of the api user associated with the permission (string)


Response:
---------
    * *String*

listPermissionsForUser: Get a specific user's permissions for an application.
=============================================================================
``agavepy.apps.listPermissionsForUser(appId, username, limit=250, offset=0)``

Parameters:
-----------
    * **appId**: The id of the application. The application id is made up of the name and version separated by a dash. (string)
    * **username**: The username of the api user associated with the permission. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Array of ApplicationPermission objects*

**ApplicationPermission schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/ApplicationPermission.json", 
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
      "title": "AgavePy ApplicationPermission schema", 
      "type": "object"
    }

updatePermissionsForUser: Add or update a user's permission for an application.
===============================================================================
``agavepy.apps.updatePermissionsForUser(appId, body, username)``

Parameters:
-----------
    * **appId**: The id of the application. The application id is made up of the name and version separated by a dash. (string)
    * **username**: The username of the api user associated with the permission (string)
    * **body**: The permission add or update.  (JSON, ApplicationPermissionRequest)


**ApplicationPermissionRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/ApplicationPermissionRequest.json", 
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
      "title": "AgavePy ApplicationPermissionRequest schema", 
      "type": "object"
    }

Response:
---------
    * *String*

listByName: Get a list of applications with the given name.
===========================================================
``agavepy.apps.listByName(name, limit=250, offset=0, privateOnly=None, publicOnly=None)``

Parameters:
-----------
    * **name**: The name of the application. This should not include the version number. (string)
    * **publicOnly**: Whether to return only public apps. (boolean)
    * **privateOnly**: Whether to return only private apps. (boolean)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Array of ApplicationSummary objects*

**ApplicationSummary schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/ApplicationSummary.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "executionSystem": {
          "description": "The system id of the execution system where this app should run.", 
          "type": "string"
        }, 
        "id": {
          "description": "Unique id of this app. Comprised of the app name-version.", 
          "type": "string"
        }, 
        "isPublic": {
          "description": "Whether the application is public or private.", 
          "type": "boolean"
        }, 
        "lastModified": {
          "description": "The date this application was last modified in ISO 8601 format.", 
          "type": "string"
        }, 
        "name": {
          "description": "The name of the application. The name does not have to be unique, but the combination of name and version does.", 
          "type": "string"
        }, 
        "revision": {
          "description": "The number of times this application has been revised.", 
          "type": "integer"
        }, 
        "shortDescription": {
          "description": "The short description of this application.", 
          "type": "string"
        }, 
        "version": {
          "description": "The version of the application in #.#.# format. While the version does not need to be unique, the combination of name and version does have to be unique.", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy ApplicationSummary schema", 
      "type": "object"
    }

listBySystemId: Get a list of applications with the given systemId as their executionHost.
==========================================================================================
``agavepy.apps.listBySystemId(systemId, limit=250, offset=0, privateOnly=None, publicOnly=None)``

Parameters:
-----------
    * **systemId**: The system in question (string)
    * **publicOnly**: Whether to return only public apps. (boolean)
    * **privateOnly**: Whether to return only private apps. (boolean)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Array of ApplicationSummary objects*

**ApplicationSummary schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/ApplicationSummary.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "executionSystem": {
          "description": "The system id of the execution system where this app should run.", 
          "type": "string"
        }, 
        "id": {
          "description": "Unique id of this app. Comprised of the app name-version.", 
          "type": "string"
        }, 
        "isPublic": {
          "description": "Whether the application is public or private.", 
          "type": "boolean"
        }, 
        "lastModified": {
          "description": "The date this application was last modified in ISO 8601 format.", 
          "type": "string"
        }, 
        "name": {
          "description": "The name of the application. The name does not have to be unique, but the combination of name and version does.", 
          "type": "string"
        }, 
        "revision": {
          "description": "The number of times this application has been revised.", 
          "type": "integer"
        }, 
        "shortDescription": {
          "description": "The short description of this application.", 
          "type": "string"
        }, 
        "version": {
          "description": "The version of the application in #.#.# format. While the version does not need to be unique, the combination of name and version does have to be unique.", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy ApplicationSummary schema", 
      "type": "object"
    }

