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


#
# @category_router.get("/{category_id}", response_model=category_models.Category)
# async def read_category(category_id: int):
#     query = category_schema.select().where(category_schema.c.id == category_id)
#     return await database.fetch_one(query)
#
#
@category_router.post("/", response_model=category_models.Category, status_code=status.HTTP_201_CREATED)
def create_category(category: category_models.CategoryCreate, db: Session = Depends(get_db)):
    created_categories = repo.create_user(db, category)
    return created_categories
#
#
# @category_router.put("/", status_code=status.HTTP_202_ACCEPTED)
# async def update_category(category: category_models.Category):
#     query = category_schema.update().where(category_schema.c.id == category.id).values(name=category.name)
#     await database.execute(query)
#     return {"Message": "Category successfully updated."}
#
#
# @category_router.delete("/{category_id}", status_code=status.HTTP_202_ACCEPTED)
# async def delete_category(category_id: int):
#     query = category_schema.delete().where(category_schema.c.id == category_id)
#     await database.execute(query)
#     return {"Message": "Category successfully deleted."}
