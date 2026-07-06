from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.middleware.error_handler import add_error_handlers
from app.routers import health, users

settings = get_settings()

app = FastAPI(
  title=settings.app_name,
  version=settings.app_version,
  docs_url="/docs",
  redoc_url="/redoc",
)

app.add_middleware(
  CORSMiddleware,
  allow_origins=settings.cors_origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

add_error_handlers(app)

app.include_router(health.router)
app.include_router(users.router, prefix=settings.api_prefix)
