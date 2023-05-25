from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from queue import Queue, Empty
from threading import Lock
from contextlib import contextmanager
from config import Config


class ConnectionPool:
    def __init__(self, pool_size=10):
        self.pool_size = pool_size
        self.pool = Queue(maxsize=pool_size)
        self.lock = Lock()

        for _ in range(pool_size):
            self.create_connection()

    def create_connection(self):
        engine = create_engine(
            f"mysql+pymysql://{Config.username}:{Config.password}@{Config.host}:{Config.port}/{Config.db_name}"
        )
        Session = sessionmaker(bind=engine)
        _session = Session()
        self.pool.put(_session)

    @contextmanager
    def get_connection(self):
        try:
            _session = self.pool.get(block=False)
        except Empty:
            with self.lock:
                if self.pool.qsize() < self.pool_size:
                    self.create_connection()
            _session = self.pool.get()

        try:
            yield _session
        finally:
            self.pool.put(_session)
