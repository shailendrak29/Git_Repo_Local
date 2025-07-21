import streamlit as st
import pandas as pd
import altair as alt
from db_connection import get_connection

st.title("Monthly Incoming vs Outgoing Summary")

# --- Fetch data ---
conn = get_connection()
query = """
SELECT trans_year, trans_month,
       SUM(outgoing) AS sum_outgoing,
       SUM(incoming) AS sum_incoming
FROM public.t_c_all_tab_cat
GROUP BY trans_year, trans_month
ORDER BY trans_year, trans_month;
"""
df = pd.read_sql_query(query, conn)

# --- Convert columns to appropriate types ---
df["trans_month"] = df["trans_month"].astype(int)
df["trans_year"] = df["trans_year"].astype(int)

# --- Filters ---
years = sorted(df["trans_year"].unique())
months = list(range(1, 13))

selected_years = st.multiselect("Select Years", years, default=years)
selected_months = st.multiselect("Select Months", months, default=months)

# --- Filtered Data ---
filtered_df = df[
    df["trans_year"].isin(selected_years) &
    df["trans_month"].isin(selected_months)
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
