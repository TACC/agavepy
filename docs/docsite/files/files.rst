.. _files:

##################
Working with files
##################

If you have already initiated a session, `authentication`, and have a storage
system setup then you start working with files.

Downloading a file
##################

Let's say you have a file name ``SP1.fq`` on your remote storage system which
is called ``tacc-globalfs-username``.

You can download the file ``SP1.fq`` to your host and specify the location of
where you want to store the file (i.e., ``/opt/data/SP1.fq``) as such:

.. code-block:: pycon

    >>> agave.files_download("tacc-globalfs-username/SP1.fq", "/opt/data/SP1.fq")
