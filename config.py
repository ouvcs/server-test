from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import Response
from starlette.exceptions import HTTPException as StarletteHTTPException
import json
from tinydb import TinyDB, Query

class PrettyJSONResponse(Response):
    def __init__(self, content, *args, **kwargs):
        super().__init__(content=json.dumps(content, indent=4, ensure_ascii=False), media_type="application/json", *args, **kwargs)

translations = TinyDB("translations.db")
lang = Query()

def translation(id: str, language: str):
    translate = translations.search(lang.id == id)
    
    if len(translate) == 0:
        return "|o|"
    else:
        if language in translate[0]:
            return translate[0][language]
        else:
            return translate[0]["eng"]