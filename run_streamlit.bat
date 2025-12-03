@echo off
echo ==================================================
echo Starting Mamameal Seal Tool (Streamlit)
echo ==================================================

cd /d %~dp0

echo Installing requirements...
pip install -r requirements.txt

echo.
echo Starting Streamlit App...
streamlit run streamlit_app.py

pause
