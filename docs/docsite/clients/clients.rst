*******
clients
*******

Summary: Create and manage API keys. Requires HTTP BASIC authentication

create: Create a new client
===========================
``clients.create(body=<BODY>)``

Keyword Args:
-------------
    * **body**: The api client to create (JSON, ClientRequest)


**ClientRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/ClientRequest.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
      "properties": {
        "callbackUrl": {
          "description": "Callback URL for OAuth authentication grant.",
          "type": "string"
        },
        "description": {
          "description": "Description of the client. This will be shown to users when authentication via OAuth web flows",
          "type": "string"
        },
        "name": {
          "description": "The name of the client.",
          "type": "string"
        },
        "tier": {
          "description": "The access tier for this client.",
          "enum": [
            "UNLIMITED",
            "GOLD",
            "SILVER",
            "BRONZE"
          ],
          "type": "string"
        }
      },
      "required": [
        "name"
      ],
      "title": "AgavePy ClientRequest schema",
      "type": "object"
    }

Response:
---------
    * *A single Client object*

list: List existing clients
===========================
``clients.list()``

**ClientRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/ClientRequest.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
      "properties": {
        "callbackUrl": {
          "description": "Callback URL for OAuth authentication grant.",
          "type": "string"
        },
        "description": {
          "description": "Description of the client. This will be shown to users when authentication via OAuth web flows",
          "type": "string"
        },
        "name": {
          "description": "The name of the client.",
          "type": "string"
        },
        "tier": {
          "description": "The access tier for this client.",
          "enum": [
            "UNLIMITED",
            "GOLD",
            "SILVER",
            "BRONZE"
          ],
          "type": "string"
        }
      },
      "required": [
        "name"
      ],
      "title": "AgavePy ClientRequest schema",
      "type": "object"
    }

Response:
---------
    * *Array of Client objects*

delete: Immediately deletes this client and renders the API keys useless.
=========================================================================
``clients.delete(clientName=<CLIENTNAME>)``

Keyword Args:
-------------
    * **clientName**: The name of the client to be deleted (string)


Response:
---------
    * *A single String object*

getClientByName: Returns a detailed description of a named client.
==================================================================
``clients.getClientByName(clientName=<CLIENTNAME>)``

Keyword Args:
-------------
    * **clientName**: The name of the client to be deleted (string)


Response:
---------
    * *Array of Client objects*

addSubscriptionForClient: Lists all APIs to which the client is subscribed
==========================================================================
``clients.addSubscriptionForClient(body=<BODY>, clientName=<CLIENTNAME>)``

Keyword Args:
-------------
    * **clientName**: The name of the client to be subscribe to this api (string)
    * **body**: The api client to create (JSON, ClientSubscriptionRequest)


**ClientSubscriptionRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/ClientSubscriptionRequest.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
      "properties": {
        "apiName": {
          "description": "The name of the API.",
          "type": "string"
        },
        "apiProvider": {
          "description": "The user who registered the API.",
          "type": "string"
        },
        "apiVersion": {
          "description": "The current major version of the API. This is appended to the api_context to create the base API url.",
          "type": "string"
        },
        "tier": {
          "description": "The access tier for this client.",
          "enum": [
            "UNLIMITED",
            "GOLD",
            "SILVER",
            "BRONZE"
          ],
          "type": "string"
        }
      },
      "required": [
        "apiProvider",
        "apiVersion",
        "apiName"
      ],
      "title": "AgavePy ClientSubscriptionRequest schema",
      "type": "object"
    }

Response:
---------
    * *A single Subscription object*

deleteSubscriptionsForClient: Unsubscribe the client from all APIs
==================================================================
``clients.deleteSubscriptionsForClient(clientName=<CLIENTNAME>)``

Keyword Args:
-------------
    * **clientName**: The name of the client to be deleted (string)


Response:
---------
    * *A single String object*

listSubscriptionsForClient: Lists all APIs to which the client is subscribed
============================================================================
``clients.listSubscriptionsForClient(clientName=<CLIENTNAME>)``

Keyword Args:
-------------
    * **clientName**: The name of the client to be deleted (string)


Response:
---------
    * *Array of Subscription objects*

