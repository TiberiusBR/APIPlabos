from sqlalchemy.orm import Session
from models import models
from schemas.review import ReviewBase


def get_all_reviews(db: Session):
    return db.query(models.Review).all()


def get_reviews_by_course_id(db: Session, course_id: int):
    return db.query(models.Review).join(models.Course).filter(models.Course.id == course_id).all()


def get_reviews_by_user_id(db: Session, user_id: int):
    return db.query(models.Review).join(models.User).filter(models.User.id == user_id).all()


def insert_review(db: Session, review: ReviewBase):
    new_review = models.Review(**review.dict())
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review
