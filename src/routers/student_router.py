from typing import Annotated

from routers.dependencies import students_service
from schemas.student_schemas import StudentCreate, StudentUpdate
from fastapi import APIRouter, Depends
from services.students_service import StudentsService

router = APIRouter()


@router.post("/create")
async def create_student(student: StudentCreate,
                         student_service: Annotated[StudentsService, Depends(students_service)]
                         ):
    student_id = await student_service.add_student(student)

    return student_id


@router.get("/detail/{student_id}")
async def detail_student(student_id: int,
                         student_service: Annotated[StudentsService, Depends(students_service)]
                         ):
    student = await student_service.detail_student(student_id)

    return student


@router.patch("/update/{student_id}")
async def update_student(student_id: int,
                         student: StudentUpdate,
                         student_service: Annotated[StudentsService, Depends(students_service)]
                         ):
    result = await student_service.update_student(student_id, student)

    return result


@router.delete("/delete/{student_id}")
async def delete_student(student_id: int,
                         student_service: Annotated[StudentsService, Depends(students_service)]
                         ):
    student = await student_service.delete_student(student_id)

    return student
