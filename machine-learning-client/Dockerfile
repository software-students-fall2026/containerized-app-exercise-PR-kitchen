FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# OpenCV system libraries
RUN apt-get update \
    && apt-get install -y --no-install-recommends libgl1 libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install pipenv
COPY Pipfile Pipfile.lock ./

# Resolve deps so Linux-only CUDA packages missing from the macOS-generated lock get installed
RUN pipenv requirements > requirements.txt \
    && pip install -r requirements.txt \
    && rm requirements.txt

COPY . .

# Bake YOLO weights into the image
RUN python -c "from ultralytics import YOLO; YOLO('yolov8n.pt')"

EXPOSE 5001
CMD ["python", "-m", "ml_client.app"]
