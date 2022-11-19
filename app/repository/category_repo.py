from sqlalchemy.orm import Session
from models import models
from schemas import category


def get_all_categories(db: Session):
    return db.query(models.Category).all()


def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()


def get_category_by_name(db: Session, category_name: str):
    return (
        db.query(models.Category).filter(models.Category.name == category_name).first()
    )


def create_category(db: Session, category_schema: category.CategoryCreate):
    new_category = models.Category(name=category_schema.name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category
