from typing import List
import cv2
from cv2 import CascadeClassifier
from common import constant
from common.constant import GrayScale


def detect_objects(cascade, frame) -> List[List]:
    """얼굴 인식 좌표"""

    gray_frame: GrayScale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    objects: CascadeClassifier(List[List]) = cascade.detectMultiScale(
        gray_frame, scaleFactor=1.1, minNeighbors=5
    )

    return objects


def draw_bounding_boxes(objects: List[List], frame: List[List]):
    """탐지 된 좌표 값을 기준으로 박스 생성"""

    _detected: bool = False

    for x, y, w, h in objects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        _detected = True

    if _detected:
        cv2.putText(
            frame,
            "Person detected",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
            2,
        )


def get_stream_video(cascade: CascadeClassifier(List[List])):
    """실시간 영상 송출"""

    success: bool
    frame: List[int, int, int, int]

    while True:
        success, frame = constant.WEBCAM.read()

        if not success:
            break

        else:
            frame = cv2.flip(frame, 1)  # Horizontal

            objects = detect_objects(cascade, frame)
            draw_bounding_boxes(objects, frame)

            ret, buffer = cv2.imencode(".jpg", frame)
            frame = buffer.tobytes()
            yield (
                b"--frame\r\n"
                b"Content-Type: image/jpeg\r\n\r\n" + bytearray(frame) + b"\r\n"
            )

    constant.WEBCAM.release()  # memory free
