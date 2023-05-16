from sqlalchemy.pool import QueuePool
from sqlalchemy import create_engine
from config import Config

engine = None


def init_db_engine():
    global engine
    if engine is None:
        engine = create_engine(
            "mysql+pymysql://{}:{}@{}:{}/{}".format(Config.username, Config.password, Config.host, Config.port, Config.db_name),
            poolclass=QueuePool,
            pool_size=10,
            max_overflow=100,
            pool_timeout=30
        )


class Connection:
    def __init__(self):
        self.conn = None

    def __enter__(self):
        self.conn = engine.connect()
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
