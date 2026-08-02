import pandas as pd

df = pd.read_csv("data/processed/properties_cleaned.csv")

print("=" * 60)
print("Dataset Shape:", df.shape)
print("=" * 60)

for i, col in enumerate(df.columns, start=1):
    print(f"{i}. {col}")