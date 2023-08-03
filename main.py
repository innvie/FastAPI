from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"greeting": "Innvie lock API", "message": "Welcome to FastAPI!"}
