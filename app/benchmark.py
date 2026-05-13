import time
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def benchmark_model(
    prompt,
    model="llama3.2:3b"
):

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    print("\nRunning benchmark...\n")

    start_time = time.time()

    response = requests.post(
        OLLAMA_URL,
        json=payload
    )

    end_time = time.time()

    data = response.json()

    answer = data["response"]

    # total latency
    latency = end_time - start_time

    # approximate token count
    tokens = len(answer.split())

    # tokens/sec
    tokens_per_sec = tokens / latency

    print("===== BENCHMARK RESULTS =====")
    print(f"Model: {model}")
    print(f"Latency: {latency:.2f} sec")
    print(f"Tokens Generated: {tokens}")
    print(f"Tokens/sec: {tokens_per_sec:.2f}")
    print("\n===== RESPONSE =====\n")
    print(answer)


if __name__ == "__main__":

    benchmark_model(
        prompt="Explain machine learning in simple terms."
    )