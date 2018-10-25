.. _files:

##################
Working with files
##################

If you have already initiated a session, `authentication`, and have a storage
system setup then you start working with files.

Download a file
###############

Let's say you have a file name ``SP1.fq`` on your remote storage system which
is called ``tacc-globalfs-username``.

You can download the file ``SP1.fq`` to your host and specify the location of
where you want to store the file (i.e., ``/opt/data/SP1.fq``) as such:

.. code-block:: pycon

    >>> agave.files_download("tacc-globalfs-username/SP1.fq", "/opt/data/SP1.fq")


Upload a file
#############

Similarly, if you want to upload a file, ``my_important_data.ext``, and you
want to save it on your stoorage system named ``tacc-globalfs-username`` under
the name ``super_cool_data.bin``.

.. code-block:: pycon

    >>> agave.files_upload("./my_important_data.ext", "tacc-globalfs-username/super_cool_data.bin")
