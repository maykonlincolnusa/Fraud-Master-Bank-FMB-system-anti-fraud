from __future__ import annotations

from typing import List, Tuple

from src.Backend.schemas import Transaction


def score_transaction(tx: Transaction) -> Tuple[float, List[str]]:
    score = 0.0
    reasons: List[str] = []

    amount = tx.amount
    if amount >= 50000:
        score += 0.45
        reasons.append("very_high_amount")
    elif amount >= 10000:
        score += 0.25
        reasons.append("high_amount")

    if tx.features.get("is_international"):
        score += 0.2
        reasons.append("international_transfer")

    recent_count = float(tx.features.get("recent_tx_count_24h", 0))
    recent_amount = float(tx.features.get("recent_amount_sum_24h", 0.0))
    unique_counterparties = float(tx.features.get("unique_counterparties_24h", 0))

    if recent_count >= 10:
        score += 0.2
        reasons.append("high_velocity_24h")
    elif recent_count >= 5:
        score += 0.1
        reasons.append("moderate_velocity_24h")

    if recent_amount >= 100000:
        score += 0.2
        reasons.append("high_total_amount_24h")

    if unique_counterparties >= 5:
        score += 0.1
        reasons.append("many_counterparties_24h")

    if tx.features.get("country_mismatch"):
        score += 0.15
        reasons.append("country_changed")

    if tx.channel and tx.channel.lower() in {"atm", "crypto"}:
        score += 0.15
        reasons.append("high_risk_channel")

    if tx.device_id and tx.device_id.endswith("new"):
        score += 0.1
        reasons.append("new_device")

    score = min(score, 1.0)
    if not reasons and score > 0:
        reasons.append("elevated_risk")
    return score, reasons
