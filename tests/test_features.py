import pandas as pd

from src.features.transaction_features import build_transaction_features


def test_build_transaction_features() -> None:
    df = pd.DataFrame(
        [
            {"amount": 15000, "country": "US"},
            {"amount": 50, "country": "BR"},
        ]
    )
    out = build_transaction_features(df)
    assert out["is_high_value"].tolist() == [True, False]
    assert out["is_international"].tolist() == [False, True]