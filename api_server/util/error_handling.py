from fastapi import Request
from fastapi.responses import JSONResponse


class CustomException(Exception):
    def __init__(self, name: str):
        self.name = name


async def video_exception_handelr(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=500,
        content={"message": f"Callabe: {exc.name} >> 웹 캠이 현재 켜져 있지 않습니다."},
    )
