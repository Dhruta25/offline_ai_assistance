import time
import json
import requests
import psutil

OLLAMA_URL = "http://localhost:11434/api/generate"


def benchmark_model(
    prompt,
    model="llama3.2:3b"
):

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": True
    }

    print("\nRunning Advanced Benchmark...\n")

    # CPU usage before inference
    cpu_before = psutil.cpu_percent()

    # RAM usage before inference
    ram_before = psutil.virtual_memory().percent

    start_time = time.time()

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        stream=True
    )

    first_token_time = None

    full_response = ""

    token_count = 0

    # stream token-by-token
    for line in response.iter_lines():

        if line:

            current_time = time.time()

            # first token timing
            if first_token_time is None:
                first_token_time = current_time

            decoded_line = line.decode("utf-8")

            try:
                data = json.loads(decoded_line)

                token = data.get("response", "")

                full_response += token

                token_count += 1

            except json.JSONDecodeError:
                pass

    end_time = time.time()

    # final metrics
    total_latency = end_time - start_time

    ttft = first_token_time - start_time

    tokens_per_sec = token_count / total_latency

    # CPU usage after inference
    cpu_after = psutil.cpu_percent()

    # RAM usage after inference
    ram_after = psutil.virtual_memory().percent

    print("===== ADVANCED BENCHMARK RESULTS =====\n")

    print(f"Model: {model}")

    print(f"\nTotal Latency: {total_latency:.2f} sec")

    print(f"TTFT (Time To First Token): {ttft:.2f} sec")

    print(f"Tokens Generated: {token_count}")

    print(f"Tokens/sec: {tokens_per_sec:.2f}")

    print(f"\nCPU Before: {cpu_before}%")
    print(f"CPU After: {cpu_after}%")

    print(f"\nRAM Before: {ram_before}%")
    print(f"RAM After: {ram_after}%")

    print("\n===== GENERATED RESPONSE =====\n")

    print(full_response)


if __name__ == "__main__":

    benchmark_model(
        prompt="Explain artificial intelligence in simple terms."
    )