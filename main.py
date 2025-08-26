from fastapi import FastAPI
from database import init_db, close_db
from contextlib import asynccontextmanager
from task_routes import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan: initialize database at startup, cleanup at shutdown."""
    init_db()
    yield #####!!!!!before yield will be executed before application starts, after will be executed after
    close_db()

app = FastAPI(lifespan=lifespan)
app.include_router(router)