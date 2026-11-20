"""Turn people counts into estimates the user cares about."""

BUSYNESS_LEVELS = ("Quiet", "Moderate", "Busy", "Packed")


def estimate_wait_minutes(people_in_line: int, avg_service_minutes: float) -> float:
    """Estimated wait for someone joining the back of the line."""
    # TODO: implement (and validate inputs).
    raise NotImplementedError


def busyness_level(people_count: int, capacity: int | None = None) -> str:
    """Return one of BUSYNESS_LEVELS.

    Uses ``people_count / capacity`` when the user gives a capacity,
    otherwise falls back to fixed count thresholds.
    """
    # TODO: implement.
    raise NotImplementedError
