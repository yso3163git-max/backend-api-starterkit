from fastapi import APIRouter, Depends

from app.config import Settings, get_settings
from app.schemas.common import SuccessResponse

router = APIRouter(tags=["health"])


@router.get("/health", response_model=SuccessResponse)
async def health_check(settings: Settings = Depends(get_settings)):
  return SuccessResponse(data={
    "status": "ok",
    "app_name": settings.app_name,
    "version": settings.app_version,
  })
