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
