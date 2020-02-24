*******
postits
*******

Summary: Create pre-authenticated, disposable URLs

create: Create a new PostIt
===========================
``postits.create(body=<BODY>)``

Keyword Args:
-------------
    * **body**: The PostIt to create. (JSON, PostItRequest)


**PostItRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/PostItRequest.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
      "properties": {
        "internalUsername": {
          "description": "The username of the internal user attached to this PostIt.",
          "type": "string"
        },
        "lifetime": {
          "description": "The maximum lifetime in seconds of this PostIt on this token. Defaults to 2592000 (30 days)",
          "type": "integer"
        },
        "maxUses": {
          "description": "The maximum number of invocations remaining on this PostIt. Defaults to no limit",
          "type": "integer"
        },
        "method": {
          "description": "The method that will be invoked when the PostIt is redeemed.",
          "enum": [
            "GET",
            "PUT",
            "POST",
            "DELETE"
          ],
          "type": "string"
        },
        "noauth": {
          "description": "If true, the provided url will be called without authentication. Default is false",
          "type": "boolean"
        },
        "url": {
          "description": "The url that will be invoked when the PostIt is redeemed.",
          "type": "string"
        }
      },
      "required": [
        "url"
      ],
      "title": "AgavePy PostItRequest schema",
      "type": "object"
    }

Response:
---------
    * *None*

list: List existing PostIts
===========================
``postits.list(limit=250, offset=0)``

Keyword Args:
-------------
    * **limit**: The max number of results. (integer, optional)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer, optional)


Response:
---------
    * *Array of PostIt objects*

delete: Immediately invalidates this PostIt URL.
================================================
``postits.delete(nonce=<NONCE>)``

Keyword Args:
-------------
    * **nonce**: The nonce of this PostIt URL (string)


Response:
---------
    * *A single PostIt object*

