from fastapi import APIRouter
from app.services.users_service import UsersService
from app.schemas.User_schema import User
from typing import Optional, List

router = APIRouter(prefix='/users', tags=['Работа с пользователями'])

@router.get("/", summary="Получить всех пользователей")
async def get_all_users() -> Optional[List[User]]:
    result = await UsersService.get_all_users()
    return result

@router.get("/{id}", summary="Получиить пользователя по id")
async def get_user_by_id(id: int) -> Optional[User]:
    data = {'id': id}
    result = await UsersService.get_user_by_id(**data)
    return result