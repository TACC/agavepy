.. _tenants:

####################
Initiating a Session
####################

To work with the Agave API, ``AgavePy`` implements the ``agavepy.agave.Agave``
object.

The first step for a user to authenticate with the Agave API is to specify the
which tenant to interact with. 
Whenever the user makes a request to the Agave api, ``Agave`` will require the
tenant's base url to make the request.
In order for the user to refer to this tenant in the future in a more
human-friendly way, the ``Agave`` object also makes available the tenant id.

Specifying a tenant interactively
#################################

``AgavePy`` provides two ways for a user to initiate a session.
The first approaches requires the user to specify the tenant information - its 
ID and/or the the base url for it - and use the method ``init`` from ``Agave``.
The ``init`` method will make sure that the ``tenant_id`` and ``api_server``
variables are set.

To see all available tenants and chose one to interact with, one can do the
following:

.. code-block:: pycon
    
    >>> from agavepy.agave import Agave
    >>> agave = Agave()
    >>> agave.init()
    ID                   NAME                                     URL
    3dem                 3dem Tenant                              https://api.3dem.org/
    agave.prod           Agave Public Tenant                      https://public.agaveapi.co/
    araport.org          Araport                                  https://api.araport.org/
    designsafe           DesignSafe                               https://agave.designsafe-ci.org/
    iplantc.org          CyVerse Science APIs                     https://agave.iplantc.org/
    irec                 iReceptor                                https://irec.tenants.prod.tacc.cloud/
    portals              Portals Tenant                           https://portals-api.tacc.utexas.edu/
    sd2e                 SD2E Tenant                              https://api.sd2e.org/
    sgci                 Science Gateways Community Institute     https://sgci.tacc.cloud/
    tacc.prod            TACC                                     https://api.tacc.utexas.edu/
    vdjserver.org        VDJ Server                               https://vdj-agave-api.tacc.utexas.edu/

    Please specify the ID for the tenant you wish to interact with: sd2e
    >>> agave.tenant_id, agave.api_server
    ('sd2e', 'https://api.sd2e.org')


If you already know the tenant id you can specify it at the moment you
instantiate the ``Agave`` object.

.. code-block:: pycon

    >>> agave = Agave(tenant_id="sd2e")
    >>> agave.init()
    >>> agave.tenant_id, agave.api_server
    ('sd2e', 'https://api.sd2e.org')

Similarly, if you know the base url for the tenant.

.. code-block:: pycon

    >>> agave = Agave(api_server="https://api.sd2e.org/")
    >>> agave.init()
    >>> agave.tenant_id, agave.api_server
    ('sd2e', 'https://api.sd2e.org/')


Using an existing session
#########################

The second authentication approach that you can follow is to load a previous
session that has been saved to a configurations file using the method
``load_configs``.

If you already created an oauth client and have a pair of access and refresh
tokens then you can save this session by using the method ``save_configs``. 
To reuse it, simply instantiate an ``Agave`` object use the method
``load_configs`` to use an existing session.

.. code-block:: pycon

    >>> from agavepy.agave import Agave
    >>> agave = Agave()
    >>> agave.load_configs()
    >>> agave.tenant_id, agave.api_server
    ('sd2e', 'https://api.sd2e.org/')

``load_configs`` takes four optional arguments:

* ``cache_dir`` directory to store configurations in (it defaults to
  ``~/.agave``)
* ``tenant_id`` tenant id of the session to restore
* ``username`` username for the session to restore
* ``client_name`` name of oauth client for the session to restore
