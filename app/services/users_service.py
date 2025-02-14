from sqlalchemy import select
from app.database import async_session_maker
from app.models.User import User

class UsersService:
    @classmethod
    async def get_all_users(cls):
        async with async_session_maker() as session:
            query = select(User)
            result = await session.execute(query)
            users = result.scalars().all()
            return users

    @classmethod
    async def get_user_by_id(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(User).filter_by(**filter_by)
            result = await session.execute(query)
            users = result.scalars().one_or_none()
            return users
