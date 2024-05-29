from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from db.db_connection import get_async_session
from db.models import Students
from schemas.student_schemas import StudentCreate, StudentUpdate
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()


@router.post("/create")
async def create_student(student: StudentCreate, db: AsyncSession = Depends(get_async_session)):
    async with db as session:
        stm = insert(Students).values(student.model_dump()).returning(Students.id)
        result = await session.execute(stm)
        await session.commit()

        return result.scalar_one()


@router.get("/detail/{student_id}")
async def detail_student(student_id: int, db: AsyncSession = Depends(get_async_session)):
    async with db as session:
        result = await session.execute(select(Students).filter(Students.id == student_id))
        db_student = result.scalar_one()

        return db_student


@router.patch("/update/{student_id}")
async def update_student(student_id: int, student: StudentUpdate, db: AsyncSession = Depends(get_async_session)):
    async with db as session:
        db_student = await session.get(Students, student_id)
        if db_student is None:
            raise HTTPException(status_code=404, detail="Student not found")

        for attr, value in student.dict().items():
            setattr(db_student, attr, value)

        await session.commit()

        return db_student


@router.delete("/delete/{student_id}")
async def delete_student(student_id: int, db: AsyncSession = Depends(get_async_session)):
    async with db as session:
        db_student = await session.get(Students, student_id)
        if db_student is None:
            raise HTTPException(status_code=404, detail="Student not found")

        await session.delete(db_student)
        await session.commit()

        return db_student
