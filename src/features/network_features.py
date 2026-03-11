from __future__ import annotations

import pandas as pd


def build_network_features(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    if "entity_id" in df.columns and "counterparty_id" in df.columns:
        df["has_counterparty"] = df["counterparty_id"].notna()
    return df