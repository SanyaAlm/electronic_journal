import fastapi
from app.routers import student_router, score_router

app = fastapi.FastAPI()

app.include_router(student_router.router, prefix='/students', tags=["Students"])
app.include_router(score_router.router, prefix='/scores', tags=["StudentsScores"])

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', port=1027, reload=True)
