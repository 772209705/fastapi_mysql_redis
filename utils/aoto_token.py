import jwt
import secrets
from datetime import datetime

# token管理器
token_manage = dict()


class AutoToken:
    def __init__(self, secret_key=None, expiration_minutes=30):
        if secret_key is None:
            self.secret_key = secrets.token_urlsafe(32)
        else:
            self.secret_key = secret_key
        self.expiration_minutes = expiration_minutes

    def auto_generate_token(self, data: str) -> str:
        # 设置token过期时间
        expiration = int(datetime.now().timestamp()) + self.expiration_minutes

        # 构造payload
        payload = {
            'unique': data,
            'exp': expiration
        }
        # 生成token
        if data not in token_manage:
            token = jwt.encode(payload, self.secret_key)
            token_manage[data] = token
        else:
            token = token_manage[data]
        return token

    def auto_token_get_user_data(self, token: str):
        print(token)
        try:
            # 解码token
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])

            # 提取存储数据
            data = payload['unique']
            return data
        except jwt.InvalidTokenError:
            # 处理无效的token
            return "token已过期"
