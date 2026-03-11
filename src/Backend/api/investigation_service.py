from __future__ import annotations

from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.Backend.services.investigation_service import investigation_service

router = APIRouter(prefix="/investigations", tags=["investigations"])


class InvestigationCreate(BaseModel):
    alert_id: UUID
    entity_id: str


class InvestigationUpdate(BaseModel):
    status: str


@router.get("")
def list_investigations() -> List[dict]:
    return [case.dict() for case in investigation_service.list_cases()]


@router.get("/{case_id}")
def get_investigation(case_id: UUID) -> dict:
    case = investigation_service.get_case(case_id)
    if not case:
        raise HTTPException(status_code=404, detail="Case not found")
    return case.dict()


@router.post("", status_code=201)
def create_investigation(payload: InvestigationCreate) -> dict:
    case = investigation_service.create_case(payload.alert_id, payload.entity_id)
    return case.dict()


@router.patch("/{case_id}")
def update_investigation(case_id: UUID, payload: InvestigationUpdate) -> dict:
    case = investigation_service.update_status(case_id, payload.status)
    if not case:
        raise HTTPException(status_code=404, detail="Case not found")
    return case.dict()
