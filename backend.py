import os
import requests
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json

# --- CONFIGURATION ---
# 1. Your remote Render server URL for prompt encapsulation
RENDER_SERVER_URL = "https://researchnexus.onrender.com"
PROMPT_ENCODE_ENDPOINT = f"{RENDER_SERVER_URL}/generate_prompt"

# 2. User's local LLM configuration (standard Ollama defaults)
LOCAL_MODEL_ENDPOINT = "http://localhost:11434/api/generate"
DEFAULT_MODEL = "qwen3:4b"  # This should be consistent with the model set in the client

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"]
)


@app.get("/")
async def root():
    return {"message": "Local Backend is running. Access the client via index.html."}


@app.post("/generate_prompt")
async def generate_prompt_and_response_endpoint(request: Request):
    """
    Step 1: Get Encapsulated Prompt from Remote Server.
    Step 2: Send Encapsulated Prompt to Local LLM (Ollama).
    Step 3: Return final response to the client.
    """
    try:
        body = await request.json()
        probe: str = body.get("probe", "")
        truth: bool = body.get("truth", False)
        model: str = body.get("model", DEFAULT_MODEL)

        # --- STEP 1: Get Encapsulated Prompt from Remote Server ---

        # Send the raw user text and polarity state to your remote server.
        remote_payload = {
            "probe": probe,
            "truth": truth
        }

        # Use synchronous requests for simplicity in this example
        remote_response = requests.post(PROMPT_ENCODE_ENDPOINT, json=remote_payload)
        remote_response.raise_for_status()  # Raise exception for bad status codes

        # Expecting JSON: {"formatted_prompt": "..."}
        remote_data = remote_response.json()
        encapsulated_prompt = remote_data.get("formatted_prompt")

        if not encapsulated_prompt:
            raise ValueError("Remote server failed to return a formatted prompt.")

        # --- STEP 2: Send Encapsulated Prompt to Local LLM ---

        local_llm_payload = {
            "model": model,
            "prompt": encapsulated_prompt,
            "stream": False  # We want the full response at once
        }

        local_llm_response = requests.post(LOCAL_MODEL_ENDPOINT, json=local_llm_payload)
        local_llm_response.raise_for_status()  # Raise exception for bad status codes

        # Assuming Ollama non-streaming response format
        local_llm_data = local_llm_response.json()
        final_response_text = local_llm_data.get("response", "[ERROR: Local LLM response missing 'response' field.]")

        # --- STEP 3: Return final response to the client ---

        # The client expects the final response text back under the 'response' key
        return JSONResponse({"response": final_response_text})

    except requests.exceptions.RequestException as e:
        error_message = f"[ERROR: Network or API failure. Check your Ollama server or Render URL. Details: {e}]"
        return JSONResponse({"response": error_message}, status_code=500)
    except ValueError as e:
        return JSONResponse({"response": str(e)}, status_code=500)
    except Exception as e:
        return JSONResponse({"response": f"[FATAL ERROR: {str(e)}]"}, status_code=500)


@app.options("/generate_prompt")
async def options():
    return {}


if __name__ == "__main__":
    # The local backend runs on port 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)
