import pandas as pd

#load dataset
df=pd.read_csv("../data/superstore.csv",encoding="latin1")

#check duplicates
print("duplicated rows:",df.duplicated().sum())

#convert date
df["Order Date"]=pd.to_datetime(df["Order Date"])
df["Ship Date"]=pd.to_datetime(df["Ship Date"])

# Create new columns
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month_name()
df["Month Number"] = df["Order Date"].dt.month

# Save cleaned dataset
df.to_csv("../data/cleaned_superstore.csv", index=False)

print("\nData cleaned successfully!")
print(df.head())

print(df.shape)