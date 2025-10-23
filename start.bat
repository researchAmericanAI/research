@echo off
ECHO Starting re:search setup...

set PYTHON_CMD=
set VENV_NAME=.venv

:: --- 1. Attempt to Find a Working Python Command ---

:: Try 'python' (common on clean installs or when added to PATH)
where python >nul 2>nul
if not errorlevel 1 set PYTHON_CMD=python

:: Try 'py' (Windows Python Launcher, common on modern installs)
if not defined PYTHON_CMD (
    where py >nul 2>nul
    if not errorlevel 1 set PYTHON_CMD=py
)

:: Try 'python3' (common when installed via external package manager)
if not defined PYTHON_CMD (
    where python3 >nul 2>nul
    if not errorlevel 1 set PYTHON_CMD=python3
)

:: --- 2. Execution Logic ---
if defined PYTHON_CMD (
    ECHO Found Python executable: %PYTHON_CMD%
    
    :: --- Virtual Environment Check (Best Practice) ---
    if not exist %VENV_NAME%\Scripts\activate.bat (
        ECHO --- Creating virtual environment (one-time setup) ---
        %PYTHON_CMD% -m venv %VENV_NAME%
        if errorlevel 1 (
            ECHO [FATAL ERROR] Failed to create virtual environment.
            ECHO Check your Python installation or permissions.
            pause
            goto :EOF
        )
    )
    
    ECHO --- Activating Virtual Environment ---
    call %VENV_NAME%\Scripts\activate.bat
    
    ECHO --- Running starter.py ---
    :: Run the starter script *within* the activated VENV
    %PYTHON_CMD% starter.py
    
    :: The starter.py script handles deactivation upon exit
    
) else (
    ECHO.
    ECHO [FATAL ERROR] Python 3 was not found.
    ECHO Please install Python 3.6 or newer.
    ECHO Ensure the Python installation option "Add python.exe to PATH" is checked.
    ECHO.
)

pause
