from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from app.exceptions import AppException


def add_error_handlers(app: FastAPI) -> None:
  @app.exception_handler(AppException)
  async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
      status_code=exc.status_code,
      content={
        "success": False,
        "error": {"code": exc.code, "message": exc.message},
      },
    )

  @app.exception_handler(RequestValidationError)
  async def validation_exception_handler(request: Request, exc: RequestValidationError):
    first_error = exc.errors()[0] if exc.errors() else {}
    message = first_error.get("msg", "입력값이 올바르지 않습니다.")
    return JSONResponse(
      status_code=422,
      content={
        "success": False,
        "error": {"code": "VALIDATION_ERROR", "message": message},
      },
    )

  @app.exception_handler(Exception)
  async def unhandled_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
      status_code=500,
      content={
        "success": False,
        "error": {"code": "INTERNAL_ERROR", "message": "서버 내부 오류가 발생했습니다."},
      },
    )
