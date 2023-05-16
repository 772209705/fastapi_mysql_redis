from fastapi import APIRouter

from mydbs.redis_method import redis

router = APIRouter()


@router.get('/list')
async def get_users():
    redis__set = redis().set("key", "ni you fun")

    print(redis__set)

    return {redis__set}


