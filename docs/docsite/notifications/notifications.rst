*************
notifications
*************

Summary: Subscribe to and manage notifications

add: Update or Add new notification.
====================================
``notifications.add(body=<BODY>)``

Keyword Args:
-------------
    * **body**: The notification to add. (JSON, NotificationRequest)


**NotificationRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/NotificationRequest.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
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
      "title": "AgavePy NotificationRequest schema",
      "type": "object"
    }

Response:
---------
    * *A single Notification object*

list: Retrieve notification for a specific resource.
====================================================
``notifications.list(associatedUuid=None, limit=250, offset=0)``

Keyword Args:
-------------
    * **associatedUuid**: The uuid of the associated resource. All notifications for this resource visible to the user will be returned. (string, optional)
    * **limit**: The max number of results. (integer, optional)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer, optional)


Response:
---------
    * *Array of Notification objects*

delete: Remove notification from the system.
============================================
``notifications.delete(uuid=<UUID>)``

Keyword Args:
-------------
    * **uuid**: The uuid of the notification item (string)


Response:
---------
    * *A single EmptyNotification object*

get: Retrieve notification.
===========================
``notifications.get(uuid=<UUID>)``

Keyword Args:
-------------
    * **uuid**: The uuid of the notification item (string)


Response:
---------
    * *A single Notification object*

update: Update or Add new notification.
=======================================
``notifications.update(body=<BODY>, uuid=<UUID>)``

Keyword Args:
-------------
    * **body**: The notification to update. (JSON, NotificationRequest)
    * **uuid**: The uuid of the notification item (string)


Response:
---------
    * *A single Notification object*

