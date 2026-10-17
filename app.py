"""Optional interactive dashboard. Run: streamlit run app.py"""
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Sales Performance Explorer", layout="wide")
st.title("Sales Performance Explorer")
st.caption("Portfolio practice dashboard — all data is synthetic, not real company data.")

df = pd.read_csv("sales_data.csv", parse_dates=["date"])
df["revenue"] = df["units_sold"] * df["unit_price"]
df["estimated_profit"] = df["units_sold"] * (df["unit_price"] - df["unit_cost"])
df["month"] = df["date"].dt.to_period("M").astype(str)

products = st.multiselect("Filter products", sorted(df["product"].unique()), default=sorted(df["product"].unique()))
regions = st.multiselect("Filter regions", sorted(df["region"].unique()), default=sorted(df["region"].unique()))
filtered = df[df["product"].isin(products) & df["region"].isin(regions)]

if filtered.empty:
    st.warning("Choose at least one product and one region.")
else:
    total_revenue = filtered["revenue"].sum()
    profit = filtered["estimated_profit"].sum()
    margin = profit / total_revenue * 100 if total_revenue else 0
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Revenue", f"${total_revenue:,.0f}")
    c2.metric("Estimated profit", f"${profit:,.0f}")
    c3.metric("Units sold", f"{filtered['units_sold'].sum():,}")
    c4.metric("Estimated margin", f"{margin:.1f}%")

    st.subheader("Monthly performance")
    monthly = filtered.groupby("month")[["revenue", "estimated_profit"]].sum()
    st.line_chart(monthly)

    left, right = st.columns(2)
    with left:
        st.subheader("Revenue by product")
        st.bar_chart(filtered.groupby("product")["revenue"].sum().sort_values(ascending=False))
    with right:
        st.subheader("Estimated profit by region")
        st.bar_chart(filtered.groupby("region")["estimated_profit"].sum().sort_values(ascending=False))

    st.subheader("Filtered data")
    st.dataframe(filtered, use_container_width=True)
    st.download_button("Download filtered CSV", filtered.to_csv(index=False).encode("utf-8"), "filtered_sales_data.csv", "text/csv")
