import pandas as pd


# Load dataset
df = pd.read_csv("../data/raw/housing_data.csv")


# Count missing values
missing = df.isnull().sum()


# Calculate percentage
missing_percentage = (missing / len(df)) * 100


# Create report
result = pd.DataFrame({
    "Missing Values": missing,
    "Percentage": missing_percentage
})


# Show columns with highest missing values
print(result.sort_values(
    by="Percentage",
    ascending=False
).head(40))
