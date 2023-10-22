from tinydb import TinyDB, Query
from fastapi import FastAPI, HTTPException, Request
from starlette.exceptions import HTTPException as StarletteHTTPException
from config import PrettyJSONResponse, translation
import infos
import methods

app = FastAPI()

db = TinyDB("accounts.db")
Account = Query()

@app.get("/", response_class=PrettyJSONResponse)
async def index(l: str = "eng"):
    return {"details": translation("index", l), "status": 400}

@app.get("/info/{cluster}.{info}", response_class=PrettyJSONResponse)
async def execute_info(cluster: str, info: str, l: str = "eng", **kwargs):
    return infos.info(cluster, info, **kwargs)

@app.get("/method/{cluster}.{method}", response_class=PrettyJSONResponse)
async def execute_method(cluster: str, method: str, l: str = "eng", **kwargs):
    return infos.info(cluster, method, **kwargs)


@app.exception_handler(HTTPException)
@app.exception_handler(StarletteHTTPException)
async def exception_handler(request: Request, exc: HTTPException | StarletteHTTPException):
    return PrettyJSONResponse(
        status_code=exc.status_code,
        content={"details": translation("error", request.query_params["l"]), "status": exc.status_code},
    )