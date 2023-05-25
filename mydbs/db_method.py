from common.logger import log
from mydbs.database import ConnectionPool

# 创建连接池实例
log.warn("创建连接池成功")
connection_pool = ConnectionPool()


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
