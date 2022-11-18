from fastapi import FastAPI
import uvicorn
from utils.settings import settings
# from fastapi.security import OAuth2PasswordBearer

from app.routes.category_router import category_router
from app.routes.video_router import video_router
from app.routes.course_router import course_router
from app.routes.auth_router import auth_router
from app.routes.registry_router import registry_router
from app.routes.review_router import review_router
from app.models import models
from app.database.conn import engine

models.Base.metadata.create_all(bind=engine)

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

app.include_router(category_router)
app.include_router(video_router)
app.include_router(course_router)
app.include_router(auth_router)
app.include_router(registry_router)
app.include_router(review_router)


@app.get("/")
async def health():
    return {"Application": "Running"}


# DEBUG

uvi_host = settings.UVICORN_HOST
if __name__ == "__main__":
    if uvi_host:
        uvicorn.run("app.main:app", host=uvi_host)
    else:
        uvicorn.run("app.main:app")
