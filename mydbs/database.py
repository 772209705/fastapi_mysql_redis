from sqlalchemy.pool import QueuePool
from sqlalchemy import create_engine
from urllib3.exceptions import EmptyPoolError

from common.logger import log
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
            pool_timeout=10,
            pool_recycle=3600,
            pool_pre_ping=True
        )


class ConnectionPool:
    def __init__(self):
        self.conn = None

    def __enter__(self):
        try:
            self.conn = engine.connect()
        except EmptyPoolError:
            log.error("失败，测试数据库连接")
            init_db_engine()
            self.conn = engine.connect()
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
