import streamlit as st
import pandas as pd

from vantrix_proyet.worker.pipeline import run_pipeline

# =========================
# ⚙️ CONFIG
# =========================
st.set_page_config(
    page_title="Vantrix AI System",
    layout="wide"
)

# =========================
# 🧠 HEADER
# =========================
st.title("🚀 VANTRIX AI SYSTEM")
st.caption("Autonomous Economic Agent")

# =========================
# 🔍 INPUT
# =========================
trend = st.text_input("🔎 Trend", "portable blender")

# =========================
# 🚀 RUN
# =========================
if st.button("Run Analysis"):

    results = run_pipeline(trend)

    if not results:
        st.warning("No products found")
    else:
        df = pd.DataFrame(results)

        # =========================
        # 🔥 FILTRO GANADORES
        # =========================
        winners = df[df["decision"] == "BUY"]

        if winners.empty:
            st.warning("No winners found")
        else:
            # ordenar por score
            winners = winners.sort_values(by="v_score", ascending=False)

            st.success(f"🔥 Winners encontrados: {len(winners)}")

            # =========================
            # 🏆 TOP 3
            # =========================
            st.subheader("🏆 TOP 3 PRODUCTOS")
            top = winners.head(3)
            st.dataframe(top, use_container_width=True)

            # =========================
            # 📊 TODOS LOS GANADORES
            # =========================
            st.subheader("📊 TODOS LOS GANADORES")
            st.dataframe(winners, use_container_width=True)

            # =========================
            # 📥 EXPORTAR CSV
            # =========================
            csv = winners.to_csv(index=False).encode("utf-8")

            st.download_button(
                label="📥 Descargar winners (CSV)",
                data=csv,
                file_name="winners_vantrix.csv",
                mime="text/csv"
            )