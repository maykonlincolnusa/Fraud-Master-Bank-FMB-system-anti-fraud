from __future__ import annotations

from datetime import timedelta
from typing import List, Tuple

from src.Backend.schemas import Alert, Transaction
from src.Backend.services.alert_service import AlertService
from src.Backend.services.transaction_service import transaction_service
from src.intelligence.risk_engine.scoring_model import score_transaction


def score_transactions(
    transactions: List[Transaction], alert_service: AlertService, threshold: float = 0.7
) -> Tuple[List[Transaction], List[Alert]]:
    alerts: List[Alert] = []
    for tx in transactions:
        _enrich_with_history(tx)
        score, reasons = score_transaction(tx)
        tx.risk_score = score
        tx.risk_reasons = reasons
        if score >= threshold:
            reason = reasons[0] if reasons else "high_risk"
            alert = alert_service.create_alert(tx.transaction_id, tx.entity_id, score, reason)
            alerts.append(alert)
    return transactions, alerts


def _enrich_with_history(tx: Transaction) -> None:
    since = tx.timestamp - timedelta(hours=24)
    history = transaction_service.get_recent_for_entity(tx.entity_id, since=since, limit=200)

    if not history:
        tx.features.update(
            {
                "recent_tx_count_24h": 0,
                "recent_amount_sum_24h": 0.0,
                "unique_counterparties_24h": 0,
                "country_mismatch": False,
            }
        )
        return

    recent_count = len(history)
    amount_sum = sum(item.amount for item in history)
    unique_counterparties = len({item.counterparty_id for item in history if item.counterparty_id})
    country_mismatch = any(
        item.country and tx.country and item.country != tx.country for item in history[:5]
    )

    tx.features.update(
        {
            "recent_tx_count_24h": recent_count,
            "recent_amount_sum_24h": amount_sum,
            "unique_counterparties_24h": unique_counterparties,
            "country_mismatch": country_mismatch,
        }
    )
