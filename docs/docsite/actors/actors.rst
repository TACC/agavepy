******
Actors
******

Summary: Create and manage actors.

add: Register an actor.
=======================
``agavepy.actors.add(body)``

Parameters:
-----------
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

list: List actors
=================
``agavepy.actors.list(limit=250, offset=0)``

Parameters:
-----------
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *Array of Actor objects*

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

delete: Delete a specific actor.
================================
``agavepy.actors.delete(actorId)``

Parameters:
-----------
    * **actorId**: The id of the actor. (string)


Response:
---------
    * *A single String object*

get: Retrieve details about a specific actor.
=============================================
``agavepy.actors.get(actorId)``

Parameters:
-----------
    * **actorId**: The id of the actor. (string)


Response:
---------
    * *A single Actor object*

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

update: Retrieve details about a specific actor.
================================================
``agavepy.actors.update(actorId, body)``

Parameters:
-----------
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

getMessages: Get the current number of messages for an actor.
=============================================================
``agavepy.actors.getMessages(actorId)``

Parameters:
-----------
    * **actorId**: The id of the actor. (string)


Response:
---------
    * *A single ActorMessages object*

**ActorMessages schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/ActorMessages.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "messages": {
          "description": "The number of messages waiting in queue to be processed by this actor.", 
          "type": "int"
        }
      }, 
      "required": [], 
      "title": "AgavePy ActorMessages schema", 
      "type": "object"
    }

sendBinaryMessage: Send a message to an actor mailbox.
======================================================
``agavepy.actors.sendBinaryMessage(actorId, message, environment=None)``

Parameters:
-----------
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
``agavepy.actors.sendMessage(actorId, body, environment=None)``

Parameters:
-----------
    * **actorId**: The id of the actor. (string)
    * **environment**: Optional dictionary of environmental variables (dict)
    * **body**: The description of the message to add. (JSON, MessageRequest)


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

getState: Get the current state for an actor.
=============================================
``agavepy.actors.getState(actorId)``

Parameters:
-----------
    * **actorId**: The id of the actor. (string)


Response:
---------
    * *A single ActorState object*

**ActorState schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/ActorState.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "state": {
          "description": "The current state of the actor.", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy ActorState schema", 
      "type": "object"
    }

updateState: Update an actor's state with a JSON-serializable object.
=====================================================================
``agavepy.actors.updateState(actorId, body)``

Parameters:
-----------
    * **actorId**: The id of the actor. (string)
    * **body**: The value of the state. Should be JSON-serializable. (JSON, string)


Response:
---------
    * *A single ActorState object*

**ActorState schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/ActorState.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "state": {
          "description": "The current state of the actor.", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy ActorState schema", 
      "type": "object"
    }

getPermissions: Get the current permissions for an actor.
=========================================================
``agavepy.actors.getPermissions(actorId)``

Parameters:
-----------
    * **actorId**: The id of the actor. (string)


Response:
---------
    * *A single ActorPermissions object*

**ActorPermissions schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/ActorPermissions.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "permissions": {
          "description": "The dictionary of permissions associated with the actor.", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy ActorPermissions schema", 
      "type": "object"
    }

updatePermissions: Update an actor's permissions with a new permission for a user.
==================================================================================
``agavepy.actors.updatePermissions(actorId, body)``

Parameters:
-----------
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
``agavepy.actors.addWorker(actorId, body)``

Parameters:
-----------
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
``agavepy.actors.listWorkers(actorId)``

Parameters:
-----------
    * **actorId**: The id of the actor. (string)


Response:
---------
    * *Array of ActorWorker objects*

**ActorWorker schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/ActorWorker.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "cid": {
          "description": "Container id of this worker.", 
          "type": "string"
        }, 
        "host_id": {
          "description": "id of the host where this worker is running.", 
          "type": "string"
        }, 
        "host_ip": {
          "description": "IP address of the host where this worker is running.", 
          "type": "string"
        }, 
        "id": {
          "description": "The unique id of this worker.", 
          "type": "string"
        }, 
        "image": {
          "description": "Docker image associated with the actor.", 
          "type": "string"
        }, 
        "last_execution": {
          "description": "Last execution for this worker.", 
          "type": "int"
        }, 
        "location": {
          "description": "Location of docker daemon that this worker is using.", 
          "type": "string"
        }, 
        "status": {
          "description": "status of the worker.", 
          "type": "string"
        }, 
        "tenant": {
          "description": "tenant this worker belongs to.", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy ActorWorker schema", 
      "type": "object"
    }

deleteWorker: Delete a worker.
==============================
``agavepy.actors.deleteWorker(actorId, workerId)``

Parameters:
-----------
    * **actorId**: The id of the actor. (string)
    * **workerId**: The id of the worker. (string)


Response:
---------
    * *A single String object*

getWorker: Get the details about a specific worker for an actor.
================================================================
``agavepy.actors.getWorker(actorId, workerId)``

Parameters:
-----------
    * **actorId**: The id of the actor. (string)
    * **workerId**: The id of the worker. (string)


Response:
---------
    * *A single ActorWorker object*

**ActorWorker schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/ActorWorker.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "cid": {
          "description": "Container id of this worker.", 
          "type": "string"
        }, 
        "host_id": {
          "description": "id of the host where this worker is running.", 
          "type": "string"
        }, 
        "host_ip": {
          "description": "IP address of the host where this worker is running.", 
          "type": "string"
        }, 
        "id": {
          "description": "The unique id of this worker.", 
          "type": "string"
        }, 
        "image": {
          "description": "Docker image associated with the actor.", 
          "type": "string"
        }, 
        "last_execution": {
          "description": "Last execution for this worker.", 
          "type": "int"
        }, 
        "location": {
          "description": "Location of docker daemon that this worker is using.", 
          "type": "string"
        }, 
        "status": {
          "description": "status of the worker.", 
          "type": "string"
        }, 
        "tenant": {
          "description": "tenant this worker belongs to.", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy ActorWorker schema", 
      "type": "object"
    }

addNonce: Add a nonce to an actor.
==================================
``agavepy.actors.addNonce(actorId, body=)``

Parameters:
-----------
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
``agavepy.actors.listNonces(actorId)``

Parameters:
-----------
    * **actorId**: The id of the actor. (string)


Response:
---------
    * *Array of ActorNonce objects*

**ActorNonce schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/ActorNonce.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "actor_id": {
          "description": "Actor id associated with nonce.", 
          "type": "string"
        }, 
        "create_time": {
          "description": "Time stamp when nonce was created.", 
          "type": "string"
        }, 
        "id": {
          "description": "The unique id of the nonce.", 
          "type": "string"
        }, 
        "last_use_time": {
          "description": "Last time nonce was used.", 
          "type": "string"
        }, 
        "level": {
          "description": "Permission level associated with nonce.", 
          "type": "string"
        }, 
        "max_uses": {
          "description": "Max number of uses for this nonce.", 
          "type": "string"
        }, 
        "remaining_uses": {
          "description": "Remaining uses of nonce.", 
          "type": "int"
        }
      }, 
      "required": [], 
      "title": "AgavePy ActorNonce schema", 
      "type": "object"
    }

deleteNonce: Delete a nonce.
============================
``agavepy.actors.deleteNonce(actorId, nonceId)``

Parameters:
-----------
    * **actorId**: The id of the actor. (string)
    * **nonceId**: The id of the nonce. (string)


Response:
---------
    * *A single String object*

getNonce: Get the details about a specific nonce for an actor.
==============================================================
``agavepy.actors.getNonce(actorId, nonceId)``

Parameters:
-----------
    * **actorId**: The id of the actor. (string)
    * **nonceId**: The id of the nonce. (string)


Response:
---------
    * *A single ActorNonce object*

**ActorNonce schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/ActorNonce.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "actor_id": {
          "description": "Actor id associated with nonce.", 
          "type": "string"
        }, 
        "create_time": {
          "description": "Time stamp when nonce was created.", 
          "type": "string"
        }, 
        "id": {
          "description": "The unique id of the nonce.", 
          "type": "string"
        }, 
        "last_use_time": {
          "description": "Last time nonce was used.", 
          "type": "string"
        }, 
        "level": {
          "description": "Permission level associated with nonce.", 
          "type": "string"
        }, 
        "max_uses": {
          "description": "Max number of uses for this nonce.", 
          "type": "string"
        }, 
        "remaining_uses": {
          "description": "Remaining uses of nonce.", 
          "type": "int"
        }
      }, 
      "required": [], 
      "title": "AgavePy ActorNonce schema", 
      "type": "object"
    }

listExecutions: Summary data of all actor executions.
=====================================================
``agavepy.actors.listExecutions(actorId, limit=250, offset=0)``

Parameters:
-----------
    * **actorId**: The id of the actor. (string)
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)


Response:
---------
    * *A single ExecutionsSummary object*

**ExecutionsSummary schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/ExecutionsSummary.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "actorId": {
          "description": "The id of the associated actor.", 
          "type": "string"
        }, 
        "ids": {
          "description": "The ids of all executions.", 
          "type": "array"
        }, 
        "owner": {
          "description": "username of the owner of the actor.", 
          "type": "string"
        }, 
        "totalCpu": {
          "description": "CPU usage, in user jiffies, of all executions.", 
          "type": "int"
        }, 
        "totalIo": {
          "description": "Block I/O usage, in number of 512-byte sectors read from and written to, by all executions.", 
          "type": "int"
        }, 
        "totalRuntime": {
          "description": "Runtime, in milliseconds, of all executions.", 
          "type": "int"
        }
      }, 
      "required": [], 
      "title": "AgavePy ExecutionsSummary schema", 
      "type": "object"
    }

getExecution: Retrieve details about a specific actor execution.
================================================================
``agavepy.actors.getExecution(actorId, executionId)``

Parameters:
-----------
    * **actorId**: The id of the actor. (string)
    * **executionId**: The id of the execution. (string)


Response:
---------
    * *A single Execution object*

**Execution schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/Execution.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "actorId": {
          "description": "The id of the associated actor.", 
          "type": "string"
        }, 
        "cpu": {
          "description": "CPU usage, in user jiffies, of this execution.", 
          "type": "int"
        }, 
        "id": {
          "description": "The id of this executions.", 
          "type": "string"
        }, 
        "io": {
          "description": "Block I/O usage, in number of 512-byte sectors read from and written to, by this execution.", 
          "type": "int"
        }, 
        "owner": {
          "description": "username of the owner of the actor.", 
          "type": "string"
        }, 
        "runtime": {
          "description": "Runtime, in milliseconds, of this execution.", 
          "type": "int"
        }, 
        "status": {
          "description": "status of the execution.", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy Execution schema", 
      "type": "object"
    }

getOneExecutionResult: Get result for a specific actor execution.
=================================================================
``agavepy.actors.getOneExecutionResult(actorId, executionId)``

Parameters:
-----------
    * **actorId**: The id of the actor. (string)
    * **executionId**: The id of the execution. (string)


Response:
---------
    * *None*

getExecutionLogs: Get logs for a specific actor execution.
==========================================================
``agavepy.actors.getExecutionLogs(actorId, executionId)``

Parameters:
-----------
    * **actorId**: The id of the actor. (string)
    * **executionId**: The id of the execution. (string)


Response:
---------
    * *A single ExecutionLogs object*

**ExecutionLogs schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/ExecutionLogs.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "logs": {
          "description": "The logs (standard out) of this execution.", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy ExecutionLogs schema", 
      "type": "object"
    }

