from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.repository import review_repo as repo
from app.schemas import review as review_schema
from app.database.conn import get_db

review_router = APIRouter(prefix="/review")


@review_router.get("/", response_model=list[review_schema.Review])
def get_reviews(db: Session = Depends(get_db)):
    reviews = repo.get_all_reviews(db)
    return reviews


@review_router.get("/course/{course_id}", response_model=list[review_schema.Review])
def get_reviews_by_course_id(course_id: int, db: Session = Depends(get_db)):
    reviews = repo.get_reviews_by_course_id(db, course_id)
    return reviews


@review_router.get("/user/{user_id}", response_model=list[review_schema.Review])
def get_reviews_by_user_id(user_id: int, db: Session = Depends(get_db)):
    reviews = repo.get_reviews_by_user_id(db, user_id)
    return reviews


@review_router.post("/create", response_model=review_schema.Review)
def create_review(review: review_schema.ReviewBase, db: Session = Depends(get_db)):
    created_review = repo.insert_review(db, review)
    return created_review
