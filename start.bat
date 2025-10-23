@echo off
ECHO Starting re:search setup...
ECHO ==============================================================
ECHO This window is intentionally being kept open to display errors.
ECHO Please read the output below.
ECHO ==============================================================

set VENV_NAME=.venv
set ERROR_FLAG=0

:: 1. TRY TO FIND PYTHON VIA THE RELIABLE 'py' LAUNCHER
:: Using py -3 is the most common way to call Python 3 on a Windows system.
ECHO Checking for Python 3...
py -3 --version 2>NUL
IF ERRORLEVEL 1 (
    ECHO [FATAL ERROR] Python 3 was not found using 'py -3'.
    ECHO Please install Python 3.6 or newer, ensuring it is added to the PATH during installation.
    SET ERROR_FLAG=1
) ELSE (
    ECHO Python 3 found.
)

:: If Python was found, attempt to set up and run
IF %ERROR_FLAG% EQU 0 (
    :: 2. Force Virtual Environment Creation (Handles 'cannot find path specified' error)
    IF NOT EXIST "%VENV_NAME%\Scripts\activate.bat" (
        ECHO --- Creating virtual environment (one-time setup) ---
        py -3 -m venv %VENV_NAME%
        
        IF ERRORLEVEL 1 (
            ECHO [FATAL ERROR] Failed to create virtual environment.
            ECHO Check your Python installation or permissions.
            SET ERROR_FLAG=1
        )
    )

    IF %ERROR_FLAG% EQU 0 (
        :: 3. Activate Virtual Environment
        ECHO --- Activating Virtual Environment ---
        call %VENV_NAME%\Scripts\activate.bat

        :: 4. Run Starter Script
        ECHO --- Running starter.py ---
        python starter.py
    )
)

ECHO.
ECHO --- END OF SCRIPT ---
PAUSE
