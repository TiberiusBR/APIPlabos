from app.schemas.lesson import LessonBase
from app.models import models
from sqlalchemy.orm import Session
from typing import List


def create_lesson(db: Session, lesson: LessonBase):
    new_lesson = models.Lesson(**lesson.dict())
    db.add(new_lesson)
    db.commit()
    db.refresh(new_lesson)
    return new_lesson