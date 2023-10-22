import datetime
import json
from tinydb import TinyDB, Query


def languages_list():
    return {
        "supported_languages": {
            "Russian": "rus",
            "English": "eng",
            "Pre-reform Russian": "rud",
            "Latin": "lat",
            "Finnish": "fin"
        },
        "query_with_language": "https://example.com/method/example.method?l=eng"
    }
    
    
def info(cluster: str, info: str, **kwargs):
    response = {"info": f"{cluster}.{info}", "status": 404, "response": {}}
    
    if cluster == "languages":
        if info == "list":
            response["response"] = languages_list()
            response["status"] = 200
    
    return response