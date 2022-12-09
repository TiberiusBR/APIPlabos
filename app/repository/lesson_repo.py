from sqlalchemy.orm import Session
from models import models
from schemas.lesson import Lesson

def get_lessons(db: Session):
    return db.query(models.Lesson).all()

def get_lessons_by_course_id(db: Session, course_id: int):
    return db.query(models.Lesson).filter(models.Lesson.course_id == course_id).all()