from __future__ import annotations

import pandas as pd


def build_behavioral_features(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    if "amount" in df.columns:
        df["amount_zscore"] = (df["amount"] - df["amount"].mean()) / (df["amount"].std() + 1e-6)
    if "channel" in df.columns:
        df["is_atm"] = df["channel"].str.lower().eq("atm")
    return df