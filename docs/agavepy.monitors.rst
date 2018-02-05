****************
agavepy.monitors
****************

Summary: Create and manage system monitors

list
====
``agavepy.monitors.list(active=None, limit=250, offset=0, target=None)``

Retrieve Monitor for a specific resource.

Parameters:
-----------
    * **target**: The target to search for. (string)
    * **active**: Filter by monitors that are active or inactive. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Coming soon*

add
===
``agavepy.monitors.add(body)``

Update or Add new Monitor.

Parameters:
-----------
    * **body**: The description of the app to add or update. This can be either a file upload or json posted to the request body. (JSON, MonitorRequest)


**MonitorRequest:**

.. code-block:: javascript

    {
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
      "title": "MonitorRequest", 
      "type": "object"
    }

Response:
---------
    * *Coming soon*

get
===
``agavepy.monitors.get(monitorId)``

Retrieve a specific monitor.

Parameters:
-----------
    * **monitorId**: The id of the monitor (string)


Response:
---------
    * *Coming soon*

update
======
``agavepy.monitors.update(body)``

Updates an existing monitor.

Parameters:
-----------
    * **body**: The description of the app to add or update. This can be either a file upload or json posted to the request body. (JSON, MonitorRequest)


**MonitorRequest:**

.. code-block:: javascript

    {
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
      "title": "MonitorRequest", 
      "type": "object"
    }

Response:
---------
    * *Coming soon*

delete
======
``agavepy.monitors.delete(monitorId)``

Deletes a monitor.

Parameters:
-----------
    * **monitorId**: The id of the monitor (string)


Response:
---------
    * *Coming soon*

listChecks
==========
``agavepy.monitors.listChecks(monitorId, endDate=None, limit=250, offset=0, result=None, startDate=None)``

Retrieve monitor checks for a specific resource.

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
    * *Coming soon*

runCheck
========
``agavepy.monitors.runCheck(monitorId)``

Forces a monitor check to run.

Parameters:
-----------
    * **monitorId**: The id of the monitor (string)


Response:
---------
    * *Coming soon*

getCheck
========
``agavepy.monitors.getCheck(checkId, monitorId)``

Retrieve a specific monitor check

Parameters:
-----------
    * **monitorId**: The id of the monitor (string)
    * **checkId**: The id of the monitor check (string)


Response:
---------
    * *Coming soon*

