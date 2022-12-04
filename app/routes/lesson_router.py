from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import lesson as lesson_models
from repository import lesson_repo as repo
from database.conn import get_db

lesson_router = APIRouter(prefix="/lesson")

@lesson_router.get("/",response_model=list[lesson_models.Lesson])
def get_lessons(db: Session = Depends(get_db)):
    lessons = repo.get_lessons(db)
    if lessons is None:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT, detail="No lessons found."
        )
    return lessons

@lesson_router.get("/course/{course_id}",response_model=list[lesson_models.Lesson])
def get_lessons_by_course_id(course_id: int, db: Session = Depends(get_db)):
    lessons = repo.get_lessons_by_course_id(db,course_id)
    if lessons is None:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT, detail="No lessons found."
        )
    return lessons