import pandas as pd

def clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["amount"] = df["amount"].fillna(0).astype(float)
    df["hour"] = df["hour"].astype(int)
    # convert categorical
    df = pd.get_dummies(df, columns=["tx_type"], prefix="tx")
    return df