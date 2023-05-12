from fastapi import File, UploadFile, APIRouter
import os

from starlette.responses import FileResponse

router = APIRouter()


@router.post("/upload-file")
async def create_upload_file(file: UploadFile = File(...)):
    """
    上传文件并保存到项目根目录
    """
    saved_location = os.path.join(os.getcwd(), "../../file", file.filename)
    with open(saved_location, "wb") as buffer:
        buffer.write(await file.read())
    print("文件已保存到：", saved_location)
    return {"filename": file.filename}


@router.get("/downloadfile/{file_path:path}")
async def download_file(file_path: str):
    """
    下载保存在项目根目录中的文件
    """
    file_location = os.path.join(os.getcwd(), "../../file", file_path)
    return FileResponse(file_location, media_type="application/octet-stream", filename=file_path)
