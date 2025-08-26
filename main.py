from fastapi import FastAPI
from database import init_db
from contextlib import asynccontextmanager
from task_routes import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan: initialize database at startup, cleanup at shutdown."""
    init_db()
    yield 

app = FastAPI(lifespan=lifespan)
app.include_router(router)