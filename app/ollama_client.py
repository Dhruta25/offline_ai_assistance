import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def generate_response(
    prompt,
    model="llama3.2:3b",
    temperature=0.0,
    stream=False
):
    """
    Sends prompt to local Ollama model
    and returns generated response.
    """

    payload = {
        "model": model,
        "prompt": prompt,
        "temperature": temperature,
        "stream": stream
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload
    )

    response.raise_for_status()

    data = response.json()

    return data["response"]