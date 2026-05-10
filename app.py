import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Superstore BI Dashboard", layout="wide")
st.title("📊 Superstore Business Intelligence Dashboard")


@st.cache_data
def load_data():
    df = pd.read_csv("data/raw/Sample - Superstore.csv", encoding="windows-1252")
    df["Order Date"] = pd.to_datetime(df["Order Date"], format="%m/%d/%Y")
    df["Month"] = df["Order Date"].dt.to_period("M").astype(str)
    return df

df = load_data()

st.sidebar.header("🔍 Filters")
regions = ["All"] + sorted(df["Region"].unique().tolist())
categories = ["All"] + sorted(df["Category"].unique().tolist())
selected_region = st.sidebar.selectbox("Region", regions)
selected_category = st.sidebar.selectbox("Category", categories)

filtered = df.copy()
if selected_region != "All":
    filtered = filtered[filtered["Region"] == selected_region]
if selected_category != "All":
    filtered = filtered[filtered["Category"] == selected_category]

total_revenue = filtered["Sales"].sum()
total_profit = filtered["Profit"].sum()
profit_margin = (total_profit / total_revenue * 100) if total_revenue > 0 else 0
total_orders = filtered["Order ID"].nunique()

col1, col2, col3, col4 = st.columns(4)
col1.metric("💰 Total Revenue", f"${total_revenue:,.0f}")
col2.metric("📈 Total Profit", f"${total_profit:,.0f}")
col3.metric("📊 Profit Margin", f"{profit_margin:.1f}%")
col4.metric("🛒 Total Orders", f"{total_orders:,}")

st.markdown("---")

col1, col2 = st.columns([2, 1])
with col1:
    monthly = filtered.groupby("Month")["Sales"].sum().reset_index()
    fig1 = px.line(monthly, x="Month", y="Sales",
                   title="📅 Monthly Revenue Trend",
                   labels={"Sales": "Revenue ($)", "Month": ""},
                   template="plotly_white")
    fig1.update_traces(line_color="#2563eb", line_width=2.5)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    by_region = filtered.groupby("Region")["Sales"].sum().reset_index()
    fig2 = px.bar(by_region, x="Sales", y="Region", orientation="h",
                  title="🗺️ Revenue by Region",
                  labels={"Sales": "Revenue ($)", "Region": ""},
                  template="plotly_white", color="Sales",
                  color_continuous_scale="Blues")
    st.plotly_chart(fig2, use_container_width=True)

col1, col2 = st.columns([1, 2])
with col1:
    by_cat = filtered.groupby("Category")["Sales"].sum().reset_index()
    fig3 = px.pie(by_cat, values="Sales", names="Category",
                  title="🏷️ Revenue by Category",
                  template="plotly_white",
                  color_discrete_sequence=px.colors.sequential.Blues_r)
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    top_products = (filtered.groupby("Product Name")["Profit"]
                    .sum().reset_index()
                    .sort_values("Profit", ascending=False)
                    .head(10))
    fig4 = px.bar(top_products, x="Profit", y="Product Name", orientation="h",
                  title="🏆 Top 10 Products by Profit",
                  labels={"Profit": "Profit ($)", "Product Name": ""},
                  template="plotly_white", color="Profit",
                  color_continuous_scale="Greens")
    fig4.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")
st.subheader("🗃️ Raw Data Explorer")
st.dataframe(filtered[["Order Date", "Region", "Category", "Product Name",
                        "Sales", "Profit", "Quantity"]].sort_values("Order Date", ascending=False),
             use_container_width=True)