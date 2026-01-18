from app.database import async_session_maker

from sqlalchemy import select


class BaseDAO:
    model = None

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).where(cls.model.id == model_id)
            result = await session.execute(query)
            return result.scalar_one()

    @classmethod
    async def find_one_or_none(cls, **filter):
        async with async_session_maker() as session:
            query = select(cls.model).filter(**filter)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_all(cls, **filter):
        async with async_session_maker() as session:
            query = select(cls.model).filter(**filter) 
            result = await session.execute(query)
            return result.fetchall()