# pakages
import cv2
import time
from typing import List

# module
from common.models import YOLO_MODEL
from common.constant import COUNTDOWN


# global variable
global_var_web_cam = None
detected_time = None


def yolo(model, frame) -> List[List]:
    """Detected objects output box"""

    results = model(frame)
    return results.pandas().xyxy[0]


def draw_bounding_boxes(objects: List[List], frame: List[List]):
    """Create a box based on detected"""

    global detected_time
    _detected: bool = False

    # Yolov5 has 82 Classes, the 0th of which use the Person class.
    class_mapping = {"person": 0}
    for _, row in objects.iterrows():
        x1, y1, x2, y2, conf, _, class_name = row
        class_num = class_mapping[class_name]

        if class_num == 0:
            label: str = f"{class_name} {conf:.2f}"  # persone: 0.85%
            frame = cv2.rectangle(
                frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2
            )
            frame = cv2.putText(
                frame,
                label,
                (int(x1), int(y1) - 5),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                1,
            )
            _detected = True

        else:  # If not detected
            _detected = False

    if _detected and detected_time is None:
        detected_time = time.time()
        cv2.putText(
            frame, "Detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2
        )

    elif detected_time and _detected:
        limit_seconds = round(time.time() - detected_time, 1)
        print(f"{limit_seconds}초 지남")

        if limit_seconds >= COUNTDOWN:
            cv2.putText(
                frame, "done", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2
            )

    elif not _detected:
        detected_time = None


def get_stream_video():
    """stream video"""

    global global_var_web_cam
    success: bool
    frame: List[int, int, int, int]

    global_var_web_cam = cv2.VideoCapture(1)  # My OS: (0) Iphone, (1) Mac book

    while True:
        success, frame = global_var_web_cam.read()

        if not success:
            break

        frame = cv2.flip(frame, 1)  # Horizontal flip

        objects = yolo(YOLO_MODEL, frame)
        draw_bounding_boxes(objects, frame)

        ret, buffer = cv2.imencode(".jpg", frame)
        frame = buffer.tobytes()
        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n" + bytearray(frame) + b"\r\n"
        )

    global_var_web_cam.release()
