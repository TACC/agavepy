.. _installation_guide:
.. _installation:

Installation Guide
==================

.. contents:: Topics

.. _what_will_be_installed:

What will be installed
``````````````````````

In this guide we will cover how to get ``AgavePy`` into your machine.
We will cover how to install the latest official release.
Also, we will cover how to install the latest from the development branch in 
case you want to get the latest features and help the TACC team build the most 
useful and performant software that meets your needs.

.. _what_version:

What version to install
```````````````````````
``AgavePy`` is under constant development. 
Some features may be missing from oficial releases but in general oficial
releases are pushed when the project has reached a stable state.

.. _from_pipy:

Latest stable release from PiPy
+++++++++++++++++++++++++++++++

You can install the latest official `releases <https://pypi.org/project/agavepy/#history>`_.

.. code-block:: console

    pip install agavepy

For a specific version:

.. code-block:: console

    pip install agavepy==0.73


.. _from_source:

Latest stable release from source
+++++++++++++++++++++++++++++++++

You can also install the latest releases from source, either from the master or
from the develop branch.

You will need to first obtain the source code. 
To get a copy of the ``AgavePy`` repository do:

.. code-block:: console

    git clone https://github.com/TACC/agavepy


Once you have cloned the repository, go into it and choose the branch you want
to install.
If you want to install the development version, you can checkout the
``develop`` branch as follows:

.. code-block:: console

    git checkout develop


If you have `GNU make <https://www.gnu.org/software/make/manual/make.html>`_
installed in your system, you can install ``AgavePy`` for Python 3 as follows:

.. code-block:: console

    make install

To install ``AgavePy`` for Python 2,

.. code-block:: console

    make install-py2

The ``Makefile`` uses the ``setup.py`` file for all installation related logic.
