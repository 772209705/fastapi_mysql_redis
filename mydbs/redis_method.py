from common.logger import log
from mydbs.redis_client import RedisConnectionPool, init_redis_engine

init_redis_engine()
log.warn("创建Redis连接池")

redis_pool = RedisConnectionPool()


def redis():
    with redis_pool as connection:
        return connection


def redis_set(key, value):
    with redis_pool as connection:
        conn_set = connection.set(key, value)
        return conn_set
