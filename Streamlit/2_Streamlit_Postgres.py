import streamlit as st
import pandas as pd
import toml
from db_connection import get_connection

# params = toml.load("secrets.toml")


st.title("PostgreSQL Demo with Streamlit")

conn = get_connection()

query = """select trans_year, trans_month, sum (outgoing) as sum_outgoing, sum (incoming) as sum_incoming  
from public.t_c_all_tab_cat
group by trans_year, trans_month
order by trans_year, trans_month;"""
# query = st.secrets["queries"]["monthly_summary"]

# df = pd.read_sql_query(params["queries"]["query1"], conn)
df = pd.read_sql_query(query, conn)
st.dataframe(df)