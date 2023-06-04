from enum import Enum


class ErrorEnum(Enum):
    TOKEN_ERROR = (401, "您的登录状态已过期")
    TOKEN_EMPTY = (402, "查看token是否为空")
    ACCESS_DENIED = (1002, "访问被拒绝")

    def __init__(self, code, message):
        self._code = code
        self._message = message

    @property
    def code(self):
        return self._code

    @property
    def message(self):
        return self._message
