#!/bin/bash
# start.command for macOS

echo "Starting re:search setup..."

# 1. Change to the directory where the script is located
# This ensures all relative paths work correctly.
cd "$(dirname "$0")"

# 2. Define Virtual Environment Directory
VENV_DIR=".venv"

# 3. Check and Create Virtual Environment
if [ ! -d "$VENV_DIR" ]; then
    echo "--- Creating virtual environment (one-time setup) ---"
    
    # Use python3 command to create venv
    if command -v python3 &>/dev/null; then
        python3 -m venv "$VENV_DIR"
    elif command -v python &>/dev/null; then
        # Fallback for systems where 'python' is already Python 3
        python -m venv "$VENV_DIR"
    else
        echo "Error: Python 3 command not found. Please ensure Python 3 is installed."
        exit 1
    fi
fi

# 4. Activate Virtual Environment
# The 'source' command activates the environment, redirecting 'python' and 'pip'
# commands to the ones inside the .venv folder.
source "$VENV_DIR/bin/activate"
echo "Virtual environment activated."

# 5. Execute the Python starter script within the VENV
# starter.py will now run its 'pip install' inside the isolated environment,
# bypassing the 'externally-managed' error.
echo "--- Running starter.py... ---"
python starter.py

# The 'deactivate' command is automatically run when this terminal window is closed
# or when the script exits, keeping your system clean.
