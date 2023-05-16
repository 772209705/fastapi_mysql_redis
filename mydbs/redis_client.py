import redis

from config import Config

redis_pool = redis.ConnectionPool(
    host=Config.redis_host,
    port=Config.redis_port,
    db=Config.redis_db,
    password='',
    max_connections=Config.max_connections,
    socket_keepalive=True,
    socket_timeout=60
)


class RedisPool:

    def __enter__(self):
        self.redis_conn = redis.StrictRedis(connection_pool=redis_pool)
        return self.redis_conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.redis_conn.close()
