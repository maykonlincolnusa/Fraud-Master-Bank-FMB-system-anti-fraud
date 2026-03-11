from __future__ import annotations

from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel
from sqlalchemy import desc, select

from src.db.db import session_scope
from src.db.models import InvestigationDB


class Investigation(BaseModel):
    case_id: UUID
    alert_id: UUID
    entity_id: str
    status: str = "open"
    created_at: datetime = datetime.utcnow()


class InvestigationService:
    def list_cases(self) -> List[Investigation]:
        with session_scope() as session:
            rows = (
                session.execute(select(InvestigationDB).order_by(desc(InvestigationDB.created_at)))
                .scalars()
                .all()
            )
            return [self._to_schema(row) for row in rows]

    def get_case(self, case_id: UUID) -> Optional[Investigation]:
        with session_scope() as session:
            row = session.get(InvestigationDB, str(case_id))
            return self._to_schema(row) if row else None

    def create_case(self, alert_id: UUID, entity_id: str) -> Investigation:
        case = Investigation(case_id=uuid4(), alert_id=alert_id, entity_id=entity_id)
        with session_scope() as session:
            session.add(
                InvestigationDB(
                    case_id=str(case.case_id),
                    alert_id=str(case.alert_id),
                    entity_id=case.entity_id,
                    status=case.status,
                    created_at=case.created_at,
                )
            )
        return case

    def update_status(self, case_id: UUID, status: str) -> Optional[Investigation]:
        with session_scope() as session:
            row = session.get(InvestigationDB, str(case_id))
            if not row:
                return None
            row.status = status
            return self._to_schema(row)

    def _to_schema(self, row: InvestigationDB) -> Investigation:
        return Investigation(
            case_id=UUID(row.case_id),
            alert_id=UUID(row.alert_id),
            entity_id=row.entity_id,
            status=row.status,
            created_at=row.created_at,
        )


investigation_service = InvestigationService()
