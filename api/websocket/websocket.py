import asyncio
import random

from fastapi import WebSocket, WebSocketDisconnect, APIRouter

router = APIRouter()

# 通过id保存websocket对象
websocket_buffer_byId = dict()
# 通过websocket保存ID
websocket_buffer_byWs = dict()


# 定义 WebSocket 的路由和处理函数
@router.websocket("/")
async def websocket_handler(websocket: WebSocket):
    await websocket_connect(websocket)
    await websocket_message(websocket)
    await websocket_disconnect(websocket)


# 连接 WebSocket
async def websocket_connect(websocket: WebSocket):
    await websocket.accept()
    random_num = random.randint(0, 10)
    print(random_num)
    websocket_buffer_byId[random_num] = websocket
    print(websocket_buffer_byId.get(random_num))
    websocket_buffer_byWs[websocket] = random_num
    print("WebSocket连接成功")


# 监听 WebSocket 消息
async def websocket_message(websocket: WebSocket):
    while True:
        try:
            data = await websocket.receive_text()
            print(f"接收到WebSocket消息：{data}")
            print(websocket_buffer_byId)
            for key, websocket_value in websocket_buffer_byId.items():
                if websocket_value != websocket:
                    await websocket_value.send_text(data)

        except WebSocketDisconnect:
            print("WebSocket连接已断开")
            break


# 关闭 WebSocket
async def websocket_disconnect(websocket: WebSocket):
    await asyncio.gather(
        websocket.close(),
        return_exceptions=True,  # 忽略可能出现的异常
    )
    del websocket_buffer_byWs[websocket]
    print(websocket_buffer_byWs)
    print("WebSocket连接已关闭")



