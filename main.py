"""Starting module for the api"""
from os import getenv
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "api:app", host="0.0.0.0", port=int(getenv("PORT", "8000")), reload=True
    )
