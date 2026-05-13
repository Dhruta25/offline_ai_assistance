from pydantic import BaseModel


class PromptRequest(BaseModel):
    prompt: str
    model: str = "llama3.2:3b"
    temperature: float = 0.0