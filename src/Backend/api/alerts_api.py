from __future__ import annotations

from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException

from src.Backend.schemas import Alert
from src.Backend.services.alert_service import alert_service

router = APIRouter(prefix="/alerts", tags=["alerts"])


@router.get("", response_model=List[Alert])
def list_alerts() -> List[Alert]:
    return alert_service.list_alerts()


@router.get("/{alert_id}", response_model=Alert)
def get_alert(alert_id: UUID) -> Alert:
    alert = alert_service.get_alert(alert_id)
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    return alert
