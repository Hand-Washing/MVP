import cv2
from typing import List
from common.models import YOLO_MODEL

global_var_web_cam = None


def yolo(model, frame) -> List[List]:
    """탐지 된 객체의 박스 좌표 출력"""

    results = model(frame)
    return results.pandas().xyxy[0]


def draw_bounding_boxes(objects: List[List], frame: List[List]):
    """탐지된 좌표 값들을 기준으로 박스 생성"""

    _detected: bool = False

    # 'person'을 클래스 번호 0으로 매핑하는 코드 추가
    class_mapping = {"person": 0}
    for _, row in objects.iterrows():
        x1, y1, x2, y2, conf, _, class_name = row
        class_num = class_mapping[class_name]
        label = f"{class_name} {conf:.2f}"
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

    if _detected:
        print("사람이 탐지 되었습니다.")
        cv2.putText(
            frame,
            "Person detected",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
            2,
        )


def get_stream_video():
    """실시간 영상 송출"""
    success: bool
    frame: List[int, int, int, int]

    global global_var_web_cam
    global_var_web_cam = cv2.VideoCapture(0)

    # Model
    YOLO_MODEL.classes = 0
    YOLO_MODEL.conf = 0.7
    YOLO_MODEL.iou = 0.6

    while True:
        success, frame = global_var_web_cam.read()

        if not success:
            break

        frame = cv2.flip(frame, 1)  # Horizontal

        objects = yolo(YOLO_MODEL, frame)
        draw_bounding_boxes(objects, frame)

        ret, buffer = cv2.imencode(".jpg", frame)
        frame = buffer.tobytes()
        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n" + bytearray(frame) + b"\r\n"
        )

    global_var_web_cam.release()
