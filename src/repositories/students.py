from db.models import Students
from utils.repository import SQLAlchemyRepository


class StudentsRepository(SQLAlchemyRepository):
    model = Students

