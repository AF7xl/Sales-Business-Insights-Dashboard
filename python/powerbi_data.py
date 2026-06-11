import pandas as pd

df = pd.read_csv("../data/cleaned_superstore.csv")

# Sales by Region
sales_region = (
    df.groupby("Region")["Sales"]
      .sum()
      .reset_index()
)

sales_region.to_csv(
    "../data/sales_by_region.csv",
    index=False
)

# Profit by Category
profit_category = (
    df.groupby("Category")["Profit"]
      .sum()
      .reset_index()
)

profit_category.to_csv(
    "../data/profit_by_category.csv",
    index=False
)

print("Power BI files created!")