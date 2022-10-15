from fastapi import FastAPI
import uvicorn
from fastapi.security import OAuth2PasswordBearer
from app.config.conn import metadata, engine, database
from app.routes.categoryRoutes import category_router
from app.routes.videoRoutes import video_router

metadata.create_all(engine)


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
app.include_router(category_router)
app.include_router(video_router)


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
