class Config:
    # fastapi服务
    fastapi_port = "8005"

    # websocket服务
    websocket = "/ws"

    # MySQL 配置信息
    username = "root"
    password = "123456"
    host = "172.16.0.67"
    port = "3306"
    db_name = "qc"
    pool_size = 50

    # redis 配置
    redis_host = "127.0.0.1"
    redis_port = 6379
    redis_db = 0
    redis_password = ""
    max_connections = 100