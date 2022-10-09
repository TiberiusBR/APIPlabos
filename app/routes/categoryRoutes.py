from fastapi import APIRouter, status
from app.config.conn import database
from app.models import category as category_models
from app.schemas.schemas import category as category_schema

category_router = APIRouter(prefix="/category")


@category_router.get("/", response_model=list[category_models.Category])
async def read_categories():
    query = category_schema.select()
    return await database.fetch_all(query)


@category_router.get("/{category_id}", response_model=category_models.Category)
async def read_category(category_id: int):
    query = category_schema.select().where(category_schema.c.id == category_id)
    return await database.fetch_one(query)


@category_router.post("/", response_model=category_models.Category, status_code=status.HTTP_201_CREATED)
async def create_category(category: category_models.CategoryCreate):
    query = category_schema.insert().values(name=category.name)
    last_record_id = await database.execute(query)
    return {**category.dict(), "id": last_record_id}


@category_router.put("/", status_code=status.HTTP_202_ACCEPTED)
async def update_category(category: category_models.Category):
    query = category_schema.update().where(category_schema.c.id == category.id).values(name=category.name)
    await database.execute(query)
    return {"Message": "Category successfully updated."}


@category_router.delete("/{category_id}", status_code=status.HTTP_202_ACCEPTED)
async def delete_category(category_id: int):
    query = category_schema.delete().where(category_schema.c.id == category_id)
    await database.execute(query)
    return {"Message": "Category successfully deleted."}
