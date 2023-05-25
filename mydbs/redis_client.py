import redis
from queue import Queue, Empty
from threading import Lock
from contextlib import contextmanager
from config import Config


class RedisConnectionPool:
    def __init__(self):
        self.host = Config.redis_host
        self.port = Config.redis_port
        self.db = Config.redis_db
        self.password = Config.redis_password
        self.max_connections = Config.max_connections
        self.socket_keepalive = True

        self.pool = Queue(maxsize=Config.max_connections)
        self.lock = Lock()

        for _ in range(Config.max_connections):
            self.create_connection()

    def create_connection(self):
        _connection = redis.Redis(
            host=self.host,
            port=self.port,
            db=self.db,
            password=self.password,
            socket_keepalive=self.socket_keepalive
        )
        self.pool.put(_connection)

    @contextmanager
    def get_connection(self):
        try:
            _connection = self.pool.get(block=False)
        except Empty:
            with self.lock:
                if self.pool.qsize() < self.max_connections:
                    self.create_connection()
            _connection = self.pool.get()

        try:
            yield _connection
        finally:
            self.pool.put(_connection)

