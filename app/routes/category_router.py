from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.schemas import category as category_models
from app.repository import category_repo as repo
from app.database.conn import get_db

category_router = APIRouter(prefix="/category")


@category_router.get("/", response_model=list[category_models.Category])
def read_categories(db: Session = Depends(get_db)):
    categories = repo.get_all_categories(db)
    return categories


@category_router.post("/", response_model=category_models.Category, status_code=status.HTTP_201_CREATED)
def create_category(category: category_models.CategoryCreate, db: Session = Depends(get_db)):
    created_categories = repo.create_category(db, category)
    return created_categories
