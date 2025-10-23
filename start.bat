@echo off
ECHO Starting re:search setup...

set VENV_NAME=.venv

:: 1. Force Virtual Environment Creation (Handles 'cannot find path specified')
IF NOT EXIST "%VENV_NAME%\Scripts\activate.bat" (
    ECHO --- Creating virtual environment (one-time setup) ---
    :: Use 'py' launcher which is the most reliable way to call Python on Windows
    py -3 -m venv %VENV_NAME%
    
    IF ERRORLEVEL 1 (
        ECHO [FATAL ERROR] Failed to create virtual environment.
        ECHO Please ensure Python 3 is correctly installed and added to PATH.
        PAUSE
        GOTO :EOF
    )
)

:: 2. Activate Virtual Environment
ECHO --- Activating Virtual Environment ---
call %VENV_NAME%\Scripts\activate.bat

:: 3. Run Starter Script
ECHO --- Running starter.py ---
:: The current python executable (now the one inside the VENV) runs starter.py
python starter.py

PAUSE
