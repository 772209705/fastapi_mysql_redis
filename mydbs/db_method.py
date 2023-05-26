from common.logger import log
from mydbs.database import ConnectionPool, init_db_engine

init_db_engine()
log.warn("创建数据库连接池")

Connection = ConnectionPool()


def query_sql(_sql: str):
    log.debug_sql(_sql)
    with Connection as conn:
        result = conn.execute(_sql).fetchall()
        return result


def save_sql(_sql: str):
    log.debug_sql(_sql)
    with Connection as conn:
        result = conn.execute(_sql).lastrowid
        return result


def update_sql(_sql: str):
    log.debug_sql(_sql)
    with Connection as conn:
        result = conn.execute(_sql).lastrowid
        return result


def delete_sql(_sql: str):
    log.debug_sql(_sql)
    with Connection as conn:
        result = conn.execute(_sql).rowcount
        return result
