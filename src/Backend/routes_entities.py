from __future__ import annotations

from typing import List

from fastapi import APIRouter, HTTPException

from src.Backend.schemas import Entity
from src.Backend.services.entity_service import entity_service

router = APIRouter(prefix="/entities", tags=["entities"])


@router.get("", response_model=List[Entity])
def list_entities() -> List[Entity]:
    return entity_service.list_entities()


@router.get("/{entity_id}", response_model=Entity)
def get_entity(entity_id: str) -> Entity:
    entity = entity_service.get_entity(entity_id)
    if not entity:
        raise HTTPException(status_code=404, detail="Entity not found")
    return entity
