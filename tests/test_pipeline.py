import os
from datetime import datetime, timedelta
from pathlib import Path
from uuid import uuid4

os.environ["DATABASE_URL"] = "sqlite:///./data/test_fmb.db"

from src.Backend.schemas import Transaction
from src.Backend.services.alert_service import alert_service
from src.Backend.services.transaction_service import transaction_service
from src.db.session import init_db
from src.pipelines.scoring_pipeline import score_transactions

DB_PATH = Path("data/test_fmb.db")


def setup_module() -> None:
    init_db()


def test_scoring_with_history() -> None:
    base_time = datetime.utcnow() - timedelta(hours=1)

    history = []
    for i in range(6):
        history.append(
            Transaction(
                transaction_id=uuid4(),
                entity_id="acct_hist",
                counterparty_id=f"cp_{i}",
                amount=1000,
                currency="USD",
                channel="card",
                device_id="device_old",
                country="US",
                timestamp=base_time + timedelta(minutes=i),
            )
        )

    transaction_service.save_transactions(history)

    incoming = Transaction(
        transaction_id=uuid4(),
        entity_id="acct_hist",
        counterparty_id="cp_x",
        amount=500,
        currency="USD",
        channel="card",
        device_id="device_new",
        country="US",
        timestamp=datetime.utcnow(),
    )

    scored, _alerts = score_transactions([incoming], alert_service=alert_service, threshold=0.95)
    assert scored[0].risk_score > 0
    assert scored[0].features["recent_tx_count_24h"] >= 6
