**********
transforms
**********

Summary: Transform and stage data

list: Find all transforms for use within the api.
=================================================
``transforms.list()``

Keyword Args:
-------------


Response:
---------
    * *Array of Transform objects*

get: Find all transforms matching the given name.
=================================================
``transforms.get(transformId=<TRANSFORMID>)``

Keyword Args:
-------------
    * **transformId**: The name of the transform requested. (string)


Response:
---------
    * *Array of Transform objects*

transformAndStage: Transform a file and stage it to a specified location.
=========================================================================
``transforms.transformAndStage(body=<BODY>, filePath=<FILEPATH>, owner=<OWNER>, transformId=<TRANSFORMID>)``

Keyword Args:
-------------
    * **transformId**: The name of the transform to apply to the given file. (string)
    * **owner**: The name of the api user owning the file at the given path. (string)
    * **filePath**: The path to the file to be transformed and staged (string)
    * **body**: The transfer request details. (JSON, TransformRequest)


**TransformRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/TransformRequest.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
      "properties": {
        "callbackUrl": {
          "description": "The URI to notify when the transfer is complete. This can be an email address or http URL. If a URL is given, a GET will be made to this address. URL templating is supported. Valid template values are: ${NAME}, ${SOURCE_FORMAT}, ${DEST_FORMAT}, ${STATUS}",
          "type": "string"
        },
        "nativeFormat": {
          "description": "The original file type of the file. If not given, the file type is assumed to be raw.",
          "type": "string"
        },
        "url": {
          "description": "The uri to which the transformed file will be staged.",
          "type": "string"
        }
      },
      "required": [
        "url"
      ],
      "title": "AgavePy TransformRequest schema",
      "type": "object"
    }

Response:
---------
    * *Array of Transform objects*

transformAndDownload: Transform a file and download it directly.
================================================================
``transforms.transformAndDownload(body=<BODY>, filePath=<FILEPATH>, owner=<OWNER>, transformId=<TRANSFORMID>)``

Keyword Args:
-------------
    * **transformId**: The name of the transform to apply to the given file. (string)
    * **owner**: The name of the api user owning the file at the given path. (string)
    * **filePath**: The path to the file to be transformed and downloaded. (string)
    * **body**: The transfer request details. (JSON, TransformRequest)


**TransformRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/TransformRequest.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
      "properties": {
        "callbackUrl": {
          "description": "The URI to notify when the transfer is complete. This can be an email address or http URL. If a URL is given, a GET will be made to this address. URL templating is supported. Valid template values are: ${NAME}, ${SOURCE_FORMAT}, ${DEST_FORMAT}, ${STATUS}",
          "type": "string"
        },
        "nativeFormat": {
          "description": "The original file type of the file. If not given, the file type is assumed to be raw.",
          "type": "string"
        },
        "url": {
          "description": "The uri to which the transformed file will be staged.",
          "type": "string"
        }
      },
      "required": [
        "url"
      ],
      "title": "AgavePy TransformRequest schema",
      "type": "object"
    }

Response:
---------
    * *None*

listByTag: Find all transforms with the given tag.
==================================================
``transforms.listByTag(tag=<TAG>)``

Keyword Args:
-------------
    * **tag**: The tag to search for transforms on. (string)


Response:
---------
    * *Array of Transform objects*

