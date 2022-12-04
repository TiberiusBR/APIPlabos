from sqlalchemy.orm import Session
from models import models
from schemas.course import CourseBase


def get_all_courses(db: Session):
    return db.query(models.Course).all()


def get_course_by_id(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id).first()


def get_courses_by_title(db: Session, title: str):
    search = "%{}%".format(title)
    return db.query(models.Course).filter(models.Course.title.like(search)).all()


def get_courses_by_author_name(db: Session, author_name: str):
    search = "%{}%".format(author_name)
    query = (
        db.query(models.Course)
        .join(models.User)
        .filter(models.User.name.like(search))
        .all()
    )
    return query


def get_courses_by_author_id(db: Session, author_id: int):
    query = (
        db.query(models.Course)
        .join(models.User)
        .filter(models.User.id == author_id)
        .all()
    )
    return query


def get_course_by_category(db: Session, category_id: int):
    return (
        db.query(models.Course)
        .join(models.CategoryCourse)
        .filter(models.CategoryCourse.category_id == category_id)
        .all()
    )


def create_course(db: Session, course: CourseBase):
    new_course = models.Course(**course.dict())
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course


def get_courses_learning_by_user_id(db: Session, user_id: int):
    return (
        db.query(models.Course)
        .join(models.Registry)
        .filter(models.Registry.user_id == user_id)
        .all()
    )
