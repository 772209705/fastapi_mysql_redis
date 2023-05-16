from fastapi import Request
from fastapi.responses import ORJSONResponse

from starlette import status
from common.logger import log
from handlers.app_confi_guration import excluded_routes


# 自定义权限拦截处理器
async def authorization_interceptor_handler(request: Request, call_next):
    if request.url.path in excluded_routes:
        response = await call_next(request)
    else:
        # 后续完善鉴权token
        headers = request.headers
        token = headers.get("token")
        # if token == redis_token:
        response = await call_next(request)
        # 请求后的逻辑，例如记录日志等
    return response


# 自定义异常拦截器
async def http_exception_handler(request, exc):
    return ORJSONResponse(
        status_code=exc.status_code,
        content={"message": str(exc)},
    )


# 自定义未知异常拦截器
async def exception_handler(request, exc):
    log.error(exc)
    return ORJSONResponse(
        status_code=status.HTTP_511_NETWORK_AUTHENTICATION_REQUIRED,
        content={
            'code': 500,
            'message': "服务器内部错误",
            'data': str(exc)
        }
    )
