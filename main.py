import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI

from db import database
from resources.routes import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)
app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run(app, host = '0.0.0.0', port=8000)