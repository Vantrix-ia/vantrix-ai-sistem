import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Vantrix AI Dashboard", layout="wide")

st.title("🚀 Vantrix AI System")

API_URL = "http://127.0.0.1:8000/run"

try:
    response = requests.get(API_URL)
    data = response.json()

    df = pd.DataFrame(data)

    st.subheader("📊 Productos detectados")
    st.dataframe(df, use_container_width=True)

    st.subheader("🔥 Top productos (V-Score alto)")
    top = df.sort_values(by="v_score", ascending=False).head(5)
    st.table(top)

except Exception as e:
    st.error(f"Error conectando a la API: {e}")