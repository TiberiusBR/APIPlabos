from sqlalchemy.orm import Session
from app.models import models


def get_all_courses(db: Session):
    return db.query(models.Course).all()


def get_course_by_id(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id).first()


def get_course_by_title(db: Session, title: str):
    return db.query(models.Course).filter(models.Course.title == title).first()


def get_course_by_author(db: Session, author_name: str):
    return db.query(models.Course)\
        .filter(models.Course.users)\
        .filter(models.User.name == author_name).all()
