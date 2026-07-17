from datetime import timezone, datetime 
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import Request

def build_response(status_code: int, message: str, data = None, error = None, path: str = ""):
    payload = {
        "statusCode"    : status_code,
        "message"       : message,
        "error"         : error,
        "data"          : jsonable_encoder(data) if data is not None else None,
        "path"          : Request.url.path,
        "timestamp"     : datetime.now(timezone.utc).isoformat(),
    }

    return JSONResponse(status_code= status_code, content= payload)