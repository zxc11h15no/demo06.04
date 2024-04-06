from fastapi import FastAPI
import uvicorn

from base import create_base

from routers.user import user_router

create_base()

app = FastAPI()

app.include_router(user_router,prefix="/user")

PORT = 8000
HOST = "127.0.0.1"

if __name__ ==" __main__":
    uvicorn.run("main:app",PORT,HOST, reload=True)