from __future__ import annotations

from fastapi import APIRouter

from src.Backend.schemas import GraphSnapshot
from src.Backend.services.graph_service import graph_service

router = APIRouter(prefix="/graph", tags=["graph"])


@router.get("", response_model=GraphSnapshot)
def get_graph() -> GraphSnapshot:
    return graph_service.snapshot()
