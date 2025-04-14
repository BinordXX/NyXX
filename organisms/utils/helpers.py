# digital_civilization/agents/utils/helpers.py

import random
import json
from datetime import datetime
from typing import Any, Dict


def generate_unique_id(prefix: str = "task") -> str:
    """
    Generate a simple unique ID with a given prefix.
    """
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
    return f"{prefix}_{timestamp}_{random.randint(1000, 9999)}"


def pretty_print(data: Any):
    """
    Nicely print any dictionary or JSON-like object.
    """
    print(json.dumps(data, indent=4, sort_keys=True))


def random_choice_weighted(choices: Dict[Any, float]) -> Any:
    """
    Pick an item based on a weighted probability.
    """
    total = sum(choices.values())
    r = random.uniform(0, total)
    upto = 0
    for item, weight in choices.items():
        if upto + weight >= r:
            return item
        upto += weight
    assert False, "Shouldn't get here"


def current_time_utc() -> str:
    """
    Return the current UTC time as a string.
    """
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")


def simulate_latency(min_delay=0.1, max_delay=0.3):
    """
    Random latency simulator, useful for emulating real-world communication lag.
    """
    from time import sleep
    sleep(random.uniform(min_delay, max_delay))
