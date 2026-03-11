from __future__ import annotations

from datetime import datetime
from typing import Iterable, List, Optional
from uuid import UUID

from sqlalchemy import desc, select

from src.Backend.schemas import Transaction
from src.db.db import session_scope
from src.db.models import TransactionDB


class TransactionService:
    def save_transactions(self, transactions: Iterable[Transaction]) -> None:
        with session_scope() as session:
            for tx in transactions:
                existing = session.get(TransactionDB, str(tx.transaction_id))
                if existing:
                    existing.amount = tx.amount
                    existing.currency = tx.currency
                    existing.channel = tx.channel
                    existing.device_id = tx.device_id
                    existing.country = tx.country
                    existing.timestamp = tx.timestamp
                    existing.features = tx.features
                    existing.risk_score = tx.risk_score
                    existing.risk_reasons = tx.risk_reasons
                    continue
                session.add(
                    TransactionDB(
                        transaction_id=str(tx.transaction_id),
                        entity_id=tx.entity_id,
                        counterparty_id=tx.counterparty_id,
                        amount=tx.amount,
                        currency=tx.currency,
                        channel=tx.channel,
                        device_id=tx.device_id,
                        country=tx.country,
                        timestamp=tx.timestamp,
                        features=tx.features,
                        risk_score=tx.risk_score,
                        risk_reasons=tx.risk_reasons,
                    )
                )

    def list_recent(self, limit: int = 200) -> List[Transaction]:
        with session_scope() as session:
            rows = session.execute(
                select(TransactionDB).order_by(desc(TransactionDB.timestamp)).limit(limit)
            ).scalars()
            return [self._to_schema(row) for row in rows]

    def get_recent_for_entity(
        self, entity_id: str, since: datetime, limit: int = 200
    ) -> List[TransactionDB]:
        with session_scope() as session:
            rows = (
                session.execute(
                    select(TransactionDB)
                    .where(TransactionDB.entity_id == entity_id)
                    .where(TransactionDB.timestamp >= since)
                    .order_by(desc(TransactionDB.timestamp))
                    .limit(limit)
                )
                .scalars()
                .all()
            )
            return rows

    def get_by_id(self, transaction_id: UUID) -> Optional[Transaction]:
        with session_scope() as session:
            row = session.get(TransactionDB, str(transaction_id))
            if not row:
                return None
            return self._to_schema(row)

    def _to_schema(self, row: TransactionDB) -> Transaction:
        return Transaction(
            transaction_id=UUID(row.transaction_id),
            entity_id=row.entity_id,
            counterparty_id=row.counterparty_id,
            amount=row.amount,
            currency=row.currency,
            channel=row.channel,
            device_id=row.device_id,
            country=row.country,
            timestamp=row.timestamp,
            features=row.features or {},
            risk_score=row.risk_score,
            risk_reasons=row.risk_reasons or [],
        )


transaction_service = TransactionService()
