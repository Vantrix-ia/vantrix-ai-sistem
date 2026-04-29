import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Vantrix AI", layout="wide")

st.title("🚀 Vantrix AI System")

API_URL= "http://127.0.0.1:8000/run"

try:
    res = requests.get(API_URL)
    data = res.json()

    products = data["products"]
    alerts = data["alerts"]

    df = pd.DataFrame(products)
    alerts_df = pd.DataFrame(alerts)

    st.subheader("📦 Productos")
    st.dataframe(df, use_container_width=True)

    st.subheader("🔥 Oportunidades (V-Score alto)")
    if not alerts_df.empty:
        st.dataframe(alerts_df, use_container_width=True)
    else:
        st.write("Sin oportunidades aún")

except Exception as e:
    st.error(f"Error conectando API: {e}")