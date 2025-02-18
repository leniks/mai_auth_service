from fastapi import APIRouter, HTTPException, status, Response, Depends

from app.schemas import User_schema
from app.services.users_service import UsersService
from app.schemas.User_schema import User, RegisterUser, AuthUser
from app.services.auth_service import get_password_hash, authenticate_user_by_username, create_access_token, \
    get_current_user
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

@router.post("/login/")
async def auth_user(response: Response, user_data: AuthUser):
    check = await authenticate_user_by_username(username=user_data.username, password=user_data.password)

    if check is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Неверная почта или пароль')

    access_token = create_access_token({"sub": str(check.id)})
    response.set_cookie(key="users_access_token", value=access_token, httponly=False)
    return {'access_token': access_token}

@router.get("/me/")
async def get_me(user_data: User = Depends(get_current_user)) -> User:
    return user_data

@router.post("/logout/")
async def logout_user(response: Response):
    response.delete_cookie(key="users_access_token")
    return {'message': 'Пользователь успешно вышел из системы'}