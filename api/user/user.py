from fastapi import APIRouter

from mydbs.db_method import delete_sql

router = APIRouter()


@router.get('/get/product/list')
async def get_users():
    product = delete_sql("DELETE FROM product WHERE id = 2")

    return product