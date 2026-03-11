from __future__ import annotations

import asyncio
from typing import Set

from fastapi import WebSocket

from src.Backend.schemas import Alert


class AlertBroadcaster:
    def __init__(self) -> None:
        self._connections: Set[WebSocket] = set()
        self._lock = asyncio.Lock()

    async def connect(self, websocket: WebSocket) -> None:
        await websocket.accept()
        async with self._lock:
            self._connections.add(websocket)

    async def disconnect(self, websocket: WebSocket) -> None:
        async with self._lock:
            self._connections.discard(websocket)

    def publish(self, alert: Alert) -> None:
        if not self._connections:
            return
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            return
        loop.create_task(self._broadcast(alert))

    async def _broadcast(self, alert: Alert) -> None:
        async with self._lock:
            connections = list(self._connections)
        payload = alert.dict()
        for ws in connections:
            try:
                await ws.send_json(payload)
            except Exception:
                await self.disconnect(ws)


broadcaster = AlertBroadcaster()
