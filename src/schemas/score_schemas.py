from pydantic import BaseModel, Field


class ScoreBase(BaseModel):
    grade: int = Field(ge=1, le=10)


class ScoreCreateUpdate(ScoreBase):
    student_id: int
