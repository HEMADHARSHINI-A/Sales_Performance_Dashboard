import pandas as pd

# Load Dataset
df = pd.read_csv("../data/SampleSuperstore.csv")

# Remove Duplicates
df.drop_duplicates(inplace=True)

# Convert Date
df["Order Date"] = pd.to_datetime(df["Order Date"])

# KPIs
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Total Orders:", total_orders)

# Category Wise Sales
category_sales = df.groupby("Category")["Sales"].sum()
print(category_sales)

# Region Wise Sales
region_sales = df.groupby("Region")["Sales"].sum()
print(region_sales)