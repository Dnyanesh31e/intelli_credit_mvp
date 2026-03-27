@echo off
echo ================================================
echo    Intelli-Credit Enterprise Platform
echo    Starting Application...
echo ================================================
echo.

REM Check Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

echo [1/3] Python found. Checking dependencies...
echo.

REM Install dependencies if needed
pip show streamlit >nul 2>&1
if errorlevel 1 (
    echo [2/3] Installing dependencies (this may take a few minutes)...
    pip install -r requirements.txt
) else (
    echo [2/3] Dependencies already installed.
)
echo.

echo [3/3] Starting Streamlit application...
echo.
echo ================================================
echo    Application starting...
echo    Open your browser to: http://localhost:8501
echo ================================================
echo.

streamlit run app_complete.py

pause
