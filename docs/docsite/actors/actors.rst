******
actors
******

Summary: Create and manage actors.

add: Register an actor.
=======================
``actors.add(body=<BODY>)``

Keyword Args:
-------------
    * **body**: The description of the actor to add. (JSON, Actor)


**Actor schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/Actor.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
      "properties": {
        "defaultEnvironment": {
          "description": "Default environmental variables and values.",
          "type": "dict"
        },
        "description": {
          "description": "Description of this actor.",
          "type": "string"
        },
        "id": {
          "description": "The unique id of the actor.",
          "type": "string"
        },
        "image": {
          "description": "Docker image associated with the actor.",
          "type": "string"
        },
        "owner": {
          "description": "username of the owner of the actor.",
          "type": "string"
        },
        "privileged": {
          "description": "Whether this actor runs in privileged mode.",
          "type": "boolean"
        },
        "stateless": {
          "description": "Whether the actor stores private state.",
          "type": "boolean"
        },
        "status": {
          "description": "Current status of the actor.",
          "type": "string"
        }
      },
      "required": [],
      "title": "AgavePy Actor schema",
      "type": "object"
    }

Response:
---------
    * *A single Actor object*

list: List actors
=================
``actors.list(limit=250, offset=0)``

Keyword Args:
-------------
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Array of Actor objects*

delete: Delete a specific actor.
================================
``actors.delete(actorId=<ACTORID>)``

Keyword Args:
-------------
    * **actorId**: The id of the actor. (string)


Response:
---------
    * *A single String object*

get: Retrieve details about a specific actor.
=============================================
``actors.get(actorId=<ACTORID>)``

Keyword Args:
-------------
    * **actorId**: The id of the actor. (string)


Response:
---------
    * *A single Actor object*

update: Retrieve details about a specific actor.
================================================
``actors.update(actorId=<ACTORID>, body=<BODY>)``

Keyword Args:
-------------
    * **actorId**: The id of the actor. (string)
    * **body**: The description of the actor to update. (JSON, Actor)


**Actor schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/Actor.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
      "properties": {
        "defaultEnvironment": {
          "description": "Default environmental variables and values.",
          "type": "dict"
        },
        "description": {
          "description": "Description of this actor.",
          "type": "string"
        },
        "id": {
          "description": "The unique id of the actor.",
          "type": "string"
        },
        "image": {
          "description": "Docker image associated with the actor.",
          "type": "string"
        },
        "owner": {
          "description": "username of the owner of the actor.",
          "type": "string"
        },
        "privileged": {
          "description": "Whether this actor runs in privileged mode.",
          "type": "boolean"
        },
        "stateless": {
          "description": "Whether the actor stores private state.",
          "type": "boolean"
        },
        "status": {
          "description": "Current status of the actor.",
          "type": "string"
        }
      },
      "required": [],
      "title": "AgavePy Actor schema",
      "type": "object"
    }

Response:
---------
    * *A single Actor object*

deleteMessages: Delete messages from an actor
=============================================
``actors.deleteMessages(actorId=<ACTORID>)``

Keyword Args:
-------------
    * **actorId**: The id of the actor. (string)


Response:
---------
    * *None*

getMessages: Get the current number of messages for an actor.
=============================================================
``actors.getMessages(actorId=<ACTORID>)``

Keyword Args:
-------------
    * **actorId**: The id of the actor. (string)


Response:
---------
    * *A single ActorMessages object*

sendBinaryMessage: Send a message to an actor mailbox.
======================================================
``actors.sendBinaryMessage(actorId=<ACTORID>, environment=None, message=<MESSAGE>)``

Keyword Args:
-------------
    * **actorId**: The id of the actor. (string)
    * **environment**: Optional dictionary of environmental variables (dict)
    * **message**: The description of the message to add. (JSON, MessageRequest)


**MessageRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/MessageRequest.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
      "properties": {
        "message": {
          "description": "The message to send to the actor.",
          "type": "string"
        }
      },
      "required": [],
      "title": "AgavePy MessageRequest schema",
      "type": "object"
    }

Response:
---------
    * *A single ActorMessageResponse object*

sendMessage: Send a message to an actor mailbox.
================================================
``actors.sendMessage(actorId=<ACTORID>, body=<BODY>, environment=None)``

Keyword Args:
-------------
    * **actorId**: The id of the actor. (string)
    * **body**: The description of the message to add. (JSON, MessageRequest)
    * **environment**: Optional dictionary of environmental variables (dict)


Response:
---------
    * *A single ActorMessageResponse object*

getState: Get the current state for an actor.
=============================================
``actors.getState(actorId=<ACTORID>)``

Keyword Args:
-------------
    * **actorId**: The id of the actor. (string)


Response:
---------
    * *A single ActorState object*

updateState: Update an actor's state with a JSON-serializable object.
=====================================================================
``actors.updateState(actorId=<ACTORID>, body=<BODY>)``

Keyword Args:
-------------
    * **actorId**: The id of the actor. (string)
    * **body**: The value of the state. Should be JSON-serializable. (JSON, string)


Response:
---------
    * *A single ActorState object*

getPermissions: Get the current permissions for an actor.
=========================================================
``actors.getPermissions(actorId=<ACTORID>)``

Keyword Args:
-------------
    * **actorId**: The id of the actor. (string)


Response:
---------
    * *A single ActorPermissions object*

updatePermissions: Update an actor's permissions with a new permission for a user.
==================================================================================
``actors.updatePermissions(actorId=<ACTORID>, body=<BODY>)``

Keyword Args:
-------------
    * **actorId**: The id of the actor. (string)
    * **body**: The permission record; user and level fields required. (JSON, PermissionsUpdateRequest)


**PermissionsUpdateRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/PermissionsUpdateRequest.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
      "properties": {
        "level": {
          "description": "The level associated with the permission.",
          "type": "string"
        },
        "user": {
          "description": "The user associated with the permission.",
          "type": "string"
        }
      },
      "required": [],
      "title": "AgavePy PermissionsUpdateRequest schema",
      "type": "object"
    }

Response:
---------
    * *A single ActorPermissionsResponse object*

addWorker: Add a worker to an actor.
====================================
``actors.addWorker(actorId=<ACTORID>, body=<BODY>)``

Keyword Args:
-------------
    * **actorId**: The id of the actor. (string)
    * **body**: The description of the workers to add. (JSON, AddWorkersRequest)


**AddWorkersRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/AddWorkersRequest.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
      "properties": {
        "num": {
          "description": "The number of workers to ensure are running.",
          "type": "int"
        }
      },
      "required": [],
      "title": "AgavePy AddWorkersRequest schema",
      "type": "object"
    }

Response:
---------
    * *A single EmptyActorWorkerRequestResponse object*

listWorkers: List the current workers for an actor.
===================================================
``actors.listWorkers(actorId=<ACTORID>)``

Keyword Args:
-------------
    * **actorId**: The id of the actor. (string)


Response:
---------
    * *Array of ActorWorker objects*

deleteWorker: Delete a worker.
==============================
``actors.deleteWorker(actorId=<ACTORID>, workerId=<WORKERID>)``

Keyword Args:
-------------
    * **actorId**: The id of the actor. (string)
    * **workerId**: The id of the worker. (string)


Response:
---------
    * *A single String object*

getWorker: Get the details about a specific worker for an actor.
================================================================
``actors.getWorker(actorId=<ACTORID>, workerId=<WORKERID>)``

Keyword Args:
-------------
    * **actorId**: The id of the actor. (string)
    * **workerId**: The id of the worker. (string)


Response:
---------
    * *A single ActorWorker object*

addNonce: Add a nonce to an actor.
==================================
``actors.addNonce(actorId=<ACTORID>, body=)``

Keyword Args:
-------------
    * **actorId**: The id of the actor. (string)
    * **body**: The description of the nonce to add. (JSON, AddNonceRequest)


**AddNonceRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/AddNonceRequest.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
      "properties": {
        "level": {
          "description": "Permissions level associated with this nonce (default is EXECUTE).",
          "type": "string"
        },
        "maxUses": {
          "description": "Max number of times nonce can be redeemed.",
          "type": "int"
        }
      },
      "required": [],
      "title": "AgavePy AddNonceRequest schema",
      "type": "object"
    }

Response:
---------
    * *A single EmptyActorNonceRequestResponse object*

listNonces: List the current nonces for an actor.
=================================================
``actors.listNonces(actorId=<ACTORID>)``

Keyword Args:
-------------
    * **actorId**: The id of the actor. (string)


Response:
---------
    * *Array of ActorNonce objects*

deleteNonce: Delete a nonce.
============================
``actors.deleteNonce(actorId=<ACTORID>, nonceId=<NONCEID>)``

Keyword Args:
-------------
    * **actorId**: The id of the actor. (string)
    * **nonceId**: The id of the nonce. (string)


Response:
---------
    * *A single String object*

getNonce: Get the details about a specific nonce for an actor.
==============================================================
``actors.getNonce(actorId=<ACTORID>, nonceId=<NONCEID>)``

Keyword Args:
-------------
    * **actorId**: The id of the actor. (string)
    * **nonceId**: The id of the nonce. (string)


Response:
---------
    * *A single ActorNonce object*

addAlias: Add an alias of an actor.
===================================
``actors.addAlias(body=)``

Keyword Args:
-------------
    * **body**: The description of the alias to add. (JSON, AddAliasRequest)


**AddAliasRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/AddAliasRequest.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
      "properties": {
        "actorId": {
          "description": "The id of the actor to associate with this alias.",
          "type": "string"
        },
        "alias": {
          "description": "The alias to create.",
          "type": "string"
        }
      },
      "required": [],
      "title": "AgavePy AddAliasRequest schema",
      "type": "object"
    }

Response:
---------
    * *A single ActorAlias object*

listAliases: List all current aliases
=====================================
``actors.listAliases()``

**AddAliasRequest schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/AddAliasRequest.json",
      "$schema": "http://json-schema.org/draft-07/schema#",
      "properties": {
        "actorId": {
          "description": "The id of the actor to associate with this alias.",
          "type": "string"
        },
        "alias": {
          "description": "The alias to create.",
          "type": "string"
        }
      },
      "required": [],
      "title": "AgavePy AddAliasRequest schema",
      "type": "object"
    }

Response:
---------
    * *Array of ActorAlias objects*

deleteAlias: Delete an alias.
=============================
``actors.deleteAlias(alias=<ALIAS>)``

Keyword Args:
-------------
    * **alias**: The id of the alias. (string)


Response:
---------
    * *A single String object*

getAlias: Get the details of a specific alias.
==============================================
``actors.getAlias(alias=<ALIAS>)``

Keyword Args:
-------------
    * **alias**: The id of the alias. (string)


Response:
---------
    * *A single ActorAlias object*

listExecutions: Summary data of all actor executions.
=====================================================
``actors.listExecutions(actorId=<ACTORID>, limit=250, offset=0)``

Keyword Args:
-------------
    * **actorId**: The id of the actor. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *A single ExecutionsSummary object*

getExecution: Retrieve details about a specific actor execution.
================================================================
``actors.getExecution(actorId=<ACTORID>, executionId=<EXECUTIONID>)``

Keyword Args:
-------------
    * **actorId**: The id of the actor. (string)
    * **executionId**: The id of the execution. (string)


Response:
---------
    * *A single Execution object*

getOneExecutionResult: Get result for a specific actor execution.
=================================================================
``actors.getOneExecutionResult(actorId=<ACTORID>, executionId=<EXECUTIONID>)``

Keyword Args:
-------------
    * **actorId**: The id of the actor. (string)
    * **executionId**: The id of the execution. (string)


Response:
---------
    * *None*

getExecutionLogs: Get logs for a specific actor execution.
==========================================================
``actors.getExecutionLogs(actorId=<ACTORID>, executionId=<EXECUTIONID>)``

Keyword Args:
-------------
    * **actorId**: The id of the actor. (string)
    * **executionId**: The id of the execution. (string)


Response:
---------
    * *A single ExecutionLogs object*

