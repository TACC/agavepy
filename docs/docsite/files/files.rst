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
is called ``tacc-globalfs-username``.

.. code-block:: pycon

    >>> agave.files_list("tacc-globalfs-username/")
    ./                 .slurm/            apps/              benchmarks/
    bigfile            cptests/           users/             myotherfile
    old-sd2e-apps/     rpmbuild/          sd2e-apps/         sd2e-data/
    singularity-test/  somefile           SP1-copy.fq        SP1.fq 
    tests/             

For more details, such as permissions and size:

.. code-block:: pycon

    >>> agave.files_list("tacc-globalfs-username/", long_format=True)
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

Let's say you have a file name ``SP1.fq`` on your remote storage system which
is called ``tacc-globalfs-username``.

You can download the file ``SP1.fq`` to your host and specify the location of
where you want to store the file (i.e., ``/opt/data/SP1.fq``) as such:

.. code-block:: pycon

    >>> agave.files_download("tacc-globalfs-username/SP1.fq", "/opt/data/SP1.fq")


Upload a file
#############

Similarly, if you want to upload a file, ``important_data.ext``, and you
want to save it on your stoorage system named ``tacc-globalfs-username`` under
the name ``cool_data.bin``.

.. code-block:: pycon

    >>> agave.files_upload("./important_data.ext",
            "tacc-globalfs-username/cool_data.bin")


Make a copy of a file on a remote system
########################################

So now, you have a file called ``important_data.ext`` on your remote storage
system ``tacc-globalfs-username``. Let's make a copy of it:


.. code-block:: pycon

    >>> agave.files_copy("tacc-globalfs-username/important_data.ext", 
            "tacc-globalfs-username/important_data-copy.ext")


Delete a file
#############

On the other hand, if there is a file or directory that you want to get rid
off:

.. code-block:: pycon

    >>> agave.files_delete("tacc-globalfs-username/somefile-or-directory")
