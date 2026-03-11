import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
import joblib

if __name__ == "__main__":
    df = pd.read_csv("data/processed/transactions_clean.csv")
    X = df.drop(columns=["label"])
    y = df["label"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)
    model = XGBClassifier(use_label_encoder=False, eval_metric="auc", n_estimators=200, max_depth=6)
    model.fit(X_train, y_train)
    pred = model.predict_proba(X_test)[:,1]
    print("AUC:", roc_auc_score(y_test, pred))
    joblib.dump(model, "models/xgb_baseline.joblib")