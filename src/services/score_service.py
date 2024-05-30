from schemas.score_schemas import ScoreCreateUpdate
from utils.repository import AbstractRepository


class ScoreServices:
    def __init__(self, scores_repo: AbstractRepository):
        self.scores_repo = scores_repo()

    async def add_score(self, score: ScoreCreateUpdate):
        score_dict = score.model_dump()
        score_id = await self.scores_repo.create(score_dict)

        return score_id

    async def detail_score(self, score_id: int):
        return await self.scores_repo.detail(score_id)

    async def update_score(self, score_id: int, score: ScoreCreateUpdate):
        return await self.scores_repo.update(score_id, score)

    async def delete_score(self, score_id: int):
        return await self.scores_repo.delete(score_id)
