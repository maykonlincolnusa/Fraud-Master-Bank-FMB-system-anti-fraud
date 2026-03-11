import pandas as pd
import numpy as np
from pathlib import Path

OUT = Path("data/raw/transactions.csv")
OUT.parent.mkdir(parents=True, exist_ok=True)

def gen_transactions(n=100000, fraud_rate=0.002, seed=42):
    rng = np.random.default_rng(seed)
    account_ids = rng.integers(100000, 199999, size=n)
    amount = np.round(np.exp(rng.normal(3.0, 1.7, n)), 2)
    hour = rng.integers(0,24,n)
    tx_type = rng.choice(["transfer","deposit","withdraw","payment"], n, p=[0.5,0.2,0.2,0.1])
    is_new_device = rng.choice([0,1], n, p=[0.98, 0.02])
    label = ( (amount>5000) & (is_new_device==1) & (rng.random(n)<0.7) ).astype(int)
    extra = rng.choice(n, size=int(n*fraud_rate), replace=False)
    label[extra] = 1
    df = pd.DataFrame({
        "account_id": account_ids,
        "amount": amount,
        "hour": hour,
        "tx_type": tx_type,
        "is_new_device": is_new_device,
        "label": label
    })
    return df

if __name__ == "__main__":
    df = gen_transactions()
    df.to_csv(OUT, index=False)
    print("Wrote", OUT)