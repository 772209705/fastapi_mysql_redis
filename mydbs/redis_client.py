import redis

redis_pool = None


# 创建Redis连接池
def redis_client():
    global redis_pool
    redis_pool = redis.ConnectionPool(
        host='localhost',
        port=6379,
        db=0,
        password='',
        max_connections=100,
        socket_keepalive=True,
        socket_timeout=60
    )


class RedisPool:
    def __init__(self):
        self.redis_conn = None

    def __enter__(self):
        self.redis_conn = redis.StrictRedis(connection_pool=redis_pool)
        return self.redis_conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.redis_conn.close()


def save_redis(_sql: str):
    with RedisPool() as conn:
        conn.set("dsd-dsd-dcca-key22", "vldssdd")
        result = conn.get("key2")
        return result