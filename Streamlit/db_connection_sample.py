import psycopg2
import streamlit as st

@st.cache_resource
def get_connection():
    return psycopg2.connect(
        host="localhost",         # e.g., "localhost" or "db.example.com"
        database="",  # e.g., "mydatabase"
        user="",     # e.g., "postgres"
        password="", # e.g., "yourpassword"
        port="5432"               # default PostgreSQL port
    )