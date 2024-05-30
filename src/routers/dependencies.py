from repositories.scores import ScoreRepository
from repositories.students import StudentsRepository
from services.score_service import ScoreServices
from services.students_service import StudentsService


def students_service():
    return StudentsService(StudentsRepository)


def scores_service():
    return ScoreServices(ScoreRepository)
