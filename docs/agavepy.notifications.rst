*********************
agavepy.notifications
*********************

Summary: Subscribe to and manage notifications

add
===
``agavepy.notifications.add(body)``

Update or Add new notification.

Parameters:
-----------
    * **body**: The notification to add. (JSON, NotificationRequest)


**NotificationRequest:**

.. code-block:: javascript

    {
      "properties": {
        "associatedUuid": {
          "description": "UUID of resource to whome the event applies.", 
          "type": "string"
        }, 
        "persistent": {
          "description": "Whether this notification should stay active after it fires the first time.", 
          "type": "boolean"
        }, 
        "url": {
          "description": "The url or email address that will be notified of the event.", 
          "type": "string"
        }
      }, 
      "required": [
        "url", 
        "associatedUuid", 
        "persistent"
      ], 
      "title": "NotificationRequest", 
      "type": "object"
    }

Response:
---------
    * *Coming soon*

list
====
``agavepy.notifications.list(associatedUuid=None, limit=250, offset=0)``

Retrieve notification for a specific resource.

Parameters:
-----------
    * **associatedUuid**: The uuid of the associated resource. All notifications for this resource visible to the user will be returned. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Coming soon*

get
===
``agavepy.notifications.get(uuid)``

Retrieve notification.

Parameters:
-----------
    * **uuid**: The uuid of the notification item (string)


Response:
---------
    * *Coming soon*

update
======
``agavepy.notifications.update(body, uuid)``

Update or Add new notification.

Parameters:
-----------
    * **uuid**: The uuid of the notification item (string)
    * **body**: The notification to update. (JSON, NotificationRequest)


**NotificationRequest:**

.. code-block:: javascript

    {
      "properties": {
        "associatedUuid": {
          "description": "UUID of resource to whome the event applies.", 
          "type": "string"
        }, 
        "persistent": {
          "description": "Whether this notification should stay active after it fires the first time.", 
          "type": "boolean"
        }, 
        "url": {
          "description": "The url or email address that will be notified of the event.", 
          "type": "string"
        }
      }, 
      "required": [
        "url", 
        "associatedUuid", 
        "persistent"
      ], 
      "title": "NotificationRequest", 
      "type": "object"
    }

Response:
---------
    * *Coming soon*

delete
======
``agavepy.notifications.delete(uuid)``

Remove notification from the system.

Parameters:
-----------
    * **uuid**: The uuid of the notification item (string)


Response:
---------
    * *Coming soon*

