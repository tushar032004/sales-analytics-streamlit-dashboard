import streamlit as st
import pandas as pd
import plotly.express as px


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)


# ==========================================
# TITLE
# ==========================================

st.title("📊 Sales Analytics Dashboard")

st.write(
    "Interactive analysis of sales performance, "
    "customers, products, regions and shipping."
)


# ==========================================
# LOAD DATA
# ==========================================

@st.cache_data
def load_data():

    df = pd.read_csv(
        "data/cleaned_sales_data.csv"
    )

    df["Order Date"] = pd.to_datetime(
        df["Order Date"]
    )

    df["Ship Date"] = pd.to_datetime(
        df["Ship Date"]
    )

    return df


df = load_data()
# ==========================================
# SIDEBAR FILTERS
# ==========================================

st.sidebar.header("🔍 Filters")


# Region filter
selected_regions = st.sidebar.multiselect(
    "Select Region",
    options=sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique())
)


# Category filter
selected_categories = st.sidebar.multiselect(
    "Select Category",
    options=sorted(df["Category"].unique()),
    default=sorted(df["Category"].unique())
)


# Segment filter
selected_segments = st.sidebar.multiselect(
    "Select Customer Segment",
    options=sorted(df["Segment"].unique()),
    default=sorted(df["Segment"].unique())
)
# Date filter
min_date = df["Order Date"].min().date()
max_date = df["Order Date"].max().date()

selected_dates = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Filter dataframe
if len(selected_dates) == 2:

    start_date, end_date = selected_dates

    filtered_df = df[
        (df["Region"].isin(selected_regions))
        &
        (df["Category"].isin(selected_categories))
        &
        (df["Segment"].isin(selected_segments))
        &
        (df["Order Date"].dt.date >= start_date)
        &
        (df["Order Date"].dt.date <= end_date)
    ]

else:
    st.info("Please select both a start date and an end date.")
    st.stop()

# ==========================================
# CHECK FOR EMPTY FILTER RESULTS
# ==========================================

if filtered_df.empty:
    st.warning(
        "⚠️ No data available for the selected filters."
    )
    st.stop()
# ==========================================
# KPI CALCULATIONS
# ==========================================

total_sales = filtered_df["Sales"].sum()

total_orders = filtered_df["Order ID"].nunique()

total_customers = filtered_df["Customer ID"].nunique()

order_totals = (
    filtered_df
    .groupby("Order ID")["Sales"]
    .sum()
)

average_order_value = order_totals.mean()


# ==========================================
# KPI CARDS
# ==========================================

st.subheader("📌 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Sales",
    f"${total_sales:,.2f}"
)

col2.metric(
    "Total Orders",
    f"{total_orders:,}"
)

col3.metric(
    "Customers",
    f"{total_customers:,}"
)

col4.metric(
    "Average Order Value",
    f"${average_order_value:,.2f}"
)
# ==========================================
# BUSINESS INSIGHTS
# ==========================================

st.subheader("💡 Business Insights")

# Top category
top_category = (
    filtered_df
    .groupby("Category")["Sales"]
    .sum()
    .idxmax()
)

top_category_sales = (
    filtered_df
    .groupby("Category")["Sales"]
    .sum()
    .max()
)

# Top region
top_region = (
    filtered_df
    .groupby("Region")["Sales"]
    .sum()
    .idxmax()
)

top_region_sales = (
    filtered_df
    .groupby("Region")["Sales"]
    .sum()
    .max()
)

# Top product
product_sales = (
    filtered_df
    .groupby("Product Name")["Sales"]
    .sum()
)

top_product = product_sales.idxmax()
top_product_sales = product_sales.max()

# Average shipping time
avg_shipping_days = (
    filtered_df["Shipping Days"].mean()
)

# Display insights
st.markdown(
    f"""
- **{top_category}** is the leading category with
  **${top_category_sales:,.2f}** in sales.

- **{top_region}** is the leading region with
  **${top_region_sales:,.2f}** in sales.

- The highest-selling product is
  **{top_product}**, generating
  **${top_product_sales:,.2f}** in sales.

- Average shipping time is
  **{avg_shipping_days:.2f} days**.
"""
)
# ==========================================
# MONTHLY SALES TREND
# ==========================================

st.subheader("📈 Sales Trend")

monthly_sales = (
    filtered_df
    .set_index("Order Date")
    .resample("ME")["Sales"]
    .sum()
    .reset_index()
)


fig_monthly = px.line(
    monthly_sales,
    x="Order Date",
    y="Sales",
    title="Monthly Sales Trend",
    markers=True
)


st.plotly_chart(
    fig_monthly,
    use_container_width=True
)
# ==========================================
# CATEGORY & REGION ANALYSIS
# ==========================================

col1, col2 = st.columns(2)


# Category Sales
category_sales = (
    filtered_df
    .groupby("Category", as_index=False)["Sales"]
    .sum()
    .sort_values("Sales", ascending=False)
)


fig_category = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    title="Sales by Category"
)


col1.plotly_chart(
    fig_category,
    use_container_width=True
)


# Region Sales
region_sales = (
    filtered_df
    .groupby("Region", as_index=False)["Sales"]
    .sum()
    .sort_values("Sales", ascending=False)
)


fig_region = px.bar(
    region_sales,
    x="Region",
    y="Sales",
    title="Sales by Region"
)


col2.plotly_chart(
    fig_region,
    use_container_width=True
)
# ==========================================
# SUB-CATEGORY ANALYSIS
# ==========================================

st.subheader("🛍️ Product & Sub-Category Analysis")

subcategory_sales = (
    filtered_df
    .groupby("Sub-Category", as_index=False)["Sales"]
    .sum()
    .sort_values("Sales", ascending=True)
)

fig_subcategory = px.bar(
    subcategory_sales,
    x="Sales",
    y="Sub-Category",
    orientation="h",
    title="Sales by Sub-Category"
)

st.plotly_chart(
    fig_subcategory,
    use_container_width=True
)
# ==========================================
# TOP PRODUCTS
# ==========================================

top_products = (
    filtered_df
    .groupby("Product Name", as_index=False)["Sales"]
    .sum()
    .sort_values("Sales", ascending=False)
    .head(10)
    .sort_values("Sales", ascending=True)
)

fig_products = px.bar(
    top_products,
    x="Sales",
    y="Product Name",
    orientation="h",
    title="Top 10 Products by Sales"
)

st.plotly_chart(
    fig_products,
    use_container_width=True
)
# ==========================================
# GEOGRAPHIC ANALYSIS
# ==========================================

st.subheader("🌎 Geographic Analysis")

col1, col2 = st.columns(2)


# Top States
top_states = (
    filtered_df
    .groupby("State", as_index=False)["Sales"]
    .sum()
    .sort_values("Sales", ascending=False)
    .head(10)
)

fig_states = px.bar(
    top_states,
    x="State",
    y="Sales",
    title="Top 10 States by Sales"
)

col1.plotly_chart(
    fig_states,
    use_container_width=True
)


# Top Cities
top_cities = (
    filtered_df
    .groupby("City", as_index=False)["Sales"]
    .sum()
    .sort_values("Sales", ascending=False)
    .head(10)
)

fig_cities = px.bar(
    top_cities,
    x="City",
    y="Sales",
    title="Top 10 Cities by Sales"
)

col2.plotly_chart(
    fig_cities,
    use_container_width=True
)
# ==========================================
# SHIPPING ANALYSIS
# ==========================================

st.subheader("🚚 Shipping Analysis")

shipping_by_mode = (
    filtered_df
    .groupby("Ship Mode", as_index=False)["Shipping Days"]
    .mean()
    .sort_values("Shipping Days")
)

fig_shipping = px.bar(
    shipping_by_mode,
    x="Ship Mode",
    y="Shipping Days",
    title="Average Shipping Time by Ship Mode"
)

st.plotly_chart(
    fig_shipping,
    use_container_width=True
)
# ==========================================
# DATA EXPLORER
# ==========================================

st.subheader("📋 Data Explorer")

with st.expander("View Filtered Dataset"):

    st.dataframe(
        filtered_df,
        use_container_width=True
    )
# ==========================================
# DOWNLOAD DATA
# ==========================================

csv = filtered_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="⬇️ Download Filtered Data",
    data=csv,
    file_name="filtered_sales_data.csv",
    mime="text/csv"
)