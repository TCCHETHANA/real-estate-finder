import pandas as pd
import numpy as np
import joblib
import re
from pathlib import Path
from sklearn.preprocessing import LabelEncoder

# Normalize raw CSV column names to stable snake_case names
def normalize_column(name):
    name = str(name).strip()
    name = re.sub(r"[^0-9a-zA-Z]+", "_", name)
    name = re.sub(r"__+", "_", name)
    return name.strip("_").lower()

# Step 1: Load raw CSV
def load_data(path=None):
    if path is None:
        path = Path(__file__).resolve().parent / "data" / "processed" / "cleaned_data.csv"
    if not Path(path).is_file():
        raise FileNotFoundError(f"Raw data file not found: {path}")
    if Path(path).stat().st_size == 0:
        raise ValueError(f"Raw data file is empty: {path}")
    df = pd.read_csv(path)
    if df.empty:
        raise ValueError(f"Raw data file contains no rows or columns: {path}")
    df.columns = [normalize_column(c) for c in df.columns]
    print("Loaded data shape:", df.shape)
    return df

# Step 2: Clean missing values
def clean_data(df):
    df = df.drop_duplicates()

    # Drop rows missing too much data
    df = df.dropna(thresh=len(df.columns) * 0.7)

    # Fill numeric missing values with median or zero if median is not available
    num_cols = df.select_dtypes(include=[np.number]).columns
    for col in num_cols:
        median = df[col].median()
        if pd.isna(median):
            df[col] = df[col].fillna(0)
        else:
            df[col] = df[col].fillna(median)

    # Fill categorical/string missing values with mode or unknown
    cat_cols = df.select_dtypes(include=['string', 'object']).columns
    for col in cat_cols:
        if not df[col].mode().empty:
            df[col] = df[col].fillna(df[col].mode()[0])
        else:
            df[col] = df[col].fillna("unknown")

    # Drop columns that are still entirely missing after filling
    all_na_cols = [col for col in df.columns if df[col].isna().all()]
    if all_na_cols:
        df = df.drop(columns=all_na_cols)
        print(f"Dropped all-NA columns: {all_na_cols}")

    print("After cleaning shape:", df.shape)
    return df

# Step 3: Feature engineering
def feature_engineering(df):
    if 'price' in df.columns and 'carpet_area' in df.columns:
        df['price_per_sqft'] = df['price'] / df['carpet_area']
    if 'year_built' in df.columns:
        df['property_age'] = 2026 - df['year_built']
    return df

# Step 4: Encode categorical features
def encode_features(df, cat_cols):
    encoders = {}
    for col in cat_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))
        encoders[col] = le
    return df, encoders

# Step 5: Save cleaned data
if __name__ == "__main__":
    df = load_data()
    df = clean_data(df)
    df = feature_engineering(df)

    if 'id' in df.columns:
        df = df.drop(columns=['id'])

    cat_cols = df.select_dtypes(include=['string', 'object']).columns.tolist()
    print('Encoding object/string columns:', cat_cols)

    df, encoders = encode_features(df, cat_cols)

    base_dir = Path(__file__).resolve().parent
    processed_dir = base_dir / 'data' / 'processed'
    processed_dir.mkdir(parents=True, exist_ok=True)
    df.to_csv(processed_dir / 'properties_cleaned.csv', index=False)

    output_dir = base_dir.parent / 'backend' / 'models'
    output_dir.mkdir(parents=True, exist_ok=True)
    joblib.dump(encoders, output_dir / 'encoders.pkl')

    print(f'✅ Preprocessing complete. Cleaned data saved to {processed_dir} and encoders saved to {output_dir}')
