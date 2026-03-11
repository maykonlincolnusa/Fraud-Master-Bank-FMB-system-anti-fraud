from __future__ import annotations

from typing import Dict

from sqlalchemy import func, select

from src.Backend.schemas import GraphEdge, GraphNode, GraphSnapshot
from src.db.db import session_scope
from src.db.models import TransactionDB


class GraphService:
    def snapshot(self) -> GraphSnapshot:
        nodes: Dict[str, GraphNode] = {}
        edges: Dict[tuple[str, str], GraphEdge] = {}

        with session_scope() as session:
            rows = (
                session.execute(
                    select(
                        TransactionDB.entity_id,
                        TransactionDB.counterparty_id,
                        func.count(TransactionDB.transaction_id),
                    )
                    .where(TransactionDB.counterparty_id.is_not(None))
                    .group_by(TransactionDB.entity_id, TransactionDB.counterparty_id)
                )
                .all()
            )
            for entity_id, counterparty_id, count in rows:
                nodes.setdefault(entity_id, GraphNode(id=entity_id))
                nodes.setdefault(counterparty_id, GraphNode(id=counterparty_id))
                edges[(entity_id, counterparty_id)] = GraphEdge(
                    source=entity_id, target=counterparty_id, weight=float(count)
                )

        return GraphSnapshot(nodes=list(nodes.values()), edges=list(edges.values()))


graph_service = GraphService()
