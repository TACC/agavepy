********
monitors
********

Summary: Create and manage system monitors

add: Update or Add new Monitor.
===============================
``monitors.add(body=<BODY>)``

Keyword Args:
-------------
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

list: Retrieve Monitor for a specific resource.
===============================================
``monitors.list(active=None, limit=250, offset=0, target=None)``

Keyword Args:
-------------
    * **target**: The target to search for. (string)
    * **active**: Filter by monitors that are active or inactive. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Array of MonitorDescription objects*

delete: Deletes a monitor.
==========================
``monitors.delete(monitorId=<MONITORID>)``

Keyword Args:
-------------
    * **monitorId**: The id of the monitor (string)


Response:
---------
    * *A single EmptyMonitor object*

get: Retrieve a specific monitor.
=================================
``monitors.get(monitorId=<MONITORID>)``

Keyword Args:
-------------
    * **monitorId**: The id of the monitor (string)


Response:
---------
    * *A single MonitorDescription object*

update: Updates an existing monitor.
====================================
``monitors.update(body=<BODY>)``

Keyword Args:
-------------
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

listChecks: Retrieve monitor checks for a specific resource.
============================================================
``monitors.listChecks(monitorId=<MONITORID>, endDate=None, limit=250, offset=0, result=None, startDate=None)``

Keyword Args:
-------------
    * **monitorId**: The id of the monitor (string)
    * **startDate**: A timestamp indicating the earliest time of the first monitor check in ISO 8601 format (string)
    * **endDate**: A timestamp indicating the latest time of the first monitor check in ISO 8601 format (string)
    * **result**: A timestamp indicating the latest time of the first monitor check in ISO 8601 format (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Array of MonitorCheck objects*

runCheck: Forces a monitor check to run.
========================================
``monitors.runCheck(monitorId=<MONITORID>)``

Keyword Args:
-------------
    * **monitorId**: The id of the monitor (string)


Response:
---------
    * *A single MonitorCheck object*

getCheck: Retrieve a specific monitor check
===========================================
``monitors.getCheck(checkId=<CHECKID>, monitorId=<MONITORID>)``

Keyword Args:
-------------
    * **monitorId**: The id of the monitor (string)
    * **checkId**: The id of the monitor check (string)


Response:
---------
    * *A single MonitorCheck object*

