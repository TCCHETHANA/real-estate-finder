import pandas as pd
import joblib
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

try:
    from xgboost import XGBRegressor
except ImportError:
    XGBRegressor = None


def train():
    base_dir = Path(__file__).resolve().parent
    data_path = base_dir / "data" / "processed" / "properties_cleaned.csv"
    model_dir = base_dir.parent / "backend" / "models"
    model_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(data_path)
    if 'price' not in df.columns:
        raise KeyError(f"Expected 'price' column in cleaned data, got: {list(df.columns)}")

    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df = df.dropna(subset=['price'])

    X = df.drop(columns=['price'])
    y = df['price']

    before_rows = len(X)
    X = X.dropna()
    y = y.loc[X.index]
    dropped = before_rows - len(X)
    if dropped > 0:
        print(f"Dropped {dropped} rows with remaining missing feature values")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    models = {
        "LinearRegression": LinearRegression(),
        "RandomForest": RandomForestRegressor(n_estimators=200, random_state=42)
    }
    if XGBRegressor is not None:
        models["XGBoost"] = XGBRegressor(n_estimators=200, learning_rate=0.05, random_state=42)
    else:
        print("Warning: xgboost is not installed; skipping XGBoost model.")

    best_model = None
    best_score = -float("inf")
    best_name = ""

    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        mae = mean_absolute_error(y_test, preds)
        r2 = r2_score(y_test, preds)
        print(f"{name}: MAE={mae:.2f}, R2={r2:.3f}")

        if r2 > best_score:
            best_score = r2
            best_model = model
            best_name = name

    print(f"\n✅ Best model: {best_name} (R2={best_score:.3f})")
    joblib.dump(best_model, model_dir / "price_model.pkl")
    joblib.dump(list(X.columns), model_dir / "feature_columns.pkl")
    print(f"✅ Model and feature columns saved to {model_dir}")


if __name__ == "__main__":
    train()
