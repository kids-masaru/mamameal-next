# Minimal diagnostic version to identify loading issues
import streamlit as st

st.set_page_config(page_title="Mamameal Debug", page_icon="🍱")

st.title("🍱 Mamameal - 診断モード")
st.success("✅ 基本的なStreamlitは動作しています")

# Step 1: Test basic imports
st.header("Step 1: 基本インポート")
try:
    import os
    import sys
    import json
    import io
    st.success("✅ 基本モジュール OK")
except Exception as e:
    st.error(f"❌ 基本モジュール エラー: {e}")

# Step 2: Test pandas
st.header("Step 2: pandas")
try:
    import pandas as pd
    st.success("✅ pandas OK")
except Exception as e:
    st.error(f"❌ pandas エラー: {e}")

# Step 3: Test openpyxl
st.header("Step 3: openpyxl")
try:
    from openpyxl import load_workbook, Workbook
    st.success("✅ openpyxl OK")
except Exception as e:
    st.error(f"❌ openpyxl エラー: {e}")

# Step 4: Test google-generativeai
st.header("Step 4: google-generativeai")
try:
    import google.generativeai as genai
    st.success("✅ google-generativeai OK")
except Exception as e:
    st.error(f"❌ google-generativeai エラー: {e}")

# Step 5: Test pdfminer with logging suppression
st.header("Step 5: pdfminer (with logging suppression)")
try:
    import logging
    logging.getLogger('pdfminer').setLevel(logging.ERROR)
    logging.getLogger('pdfplumber').setLevel(logging.ERROR)
    logging.getLogger('pdfminer.pdfpage').setLevel(logging.ERROR)
    logging.getLogger('pdfminer.pdfinterp').setLevel(logging.ERROR)
    logging.getLogger('pdfminer.converter').setLevel(logging.ERROR)
    logging.getLogger('pdfminer.pdfdocument').setLevel(logging.ERROR)
    
    import pdfplumber
    st.success("✅ pdfplumber/pdfminer OK")
except Exception as e:
    st.error(f"❌ pdfplumber/pdfminer エラー: {e}")

# Step 6: Test pdf_utils import
st.header("Step 6: api.pdf_utils")
try:
    from pathlib import Path
    APP_DIR = Path(__file__).parent.resolve()
    sys.path.insert(0, str(APP_DIR))
    
    from api.pdf_utils import safe_write_df
    st.success("✅ api.pdf_utils OK")
except Exception as e:
    st.error(f"❌ api.pdf_utils エラー: {e}")

# Step 7: Test assets directory
st.header("Step 7: assets ディレクトリ")
try:
    from pathlib import Path
    ASSETS_DIR = Path(__file__).parent / 'api' / 'assets'
    if ASSETS_DIR.exists():
        files = list(ASSETS_DIR.iterdir())
        st.success(f"✅ assets ディレクトリ OK ({len(files)} ファイル)")
        for f in files:
            st.write(f"  - {f.name} ({f.stat().st_size / 1024:.1f} KB)")
    else:
        st.warning("⚠️ assets ディレクトリが見つかりません")
except Exception as e:
    st.error(f"❌ assets エラー: {e}")

st.header("結論")
st.info("全てのステップが ✅ であれば、本番アプリに戻して試してください。")
