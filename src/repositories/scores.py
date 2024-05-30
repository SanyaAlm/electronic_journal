from db.models import Score
from utils.repository import SQLAlchemyRepository


class ScoreRepository(SQLAlchemyRepository):
    model = Score
