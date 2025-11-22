@echo off
echo ========================================
echo Motor Insurance Dashboard Setup
echo ========================================

echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

echo Generating synthetic data...
python utils\data_generator.py

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo To run the dashboard:
echo   1. Activate the environment: venv\Scripts\activate.bat
echo   2. Run the dashboard: streamlit run Home.py
echo.
pause
