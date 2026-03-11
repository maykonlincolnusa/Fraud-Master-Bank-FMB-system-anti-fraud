from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict

from .event_types import EventType


@dataclass
class Event:
    event_type: EventType
    payload: Dict[str, Any]
    timestamp: datetime = datetime.utcnow()
    source: str = "system"
