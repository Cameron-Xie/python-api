from fastapi import APIRouter

router = APIRouter()


@router.get("/{username}")
async def greeting(username: str):
    return {"username": username}
