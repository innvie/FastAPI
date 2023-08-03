from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"greeting": "Hello, Gabo!", "message": "Welcome to FastAPI!"}
