from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.db.main import init_db
from src.users.route import user_router
from src.masterData.router import master_router
@asynccontextmanager
async def lifespan(app:FastAPI):
    print("server is running on port 8000")
    await init_db()

    yield
    print("server is shutting down")




app =FastAPI(
    title="Close BI",
    version="0.1.0",
    description="A simple crud Application using FastAPI",
    lifespan=lifespan
)

app.include_router(user_router,tags=["users"])
app.include_router(master_router, tags=["masterData"])