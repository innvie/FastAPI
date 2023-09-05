import uvicorn
from os import getenv

if __name__ == "__main__":
    uvicorn.run(
        "api:app", host="0.0.0.0", port=int(getenv("PORT", "8000")), reload=True
    )
