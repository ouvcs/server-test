import datetime
import json
from tinydb import TinyDB, Query


def method(cluster: str, method: str, **kwargs):
    response = {"info": f"{cluster}.{method}", "status": 404, "response": {}}
    
    if cluster == "countries":
        if method == "all":
            response["response"] = ""
            response["status"] = 200
        elif method == "get":
            response["response"] = ""
            response["status"] = 200
    elif cluster == "valutes":
        if method == "all":
            response["response"] = ""
            response["status"] = 200
        elif method == "get":
            response["response"] = ""
            response["status"] = 200
        elif method == "change":
            response["response"] = ""
            response["status"] = 200
    elif cluster == "accounts":
        if method == "all":
            response["response"] = ""
            response["status"] = 200
        elif method == "get":
            response["response"] = ""
            response["status"] = 200
        elif method == "create":
            response["response"] = ""
            response["status"] = 200
        elif method == "update":
            response["response"] = ""
            response["status"] = 200
    
    return response