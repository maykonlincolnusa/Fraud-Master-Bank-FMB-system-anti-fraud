from __future__ import annotations

from typing import Iterable, List

from src.Backend.schemas import Transaction, TransactionIn


def normalize_transactions(payload: Iterable[TransactionIn]) -> List[Transaction]:
    return [item.normalized() for item in payload]
