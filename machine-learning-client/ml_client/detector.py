"""People detection using a YOLO model (ultralytics)."""

import os

MODEL_PATH = os.environ.get("YOLO_MODEL", "yolov8n.pt")
PERSON_CLASS_ID = 0  # "person" in the COCO classes YOLO is trained on


def load_model():
    """Load (and cache) the YOLO model from ``MODEL_PATH``."""
    # TODO: import ultralytics.YOLO and load/cache the model here.
    raise NotImplementedError


def count_people(image) -> int:
    """Return the number of people YOLO detects in ``image`` (a PIL image)."""
    # TODO: run the model, keep detections with class == PERSON_CLASS_ID.
    raise NotImplementedError
