from __future__ import annotations

from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4

from sqlalchemy import desc, select

from src.Backend.schemas import Alert
from src.Backend.websocket.realtime_stram import broadcaster
from src.db.db import session_scope
from src.db.models import AlertDB


class AlertService:
    def list_alerts(self) -> List[Alert]:
        with session_scope() as session:
            rows = (
                session.execute(select(AlertDB).order_by(desc(AlertDB.created_at)))
                .scalars()
                .all()
            )
            return [self._to_schema(row) for row in rows]

    def get_alert(self, alert_id: UUID) -> Optional[Alert]:
        with session_scope() as session:
            row = session.get(AlertDB, str(alert_id))
            return self._to_schema(row) if row else None

    def create_alert(self, transaction_id: UUID, entity_id: str, score: float, reason: str) -> Alert:
        alert = Alert(
            alert_id=uuid4(),
            transaction_id=transaction_id,
            entity_id=entity_id,
            score=score,
            reason=reason,
            status="open",
            created_at=datetime.utcnow(),
        )
        with session_scope() as session:
            session.add(
                AlertDB(
                    alert_id=str(alert.alert_id),
                    transaction_id=str(alert.transaction_id),
                    entity_id=alert.entity_id,
                    score=alert.score,
                    reason=alert.reason,
                    status=alert.status,
                    created_at=alert.created_at,
                )
            )
        broadcaster.publish(alert)
        return alert

    def _to_schema(self, row: AlertDB) -> Alert:
        return Alert(
            alert_id=UUID(row.alert_id),
            transaction_id=UUID(row.transaction_id),
            entity_id=row.entity_id,
            score=row.score,
            reason=row.reason,
            status=row.status,
            created_at=row.created_at,
        )


alert_service = AlertService()
