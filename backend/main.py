from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.cover_letter import router as cover_letter_router
from app.api.job_application import router as job_application_router
from app.api.jobs import router as jobs_router
from app.api.resume import router as resume_router
from app.core import logger
from app.core.config import settings
from app.core.exceptions import AppException
from app.core.handlers import app_exception_handler
from app.middleware.logging import logging_middleware
# NEW
from app.scheduler.job_scheduler import start_scheduler, stop_scheduler


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Runs when FastAPI starts and stops.
    """

    # Start scheduler
    if not settings.TESTING:
        start_scheduler()

    yield

    # Stop scheduler
    if not settings.TESTING:
        stop_scheduler()


app = FastAPI(title="JobPilot AI", version="1.0.0", debug=True, lifespan=lifespan)
app.add_exception_handler(AppException, app_exception_handler)

app.include_router(auth_router)
app.include_router(jobs_router)
app.include_router(resume_router)
app.include_router(cover_letter_router)
app.include_router(job_application_router)
app.middleware("http")(logging_middleware)


@app.get("/")
def home():
    return {"message": "Welcome to JobPilot AI"}
