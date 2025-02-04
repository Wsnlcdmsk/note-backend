from fastapi import FastAPI
from src.routers import tasks, auth
from src.init_db import init_db

app = FastAPI()

init_db()

app.include_router(auth.router, prefix="/auth", tags=["authification"])
app.include_router(tasks.router, tags=["tasks"])
