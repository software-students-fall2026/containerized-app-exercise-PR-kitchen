"""Client for the machine-learning-client HTTP service."""


def request_detection(ml_client_url: str, image_file, mode: str) -> dict:
    """POST an image to the ML client's /detect endpoint and return its JSON."""
    # TODO: use requests.post(f"{ml_client_url}/detect", files=..., data=...).
    raise NotImplementedError
