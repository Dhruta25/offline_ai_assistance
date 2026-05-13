from fastapi import FastAPI
from app.schemas import PromptRequest
from app.ollama_client import generate_response

app = FastAPI(
    title="Offline AI Assistant",
    description="Local LLM API using Ollama",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "Offline AI Assistant Running"
    }


@app.post("/chat")
def chat(request: PromptRequest):

    answer = generate_response(
        prompt=request.prompt,
        model=request.model,
        temperature=request.temperature
    )

    return {
        "prompt": request.prompt,
        "response": answer,
        "model": request.model
    }