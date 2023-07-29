from fastapi import APIRouter

# from util.opencv_webcam import get_stream_video
from util.test import get_stream_video
from util.error_handling import CustomException
from fastapi.responses import StreamingResponse
from common import constant

router = APIRouter()


@router.get("/video")
async def realtime_webcam():
    return StreamingResponse(
        get_stream_video(),
        media_type=constant.MEDIA_TYPE,
    )


@router.get("/close")
async def realtime_cam_exit():
    from util.opencv_webcam import global_var_web_cam

    if global_var_web_cam:
        global_var_web_cam.release()
        return {"message": "Webcam streaming stopped."}

    raise CustomException(name="realtime_cam_exit")
