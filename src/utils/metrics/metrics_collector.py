from __future__ import annotations

from typing import Dict


class MetricsCollector:
    def __init__(self) -> None:
        self._counts: Dict[str, int] = {}

    def inc(self, name: str, value: int = 1) -> None:
        self._counts[name] = self._counts.get(name, 0) + value

    def snapshot(self) -> Dict[str, int]:
        return dict(self._counts)


metrics = MetricsCollector()