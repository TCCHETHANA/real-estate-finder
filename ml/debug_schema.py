import pandas as pd
from pathlib import Path

path = Path(__file__).resolve().parent / "data" / "processed" / "properties_cleaned.csv"
df = pd.read_csv(path)
print('shape', df.shape)
print('total_na', int(df.isna().sum().sum()))
na_cols = [c for c in df.columns if df[c].isna().any()]
print('na_cols', na_cols)
print('dtypes', df.dtypes.value_counts().to_dict())
print('sample na rows for first na cols')
for c in na_cols[:5]:
    print(c, df[df[c].isna()].head(3).to_dict('records'))
