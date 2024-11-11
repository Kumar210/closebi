from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.db.main import init_db
from src.users.route import user_router
from src.master_data.router import master_router
from src.google_analatics.router import analytics_router
from src.gcb.router import gcb_router
from src.sc_log.router import sc_log_router
from src.call_log.router import call_log_router
from src.invoice_log.router import invoice_log_router
from src.permission.route import permission_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("server is running on port 8000")
    await init_db()

    yield
    print("server is shutting down")


app = FastAPI(
    title="Close BI",
    version="0.1.0",
    description="A simple crud Application using FastAPI",
    lifespan=lifespan,
)

app.include_router(user_router,tags=["users"])
app.include_router(master_router, tags=["Master Data"])
app.include_router(analytics_router, tags=["Google Analytics"])
app.include_router(gcb_router, tags=["GCB"])
app.include_router(sc_log_router, tags=["Search Console"])
app.include_router(call_log_router, tags=["Call logs service"])
app.include_router(invoice_log_router, tags=["Revenue service"])
app.include_router(permission_router,tags=["Permission"])
