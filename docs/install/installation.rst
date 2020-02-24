##################
Installing AgavePy
##################

.. _from_pipy:

The preferred, most compatible way to install AgavePy is to use 
PyPi. Current and all past `releases <https://pypi.org/project/agavepy/#history>`_ 
are available unless deprecated to resolve security issues 
or functional defects. 

.. code-block:: console

    pip install agavepy

For a specific version:

.. code-block:: console

    pip install agavepy==1.0.0


.. _from_source:

***********
From source
***********

You can also install the latest AgavePy releases from source.

Obtain the source code from GitHub 
==================================

.. code-block:: console

    git clone https://github.com/TACC/agavepy

This will check out the ``master`` branch. To checkout an alternative 
branch (for example ``develop``), do the following:

.. code-block:: console

    cd agavepy
    git checkout develop

Install with setuptools
=======================

Within the ``agavepy`` source directory:

.. code-block:: console
    
    python setup.py install

Install with GNU make
=====================

If `GNU make <https://www.gnu.org/software/make/manual/make.html>`_ 
is installed in your system, you can install ``AgavePy`` for Python 3 
as follows:

.. code-block:: console

    make install

You can install for Python 2 like so:

.. code-block:: console

    make install-py2

.. only::  subproject and html

   Indices
   =======

   * :ref:`genindex`
