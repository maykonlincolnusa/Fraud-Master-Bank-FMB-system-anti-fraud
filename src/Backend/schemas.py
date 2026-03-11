from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class OrmBase(BaseModel):
    class Config:
        from_attributes = True


class TransactionIn(OrmBase):
    transaction_id: Optional[UUID] = Field(default=None)
    entity_id: str = Field(..., min_length=1)
    counterparty_id: Optional[str] = Field(default=None)
    amount: float = Field(..., ge=0)
    currency: str = Field(default="USD", min_length=3, max_length=3)
    channel: Optional[str] = None
    device_id: Optional[str] = None
    country: Optional[str] = None
    timestamp: Optional[datetime] = None

    def normalized(self) -> "Transaction":
        return Transaction(
            transaction_id=self.transaction_id or uuid4(),
            entity_id=self.entity_id,
            counterparty_id=self.counterparty_id,
            amount=self.amount,
            currency=self.currency.upper(),
            channel=self.channel,
            device_id=self.device_id,
            country=self.country,
            timestamp=self.timestamp or datetime.utcnow(),
        )


class Transaction(OrmBase):
    transaction_id: UUID
    entity_id: str
    counterparty_id: Optional[str]
    amount: float
    currency: str
    channel: Optional[str]
    device_id: Optional[str]
    country: Optional[str]
    timestamp: datetime
    features: Dict[str, Any] = Field(default_factory=dict)
    risk_score: float = 0.0
    risk_reasons: List[str] = Field(default_factory=list)


class Alert(OrmBase):
    alert_id: UUID
    transaction_id: UUID
    entity_id: str
    score: float
    reason: str
    status: str = "open"
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Entity(OrmBase):
    entity_id: str
    risk_score: float = 0.0
    last_updated: datetime = Field(default_factory=datetime.utcnow)


class GraphNode(OrmBase):
    id: str
    type: str = "entity"


class GraphEdge(OrmBase):
    source: str
    target: str
    weight: float = 1.0


class GraphSnapshot(OrmBase):
    nodes: List[GraphNode]
    edges: List[GraphEdge]
