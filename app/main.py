from fastapi import FastAPI

from app.schemas import PromptRequest
from app.retry_logic import generate_validated_response

app = FastAPI(
    title="Offline AI Assistant",
    version="2.0"
)


@app.get("/")
def home():

    return {
        "message": "Offline AI Assistant Running"
    }


@app.post("/chat")
def chat(request: PromptRequest):

    result = generate_validated_response(
        request.prompt
    )

    return result