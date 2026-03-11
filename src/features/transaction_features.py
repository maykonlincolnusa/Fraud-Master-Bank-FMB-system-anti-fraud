from __future__ import annotations

import pandas as pd


def build_transaction_features(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    if "amount" in df.columns:
        df["is_high_value"] = df["amount"] >= 10000
    if "country" in df.columns:
        df["is_international"] = df["country"].str.upper().ne("US")
    return df