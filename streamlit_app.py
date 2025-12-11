# Ultra minimal test - just pandas and openpyxl
import streamlit as st

st.set_page_config(page_title="Mamameal Test", page_icon="🍱")
st.title("🍱 最小テスト")

st.header("Step 1: pandas")
try:
    import pandas as pd
    st.success("✅ pandas OK")
except Exception as e:
    st.error(f"❌ pandas: {e}")

st.header("Step 2: openpyxl")
try:
    from openpyxl import Workbook
    st.success("✅ openpyxl OK")
except Exception as e:
    st.error(f"❌ openpyxl: {e}")

st.success("テスト完了！")
