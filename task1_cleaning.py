import pandas as pd

df = pd.read_csv("startup_funding.csv", encoding="latin1")

# Fill missing values
df["Industry Vertical"] = df["Industry Vertical"].fillna("Unknown")
df["SubVertical"] = df["SubVertical"].fillna("Unknown")
df["City  Location"] = df["City  Location"].fillna("Unknown")
df["Investors Name"] = df["Investors Name"].fillna("Undisclosed")
df["InvestmentnType"] = df["InvestmentnType"].fillna("Unknown")
df["Remarks"] = df["Remarks"].fillna("No Remarks")

# Clean Amount column
df["Amount in USD"] = (
    df["Amount in USD"]
    .astype(str)
    .str.replace(",", "", regex=False)
)

print(df["Amount in USD"].head(20))
df["Date dd/mm/yyyy"] = pd.to_datetime(
    df["Date dd/mm/yyyy"],
    dayfirst=True,
    errors="coerce"
)

print(df["Date dd/mm/yyyy"].head())
df["Year"] = df["Date dd/mm/yyyy"].dt.year
df["Month"] = df["Date dd/mm/yyyy"].dt.month
df.to_csv(
    "cleaned_startup_funding_v2.csv",
    index=False
)

print("Dataset Saved Successfully")