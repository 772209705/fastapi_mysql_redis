# 项目 fastapi 后端
```
python `3.8.9` 

```
![Python Version](https://img.shields.io/badge/Python-3.8.9-blue.svg)
# uvicorn main:app --host=127.0.0.1 --port=8005 --reload

## 项目架构
```
├── api                               #包含各种API的模块，例如索引、上传、用户、WebSocket等。
│   ├── __init__.py
│   ├── index                         # API接口-首页
│   │   ├── __init__.py
│   │   └── product.py                # API接口-商品
│   ├── upload                        # API接口-上传
│   │   ├── __init__.py
│   │   └── upload_os.py              # API接口-上传操作系统
│   ├── user                          # API接口-用户
│   │   ├── __init__.py
│   │   ├── login.py                  # API接口-用户登录
│   │   └── user.py                   # API接口-用户信息
│   └── websocket                     # API接口-WebSocket
│       ├── __init__.py
│       └── websocket.py              # API接口-WebSocket实现
├── common
│   ├── logger.py                     # 日志模块
│   ├── result.py                     # 接口统一返回响应模块
│   └── __init__.py
├── db_sql                            # 编写SQL模块
│   ├── index_sql.py                  # 数据库SQL-首页
│   ├── user.py                       # 数据库SQL-用户
│   └── __init__.py
├── handlers                          #包含各种处理程序的模块，例如授权拦截器等
│   ├── authorization_interceptor.py  # 接口拦截器-授权-异常拦截
│   └── __init__.py
├── models
│   ├── login_model.py                # 模型-用户登录
│   ├── product_model.py              # 模型-产品
│   └── __init__.py
├── mydbs                             # 包含Mysql、redis数据库连接和操作的模块，例如数据库连接、数据库方法等。
│   ├── database.py                   # 数据库连接模块
│   ├── db_method.py                  # 数据库操作方法
│   └── __init__.py
├── routers
│   ├── router.py                     # 路由处理程序模块
│   └── __init__.py
└── utils                             # 包含各种工具函数的模块。
    ├── tools.py                      # 工具模块
    └── __init__.py
├── app.log                           # 应用程序日志文件
├── config.py                         # 整个项目配置入口
├── main.py                           # 应用程序主入口文件
├── main.py.backups
├── README.md                         # 应用程序的说明文档
├── test_main.http                    # 测试模块

```
