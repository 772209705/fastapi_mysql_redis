from fastapi import status
from fastapi.responses import ORJSONResponse, Response
from typing import Union


def success(*, data: Union[list, dict, str]) -> Response:
    # 判断 数据库 类型 list
    if isinstance(data, list):
        data = [dict(row) for row in data]
    return ORJSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'code': 200,
            'message': "success",
            'data': data,
        }
    )


def error(*, message: str = "fail") -> Response:
    return ORJSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            'code': 400,
            'message': message,
        }
    )


def error_500(*, message: str = "BAD REQUEST", data: str = None) -> Response:
    return ORJSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            'code': 500,
            'message': message,
            'data': data,
        }
    )
