"""main API module"""
from fastapi import FastAPI, Request
from pydantic import BaseModel
import requests
from get_token import get_access_token
from list_locks import get_list_locks, get_lock_id_for_room
from get_passcode import get_access_passcode

app = FastAPI()


# Define a custom middleware function
@app.middleware("http")
async def add_cors_header(request: Request, call_next):
    """function to add cors"""
    response = await call_next(request)
    response.headers[
        "Access-Control-Allow-Origin"
    ] = "*"  # You can specify specific origins instead of "*"
    return response


class DateRange(BaseModel):
    """Data range model"""
    startDate: str
    endDate: str


@app.get("/")
async def root():
    """home page"""
    return {"message": "Welcome to the Locks API"}


@app.get("/token")
async def token():
    """create or refresh a token"""
    try:
        access_token = get_access_token()
        return {"Access Token": access_token, "message": "Success!!!"}
    except requests.exceptions.ConnectionError as exception:
        return {"error": str(exception)}


@app.get("/list_locks")
async def list_locks():
    """gets all the locks registered"""
    try:
        access_token = get_access_token()
        current_list = get_list_locks(access_token)
        return current_list
    except requests.exceptions.ConnectionError as exception:
        return {"error": str(exception)}


@app.get("/get_passcode")
async def get_passcode(room_no: str, start_date: str, end_date: str):
    """gets a passcode for a specific lock for the specific days"""
    try:
        access_token = get_access_token()
        passcode = get_access_passcode(access_token, room_no, start_date, end_date)
        return {"Passcode": passcode}

    except requests.exceptions.ConnectionError as exception:
        return {"error": str(exception)}


@app.get("/get_lock_id")
async def get_lock_id(room_no):
    """gets the id for a room number"""
    try:
        access_token = get_access_token()
        lock_id = get_lock_id_for_room(access_token, room_no)
        return lock_id

    except requests.exceptions.ConnectionError as exception:
        return {"error": str(exception)}
