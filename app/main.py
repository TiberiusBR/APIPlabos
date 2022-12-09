from fastapi import FastAPI
import uvicorn
from utils.settings import settings
# from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware

from routes.category_router import category_router
from routes.video_router import video_router
from routes.course_router import course_router
from routes.auth_router import auth_router
from routes.registry_router import registry_router
from routes.review_router import review_router
from routes.lesson_router import lesson_router
from routes.user_router import user_router
from models import models
from database.conn import engine

models.Base.metadata.create_all(bind=engine)

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(category_router)
app.include_router(video_router)
app.include_router(course_router)
app.include_router(auth_router)
app.include_router(registry_router)
app.include_router(review_router)
app.include_router(lesson_router)
app.include_router(user_router)


@app.get("/")
async def health():
    return {"Application": "Running"}

uvi_host = settings.UVICORN_HOST
api_port = settings.API_PORT

if __name__ == "__main__":
    if uvi_host != 'None':
        uvicorn.run("main:app", host=uvi_host, port=api_port)
    else:
        uvicorn.run("main:app", port=api_port)
