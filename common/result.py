from fastapi import status
from fastapi.responses import ORJSONResponse, Response
from typing import Union, Dict, Any, List

from sqlalchemy.engine import LegacyRow


def success(*, data: Union[list, dict, str, LegacyRow], ) -> Response:
    data = type_conversion(data)
    return ORJSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'code': 200,
            'message': "success",
            'data': data,
        }
    )


def ok(*, message: str, data: Union[list, dict, str, LegacyRow]) -> Response:
    data = type_conversion(data)
    return ORJSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'code': 200,
            'message': message,
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


def error_enum(enum):
    return ORJSONResponse(
        status_code=enum.code,
        content={
            "code": enum.code,
            "message": enum.message,
            "data": ""
        }
    )


# 数据类型转换
def type_conversion(data: Union[list, dict, str, LegacyRow]) -> Union[
    Dict[Union[str, Any], Union[Dict[Union[str, Any], Any], Any]], dict, List[Dict[Any, Any]], str]:
    # 判断 数据库 类型 list
    if isinstance(data, list):
        data = [dict(row) for row in data]

    # 转换dict类型中有LegacyRow类型的数据为可输出的数据类型
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, LegacyRow):
                time = data[key].create_time.strftime("%Y-%m-%d %H:%M:%S")
                json_data = dict(value.items())
                json_data["create_time"] = time
                data[key] = json_data
                break

    # 转LegacyRow类型为可输出的数据类型
    if isinstance(data, LegacyRow):
        data = dict(data.items())
        time = data["create_time"].strftime("%Y-%m-%d %H:%M:%S")
        data["create_time"] = time

    return data
