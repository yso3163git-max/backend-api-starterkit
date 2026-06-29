class AppException(Exception):
  def __init__(self, status_code: int, code: str, message: str):
    self.status_code = status_code
    self.code = code
    self.message = message
    super().__init__(message)


class NotFoundError(AppException):
  def __init__(self, message: str = "리소스를 찾을 수 없습니다."):
    super().__init__(status_code=404, code="NOT_FOUND", message=message)


class UnauthorizedError(AppException):
  def __init__(self, message: str = "인증이 필요합니다."):
    super().__init__(status_code=401, code="UNAUTHORIZED", message=message)


class ForbiddenError(AppException):
  def __init__(self, message: str = "접근 권한이 없습니다."):
    super().__init__(status_code=403, code="FORBIDDEN", message=message)


class BadRequestError(AppException):
  def __init__(self, message: str = "잘못된 요청입니다."):
    super().__init__(status_code=400, code="BAD_REQUEST", message=message)
