@echo off
echo Starting Motor Insurance Analytics Dashboard...
echo.

if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
)

streamlit run Home.py
