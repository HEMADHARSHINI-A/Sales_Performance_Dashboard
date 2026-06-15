import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE SETTINGS ---------------- #

st.set_page_config(
    page_title="Sales Performance Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------- LOAD CSS ---------------- #

try:
    with open("dashboard/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
except:
    pass

# ---------------- TITLE ---------------- #

st.markdown("""
<h1 style='text-align:center; color:#1f4e79;'>
📊 Sales Performance Dashboard
</h1>

<p style='text-align:center; font-size:18px;'>
Analyze Sales Trends, Revenue, Profit & Product Performance
</p>
""", unsafe_allow_html=True)

st.markdown("---")

st.info("""
✔ Dataset Loaded Successfully

✔ Duplicate Records Removed

✔ Date Format Converted

✔ Ready For Analysis
""")

# ---------------- LOAD DATA ---------------- #

@st.cache_data
def load_data():
    df = pd.read_csv("data/SampleSuperstore.csv")

    df.drop_duplicates(inplace=True)

    df["Order Date"] = pd.to_datetime(df["Order Date"])

    return df

df = load_data()

# ---------------- SIDEBAR ---------------- #

st.sidebar.header("🔍 Filters")

region = st.sidebar.multiselect(
    "Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

category = st.sidebar.multiselect(
    "Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

segment = st.sidebar.multiselect(
    "Segment",
    options=df["Segment"].unique(),
    default=df["Segment"].unique()
)

filtered_df = df[
    (df["Region"].isin(region)) &
    (df["Category"].isin(category)) &
    (df["Segment"].isin(segment))
]

# ---------------- KPI SECTION ---------------- #

total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Order ID"].nunique()
avg_sales = filtered_df["Sales"].mean()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("💰 Total Sales", f"${total_sales:,.0f}")

with col2:
    st.metric("📈 Total Profit", f"${total_profit:,.0f}")

with col3:
    st.metric("🛒 Total Orders", total_orders)

with col4:
    st.metric("📊 Avg Sales", f"${avg_sales:,.0f}")

st.markdown("---")

# ---------------- MONTHLY SALES ---------------- #

st.subheader("📈 Monthly Sales Trend")

monthly_sales = filtered_df.groupby(
    filtered_df["Order Date"].dt.to_period("M")
)["Sales"].sum().reset_index()

monthly_sales["Order Date"] = monthly_sales["Order Date"].astype(str)

fig1 = px.line(
    monthly_sales,
    x="Order Date",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)

st.plotly_chart(fig1, use_container_width=True)

# ---------------- QUARTERLY SALES ---------------- #

st.subheader("📅 Quarterly Sales Trend")

quarterly_sales = filtered_df.groupby(
    filtered_df["Order Date"].dt.to_period("Q")
)["Sales"].sum().reset_index()

quarterly_sales["Order Date"] = quarterly_sales["Order Date"].astype(str)

fig2 = px.bar(
    quarterly_sales,
    x="Order Date",
    y="Sales",
    title="Quarterly Sales Trend"
)

st.plotly_chart(fig2, use_container_width=True)

# ---------------- YEARLY SALES ---------------- #

st.subheader("📆 Yearly Sales Trend")

yearly_sales = filtered_df.groupby(
    filtered_df["Order Date"].dt.year
)["Sales"].sum().reset_index()

fig3 = px.line(
    yearly_sales,
    x="Order Date",
    y="Sales",
    markers=True,
    title="Yearly Sales Trend"
)

st.plotly_chart(fig3, use_container_width=True)

# ---------------- CATEGORY & REGION ---------------- #

col1, col2 = st.columns(2)

with col1:
    st.subheader("📦 Category-wise Sales")

    category_sales = filtered_df.groupby(
        "Category"
    )["Sales"].sum().reset_index()

    fig4 = px.bar(
        category_sales,
        x="Category",
        y="Sales",
        title="Sales by Category"
    )

    st.plotly_chart(fig4, use_container_width=True)

with col2:
    st.subheader("🌎 Region-wise Sales")

    region_sales = filtered_df.groupby(
        "Region"
    )["Sales"].sum().reset_index()

    fig5 = px.pie(
        region_sales,
        names="Region",
        values="Sales",
        title="Sales Distribution by Region"
    )

    st.plotly_chart(fig5, use_container_width=True)

# ---------------- PROFIT ---------------- #

st.subheader("💵 Profit by Category")

profit_category = filtered_df.groupby(
    "Category"
)["Profit"].sum().reset_index()

fig6 = px.bar(
    profit_category,
    x="Category",
    y="Profit",
    title="Profit by Category"
)

st.plotly_chart(fig6, use_container_width=True)

# ---------------- TOP PRODUCTS ---------------- #

st.subheader("🏆 Top 10 Products")

top_products = (
    filtered_df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig7 = px.bar(
    top_products,
    x="Sales",
    y="Product Name",
    orientation="h",
    title="Top 10 Products"
)

st.plotly_chart(fig7, use_container_width=True)

# ---------------- LOW PRODUCTS ---------------- #

st.subheader("⚠️ Bottom 10 Products")

low_products = (
    filtered_df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values()
    .head(10)
    .reset_index()
)

fig8 = px.bar(
    low_products,
    x="Sales",
    y="Product Name",
    orientation="h",
    title="Bottom 10 Products"
)

st.plotly_chart(fig8, use_container_width=True)

# ---------------- DATA PREVIEW ---------------- #

st.subheader("📋 Dataset Preview")

st.dataframe(
    filtered_df.head(20),
    use_container_width=True
)

# ---------------- BUSINESS INSIGHTS ---------------- #

st.subheader("📌 Key Business Insights")

top_region = region_sales.sort_values(
    by="Sales",
    ascending=False
).iloc[0]["Region"]

top_category = category_sales.sort_values(
    by="Sales",
    ascending=False
).iloc[0]["Category"]

st.success(
f"""
Top Region: {top_region}

Top Category: {top_category}

Total Revenue: ${total_sales:,.0f}

Total Profit: ${total_profit:,.0f}
"""
)

# ---------------- FOOTER ---------------- #

st.markdown("---")

st.markdown(
    """
    <div style='text-align:center'>
    Created Using Python • Pandas • Plotly • Streamlit 🚀
    </div>
    """,
    unsafe_allow_html=True
)