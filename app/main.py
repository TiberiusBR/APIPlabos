from fastapi import FastAPI
import uvicorn
from app.config.conn import metadata, engine, database
from app.routes.categoryRoutes import category_router

metadata.create_all(engine)


app = FastAPI()
app.include_router(category_router)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
async def health():
    return {"Application": "Running"}


#DEBUG

if __name__ == "__main__":
    uvicorn.run(app)
