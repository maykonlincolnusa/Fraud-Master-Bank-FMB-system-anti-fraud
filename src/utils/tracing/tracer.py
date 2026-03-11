from __future__ import annotations

from contextlib import contextmanager
from time import perf_counter
from typing import Iterator

from src.utils.logging.logger import get_logger

logger = get_logger("tracing")


@contextmanager
def trace(name: str) -> Iterator[None]:
    start = perf_counter()
    try:
        yield
    finally:
        elapsed_ms = (perf_counter() - start) * 1000
        logger.info("%s took %.2f ms", name, elapsed_ms)