********
Profiles
********

Summary: Create and manage application users

list: List user profiles
========================
``agavepy.profiles.list(email=None, first_name=None, full_name=None, last_name=None, limit=250, name=None, offset=0, status=None, username=None)``

Parameters:
-----------
    * **limit**: The max number of results. (integer)
    * **offset**: The number of records to when returning the results. When paginating results, the page number = ceil(offset/limit) (integer)
    * **name**: Filter results by name. (string)
    * **email**: Filter results by email. (string)
    * **first_name**: Filter results by first_name. (string)
    * **last_name**: Filter results by last_name. (string)
    * **full_name**: Filter results by full_name. (string)
    * **status**: Filter results by status. (string)
    * **username**: Filter results by username. (string)


Response:
---------
    * *Array of Profile objects*

**Profile schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/Profile.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "city": {
          "description": "The api user's city.", 
          "type": "string"
        }, 
        "country": {
          "description": "The api user's country.", 
          "type": "string"
        }, 
        "department": {
          "description": "The api user's institutional department.", 
          "type": "string"
        }, 
        "email": {
          "description": "The api user's unique email address.", 
          "type": "string"
        }, 
        "fax": {
          "description": "The api user's fax number.", 
          "type": "string"
        }, 
        "firstName": {
          "description": "The api user's first name.", 
          "type": "string"
        }, 
        "gender": {
          "description": "The api user's gender. male or female.", 
          "type": "string"
        }, 
        "institution": {
          "description": "The api user's home institution", 
          "type": "string"
        }, 
        "lastName": {
          "description": "The api user's last name.", 
          "type": "string"
        }, 
        "phone": {
          "description": "The api user's phone number.", 
          "type": "string"
        }, 
        "position": {
          "description": "The api user's position of employment.", 
          "type": "string"
        }, 
        "researchArea": {
          "description": "The api user's primary area of research.", 
          "type": "string"
        }, 
        "state": {
          "description": "The api user's state.", 
          "type": "string"
        }, 
        "username": {
          "description": "The api user's unique username.", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy Profile schema", 
      "type": "object"
    }

get: Find authenticated user profile
====================================
``agavepy.profiles.get()``

Parameters:
-----------


Response:
---------
    * *A single Profile object*

**Profile schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/Profile.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "city": {
          "description": "The api user's city.", 
          "type": "string"
        }, 
        "country": {
          "description": "The api user's country.", 
          "type": "string"
        }, 
        "department": {
          "description": "The api user's institutional department.", 
          "type": "string"
        }, 
        "email": {
          "description": "The api user's unique email address.", 
          "type": "string"
        }, 
        "fax": {
          "description": "The api user's fax number.", 
          "type": "string"
        }, 
        "firstName": {
          "description": "The api user's first name.", 
          "type": "string"
        }, 
        "gender": {
          "description": "The api user's gender. male or female.", 
          "type": "string"
        }, 
        "institution": {
          "description": "The api user's home institution", 
          "type": "string"
        }, 
        "lastName": {
          "description": "The api user's last name.", 
          "type": "string"
        }, 
        "phone": {
          "description": "The api user's phone number.", 
          "type": "string"
        }, 
        "position": {
          "description": "The api user's position of employment.", 
          "type": "string"
        }, 
        "researchArea": {
          "description": "The api user's primary area of research.", 
          "type": "string"
        }, 
        "state": {
          "description": "The api user's state.", 
          "type": "string"
        }, 
        "username": {
          "description": "The api user's unique username.", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy Profile schema", 
      "type": "object"
    }

listByUsername: Find api user profile by their api username
===========================================================
``agavepy.profiles.listByUsername(username)``

Parameters:
-----------
    * **username**: The username of a valid api user (string)


Response:
---------
    * *A single Profile object*

**Profile schema**

.. code-block:: javascript

    {
      "$id": "http://agavepy.readthedocs.io/en/latest/Profile.json", 
      "$schema": "http://json-schema.org/draft-07/schema#", 
      "properties": {
        "city": {
          "description": "The api user's city.", 
          "type": "string"
        }, 
        "country": {
          "description": "The api user's country.", 
          "type": "string"
        }, 
        "department": {
          "description": "The api user's institutional department.", 
          "type": "string"
        }, 
        "email": {
          "description": "The api user's unique email address.", 
          "type": "string"
        }, 
        "fax": {
          "description": "The api user's fax number.", 
          "type": "string"
        }, 
        "firstName": {
          "description": "The api user's first name.", 
          "type": "string"
        }, 
        "gender": {
          "description": "The api user's gender. male or female.", 
          "type": "string"
        }, 
        "institution": {
          "description": "The api user's home institution", 
          "type": "string"
        }, 
        "lastName": {
          "description": "The api user's last name.", 
          "type": "string"
        }, 
        "phone": {
          "description": "The api user's phone number.", 
          "type": "string"
        }, 
        "position": {
          "description": "The api user's position of employment.", 
          "type": "string"
        }, 
        "researchArea": {
          "description": "The api user's primary area of research.", 
          "type": "string"
        }, 
        "state": {
          "description": "The api user's state.", 
          "type": "string"
        }, 
        "username": {
          "description": "The api user's unique username.", 
          "type": "string"
        }
      }, 
      "required": [], 
      "title": "AgavePy Profile schema", 
      "type": "object"
    }

