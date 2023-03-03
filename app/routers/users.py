from fastapi import APIRouter
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate

router = APIRouter()

@router.get("/users")
async def get_users():
    ...
