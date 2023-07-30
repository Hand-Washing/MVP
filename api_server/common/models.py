"""Run server before memory allocation"""
import torch

# torch.cuda.get_device_name(0)	# use gpu
# torch.cuda.is_available()		# cuda

YOLO_MODEL: torch = torch.hub.load(
    "ultralytics/yolov5", "yolov5s", pretrained=True, force_reload=False
)

# Model set default values
YOLO_MODEL.classes = 0
YOLO_MODEL.conf = 0.6
YOLO_MODEL.iou = 0.6
