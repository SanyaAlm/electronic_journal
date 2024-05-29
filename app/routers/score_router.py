from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from db.db_connection import get_async_session
from db.models import Score
from schemas.score_schemas import ScoreCreate

router = APIRouter()


@router.post("/create")
async def score_create(score: ScoreCreate, db: AsyncSession = Depends(get_async_session)):
    async with db as session:
        stm = insert(Score).values(score.model_dump())
        result = await session.execute(stm)
        await session.commit()

        return result.scalars().first()


@router.get("/detail/{score_id}")
async def score_detail(score_id: int, db: AsyncSession = Depends(get_async_session)):
    async with db as session:
        result = await session.execute(select(Score).filter(Score.id == score_id))
        db_score = result.scalar_one()

        return db_score


@router.patch("/update/{score_id}")
async def score_update(score_id: int, score: ScoreCreate, db: AsyncSession = Depends(get_async_session)):
    async with db as session:
        db_score = await session.get(Score, score_id)
        if db_score is None:
            raise HTTPException(status_code=404, detail="Score not found")

        for attr, val in score.dict().items():
            setattr(db_score, attr, val)
        await session.commit()

        return db_score


@router.delete("/delete/{score_id}")
async def score_delete(score_id: int, db: AsyncSession = Depends(get_async_session)):
    async with db as session:
        db_score = await session.get(Score, score_id)
        if db_score is None:
            raise HTTPException(status_code=404, detail="Score not found")

        await session.delete(db_score)
        await session.commit()

        return db_score
