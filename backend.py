import os
import requests
import re
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json

RENDER_SERVER_URL = "https://researchnexus.onrender.com"
PROMPT_ENCODE_ENDPOINT = f"{RENDER_SERVER_URL}/generate_prompt"
LOCAL_MODEL_ENDPOINT = "http://localhost:11434/api/generate"
DEFAULT_MODEL = "qwen3:4b"

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"]
)

def clean_text(text: str) -> str:
    text = re.sub(r'[\U0001F300-\U0001F9FF]|[\u2600-\u26FF]|[\u2700-\u27BF]', '', text)
    text = re.sub(r'\*+', '', text)
    text = re.sub(r'#+\s*', '', text)
    text = re.sub(r'\\n', ' ', text)
    text = re.sub(r'\bn\s', ' ', text)
    text = re.sub(r'-{2,}', '', text)
    text = re.sub(r'\|', '', text)
    text = re.sub(r'\s{2,}', ' ', text)
    return text.strip()

@app.get("/")
async def root():
    return {"message": "Local Backend is running. Access the client via index.html."}

@app.post("/generate_prompt")
async def generate_prompt_and_response_endpoint(request: Request):
    try:
        body = await request.json()
        probe: str = body.get("probe", "")
        truth: bool = body.get("truth", False)
        model: str = body.get("model", DEFAULT_MODEL)

        remote_payload = {"probe": probe, "truth": truth}
        remote_response = requests.post(PROMPT_ENCODE_ENDPOINT, json=remote_payload)
        remote_response.raise_for_status()
        remote_data = remote_response.json()
        encapsulated_prompt = remote_data.get("formatted_prompt")
        
        if not encapsulated_prompt:
            raise ValueError("Remote server failed to return a formatted prompt.")

        local_llm_payload = {
            "model": model,
            "prompt": encapsulated_prompt,
            "stream": False
        }
        local_llm_response = requests.post(LOCAL_MODEL_ENDPOINT, json=local_llm_payload)
        local_llm_response.raise_for_status()
        local_llm_data = local_llm_response.json()
        final_response_text = local_llm_data.get("response", "[ERROR: Local LLM response missing 'response' field.]")

        cleaned_response = clean_text(final_response_text)
        return JSONResponse({"response": cleaned_response})

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
    uvicorn.run(app, host="0.0.0.0", port=8000)
