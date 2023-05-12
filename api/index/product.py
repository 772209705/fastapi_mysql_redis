from fastapi import APIRouter

from common.logger import log
from db_sql.index_sql import update_product_db, save_new_product_db, query_product_list, delete_product_db
from models.product_model import ProductModel

router = APIRouter()


@router.get('/get/product/list')
async def get_users():
    product = query_product_list()
    log.info("获取列表数据：" + str(product))
    return product


@router.post("/save/new/product")
async def save_product(productMethod: ProductModel):
    print(productMethod)
    new_product = save_new_product_db(productMethod)
    return new_product


@router.post("/update/product")
async def update_product(productMethod: ProductModel):
    new_product = update_product_db(productMethod)
    return new_product


@router.delete("/delete/product")
async def delete_product(product_id: int):
    new_product = delete_product_db(product_id)
    return new_product
