import pandas as pd

df=pd.read_csv("../data/cleaned_superstore.csv",encoding="latin1")

# Total Sales
total_sales = df["Sales"].sum()

# Total Profit
total_profit = df["Profit"].sum()

# Total Orders
total_orders = df["Order ID"].nunique()

print("===== BUSINESS KPIs =====")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Orders: {total_orders}")


# Top 10 Products
top_products=(df.groupby("Product Name")["Sales"].sum().
    sort_values(ascending=False).head(10)
    )
print(top_products)

# Top 10 customer
top_customer=(df.groupby("Customer Name")["Sales"].sum().
    sort_values(ascending=False).head(10)
    )
print(top_customer)


# Sales by Region
sales_by_region = (
    df.groupby("Region")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print(sales_by_region)

#Profit by Region
profit_by_region = (
    df.groupby("Region")["Profit"]
      .sum()
      .sort_values(ascending=False)
)

print(profit_by_region)

#Sales by Category

sales_by_category = (
    df.groupby("Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print(sales_by_category)


#Profit by Category

profit_by_category = (
    df.groupby("Category")["Profit"]
      .sum()
      .sort_values(ascending=False)
)

print(profit_by_category)

#Category Summary

category_summaryy=(df.groupby("Category").agg({
"Sales":"sum",
"Profit":"sum",
"Quantity":"sum"
})
)
print(category_summaryy)


#Monthly Sales
monthly_sales = (
    df.groupby(["Year", "Month Number", "Month"])["Sales"]
      .sum()
      .reset_index()
      .sort_values(["Year", "Month Number"])
)

print(monthly_sales)

monthly_sales.to_csv(
    "../data/monthly_sales_trend.csv",
    index=False
)

print("\nMonthly trend file created!")

#Best Month
best_month=monthly_sales.loc[
    monthly_sales["Sales"].idxmax()
]
print(best_month)