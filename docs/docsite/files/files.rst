.. _files:

##################
Working with files
##################

If you have already initiated a session, `authentication`, and have a storage
system setup then you start working with files.


Listing files and directories
#############################

Before we even get started, we should know what it is we are going to be
working with.
To see any files or directories in your remote storage system, let's say this
is called ``data-tacc-user``.

.. code-block:: pycon

    >>> agave.files_list("/data-tacc-user")
    ./                 .slurm/            apps/              benchmarks/
    bigfile            cptests/           users/             myotherfile
    old-sd2e-apps/     rpmbuild/          sd2e-apps/         sd2e-data/
    singularity-test/  somefile           SP1-copy.fq        SP1.fq 
    tests/             

For more details, such as permissions and size:

.. code-block:: pycon

    >>> agave.files_list("data-tacc-user/", long_format=True)
    drwx       4096 Oct 25 14:47 ./
    drwx       4096 May 25 16:13 .slurm/
    drwx       4096 Jun  5 10:14 apps/ 
    drwx       4096 Jun  9 18:39 benchmarks/
    -rw- 1073741824 Oct 25 14:48 bigfile
    drwx       4096 Jul 13 09:17 cptests/
    drwx       4096 Aug  1 14:26 users/ 
    -rw-         24 Oct 25 14:42 myotherfile 
    drwx       4096 Jul 10 11:27 old-sd2e-apps/   
    drwx       4096 Jun 29 10:40 rpmbuild/    
    drwx       4096 Jul 13 15:41 sd2e-apps/
    drwx       4096 Jul  7 20:43 sd2e-data/   
    drwx       4096 Jul  9 16:50 singularity-test/  
    -rw-         24 Oct 25 14:20 somefile
    -rw-      22471 Aug 22 14:40 SP1-copy.fq   
    -rw-      22471 Jul  7 20:42 SP1.fq 
    drwx       4096 Aug 24 13:44 tests/   
    

Download a file
###############

Let's say you have a file named ``SP1.fq`` on your remote storage system,
``data-tacc-user``.

You can download the file, ``SP1.fq``, to your host and specify the location of
where you want to store the file (i.e., ``/opt/data/SP1.fq``) as such:

.. code-block:: pycon

    >>> agave.files_download("data-tacc-user/SP1.fq", "/opt/data/SP1.fq")


Upload a file
#############

Similarly, if you want to upload a file, ``data.ext``, and you
want to save it on your stoorage system named, ``data-tacc-user`` under
the name ``cool_data.bin``.

.. code-block:: pycon

    >>> agave.files_upload("./data.ext", "data-tacc-user/cool.ext")


Make a copy of a file on a remote system
########################################

So now, you have a ``cool.ext`` file on your remote storage
system, ``data-tacc-user``. Let's make a copy of it!


.. code-block:: pycon

    >>> agave.files_copy("data-tacc-user/cool.ext", "data-tacc-user/copy.ext")


Move files
##########

To move files around on a remote storage system, you can do so as follows:

.. code-block:: pycon

    >>> agave.files_move("data-tacc-user/file.ext", "data-tacc-user/dir/file.ext")



Delete a file
#############

On the other hand, if there is a file or directory that you want to get rid
off:

.. code-block:: pycon

    >>> agave.files_delete("data-tacc-user/somefile-or-directory")


Import files from ther systems
##############################

It may be useful to import data from other storage systems, e.g. from the
community data space to your private data space.
The ``files_import`` method can be used for that purpose.

.. code-block:: pycon

    agave.files_import("agave://data-community/test.txt", "system-id/")

Please also note that even though you are able to import files from other Agave
storage systems, you may not always need to import those files.
Also, note that the source, the first argument, must be an agave compliant uri
by prefixing the system if and path convination with the string ``agave://``.


Making a directory
##################

``AgavePy`` also provides ``mkdir``-like functionality.
To create a directory on a remote storage system:

.. code-block:: pycon

    >>> agave.files_mkdir("data-tacc-user/new_dir")
