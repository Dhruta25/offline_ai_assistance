# Benchmark Report — Local Offline AI Assistant

## Project Overview

This project explores local offline Large Language Models (LLMs) using Ollama and FastAPI on Apple Silicon hardware (MacBook Air M2).  

The goal of the project was to:

- Run open-source LLMs locally
- Build a FastAPI-based AI backend
- Benchmark inference performance
- Compare multiple LLMs under identical hardware conditions
- Analyze tradeoffs between speed, quality, and resource usage
- Implement structured AI engineering workflows

---

# System Architecture

The following architecture was implemented for local AI inference:

```text
User Prompt
     ↓
FastAPI Backend
     ↓
Retry + Validation Layer
     ↓
Ollama Client
     ↓
Ollama Local API
     ↓
Local LLM
     ↓
Generated Response
```

---

# Hardware Configuration

| Component | Details |
|---|---|
| Device | MacBook Air M2 |
| RAM | 16 GB Unified Memory |
| Operating System | macOS |
| Python Version | Python 3.13 |

---

# Models Evaluated

| Model | Description |
|---|---|
| llama3.2:3b | Balanced reasoning-focused model |
| phi3:mini | Lightweight and speed-optimized model |

---

# Benchmarking Metrics

The following metrics were measured during inference:

| Metric | Description |
|---|---|
| Latency | Total response generation time |
| TTFT | Time To First Token |
| Tokens/sec | Token generation speed |
| CPU Usage | CPU utilization during inference |
| RAM Usage | Memory utilization during inference |
| Response Length | Number of generated words/tokens |

---

# Benchmark Methodology

- All models were evaluated on identical hardware.
- The same prompts were used for both models.
- Streaming inference was enabled.
- Metrics were collected programmatically using Python and `psutil`.
- Ollama was used as the local inference engine.

---

# Test Prompts

The following prompts were used:

1. Explain machine learning simply.
2. What is recursion in programming?
3. Write a short summary of artificial intelligence.
4. Suggest an AI startup idea.
5. Explain neural networks.

---

# Raw Benchmark Results

| Model | Prompt | Latency (s) | TTFT (s) | Tokens/sec | RAM After (%) | Response Length |
|---|---|---|---|---|---|---|
| Llama 3.2 3B | Machine Learning | 10.42 | 2.85 | 28.04 | 90.4 | 240 |
| Llama 3.2 3B | Recursion | 12.86 | 0.21 | 38.32 | 88.7 | 379 |
| Llama 3.2 3B | AI Summary | 8.18 | 0.21 | 38.14 | 89.3 | 242 |
| Llama 3.2 3B | Startup Idea | 12.68 | 0.21 | 38.32 | 88.9 | 346 |
| Llama 3.2 3B | Neural Networks | 16.80 | 0.20 | 38.34 | 89.0 | 461 |
| Phi-3 Mini | Machine Learning | 5.76 | 2.72 | 19.95 | 92.2 | 88 |
| Phi-3 Mini | Recursion | 4.56 | 0.14 | 35.52 | 92.6 | 123 |
| Phi-3 Mini | AI Summary | 5.92 | 0.16 | 35.65 | 91.6 | 153 |
| Phi-3 Mini | Startup Idea | 11.32 | 0.15 | 36.48 | 91.6 | 281 |
| Phi-3 Mini | Neural Networks | 20.18 | 0.14 | 35.09 | 91.4 | 555 |

---

# Average Performance Comparison

## Llama 3.2 3B

| Metric | Average |
|---|---|
| Average Latency | 12.19 sec |
| Average TTFT | 0.74 sec |
| Average Tokens/sec | 36.23 |
| Average RAM Usage | ~89% |
| Average Response Length | 333 words |

---

## Phi-3 Mini

| Metric | Average |
|---|---|
| Average Latency | 9.54 sec |
| Average TTFT | 0.66 sec |
| Average Tokens/sec | 32.54 |
| Average RAM Usage | ~92% |
| Average Response Length | 240 words |

---

# Observations & Analysis

## 1. Latency Comparison

Phi-3 Mini demonstrated lower overall latency for most prompts.  
This indicates that Phi-3 Mini is better optimized for fast local inference on lightweight hardware.

However, for more detailed prompts such as neural network explanations, Phi-3 Mini occasionally produced higher latency due to longer outputs.

---

## 2. Response Quality & Detail

Llama 3.2 3B consistently generated:

- more structured explanations
- deeper reasoning
- longer responses
- better educational formatting

The average response length for Llama was significantly larger than Phi-3 Mini.

This suggests that Llama prioritizes explanation quality over speed.

---

## 3. Tokens/sec Performance

Llama achieved slightly higher token generation speed during most tasks.

This indicates efficient streaming generation despite its larger reasoning complexity.

---

## 4. TTFT (Time To First Token)

Both models showed low TTFT values.

Phi-3 Mini achieved slightly faster response initiation in most cases, improving perceived responsiveness.

---

## 5. Memory Usage

Both models consumed high RAM due to local inference on Apple Silicon hardware.

However:

- Phi-3 Mini generally consumed slightly higher RAM percentages during execution.
- Llama maintained more stable memory behavior.

---

# Tradeoff Analysis

The benchmark experiments revealed a clear tradeoff:

```text
Speed vs Quality vs Resource Usage
```

| Category | Better Model |
|---|---|
| Faster Inference | Phi-3 Mini |
| Better Explanations | Llama 3.2 3B |
| More Detailed Responses | Llama 3.2 3B |
| Lower Latency | Phi-3 Mini |
| Better Educational Output | Llama 3.2 3B |
| Lightweight Usage | Phi-3 Mini |

---

# Temperature Experiment Findings

Temperature-based experiments showed:

| Temperature | Behavior |
|---|---|
| 0.0 | Deterministic and consistent outputs |
| 0.3 | Balanced responses |
| 0.7 | More creative outputs |
| 1.0 | Highly random and less stable outputs |

Low temperature settings were found to be more suitable for structured JSON generation and deterministic AI pipelines.

---

# Reliability Engineering Features

The system also implemented:

- Retry mechanisms
- Structured JSON generation
- Pydantic validation
- Streaming inference
- Benchmark automation

These features improved reliability and simulated production-style AI backend workflows.

---

# Conclusion

This project successfully demonstrated the deployment and benchmarking of local offline LLMs using Ollama and FastAPI.

Key findings include:

- Phi-3 Mini performs better for lightweight, low-latency inference tasks.
- Llama 3.2 3B generates higher quality and more detailed responses.
- There is no universally “best” model; practical usage depends on the tradeoff between:
  - speed
  - quality
  - resource consumption

The project highlights important AI systems engineering concepts including:

- local inference
- benchmarking
- structured validation
- reliability engineering
- model tradeoff analysis

---

# Future Improvements

Future work may include:

- Quantized GGUF model comparison
- GPU benchmarking
- Graph-based result visualization
- Docker deployment
- Multi-user API serving
- Automated quality scoring
- Frontend integration

---

# Author

Dhrutabrata Biswal
National Institute of Technology, Rourkela