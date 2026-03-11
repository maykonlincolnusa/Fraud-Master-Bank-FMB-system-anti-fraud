from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from sqlalchemy import desc, select

from src.Backend.schemas import Entity
from src.db.db import session_scope
from src.db.models import EntityDB


class EntityService:
    def list_entities(self) -> List[Entity]:
        with session_scope() as session:
            rows = (
                session.execute(select(EntityDB).order_by(desc(EntityDB.last_updated)))
                .scalars()
                .all()
            )
            return [self._to_schema(row) for row in rows]

    def get_entity(self, entity_id: str) -> Optional[Entity]:
        with session_scope() as session:
            row = session.get(EntityDB, entity_id)
            return self._to_schema(row) if row else None

    def update_risk(self, entity_id: str, score: float) -> Entity:
        with session_scope() as session:
            entity = session.get(EntityDB, entity_id)
            if not entity:
                entity = EntityDB(
                    entity_id=entity_id, risk_score=score, last_updated=datetime.utcnow()
                )
                session.add(entity)
            else:
                if score > entity.risk_score:
                    entity.risk_score = score
                entity.last_updated = datetime.utcnow()
            return self._to_schema(entity)

    def _to_schema(self, row: EntityDB) -> Entity:
        return Entity(
            entity_id=row.entity_id,
            risk_score=row.risk_score,
            last_updated=row.last_updated,
        )


entity_service = EntityService()
