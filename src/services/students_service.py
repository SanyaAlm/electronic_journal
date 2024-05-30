from schemas.student_schemas import StudentCreate, StudentUpdate
from utils.repository import AbstractRepository


class StudentsService:
    def __init__(self, students_repo: AbstractRepository):
        self.students_repo: AbstractRepository = students_repo()

    async def add_student(self, student: StudentCreate):
        students_dict = student.model_dump()
        student_id = await self.students_repo.create(students_dict)
        return student_id

    async def detail_student(self, student_id: int):
        return await self.students_repo.detail(student_id)

    async def update_student(self, student_id: int, student: StudentUpdate):
        return await self.students_repo.update(student_id, student)

    async def delete_student(self, student_id: int):
        return await self.students_repo.delete(student_id)
