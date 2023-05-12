import importlib
import os
import pkgutil
from fastapi import APIRouter

router = APIRouter()

# 自动装载 api 文件夹下的所有路由器
dirs = [f for f in os.listdir("api") if os.path.isdir(os.path.join("api", f))]
dirs = [d for d in dirs if d != '__pycache__']
print(dirs)
for dir_name in dirs:
    for (module_loader, name, ispkg) in pkgutil.iter_modules(["api/"+dir_name]):
        if not ispkg:
            # 导入 api 文件夹下的路由器模块
            module = importlib.import_module(f"api.{dir_name}.{name}")
            # 将路由器挂载到主路由器下，路由前缀使用文件名
            router.include_router(module.router, prefix="", tags=[name])