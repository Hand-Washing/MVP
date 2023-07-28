from fastapi import APIRouter
from util.opencv_webcam import get_stream_video
from fastapi.responses import StreamingResponse
from common import constant

router = APIRouter()


@router.get("/video")
def realtime_webcam():
    return StreamingResponse(
        get_stream_video(constant.FACE_CASCADE),
        media_type=constant.MEDIA_TYPE,
    )
