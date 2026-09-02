import pandas as pd
import joblib
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np


def evaluate():
    base_dir = Path(__file__).resolve().parent
    data_path = base_dir / "data" / "processed" / "properties_cleaned.csv"
    model_path = base_dir.parent / "backend" / "models" / "price_model.pkl"
    output_path = base_dir.parent / "docs" / "actual_vs_predicted.png"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    model = joblib.load(model_path)
    df = pd.read_csv(data_path)

    if 'price' not in df.columns:
        raise KeyError(f"Expected 'price' column in cleaned data, got: {list(df.columns)}")

    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df = df.dropna(subset=['price'])

    X = df.drop(columns=['price'])
    y = df['price']

    _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    preds = model.predict(X_test)

    mae = mean_absolute_error(y_test, preds)
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    r2 = r2_score(y_test, preds)

    print(f"MAE:  {mae:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"R²:   {r2:.3f}")

    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, preds, alpha=0.5)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
    plt.xlabel("Actual Price")
    plt.ylabel("Predicted Price")
    plt.title("Actual vs Predicted Prices")
    plt.savefig(output_path)
    plt.show()
    print(f"✅ Evaluation plot saved to {output_path}")


if __name__ == "__main__":
    evaluate()
