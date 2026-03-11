from __future__ import annotations

from typing import List

from src.Backend.schemas import Transaction


def build_transaction_features(transactions: List[Transaction]) -> List[Transaction]:
    for tx in transactions:
        tx.features = {
            "amount_log": _log_amount(tx.amount),
            "is_high_value": tx.amount >= 10000,
            "is_international": bool(tx.country and tx.country.upper() not in {"US", "BR"}),
        }
    return transactions


def _log_amount(amount: float) -> float:
    if amount <= 0:
        return 0.0
    # Avoid numpy dependency here for speed in the API path
    import math

    return math.log1p(amount)
