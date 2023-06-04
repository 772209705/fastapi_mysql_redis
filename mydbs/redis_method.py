from common.logger import log
from config import Config
from mydbs.redis_client import RedisConnectionPool, init_redis_engine

init_redis_engine()
log.warn("创建Redis连接池")

redis_pool = RedisConnectionPool()


def redis():
    with redis_pool as connection:
        return connection


def redis_set(key, value, expire=None):
    with redis_pool as connection:
        conn_set = connection.set(key, value, ex=expire)
        return conn_set


def redis_get(key):
    with redis_pool as connection:
        conn_set = connection.get(key)
        return conn_set


def redis_set_token(key, value):
    with redis_pool as connection:
        conn_set_token = connection.set(key, value, ex=Config.token_expire_seconds)
        return conn_set_token
