from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from src.Backend.api.alerts_api import router as alerts_router
from src.Backend.api.graph_api import router as graph_router
from src.Backend.api.investigation_service import router as investigations_router
from src.Backend.api.transactions_api import router as transactions_router
from src.Backend.routes_entities import router as entities_router
from src.Backend.websocket.realtime_stram import broadcaster
from src.core.settings import settings
from src.db.session import init_db

app = FastAPI(title=settings.APP_NAME, version=settings.VERSION)

app.include_router(alerts_router, prefix=settings.API_PREFIX)
app.include_router(entities_router, prefix=settings.API_PREFIX)
app.include_router(graph_router, prefix=settings.API_PREFIX)
app.include_router(investigations_router, prefix=settings.API_PREFIX)
app.include_router(transactions_router, prefix=settings.API_PREFIX)


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "version": settings.VERSION}


@app.on_event("startup")
def startup() -> None:
    init_db()


BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/")
def index() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")


@app.websocket("/ws/alerts")
async def alerts_ws(websocket: WebSocket) -> None:
    await broadcaster.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        await broadcaster.disconnect(websocket)
