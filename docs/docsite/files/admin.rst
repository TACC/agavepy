##############
Managing Files
##############

Managing permissions
####################
Use ``files-pems-list`` to list the user permissions associated with a file or
folder. These permissions are set at the API level and do not reflect unix-like
or other file system ACL.

.. code-block:: pycon

    >>> ag.files_pems_list("system-id/some-dir")
    USER     READ   WRITE  EXEC
    username yes    yes    yes

To remove all the permissions on a file, except those of the owner:

.. code-block:: pycon

    agave.files_pems_delete("system-id/some-dir")


To edit permissions for another user, let's say her username is "collab,"
to view a file:

.. code-block:: pycon

    ag.files_pems_update("system-id/path", "collab", "ALL", recursive=True)

Now, a user with username "collab" has permissions to access the all contents
of the specified directory (hence the ``recursive=True`` option).

Valid values for setting permission are ``READ``, ``WRITE``, ``EXECUTE``, 
``READ_WRITE``, ``READ_EXECUTE``, ``WRITE_EXECUTE``, ``ALL``, and ``NONE``.
This same action can be performed recursively on directories using ``recursive=True``.


File or Directory History
#########################
You can list the history of events for a specific file or folder. 
This will give more descriptive information (when applicable) related to number
of retries, permission grants and revocations, reasons for failure, and hiccups
that may have occurred in a recent process.

.. code-block:: pycon

    >>> ag.files_history("system-id/path/to/dir")
    USER          EVENT                DATE                             DESCRIPTION
    username      CREATED              2018-11-02T10:08:54.000-05:00    New directory created at https://api.sd2e.org/files/v2/media/system/system-id//path/to/dir
    username      PERMISSION_REVOKE    2018-11-30T11:22:01.000-06:00    All permissions revoked
    username      PERMISSION_GRANT     2018-12-03T10:11:07.000-06:00    OWNER permission granted to collaborator

