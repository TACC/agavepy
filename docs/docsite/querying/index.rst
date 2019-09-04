========                                       
Querying
========                                       
                                                                                
Agave resources can be queried to search for items using parameters. Every resource list operation
can be passed a dictionary of search terms and values using the ``query`` argument. For example,
you may search Jobs submissions for a specific appId using the following agavepy code:

``agave.jobs.list(query={"appId.like", "*matlab*"})``