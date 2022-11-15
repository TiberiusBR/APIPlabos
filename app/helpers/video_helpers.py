import uuid
import os
from starlette.datastructures import Headers
from app.schemas.lesson import LessonBase

class GeneratedFileInfo:
    def __init__(self, video_uuid: str, file_location: str) -> None:
        self.video_uuid = video_uuid
        self.file_location = file_location


def generate_file_location(file_name: str) -> GeneratedFileInfo:
    video_uuid = str(uuid.uuid4())
    extension = file_name.split(".")[-1]
    video_name = f"{video_uuid}.{extension}"
    file_location = os.path.join(os.path.abspath(os.getcwd()), "files", video_name)
    return GeneratedFileInfo(video_uuid, file_location)