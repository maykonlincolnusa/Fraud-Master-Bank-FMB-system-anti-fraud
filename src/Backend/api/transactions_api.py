from __future__ import annotations

from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from src.Backend.schemas import Alert, Transaction, TransactionIn
from src.Backend.services.alert_service import alert_service
from src.Backend.services.entity_service import entity_service
from src.Backend.services.transaction_service import transaction_service
from src.pipelines.feature_pipeline import build_transaction_features
from src.pipelines.ingestion_pipeline import normalize_transactions
from src.pipelines.scoring_pipeline import score_transactions

router = APIRouter(prefix="/transactions", tags=["transactions"])


class IngestResponse(BaseModel):
    transactions: List[Transaction]
    alerts: List[Alert]


@router.post("/ingest", response_model=IngestResponse)
async def ingest_transactions(payload: List[TransactionIn]) -> IngestResponse:
    transactions = normalize_transactions(payload)
    transactions = build_transaction_features(transactions)
    scored, alerts = score_transactions(transactions, alert_service=alert_service)
    transaction_service.save_transactions(scored)
    for tx in scored:
        entity_service.update_risk(tx.entity_id, tx.risk_score)
    return IngestResponse(transactions=scored, alerts=alerts)


@router.get("", response_model=List[Transaction])
def list_transactions() -> List[Transaction]:
    return transaction_service.list_recent()
