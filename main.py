from fastapi import FastAPI, Request, Response, HTTPException
from get_token import get_access_token
from list_locks import get_list_locks
from get_passcode import get_access_passcode
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()


# Define a custom middleware function
@app.middleware("http")
async def add_cors_header(request: Request, call_next):
    response = await call_next(request)
    response.headers[
        "Access-Control-Allow-Origin"
    ] = "*"  # You can specify specific origins instead of "*"
    return response


class DateRange(BaseModel):
    startDate: str
    endDate: str


@app.get("/")
async def root():
    return {"message": "Welcome to the Locks API"}


@app.get("/token")
async def root():
    try:
        access_token = get_access_token()
        return {"Access Token": access_token, "message": "Success!!!"}
    except Exception as e:
        return {"error": str(e)}


@app.get("/list_locks")
async def list_locks():
    try:
        access_token = get_access_token()
        current_list = get_list_locks(access_token)
        return current_list
    except Exception as e:
        return {"error": str(e)}


@app.get("/get_passcode")
async def get_passcode(roomNo: str, startDate: str, endDate: str):
    try:
        access_token = get_access_token()
        passcode = get_access_passcode(access_token, roomNo, startDate, endDate)
        return {"Passcode": passcode}

    except Exception as e:
        return {"error": str(e)}


@app.get("/get_lock_id")
async def get_passcode():
    try:
        access_token = get_access_token()
        passcode = get_access_passcode(access_token, roomNo, startDate, endDate)
        return {"Passcode": passcode}

    except Exception as e:
        return {"error": str(e)}
