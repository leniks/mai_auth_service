from fastapi import APIRouter, HTTPException, status
from app.services.users_service import UsersService
from app.schemas.User_schema import User, RegisterUser
from app.services.auth_service import get_password_hash
from typing import Optional, List


router = APIRouter(prefix='/users', tags=['Работа с пользователями'])

@router.get("/", summary="Получить всех пользователей")
async def get_all_users() -> Optional[List[User]]:
    result = await UsersService.get_all_users()
    return result

@router.get("/{id}", summary="Получиить пользователя по id")
async def get_user_by_id(id: int) -> Optional[User] | str:
    result = await UsersService.get_user_by_id(id)
    if result is None:
        return f'Пользователь с id {id} не найден'
    return result

@router.post("/register", summary="Добавить пользователя")
async def add_user(user_add: RegisterUser)  -> dict:
    user = await UsersService.get_user_by_username(username=user_add.username)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Пользователь уже существует'
        )

    user_dict = user_add.model_dump()
    user_dict['password'] = get_password_hash(user_add.password)
    await UsersService.add_user(**user_dict)
    return {'message': 'Вы успешно зарегистрированы!'}
