"""Sales Performance Analysis — synthetic practice dataset."""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv", parse_dates=["date"])

# 1. Check data quality
print("Rows and columns:", df.shape)
print("\nMissing values by column:\n", df.isna().sum())
print("\nDuplicate rows:", df.duplicated().sum())

# 2. Calculate financial metrics
df["revenue"] = df["units_sold"] * df["unit_price"]
df["cost"] = df["units_sold"] * df["unit_cost"]
df["profit"] = df["revenue"] - df["cost"]
df["profit_margin_pct"] = (df["profit"] / df["revenue"]) * 100

# 3. Summaries
df["month"] = df["date"].dt.to_period("M").astype(str)
monthly = df.groupby("month").agg(
    revenue=("revenue", "sum"),
    estimated_profit=("profit", "sum"),
    units_sold=("units_sold", "sum"),
)
by_product = df.groupby("product").agg(
    revenue=("revenue", "sum"),
    estimated_profit=("profit", "sum"),
    units_sold=("units_sold", "sum"),
).sort_values("revenue", ascending=False)
by_region = df.groupby("region").agg(
    revenue=("revenue", "sum"),
    estimated_profit=("profit", "sum"),
    units_sold=("units_sold", "sum"),
).sort_values("revenue", ascending=False)

print(f"\nTotal revenue: ${df['revenue'].sum():,.2f}")
print(f"Estimated profit: ${df['profit'].sum():,.2f}")
print(f"Overall estimated margin: {df['profit'].sum()/df['revenue'].sum()*100:.1f}%")
print("\nMonthly summary:\n", monthly.round(2))
print("\nProduct summary:\n", by_product.round(2))
print("\nRegion summary:\n", by_region.round(2))

# 4. Visualize results and save charts
monthly[["revenue", "estimated_profit"]].plot(marker="o", title="Monthly Revenue and Estimated Profit")
plt.xlabel("Month"); plt.ylabel("USD"); plt.tight_layout()
plt.savefig("monthly_revenue_profit.png", dpi=160); plt.show()

by_product["revenue"].sort_values().plot(kind="barh", title="Revenue by Product")
plt.xlabel("Revenue (USD)"); plt.ylabel("Product"); plt.tight_layout()
plt.savefig("revenue_by_product.png", dpi=160); plt.show()

by_region["estimated_profit"].sort_values().plot(kind="barh", title="Estimated Profit by Region")
plt.xlabel("Estimated profit (USD)"); plt.ylabel("Region"); plt.tight_layout()
plt.savefig("profit_by_region.png", dpi=160); plt.show()
