######                                      
Search
######                                      
                                                                                
Tapis resources can be queried to search for items using parameters. Every resource ``list`` operation
can be passed a dictionary of search terms and values using the ``query`` argument. For example,
you may search Jobs submissions for a specific appId using the following code:

``Agave.jobs.list(query={"appId.like", "*matlab*"})``

Additional detail on Tapis seach is available from the Tapis API documentation_. 

.. Links

.. _documentation: https://tacc-cloud.readthedocs.io/projects/agave/en/latest/agave/guides/search/introduction.html
