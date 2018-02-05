****************
agavepy.profiles
****************

Summary: Create and manage application users

list
====
``agavepy.profiles.list(email=None, first_name=None, full_name=None, last_name=None, limit=250, name=None, offset=0, status=None, username=None)``

List user profiles

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
    * *Coming soon*

get
===
``agavepy.profiles.get()``

Find authenticated user profile

Parameters:
-----------


Response:
---------
    * *Coming soon*

listByUsername
==============
``agavepy.profiles.listByUsername(username)``

Find api user profile by their api username

Parameters:
-----------
    * **username**: The username of a valid api user (string)


Response:
---------
    * *Coming soon*

