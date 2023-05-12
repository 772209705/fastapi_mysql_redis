from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from api.websocket.websocket import websocket_handler
from mydbs.database import init_db_engine
from routers.router import router as api_router
from handlers.authorization_interceptor import authorization_interceptor_handler, http_exception_handler, exception_handler


# 程序入口
app = FastAPI()

app.include_router(api_router)
app.add_websocket_route("/ws", websocket_handler)


# 初始化数据库连接池
init_db_engine()


# 注入请求拦截器
app.middleware("http")(authorization_interceptor_handler)

# 注入异常处理器
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, exception_handler)


# 配置跨域中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)