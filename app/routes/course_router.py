from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.repository import course_repo as repo
from app.schemas import course as course_models
from app.database.conn import get_db

course_router = APIRouter(prefix="/course")


@course_router.get("/", response_model=list[course_models.Course])
def get_courses(db: Session = Depends(get_db)):
    courses = repo.get_all_courses(db)
    return courses


@course_router.get("/{author_name}", response_model=list[course_models.Course])
def find_courses_by_author_name(author_name: str, db: Session = Depends(get_db)):
    courses = repo.get_course_by_author(db, author_name)
    return courses
