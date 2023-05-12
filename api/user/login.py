import json

import requests
from fastapi import APIRouter
from jsonpath import jsonpath


from models.login_model import LoginModel
from common.logger import log
from common import result

router = APIRouter()


@router.get("/info")
def get_user_info():
    log.info("测试文件名")
    log.info("Test log message")


@router.post("/login")
def login(loginModel: LoginModel):
    log.info(loginModel)
    getSessionParams = {
        "m": "api",
        "f": "getSessionID",
        "t": "json",
    }
    getSession = requests.get("https://pj.gdsre.cn/index.php", getSessionParams)
    data = json.loads(getSession.json()['data'])
    session = jsonpath(data, '$.sessionID')[0]
    params = {
        "m": "user",
        "f": "login",
        "t": "json",
        "account": loginModel.username,
        "password": loginModel.password,
        "zentaosid": session,
    }
    response = requests.get("https://pj.gdsre.cn/index.php", params)
    print(response.json()['status'])
    if response.json()['status'] == "success":
        str_data = json.dumps(response.json()['user'])
        data = json.loads(str_data)
        token = jsonpath(data, '$.token')[0]
        username = jsonpath(data, '$.realname')[0]
        log.info("token: "+token)
        return result.success(data={
            "token": token,
            "username": username
        })
    else:
        log.error(response.json())
        err_msg = str(response.json()['reason'])
        return result.error(message=err_msg)





