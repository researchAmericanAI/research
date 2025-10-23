import subprocess
import time
import sys
import os
import webbrowser
import platform

# --- Configuration ---
BACKEND_SCRIPT = "backend.py"
HTML_FILE = "index.html"
REQUIREMENTS_FILE = "requirements.txt"
BACKEND_PORT = 8000

def install_dependencies():
    """Installs dependencies from requirements.txt."""
    print("--- 1. Installing Python Requirements ---")
    try:
        # Use python -m pip for robustness
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", REQUIREMENTS_FILE])
        print("Installation complete.")
    except subprocess.CalledProcessError as e:
        print(f"\n[ERROR] Failed to install dependencies.")
        print("Please ensure you have Python and pip installed correctly.")
        print(f"Details: {e}")
        sys.exit(1)

def start_backend():
    """Starts the backend server in a separate, non-blocking process."""
    print("--- 2. Starting Local Backend (FastAPI) ---")
    
    # Use sys.executable for cross-platform compatibility
    command = [sys.executable, "-m", "uvicorn", "backend:app", "--port", str(BACKEND_PORT)]
    
    # Start the process in the background. The main script will handle termination.
    process = subprocess.Popen(command, cwd=os.getcwd())
    print(f"Backend started with process ID: {process.pid}")
    
    return process

def launch_html(backend_process):
    """Waits for the server and launches the HTML file in the default browser."""
    print("Waiting 3 seconds for server to initialize...")
    time.sleep(3)
    
    print("--- 3. Launching Client (index.html) ---")
    try:
        # Convert the relative path to an absolute file URL for the browser
        file_path = os.path.abspath(HTML_FILE)
        # Ensure correct file URL format for all OSes
        url = f"file://{file_path.replace(os.path.sep, '/')}"
        webbrowser.open_new_tab(url)
        print(f"Client launched in default browser.")
    except Exception as e:
        print(f"\n[WARNING] Could not automatically launch browser.")
        print(f"Please open this file manually: {file_path}")

    print("\n--- re:search is running ---")
    print("Do NOT close this window. Closing it will terminate the backend server.")

    # Keep the main script alive until the user closes the window (or hits Ctrl+C)
    try:
        # Wait for the backend process to finish (which should not happen unless it crashes)
        backend_process.wait()
    except KeyboardInterrupt:
        # Handle Ctrl+C from the user
        print("\nUser requested shutdown.")
    except Exception:
        # Handle unexpected exit
        pass
    finally:
        # Attempt to safely terminate the backend process
        if backend_process and backend_process.poll() is None:
            print(f"Attempting to terminate backend process {backend_process.pid}...")
            backend_process.terminate()
            try:
                backend_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                print("Process did not terminate gracefully. Forcing kill.")
                backend_process.kill()
        print("Shutdown complete. Thank you for using re:search.")


if __name__ == "__main__":
    # Check for basic Python/pip existence
    if sys.version_info < (3, 6):
        print("[FATAL] re:search requires Python 3.6 or higher.")
        sys.exit(1)
        
    backend_process = None
    try:
        install_dependencies()
        backend_process = start_backend()
        launch_html(backend_process)
    except Exception as e:
        print(f"\n[FATAL ERROR] An unexpected error occurred: {e}")
    finally:
        if backend_process and backend_process.poll() is None:
            # If the script exits prematurely, try to clean up the running backend
            backend_process.terminate()
