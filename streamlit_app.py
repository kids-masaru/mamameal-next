# Step 1: Test with pandas and openpyxl
import streamlit as st

st.set_page_config(page_title="Mamameal Test", page_icon="🍱")
st.title("🍱 依存関係テスト")

# Test pandas
st.header("Step 1: pandas")
try:
    import pandas as pd
    st.success("✅ pandas OK")
except Exception as e:
    st.error(f"❌ pandas: {e}")

# Test openpyxl
st.header("Step 2: openpyxl")
try:
    from openpyxl import Workbook
    st.success("✅ openpyxl OK")
except Exception as e:
    st.error(f"❌ openpyxl: {e}")

# Test google-generativeai
st.header("Step 3: google-generativeai")
try:
    import google.generativeai as genai
    st.success("✅ google-generativeai OK")
except Exception as e:
    st.error(f"❌ google-generativeai: {e}")

# Test pdfplumber (with logging suppression)
st.header("Step 4: pdfplumber")
try:
    import logging
    logging.getLogger('pdfminer').setLevel(logging.ERROR)
    import pdfplumber
    st.success("✅ pdfplumber OK")
except Exception as e:
    st.error(f"❌ pdfplumber: {e}")

st.header("結果")
st.info("全て ✅ なら、本番アプリに戻せます！")
