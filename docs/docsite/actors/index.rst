======                                           
Actors
======                                           

`Abaco <http://useabaco.cloud/>`_ is a Tapis web service providing 
functions-as-a-service (FaaS) to the research computing community. 
It implements functions using the `Actor Model <https://en.wikipedia.org/wiki/Actor_model>`_ 
of concurrent computation, so the relevant API name in Tapis is **actors**.

In Abaco, each actor is associated with a Docker image, and actor containers 
are executed in response to messages posted to their inbox, which itself is 
given by a URI exposed over HTTP. Use cases for Abaco actors include moving 
data, running Tapis apps, interacting with other actors, and interoperating 
with third-party web services. 

The functions documented here help you to discover, inspect, manage, and 
use Abaco actors_.

.. toctree::                                                                    
   :maxdepth: 2                                                                 
                                                                                
   actors

.. only::  subproject and html                                                  
                                                                                
   Indices                                                                      
   =======                                                                      
                                                                                
   * :ref:`genindex`

.. Links

.. _actors: https://tacc-cloud.readthedocs.io/projects/abaco/en/latest/
