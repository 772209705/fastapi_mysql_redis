from fastapi import Request
from fastapi.responses import ORJSONResponse


from starlette import status
from common.logger import log


# 权限拦截处理器
async def authorization_interceptor_handler(request: Request, call_next):
    # 这里可以写一些请求前的逻辑，例如记录日志等
    headers = request.headers
    # 后续完善鉴权token
    token = headers.get("token")
    # if token == redis_token:
    response = await call_next(request)
    # 这里可以写一些请求后的逻辑，例如记录日志等
    return response


# 异常拦截器
async def http_exception_handler(request, exc):
    return ORJSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )


# 异常拦截器
async def exception_handler(request, exc):
    # 这里可以处理一些未知异常
    log.error(exc.detail)
    return ORJSONResponse(
        status_code=status.HTTP_511_NETWORK_AUTHENTICATION_REQUIRED,
        content={
            'code': 500,
            'message': "服务器内部错误",
            'data': exc.detail,
        }
    )

