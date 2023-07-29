"""Run server before memory allocation"""


import torch

YOLO_MODEL = torch.hub.load(
    "ultralytics/yolov5", "yolov5s", pretrained=True, force_reload=False
)
