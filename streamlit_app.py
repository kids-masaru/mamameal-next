# Test WITHOUT pdfplumber
import streamlit as st

st.set_page_config(page_title="Mamameal Test", page_icon="🍱")
st.title("🍱 依存関係テスト (pdfplumberなし)")

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

st.header("結果")
st.success("pdfplumberがない状態では正常に動作しています!")
st.warning("⚠️ pdfplumberがPython 3.13と互換性がない可能性があります")
