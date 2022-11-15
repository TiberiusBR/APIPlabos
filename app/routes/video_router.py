import os
import re

from fastapi import APIRouter, Request, status, File, UploadFile, Depends, Header
from fastapi.responses import Response

from app.helpers.video_helpers import generate_file_location
from app.repository import video_repo as repo
from sqlalchemy.orm import Session
from app.database.conn import get_db
from app.schemas.lesson import Lesson
from app.schemas.lesson import LessonBase
from app.middlewares.auth_middleware import get_current_user


video_router = APIRouter(prefix="/video")


@video_router.get("/{video_uuid}")
def play_video(video_uuid: str, request: Request, response: Response):
    header_range = request.headers.get("range")
    # TODO RETURN 400 if range header doesn't exist.
    file_path = os.path.join(os.path.abspath(os.getcwd()), "files", f"{video_uuid}.mp4")
    file_size = os.stat(file_path).st_size  # Size in bytes
    # Parse Range
    # Example "bytes=32324"

    chunk_size = pow(10, 6)  # 1mb ?
    start_range = int(
        re.sub(r",\D", "", header_range)
    )  # range comes in this pattern: 'bytes=0-'.
    # This regex removes the letters

    # Uses minimum value so range value doesn't extends file size.
    end_range = min(start_range + chunk_size, file_size - 1)

    with open(file_path, "rb") as myfile:
        myfile.seek(start_range)
        data = myfile.read(end_range - start_range + 1)
        headers = {
            "Content-Range": f"bytes {start_range}-{end_range}/{file_size}",
            "Accept-Ranges": "bytes",
        }

        return Response(
            content=data,
            status_code=status.HTTP_206_PARTIAL_CONTENT,
            headers=headers,
            media_type="video/mp4",
        )


@video_router.post("/upload", response_model=Lesson)
def upload_file(
    user = Depends(get_current_user),
    lesson_name: str = Header(),
    course_id: str = Header(),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    print(user.name)
    file_info = generate_file_location(file.filename)
    lesson = LessonBase(
        name=lesson_name, video_uuid=file_info.video_uuid, course_id=course_id
    )
    with open(file_info.file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    created_lessons = repo.create_lesson(db, lesson)
    return created_lessons
