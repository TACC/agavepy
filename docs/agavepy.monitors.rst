****************
agavepy.monitors
****************

Summary: Create and manage system monitors

add: Update or Add new Monitor.
===============================
``agavepy.monitors.add(body)``

Parameters:
-----------
    * **body**: The description of the app to add or update. This can be either a file upload or json posted to the request body. (JSON, MonitorRequest)


**MonitorRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/MonitorRequest.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "active": {
          "description": "Whether this monitor is currently active.", 
          "type": "boolean"
        }, 
        "frequency": {
          "description": "The interval in minutes on which this monitor will run. Minimum is 5. Default is 720.", 
          "type": "integer"
        }, 
        "internalUsername": {
          "description": "Internal user account used to perform the check.", 
          "type": "string"
        }, 
        "target": {
          "description": "The id of the sytem to be monitored. This must be an active system registered with the Systems service.", 
          "type": "string"
        }, 
        "updateSystemStatus": {
          "description": "Whether this Monitor should update the system status when the results change. You must have the ADMIN role on the target system to use this feature.", 
          "type": "boolean"
        }
      }, 
      "required": [
        "active", 
        "frequency", 
        "target"
      ], 
      "title": "AgavePy MonitorRequest schema", 
      "type": "object"
    }

Response:
---------
    * *A single MonitorDescription object*

**MonitorDescription schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/MonitorDescription.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "active": {
          "description": "Whether this monitor is currently active.", 
          "type": "boolean"
        }, 
        "created": {
          "description": "A timestamp indicating when this Monitor was created.", 
          "type": "string"
        }, 
        "frequency": {
          "description": "The interval in minutes on which this monitor will run. Minimum is 5. Default is 720.", 
          "type": "integer"
        }, 
        "id": {
          "description": "The UUID for this monitor.", 
          "type": "string"
        }, 
        "internalUsername": {
          "description": "Internal user account used to perform the check.", 
          "type": "string"
        }, 
        "lastCheck": {
          "description": "The results of the last check run by this monitor.", 
          "type": "MonitorCheck"
        }, 
        "lastSuccess": {
          "description": "A timestamp indicating the last time this Monitor succeeded in ISO 8601 format", 
          "type": "string"
        }, 
        "lastUpdated": {
          "description": "A timestamp indicating the last time this Monitor was updated in ISO 8601 format", 
          "type": "string"
        }, 
        "nextUpdate": {
          "description": "A timestamp indicating the next time this Monitor will be run in ISO 8601 format", 
          "type": "string"
        }, 
        "owner": {
          "description": "The API user who owns this Monitor.", 
          "type": "string"
        }, 
        "target": {
          "description": "The id of the sytem to be monitored. This must be an active system registered with the Systems service.", 
          "type": "boolean"
        }, 
        "updateSystemStatus": {
          "description": "Whether this Monitor should update the system status when the results change. You must have the ADMIN role on the target system to use this feature.", 
          "type": "boolean"
        }
      }, 
      "required": [], 
      "title": "AgavePy MonitorDescription schema", 
      "type": "object"
    }

list: Retrieve Monitor for a specific resource.
===============================================
``agavepy.monitors.list(active=None, limit=250, offset=0, target=None)``

Parameters:
-----------
    * **target**: The target to search for. (string)
    * **active**: Filter by monitors that are active or inactive. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Array of MonitorDescription objects*

**MonitorDescription schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/MonitorDescription.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "active": {
          "description": "Whether this monitor is currently active.", 
          "type": "boolean"
        }, 
        "created": {
          "description": "A timestamp indicating when this Monitor was created.", 
          "type": "string"
        }, 
        "frequency": {
          "description": "The interval in minutes on which this monitor will run. Minimum is 5. Default is 720.", 
          "type": "integer"
        }, 
        "id": {
          "description": "The UUID for this monitor.", 
          "type": "string"
        }, 
        "internalUsername": {
          "description": "Internal user account used to perform the check.", 
          "type": "string"
        }, 
        "lastCheck": {
          "description": "The results of the last check run by this monitor.", 
          "type": "MonitorCheck"
        }, 
        "lastSuccess": {
          "description": "A timestamp indicating the last time this Monitor succeeded in ISO 8601 format", 
          "type": "string"
        }, 
        "lastUpdated": {
          "description": "A timestamp indicating the last time this Monitor was updated in ISO 8601 format", 
          "type": "string"
        }, 
        "nextUpdate": {
          "description": "A timestamp indicating the next time this Monitor will be run in ISO 8601 format", 
          "type": "string"
        }, 
        "owner": {
          "description": "The API user who owns this Monitor.", 
          "type": "string"
        }, 
        "target": {
          "description": "The id of the sytem to be monitored. This must be an active system registered with the Systems service.", 
          "type": "boolean"
        }, 
        "updateSystemStatus": {
          "description": "Whether this Monitor should update the system status when the results change. You must have the ADMIN role on the target system to use this feature.", 
          "type": "boolean"
        }
      }, 
      "required": [], 
      "title": "AgavePy MonitorDescription schema", 
      "type": "object"
    }

delete: Deletes a monitor.
==========================
``agavepy.monitors.delete(monitorId)``

Parameters:
-----------
    * **monitorId**: The id of the monitor (string)


Response:
---------
    * *A single EmptyMonitor object*

**EmptyMonitor schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/EmptyMonitor.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {}, 
      "required": [], 
      "title": "AgavePy EmptyMonitor schema", 
      "type": "object"
    }

get: Retrieve a specific monitor.
=================================
``agavepy.monitors.get(monitorId)``

Parameters:
-----------
    * **monitorId**: The id of the monitor (string)


Response:
---------
    * *A single MonitorDescription object*

**MonitorDescription schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/MonitorDescription.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "active": {
          "description": "Whether this monitor is currently active.", 
          "type": "boolean"
        }, 
        "created": {
          "description": "A timestamp indicating when this Monitor was created.", 
          "type": "string"
        }, 
        "frequency": {
          "description": "The interval in minutes on which this monitor will run. Minimum is 5. Default is 720.", 
          "type": "integer"
        }, 
        "id": {
          "description": "The UUID for this monitor.", 
          "type": "string"
        }, 
        "internalUsername": {
          "description": "Internal user account used to perform the check.", 
          "type": "string"
        }, 
        "lastCheck": {
          "description": "The results of the last check run by this monitor.", 
          "type": "MonitorCheck"
        }, 
        "lastSuccess": {
          "description": "A timestamp indicating the last time this Monitor succeeded in ISO 8601 format", 
          "type": "string"
        }, 
        "lastUpdated": {
          "description": "A timestamp indicating the last time this Monitor was updated in ISO 8601 format", 
          "type": "string"
        }, 
        "nextUpdate": {
          "description": "A timestamp indicating the next time this Monitor will be run in ISO 8601 format", 
          "type": "string"
        }, 
        "owner": {
          "description": "The API user who owns this Monitor.", 
          "type": "string"
        }, 
        "target": {
          "description": "The id of the sytem to be monitored. This must be an active system registered with the Systems service.", 
          "type": "boolean"
        }, 
        "updateSystemStatus": {
          "description": "Whether this Monitor should update the system status when the results change. You must have the ADMIN role on the target system to use this feature.", 
          "type": "boolean"
        }
      }, 
      "required": [], 
      "title": "AgavePy MonitorDescription schema", 
      "type": "object"
    }

update: Updates an existing monitor.
====================================
``agavepy.monitors.update(body)``

Parameters:
-----------
    * **body**: The description of the app to add or update. This can be either a file upload or json posted to the request body. (JSON, MonitorRequest)


**MonitorRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/MonitorRequest.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "active": {
          "description": "Whether this monitor is currently active.", 
          "type": "boolean"
        }, 
        "frequency": {
          "description": "The interval in minutes on which this monitor will run. Minimum is 5. Default is 720.", 
          "type": "integer"
        }, 
        "internalUsername": {
          "description": "Internal user account used to perform the check.", 
          "type": "string"
        }, 
        "target": {
          "description": "The id of the sytem to be monitored. This must be an active system registered with the Systems service.", 
          "type": "string"
        }, 
        "updateSystemStatus": {
          "description": "Whether this Monitor should update the system status when the results change. You must have the ADMIN role on the target system to use this feature.", 
          "type": "boolean"
        }
      }, 
      "required": [
        "active", 
        "frequency", 
        "target"
      ], 
      "title": "AgavePy MonitorRequest schema", 
      "type": "object"
    }

Response:
---------
    * *A single MonitorDescription object*

**MonitorDescription schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/MonitorDescription.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "active": {
          "description": "Whether this monitor is currently active.", 
          "type": "boolean"
        }, 
        "created": {
          "description": "A timestamp indicating when this Monitor was created.", 
          "type": "string"
        }, 
        "frequency": {
          "description": "The interval in minutes on which this monitor will run. Minimum is 5. Default is 720.", 
          "type": "integer"
        }, 
        "id": {
          "description": "The UUID for this monitor.", 
          "type": "string"
        }, 
        "internalUsername": {
          "description": "Internal user account used to perform the check.", 
          "type": "string"
        }, 
        "lastCheck": {
          "description": "The results of the last check run by this monitor.", 
          "type": "MonitorCheck"
        }, 
        "lastSuccess": {
          "description": "A timestamp indicating the last time this Monitor succeeded in ISO 8601 format", 
          "type": "string"
        }, 
        "lastUpdated": {
          "description": "A timestamp indicating the last time this Monitor was updated in ISO 8601 format", 
          "type": "string"
        }, 
        "nextUpdate": {
          "description": "A timestamp indicating the next time this Monitor will be run in ISO 8601 format", 
          "type": "string"
        }, 
        "owner": {
          "description": "The API user who owns this Monitor.", 
          "type": "string"
        }, 
        "target": {
          "description": "The id of the sytem to be monitored. This must be an active system registered with the Systems service.", 
          "type": "boolean"
        }, 
        "updateSystemStatus": {
          "description": "Whether this Monitor should update the system status when the results change. You must have the ADMIN role on the target system to use this feature.", 
          "type": "boolean"
        }
      }, 
      "required": [], 
      "title": "AgavePy MonitorDescription schema", 
      "type": "object"
    }

listChecks: Retrieve monitor checks for a specific resource.
============================================================
``agavepy.monitors.listChecks(monitorId, endDate=None, limit=250, offset=0, result=None, startDate=None)``

Parameters:
-----------
    * **monitorId**: The id of the monitor (string)
    * **startDate**: A timestamp indicating the earliest time of the first monitor check in ISO 8601 format (string)
    * **endDate**: A timestamp indicating the latest time of the first monitor check in ISO 8601 format (string)
    * **result**: A timestamp indicating the latest time of the first monitor check in ISO 8601 format (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Array of MonitorCheck objects*

**MonitorCheck schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/MonitorCheck.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "created": {
          "description": "A timestamp indicating when this monitor check was created.", 
          "type": "string"
        }, 
        "id": {
          "description": "The UUID for this monitor check.", 
          "type": "string"
        }, 
        "message": {
          "description": "The error message if this monitor check failed.", 
          "type": "string"
        }, 
        "result": {
          "description": "The results of this monitor check.", 
          "enum": [
            "PASSED", 
            "FAILED", 
            "UNKNOWN"
          ], 
          "type": "string"
        }
      }, 
      "required": [
        "result", 
        "created"
      ], 
      "title": "AgavePy MonitorCheck schema", 
      "type": "object"
    }

runCheck: Forces a monitor check to run.
========================================
``agavepy.monitors.runCheck(monitorId)``

Parameters:
-----------
    * **monitorId**: The id of the monitor (string)


Response:
---------
    * *A single MonitorCheck object*

**MonitorCheck schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/MonitorCheck.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "created": {
          "description": "A timestamp indicating when this monitor check was created.", 
          "type": "string"
        }, 
        "id": {
          "description": "The UUID for this monitor check.", 
          "type": "string"
        }, 
        "message": {
          "description": "The error message if this monitor check failed.", 
          "type": "string"
        }, 
        "result": {
          "description": "The results of this monitor check.", 
          "enum": [
            "PASSED", 
            "FAILED", 
            "UNKNOWN"
          ], 
          "type": "string"
        }
      }, 
      "required": [
        "result", 
        "created"
      ], 
      "title": "AgavePy MonitorCheck schema", 
      "type": "object"
    }

getCheck: Retrieve a specific monitor check
===========================================
``agavepy.monitors.getCheck(checkId, monitorId)``

Parameters:
-----------
    * **monitorId**: The id of the monitor (string)
    * **checkId**: The id of the monitor check (string)


Response:
---------
    * *A single MonitorCheck object*

**MonitorCheck schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/MonitorCheck.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "created": {
          "description": "A timestamp indicating when this monitor check was created.", 
          "type": "string"
        }, 
        "id": {
          "description": "The UUID for this monitor check.", 
          "type": "string"
        }, 
        "message": {
          "description": "The error message if this monitor check failed.", 
          "type": "string"
        }, 
        "result": {
          "description": "The results of this monitor check.", 
          "enum": [
            "PASSED", 
            "FAILED", 
            "UNKNOWN"
          ], 
          "type": "string"
        }
      }, 
      "required": [
        "result", 
        "created"
      ], 
      "title": "AgavePy MonitorCheck schema", 
      "type": "object"
    }

