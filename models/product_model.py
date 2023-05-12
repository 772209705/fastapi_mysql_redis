from datetime import datetime

from pydantic import BaseModel


class ProductModel(BaseModel):
    id: int = ''
    images: str = ''
    title: str = ''
    url: str = ''
    env: str = ''
    sort_key: int = 1
    create_time: datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")