"""
    response_hanlders.py
"""
from __future__ import print_function
import sys



def handle_bad_response_status_code(r):                                         
    """ Handle a response with a bad status code                                
    """                                                                         
    if not r.ok:                                                             
        print("Bad {0} request to {1}, status code {2}".format(                 
                r.request.method, r.url, r.status_code),                        
                file=sys.stderr)
        print(r.request.body)
        print(r.json())                                                         
        sys.exit(1)
