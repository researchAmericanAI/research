#!/bin/bash
# start.command for macOS
echo "Starting re:search setup..."
# Find the directory the script is in and change to it
cd "$(dirname "$0")"

# Use python3 if available, otherwise fall back to python
if command -v python3 &>/dev/null; then
    python3 starter.py
elif command -v python &>/dev/null; then
    python starter.py
else
    echo "Error: Python not found. Please install Python 3."
fi
