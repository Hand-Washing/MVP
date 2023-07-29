"""Run server before memory allocation"""
import torch


YOLO_MODEL: torch = torch.hub.load(
    "ultralytics/yolov5", "yolov5s", pretrained=True, force_reload=False
)

# Model set default values
YOLO_MODEL.classes = 0
YOLO_MODEL.conf = 0.7
YOLO_MODEL.iou = 0.6
