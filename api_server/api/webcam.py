# Pakages
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from typing import Final

# Module
from util.opencv_webcam import get_stream_video
from util.error_handling import CustomException
from common import constant


router: Final[APIRouter] = APIRouter()


# endpoints
@router.get("/video")
async def realtime_webcam():
    """cam on"""

    return StreamingResponse(
        get_stream_video(),
        media_type=constant.MEDIA_TYPE,
    )


@router.get("/close")
async def realtime_cam_exit():
    """cam off"""

    from util.opencv_webcam import global_var_web_cam

    if global_var_web_cam:
        global_var_web_cam.release()
        return {"message": "Webcam streaming stopped."}

    raise CustomException(name="realtime_cam_exit")
