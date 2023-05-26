import redis
from urllib3.exceptions import EmptyPoolError

from common.logger import log
from config import Config

engine = None


def init_redis_engine():
    global engine
    if engine is None:
        engine = redis.ConnectionPool(
            host=Config.redis_host,
            port=Config.redis_port,
            db=Config.redis_db,
            password=Config.redis_password,
            max_connections=Config.max_connections,
            socket_keepalive=True,
            socket_timeout=60
        )


start_redis = redis.Redis(connection_pool=engine)


class RedisConnectionPool:
    def __init__(self):
        self.conn = None

    def __enter__(self):
        try:
            self.conn = start_redis
        except EmptyPoolError:
            log.error("redis连接失败,重新创建redis连接池")
            init_redis_engine()
            self.conn = start_redis
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
