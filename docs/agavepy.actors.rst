**************
agavepy.actors
**************

Summary: Create and manage actors.

list
====
``agavepy.actors.list(limit=250, offset=0)``

List actors

Parameters:
-----------
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Coming soon*

add
===
``agavepy.actors.add(body)``

Register an actor.

Parameters:
-----------
    * **body**: The description of the actor to add. (JSON, Actor)


**Actor:**

.. code-block:: javascript

    {
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
      "title": "Actor", 
      "type": "object"
    }

Response:
---------
    * *Coming soon*

get
===
``agavepy.actors.get(actorId)``

Retrieve details about a specific actor.

Parameters:
-----------
    * **actorId**: The id of the actor. (string)


Response:
---------
    * *Coming soon*

update
======
``agavepy.actors.update(actorId, body)``

Retrieve details about a specific actor.

Parameters:
-----------
    * **actorId**: The id of the actor. (string)
    * **body**: The description of the actor to update. (JSON, Actor)


**Actor:**

.. code-block:: javascript

    {
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
      "title": "Actor", 
      "type": "object"
    }

Response:
---------
    * *Coming soon*

delete
======
``agavepy.actors.delete(actorId)``

Delete a specific actor.

Parameters:
-----------
    * **actorId**: The id of the actor. (string)


Response:
---------
    * *Coming soon*

getMessages
===========
``agavepy.actors.getMessages(actorId)``

Get the current number of messages for an actor.

Parameters:
-----------
    * **actorId**: The id of the actor. (string)


Response:
---------
    * *Coming soon*

sendMessage
===========
``agavepy.actors.sendMessage(actorId, body, environment=None)``

Send a message to an actor mailbox.

Parameters:
-----------
    * **actorId**: The id of the actor. (string)
    * **environment**: Optional dictionary of environmental variables (dict)
    * **body**: The description of the message to add. (JSON, MessageRequest)


**MessageRequest:**

.. code-block:: javascript

    {
      "properties": {
        "message": {
          "description": "The message to send to the actor.", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "MessageRequest", 
      "type": "object"
    }

Response:
---------
    * *Coming soon*

listWorkers
===========
``agavepy.actors.listWorkers(actorId)``

List the current workers for an actor.

Parameters:
-----------
    * **actorId**: The id of the actor. (string)


Response:
---------
    * *Coming soon*

addWorker
=========
``agavepy.actors.addWorker(actorId, body)``

Add a worker to an actor.

Parameters:
-----------
    * **actorId**: The id of the actor. (string)
    * **body**: The description of the workers to add. (JSON, AddWorkersRequest)


**AddWorkersRequest:**

.. code-block:: javascript

    {
      "properties": {
        "num": {
          "description": "The number of workers to ensure are running.", 
          "type": "int"
        }
      }, 
      "required": [], 
      "title": "AddWorkersRequest", 
      "type": "object"
    }

Response:
---------
    * *Coming soon*

getWorker
=========
``agavepy.actors.getWorker(actorId, workerId)``

Get the details about a specific worker for an actor.

Parameters:
-----------
    * **actorId**: The id of the actor. (string)
    * **workerId**: The id of the worker. (string)


Response:
---------
    * *Coming soon*

deleteWorker
============
``agavepy.actors.deleteWorker(actorId, workerId)``

Delete a worker.

Parameters:
-----------
    * **actorId**: The id of the actor. (string)
    * **workerId**: The id of the worker. (string)


Response:
---------
    * *Coming soon*

listNonces
==========
``agavepy.actors.listNonces(actorId)``

List the current nonces for an actor.

Parameters:
-----------
    * **actorId**: The id of the actor. (string)


Response:
---------
    * *Coming soon*

addNonce
========
``agavepy.actors.addNonce(actorId, body=)``

Add a nonce to an actor.

Parameters:
-----------
    * **actorId**: The id of the actor. (string)
    * **body**: The description of the nonce to add. (JSON, AddNonceRequest)


**AddNonceRequest:**

.. code-block:: javascript

    {
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
      "title": "AddNonceRequest", 
      "type": "object"
    }

Response:
---------
    * *Coming soon*

getNonce
========
``agavepy.actors.getNonce(actorId, nonceId)``

Get the details about a specific nonce for an actor.

Parameters:
-----------
    * **actorId**: The id of the actor. (string)
    * **nonceId**: The id of the nonce. (string)


Response:
---------
    * *Coming soon*

deleteNonce
===========
``agavepy.actors.deleteNonce(actorId, nonceId)``

Delete a nonce.

Parameters:
-----------
    * **actorId**: The id of the actor. (string)
    * **nonceId**: The id of the nonce. (string)


Response:
---------
    * *Coming soon*

listExecutions
==============
``agavepy.actors.listExecutions(actorId, limit=250, offset=0)``

Summary data of all actor executions.

Parameters:
-----------
    * **actorId**: The id of the actor. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Coming soon*

addExecution
============
``agavepy.actors.addExecution(actorId, body)``

Register an actor execution.

Parameters:
-----------
    * **actorId**: The id of the actor. (string)
    * **body**: The description of the actor execution to add. (JSON, ActorExecution)


Response:
---------
    * *Coming soon*

getExecution
============
``agavepy.actors.getExecution(actorId, executionId)``

Retrieve details about a specific actor execution.

Parameters:
-----------
    * **actorId**: The id of the actor. (string)
    * **executionId**: The id of the execution. (string)


Response:
---------
    * *Coming soon*

getExecutionLogs
================
``agavepy.actors.getExecutionLogs(actorId, executionId)``

Get logs for a specific actor execution.

Parameters:
-----------
    * **actorId**: The id of the actor. (string)
    * **executionId**: The id of the execution. (string)


Response:
---------
    * *Coming soon*

