from fastapi import Request
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from response import build_response


class AppException(Exception):
    def __init__(self, status_code: int, message: str, error: str = "APP_ERROR"):
        self.status_code = status_code
        self.message = message
        self.error = error


async def app_exception_handler(request: Request, exc: AppException):
    return build_response(
        status_code=exc.status_code,
        message=exc.message,
        error=exc.error,
        path=str(request.url.path),
    )


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return build_response(
        status_code=422,
        message="Dữ liệu gửi lên không hợp lệ",
        error="VALIDATION_ERROR",
        data=exc.errors(),
        path=str(request.url.path),
    )


async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return build_response(
        status_code=exc.status_code,
        message=str(exc.detail),
        error="HTTP_ERROR",
        path=str(request.url.path),
    )


async def general_exception_handler(request: Request, exc: Exception):
    return build_response(
        status_code=500,
        message="Đã xảy ra lỗi hệ thống, vui lòng thử lại sau",
        error="INTERNAL_SERVER_ERROR",
        path=str(request.url.path),
    )
