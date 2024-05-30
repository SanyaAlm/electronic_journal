from typing import Annotated
from fastapi import APIRouter, Depends
from schemas.score_schemas import ScoreCreateUpdate
from services.score_service import ScoreServices
from routers.dependencies import scores_service

router = APIRouter()


@router.post("/create")
async def score_create(score: ScoreCreateUpdate,
                       score_service: Annotated[ScoreServices, Depends(scores_service)]
                       ):
    score_id = await score_service.add_score(score)

    return score_id


@router.get("/detail/{score_id}")
async def score_detail(score_id: int,
                       score_service: Annotated[ScoreServices, Depends(scores_service)]
                       ):
    score = await score_service.detail_score(score_id)

    return score


@router.patch("/update/{score_id}")
async def score_update(score_id: int,
                       score: ScoreCreateUpdate,
                       score_service: Annotated[ScoreServices, Depends(scores_service)]
                       ):
    result = await score_service.update_score(score_id, score)

    return result


@router.delete("/delete/{score_id}")
async def score_delete(score_id: int,
                       score_service: Annotated[ScoreServices, Depends(scores_service)]
                       ):
    result = await score_service.delete_score(score_id)

    return result
