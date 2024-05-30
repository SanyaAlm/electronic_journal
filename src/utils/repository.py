from abc import ABC, abstractmethod
from typing import Union

from fastapi import HTTPException
from sqlalchemy import insert, select

from db.db_connection import async_session_maker


class AbstractRepository(ABC):
    @abstractmethod
    async def create(self, data):
        pass

    @abstractmethod
    async def detail(self, id_):
        pass

    @abstractmethod
    async def update(self, id_: int, data: dict):
        pass

    @abstractmethod
    async def delete(self, id_: int):
        pass


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def create(self, data: dict):
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            result = await session.execute(stmt)
            await session.commit()

            return result.scalar_one()

    async def detail(self, id_: int):
        async with async_session_maker() as session:
            result = await session.execute(select(self.model).filter(self.model.id == id_))

            db_student = result.scalar_one_or_none()
            if db_student is None:
                raise HTTPException(status_code=404, detail="Not found!")

            return db_student

    async def update(self, id_: int, data: Union[dict]):
        async with async_session_maker() as session:
            result = await session.get(self.model, id_)
            if result is None:
                raise HTTPException(status_code=404, detail="Not found!")

            for attr, value in data.dict().items():
                setattr(result, attr, value)
            await session.commit()

            return result

    async def delete(self, id_: int):
        async with async_session_maker() as session:
            result = await session.get(self.model, id_)
            if result is None:
                raise HTTPException(status_code=404, detail="Not found!")

            await session.delete(result)
            await session.commit()

            return result
