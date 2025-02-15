from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

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
    async def get_user_by_id(cls, id):
        async with async_session_maker() as session:
            query = select(User).filter_by(id=id)
            result = await session.execute(query)
            users = result.scalars().one_or_none()
            return users

    @classmethod
    async def add_user(cls, **values):
        async with async_session_maker() as session:
            async with session.begin():
                new_instance = User(**values)
                session.add(new_instance)
                try:
                    await session.commit()

                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e
                return new_instance
