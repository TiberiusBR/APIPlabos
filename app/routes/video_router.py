import os
import re

from fastapi import APIRouter, Request, status
from fastapi.responses import Response

video_router = APIRouter(prefix="/video")


@video_router.get("/")
def play_video(request: Request, response: Response):
    header_range = request.headers.get("range")
    # TODO RETURN 400 if range header doesn't exist.
    file_path = os.path.abspath("./video.mp4")
    file_size = os.stat(file_path).st_size  # Size in bytes
    # Parse Range
    # Example "bytes=32324"

    chunk_size = pow(10, 6)  # 1mb ?
    start_range = int(
        re.sub(r"\D", "", header_range))  # range comes in this pattern: 'bytes=0-'. This regex removes the letters

    # Uses minimum value so range value doesn't extends file size.
    end_range = min(start_range + chunk_size, file_size - 1)

    with open(file_path, "rb") as myfile:
        myfile.seek(start_range)
        data = myfile.read(end_range - start_range + 1)
        headers = {
            "Content-Range": f"bytes {start_range}-{end_range}/{file_size}",
            "Accept-Ranges": "bytes"
        }

        return Response(
            content=data,
            status_code=status.HTTP_206_PARTIAL_CONTENT,
            headers=headers,
            media_type="video/mp4"
        )
