*************
Notifications
*************

Summary: Subscribe to and manage notifications

add: Update or Add new notification.
====================================
``agavepy.notifications.add(body)``

Parameters:
-----------
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

**Notification schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/Notification.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "associatedUuid": {
          "description": "UUID of resource to whome the event applies.", 
          "type": "string"
        }, 
        "attempts": {
          "description": "The number of times this notification has been attempted to be fulfilled.", 
          "type": "integer"
        }, 
        "created": {
          "description": "A timestamp indicating when this notification was created in the notification store.", 
          "type": "string"
        }, 
        "lastSent": {
          "description": "A timestamp indicating the last time this notification was sent.", 
          "type": "string"
        }, 
        "owner": {
          "description": "The API user who owns this notification.", 
          "type": "string"
        }, 
        "persistent": {
          "description": "Whether this notification should stay active after it fires the first time.", 
          "type": "boolean"
        }, 
        "responseCode": {
          "description": "The response code from POSTing to the url or sending an email.", 
          "type": "integer"
        }, 
        "success": {
          "description": "Whether this notification was sent successfully.", 
          "type": "boolean"
        }, 
        "url": {
          "description": "The url or email address that will be notified of the event.", 
          "type": "string"
        }, 
        "uuid": {
          "description": "The UUID for this notification.", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy Notification schema", 
      "type": "object"
    }

list: Retrieve notification for a specific resource.
====================================================
``agavepy.notifications.list(associatedUuid=None, limit=250, offset=0)``

Parameters:
-----------
    * **associatedUuid**: The uuid of the associated resource. All notifications for this resource visible to the user will be returned. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Array of Notification objects*

**Notification schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/Notification.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "associatedUuid": {
          "description": "UUID of resource to whome the event applies.", 
          "type": "string"
        }, 
        "attempts": {
          "description": "The number of times this notification has been attempted to be fulfilled.", 
          "type": "integer"
        }, 
        "created": {
          "description": "A timestamp indicating when this notification was created in the notification store.", 
          "type": "string"
        }, 
        "lastSent": {
          "description": "A timestamp indicating the last time this notification was sent.", 
          "type": "string"
        }, 
        "owner": {
          "description": "The API user who owns this notification.", 
          "type": "string"
        }, 
        "persistent": {
          "description": "Whether this notification should stay active after it fires the first time.", 
          "type": "boolean"
        }, 
        "responseCode": {
          "description": "The response code from POSTing to the url or sending an email.", 
          "type": "integer"
        }, 
        "success": {
          "description": "Whether this notification was sent successfully.", 
          "type": "boolean"
        }, 
        "url": {
          "description": "The url or email address that will be notified of the event.", 
          "type": "string"
        }, 
        "uuid": {
          "description": "The UUID for this notification.", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy Notification schema", 
      "type": "object"
    }

delete: Remove notification from the system.
============================================
``agavepy.notifications.delete(uuid)``

Parameters:
-----------
    * **uuid**: The uuid of the notification item (string)


Response:
---------
    * *A single EmptyNotification object*

**EmptyNotification schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/EmptyNotification.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {}, 
      "required": [], 
      "title": "AgavePy EmptyNotification schema", 
      "type": "object"
    }

get: Retrieve notification.
===========================
``agavepy.notifications.get(uuid)``

Parameters:
-----------
    * **uuid**: The uuid of the notification item (string)


Response:
---------
    * *A single Notification object*

**Notification schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/Notification.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "associatedUuid": {
          "description": "UUID of resource to whome the event applies.", 
          "type": "string"
        }, 
        "attempts": {
          "description": "The number of times this notification has been attempted to be fulfilled.", 
          "type": "integer"
        }, 
        "created": {
          "description": "A timestamp indicating when this notification was created in the notification store.", 
          "type": "string"
        }, 
        "lastSent": {
          "description": "A timestamp indicating the last time this notification was sent.", 
          "type": "string"
        }, 
        "owner": {
          "description": "The API user who owns this notification.", 
          "type": "string"
        }, 
        "persistent": {
          "description": "Whether this notification should stay active after it fires the first time.", 
          "type": "boolean"
        }, 
        "responseCode": {
          "description": "The response code from POSTing to the url or sending an email.", 
          "type": "integer"
        }, 
        "success": {
          "description": "Whether this notification was sent successfully.", 
          "type": "boolean"
        }, 
        "url": {
          "description": "The url or email address that will be notified of the event.", 
          "type": "string"
        }, 
        "uuid": {
          "description": "The UUID for this notification.", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy Notification schema", 
      "type": "object"
    }

update: Update or Add new notification.
=======================================
``agavepy.notifications.update(body, uuid)``

Parameters:
-----------
    * **uuid**: The uuid of the notification item (string)
    * **body**: The notification to update. (JSON, NotificationRequest)


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

**Notification schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/Notification.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "associatedUuid": {
          "description": "UUID of resource to whome the event applies.", 
          "type": "string"
        }, 
        "attempts": {
          "description": "The number of times this notification has been attempted to be fulfilled.", 
          "type": "integer"
        }, 
        "created": {
          "description": "A timestamp indicating when this notification was created in the notification store.", 
          "type": "string"
        }, 
        "lastSent": {
          "description": "A timestamp indicating the last time this notification was sent.", 
          "type": "string"
        }, 
        "owner": {
          "description": "The API user who owns this notification.", 
          "type": "string"
        }, 
        "persistent": {
          "description": "Whether this notification should stay active after it fires the first time.", 
          "type": "boolean"
        }, 
        "responseCode": {
          "description": "The response code from POSTing to the url or sending an email.", 
          "type": "integer"
        }, 
        "success": {
          "description": "Whether this notification was sent successfully.", 
          "type": "boolean"
        }, 
        "url": {
          "description": "The url or email address that will be notified of the event.", 
          "type": "string"
        }, 
        "uuid": {
          "description": "The UUID for this notification.", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy Notification schema", 
      "type": "object"
    }

