from fastapi import FastAPI
import uvicorn
from app.routes.category_routes import category_router
from app.routes.video_routes import video_router
from app.routes.course_routes import course_router
from app.models import models
from app.config.conn import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(category_router)
app.include_router(video_router)
app.include_router(course_router)

@app.get("/")
async def health():
    return {"Application": "Running"}


# DEBUG

if __name__ == "__main__":
    uvicorn.run(app)
