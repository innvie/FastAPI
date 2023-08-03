from fastapi import FastAPI
from get_token import get_access_token

app = FastAPI()


@app.get("/")
async def root():
    access_token_info = get_access_token()
    if access_token_info:
        access_token = access_token_info.get("access_token")
        print("Access Token:", access_token)
    return {"Access Token": access_token, "message": "Success!!!"}
