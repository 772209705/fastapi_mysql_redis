from common.logger import log
from mydbs.database import ConnectionPool

# 创建连接池实例
connection_pool = ConnectionPool()
log.warn("创建连接池成功")


def query_sql(_sql: str):
    log.debug_sql(_sql)
    with connection_pool.get_connection() as conn:
        result = conn.execute(_sql).fetchall()
        return result


def save_sql(_sql: str):
    log.debug_sql(_sql)
    with connection_pool.get_connection() as conn:
        result = conn.execute(_sql).lastrowid
        return result


def update_sql(_sql: str):
    log.debug_sql(_sql)
    with connection_pool.get_connection() as conn:
        result = conn.execute(_sql).lastrowid
        return result


def delete_sql(_sql: str):
    log.debug_sql(_sql)
    with connection_pool.get_connection() as conn:
        result = conn.execute(_sql).rowcount
        return result
