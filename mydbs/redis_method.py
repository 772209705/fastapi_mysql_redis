from common.logger import log
from mydbs.redis_client import RedisConnectionPool


# 创建 Redis 连接池实例
log.warn("创建Redis连接池")
redis_pool = RedisConnectionPool()


def redis():
    with redis_pool.get_connection() as connection:
        return connection


def redis_set(key, value):
    with redis_pool.get_connection() as connection:
        conn_set = connection.set(key, value)
        return conn_set