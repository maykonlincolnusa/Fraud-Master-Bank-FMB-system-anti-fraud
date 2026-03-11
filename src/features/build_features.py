from __future__ import annotations

import pandas as pd
import numpy as np


def add_rolling_feats(df: pd.DataFrame) -> pd.DataFrame:
    df = df.sort_index()
    # example: count last 24h (needs timestamp in real project)
    if "amount" in df.columns:
        df["amount_log"] = np.log1p(df["amount"])
    return df
