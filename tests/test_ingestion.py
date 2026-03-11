import os
from pathlib import Path

os.environ["DATABASE_URL"] = "sqlite:///./data/test_fmb.db"

from fastapi.testclient import TestClient

from src.Backend.app import app
from src.db.session import init_db

DB_PATH = Path("data/test_fmb.db")


def setup_module() -> None:
    if DB_PATH.exists():
        DB_PATH.unlink()
    init_db()


def test_ingest_creates_alert_and_entity() -> None:
    payload = [
        {
            "entity_id": "acct_1",
            "counterparty_id": "acct_2",
            "amount": 50000,
            "currency": "USD",
            "channel": "atm",
            "country": "FR",
        }
    ]

    with TestClient(app) as client:
        response = client.post("/api/v1/transactions/ingest", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert data["transactions"]
        assert data["transactions"][0]["entity_id"] == "acct_1"
        assert data["alerts"]

        entities = client.get("/api/v1/entities").json()
        assert any(entity["entity_id"] == "acct_1" for entity in entities)
