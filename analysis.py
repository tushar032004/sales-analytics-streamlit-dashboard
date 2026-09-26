import pandas as pd

# ==========================================
# 1. LOAD DATA
# ==========================================

df = pd.read_csv("data/sales_data.csv")

print("Original shape:", df.shape)


# ==========================================
# 2. CHECK DUPLICATES
# ==========================================

print("Duplicate rows:", df.duplicated().sum())

df = df.drop_duplicates()


# ==========================================
# 3. CONVERT DATE COLUMNS
# ==========================================

df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    format="%d/%m/%Y",
    errors="coerce"
)

df["Ship Date"] = pd.to_datetime(
    df["Ship Date"],
    format="%d/%m/%Y",
    errors="coerce"
)


# ==========================================
# 4. HANDLE POSTAL CODE
# ==========================================

df["Postal Code"] = (
    df["Postal Code"]
    .astype("Int64")
    .astype("string")
)

df["Postal Code"] = df["Postal Code"].fillna("Unknown")


# ==========================================
# 5. CHECK SALES
# ==========================================

df["Sales"] = pd.to_numeric(
    df["Sales"],
    errors="coerce"
)

df = df.dropna(subset=["Sales"])


# ==========================================
# 6. CREATE NEW FEATURES
# ==========================================

df["Order Year"] = df["Order Date"].dt.year

df["Order Month"] = df["Order Date"].dt.month

df["Month Name"] = df["Order Date"].dt.month_name()

df["Year-Month"] = df["Order Date"].dt.to_period("M")

df["Shipping Days"] = (
    df["Ship Date"] - df["Order Date"]
).dt.days


# ==========================================
# 7. FINAL VALIDATION
# ==========================================

print("\n===== CLEANED DATA =====")

print("\nShape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nFirst 5 Rows:")
print(df.head())

# ==========================================
# BUSINESS ANALYSIS
# ==========================================

# Total Sales
total_sales = df["Sales"].sum()

# Unique Orders
total_orders = df["Order ID"].nunique()

# Unique Customers
total_customers = df["Customer ID"].nunique()

# Average Order Value
order_totals = df.groupby("Order ID")["Sales"].sum()
average_order_value = order_totals.mean()

# ==========================================
# DETAILED BUSINESS ANALYSIS
# ==========================================

print("\n===== SALES BY CATEGORY =====")

sales_by_category = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(sales_by_category)


# ==========================================
# SALES BY SUB-CATEGORY
# ==========================================

print("\n===== SALES BY SUB-CATEGORY =====")

sales_by_subcategory = (
    df.groupby("Sub-Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(sales_by_subcategory)


# ==========================================
# SALES BY REGION
# ==========================================

print("\n===== SALES BY REGION =====")

sales_by_region = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(sales_by_region)


# ==========================================
# SALES BY SEGMENT
# ==========================================

print("\n===== SALES BY CUSTOMER SEGMENT =====")

sales_by_segment = (
    df.groupby("Segment")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(sales_by_segment)


# ==========================================
# TOP 10 STATES
# ==========================================

print("\n===== TOP 10 STATES BY SALES =====")

top_states = (
    df.groupby("State")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_states)


# ==========================================
# TOP 10 CITIES
# ==========================================

print("\n===== TOP 10 CITIES BY SALES =====")

top_cities = (
    df.groupby("City")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_cities)


# ==========================================
# TOP 10 PRODUCTS
# ==========================================

print("\n===== TOP 10 PRODUCTS BY SALES =====")

top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_products)


# ==========================================
# YEARLY SALES
# ==========================================

print("\n===== YEARLY SALES =====")

yearly_sales = (
    df.groupby("Order Year")["Sales"]
    .sum()
    .sort_index()
)

print(yearly_sales)


# ==========================================
# SHIPPING ANALYSIS
# ==========================================

print("\n===== SHIPPING ANALYSIS =====")

average_shipping_days = df["Shipping Days"].mean()

print(
    f"Average Shipping Time: "
    f"{average_shipping_days:.2f} days"
)


# ==========================================
# SHIPPING BY MODE
# ==========================================

print("\n===== SHIPPING TIME BY MODE =====")

shipping_by_mode = (
    df.groupby("Ship Mode")["Shipping Days"]
    .mean()
    .sort_values()
)

print(shipping_by_mode)
print("\n===== BUSINESS SUMMARY =====")

print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Orders: {total_orders:,}")
print(f"Total Customers: {total_customers:,}")
print(f"Average Order Value: ${average_order_value:,.2f}")
# ==========================================
# 8. SAVE CLEANED DATA
# ==========================================

df.to_csv(
    "data/cleaned_sales_data.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")