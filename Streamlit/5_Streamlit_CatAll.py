import streamlit as st
import pandas as pd
import altair as alt
from db_connection import get_connection

st.title("Monthly Incoming vs Outgoing Summary")

# --- Fetch data ---
conn = get_connection()
query = """
select trans_year, trans_month, trans_type, sum (outgoing) as sum_outgoing, sum (incoming) as sum_incoming  
from public.t_c_all_tab_cat
group by trans_year, trans_month, trans_type
order by trans_year, trans_month;
"""
df = pd.read_sql_query(query, conn)

# --- Convert columns to appropriate types ---
df["trans_month"] = df["trans_month"].astype(int)
df["trans_year"] = df["trans_year"].astype(int)
df["trans_type"] = df["trans_type"].astype(str)

# --- Filters ---
years = sorted(df["trans_year"].unique())
months = list(range(1, 13))
category = sorted(df["trans_type"].unique())

# Add "All" option to the lists
all_years = ["All"] + years
all_months = ["All"] + months
all_category = ["All"] + category

selected_years = st.multiselect("Select Years", all_years, default=["All"])
selected_months = st.multiselect("Select Months", all_months, default=["All"])
selected_cat = st.multiselect("Select Category", all_category, default=["All"])

# --- Filtered Data ---
# Apply filtering logic based on "All" selection
if "All" in selected_years:
    filtered_years = years
else:
    filtered_years = selected_years

if "All" in selected_months:
    filtered_months = months
else:
    filtered_months = selected_months

if "All" in selected_cat:
    filtered_category = category
else:
    filtered_category = selected_cat

filtered_df = df[
    df["trans_year"].isin(filtered_years) &
    df["trans_month"].isin(filtered_months) &
    df["trans_type"].isin(filtered_category)
]

# --- Combine Year & Month into a label for X-axis ---
filtered_df["period"] = filtered_df["trans_year"].astype(str) + "-" + filtered_df["trans_month"].astype(str).str.zfill(2)

# --- Melt data for grouped bar chart ---
melted_df = filtered_df.melt(id_vars=["period"], value_vars=["sum_incoming", "sum_outgoing"],
                             var_name="type", value_name="amount")

# --- Bar Chart using Altair ---
chart = alt.Chart(melted_df).mark_bar().encode(
    x=alt.X("period:N", title="Year-Month", sort=None),
    y=alt.Y("amount:Q", title="Amount"),
    color="type:N",
    xOffset='type:N',   # important to have 2 bars
    tooltip=["period", "type", "amount"]
).properties(
    width=700,
    height=400,
    title="Incoming vs Outgoing by Month"
)

st.altair_chart(chart, use_container_width=True)