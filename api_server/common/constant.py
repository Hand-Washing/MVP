# pakages
import cv2
from typing import TypeVar, Final

# typing
GrayScale = TypeVar("gray_frame")
WebCam = TypeVar("WEBCAM")
Image = TypeVar("IMAGE")


# images
# VIDEO = cv2.VideoCapture("dummy_video.mp4")
# IMAGE: Final[Image] = cv2.imread("/Users/juhwan.lee/Downloads/QHD 검은색 배경화면.jpg")

# stream-type
MEDIA_TYPE: Final[str] = "multipart/x-mixed-replace; boundary=frame"

# washing hand counting
COUNTDOWN: Final[int] = 20
