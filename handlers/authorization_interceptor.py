from fastapi import Request
from fastapi.responses import ORJSONResponse

from starlette import status

from common import result
from common.error_enum import ErrorEnum
from common.logger import log
from handlers.app_confi_guration import excluded_routes
from mydbs.redis_method import redis_get


# 自定义权限拦截处理器
async def authorization_interceptor_handler(request: Request, call_next):
    # 记录请求
    if request.query_params:
        data = dict(request.query_params)
    else:
        data = await request.json()
    log.info("IP: {}, 参数: {}, method: {}, url: {}".format(request.client.host, data, request.method, request.url))

    # 排除掉不需要拦截的路由
    if request.url.path in excluded_routes:
        response = await call_next(request)
    else:
        # 鉴权token
        headers = request.headers
        token = headers.get("token")
        if not token:
            return result.error_enum(ErrorEnum.TOKEN_EMPTY)

        else:
            # 判断token是否正确
            token_value = redis_get(token)
            if token_value is None:
                return result.error_enum(ErrorEnum.TOKEN_ERROR)

            response = await call_next(request)

    return response


# 自定义异常拦截器
async def http_exception_handler(request, exc):
    return ORJSONResponse(
        status_code=exc.status_code,
        content={
            "message": "{}".format(exc)
        },
    )


# 自定义未知异常拦截器
async def exception_handler(request, exc):
    log.error(str(exc))
    return ORJSONResponse(
        status_code=status.HTTP_511_NETWORK_AUTHENTICATION_REQUIRED,
        content={
            'code': 500,
            'message': "服务器内部错误",
            'data': "{}".format(exc)
        }
    )
