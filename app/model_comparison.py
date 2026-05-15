import time
import json
import requests
import psutil
import pandas as pd

OLLAMA_URL = "http://localhost:11434/api/generate"

MODELS = [
    "llama3.2:3b",
    "phi3:mini"
]


def benchmark_model(model, prompt):

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": True
    }

    cpu_before = psutil.cpu_percent()

    ram_before = psutil.virtual_memory().percent

    start_time = time.time()

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        stream=True
    )

    first_token_time = None

    token_count = 0

    full_response = ""

    for line in response.iter_lines():

        if line:

            current_time = time.time()

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

    total_latency = end_time - start_time

    ttft = first_token_time - start_time

    tokens_per_sec = token_count / total_latency

    cpu_after = psutil.cpu_percent()

    ram_after = psutil.virtual_memory().percent

    return {
        "model": model,
        "prompt": prompt,
        "latency": round(total_latency, 2),
        "ttft": round(ttft, 2),
        "tokens_per_sec": round(tokens_per_sec, 2),
        "cpu_before": cpu_before,
        "cpu_after": cpu_after,
        "ram_before": ram_before,
        "ram_after": ram_after,
        "response_length": len(full_response.split())
    }


def load_prompts():

    with open("test_prompts/prompts.txt", "r") as file:

        prompts = file.readlines()

    return [p.strip() for p in prompts if p.strip()]


def run_comparison():

    prompts = load_prompts()

    results = []

    for model in MODELS:

        print(f"\n===== Testing {model} =====\n")

        for prompt in prompts:

            print(f"Running Prompt: {prompt}")

            result = benchmark_model(model, prompt)

            results.append(result)

    df = pd.DataFrame(results)

    df.to_csv("results/model_comparison.csv", index=False)

    print("\nResults saved to results/model_comparison.csv")


if __name__ == "__main__":

    run_comparison()