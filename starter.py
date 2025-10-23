import subprocess
import time
import sys
import os
import webbrowser
import platform
import socket # Added for finding a free port

# --- Configuration ---
BACKEND_SCRIPT = "backend.py"
HTML_FILE = "index.html"
REQUIREMENTS_FILE = "requirements.txt"
BACKEND_PORT = 8000 # Starting port

def find_free_port(start_port):
    """Dynamically finds an available port starting from start_port."""
    port = start_port
    while port < start_port + 10: # Check up to 10 ports
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('localhost', port))
                return port
        except OSError:
            port += 1
    return None

def install_dependencies():
    """Installs dependencies from requirements.txt."""
    print("--- 1. Installing Python Requirements ---")
    try:
        # Use python -m pip for robustness
        # This will install packages into the active virtual environment (if present)
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", REQUIREMENTS_FILE])
        print("Installation complete.")
    except subprocess.CalledProcessError as e:
        print(f"\n[ERROR] Failed to install dependencies.")
        print("Please ensure you have Python and pip installed correctly.")
        print(f"Details: {e}")
        sys.exit(1)

def start_backend():
    """Starts the backend server in a separate, non-blocking process."""
    
    # Check for a free port before attempting to start the server
    current_port = find_free_port(BACKEND_PORT)
    if current_port is None:
        print(f"[FATAL ERROR] Could not find a free port between {BACKEND_PORT} and {BACKEND_PORT + 9}.")
        sys.exit(1)

    print(f"--- 2. Starting Local Backend (FastAPI) on Port {current_port} ---")
    
    # Use sys.executable for cross-platform compatibility
    command = [sys.executable, "-m", "uvicorn", "backend:app", "--port", str(current_port)]
    
    # Start the process in the background. The main script will handle termination.
    # Using bufsize=1 forces output buffer flushing for better real-time logging.
    process = subprocess.Popen(command, cwd=os.getcwd(), bufsize=1)
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

    # FIX: Use an explicit polling loop to robustly keep the launcher process alive
    # as long as the backend server (Uvicorn) is running.
    try:
        while backend_process.poll() is None:
            time.sleep(1)
        
        # If the loop breaks, check if the backend died with an error code
        if backend_process.returncode is not None and backend_process.returncode != 0:
            print(f"\n[FATAL ERROR] Backend server stopped unexpectedly (Exit Code: {backend_process.returncode}).")
            print("Check if port 8000 is free, or if Uvicorn failed to start.")

    except KeyboardInterrupt:
        # Handle Ctrl+C from the user
        print("\nUser requested shutdown.")
    except Exception:
        # Catch unexpected errors in the waiting loop
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
        
        # This print ensures the user sees the final message before the window closes
        print("Shutdown complete. Thank you for using re:search.")


if __name__ == "__main__":
    # Check for basic Python/pip existence
    if sys.version_info < (3, 6):
        print("[FATAL] re:search requires Python 3.6 or higher.")
        sys.exit(1)
        
    backend_process = None
    try:
        # The start.bat/start.command handles the virtual environment and activation
        install_dependencies()
        backend_process = start_backend()
        launch_html(backend_process)
    except Exception as e:
        print(f"\n[FATAL ERROR] An unexpected error occurred: {e}")
    finally:
        # This cleanup is a failsafe if the main launch_html function exited prematurely
        if backend_process and backend_process.poll() is None:
            backend_process.terminate()
