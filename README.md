# Local Offline AI Assistant

A production-style local AI assistant backend built using Ollama, FastAPI, and open-source Large Language Models (LLMs).  

This project focuses on running AI models completely offline while exploring important AI engineering concepts such as:

- Local LLM inference
- AI backend development
- Streaming generation
- Benchmarking & performance evaluation
- Structured JSON generation
- Pydantic validation
- Retry-based reliability engineering
- Multi-model comparison
- Temperature-based stochasticity analysis

The entire system was developed and benchmarked on Apple Silicon hardware (MacBook Air M2).

---

# Project Objective

The primary goals of this project were to:

- Run open-source LLMs locally without cloud dependency
- Build a FastAPI-based AI backend
- Benchmark local inference performance
- Compare multiple LLMs on identical hardware
- Analyze tradeoffs between:
  - speed
  - response quality
  - memory usage
  - latency
- Implement production-style structured AI pipelines
- Understand real-world AI systems engineering concepts

---

# Features Implemented

## Phase 1 — Local LLM Setup

- Installed and configured Ollama locally
- Pulled open-source LLMs
- Ran local inference completely offline
- Connected Python backend with Ollama API
- Verified successful local response generation

---

## Phase 2 — FastAPI Backend Development

Built a modular FastAPI backend for local AI interaction.

### Implemented Features

- FastAPI server setup
- `/chat` API endpoint
- Request validation using Pydantic
- Reusable Ollama client
- Modular backend architecture
- Swagger API documentation

---

## Phase 3 — Advanced Benchmarking System

Implemented a full benchmarking pipeline for local LLM evaluation.

### Metrics Measured

- Total Latency
- TTFT (Time To First Token)
- Tokens/sec
- CPU Usage
- RAM Usage
- Response Length

### Additional Features

- Streaming inference support
- Automated benchmark execution
- CSV result generation
- Multi-prompt testing pipeline

---

## Phase 4 — Structured Output Validation

Implemented structured AI response workflows.

### Features

- JSON-only AI responses
- Pydantic schema validation
- Structured response enforcement
- Automatic retry mechanism
- Reliability-focused inference pipeline

### Example Structured Response

```json
{
  "topic": "Machine Learning",
  "summary": "Machine learning is a branch of AI that enables systems to learn from data.",
  "confidence": 0.94
}
```

---

## Phase 5 — Temperature Experiments

Implemented temperature-based stochasticity experiments to analyze model behavior.

### Temperature Settings Tested

- 0.0
- 0.3
- 0.7
- 1.0

### Key Findings

| Temperature | Behavior |
|---|---|
| 0.0 | Deterministic and stable |
| 0.3 | Balanced generation |
| 0.7 | Creative outputs |
| 1.0 | Highly random outputs |

These experiments demonstrated how temperature affects:
- creativity
- randomness
- output consistency
- structured generation stability

---

## Phase 6 — Multi-Model Benchmark Comparison

Implemented comparative evaluation between multiple local LLMs.

### Models Compared

| Model | Purpose |
|---|---|
| llama3.2:3b | Balanced reasoning-focused model |
| phi3:mini | Lightweight low-latency model |

### Benchmark Workflow

- Same prompts
- Same hardware
- Same inference conditions
- Automated metric collection

### Comparison Goals

- Speed evaluation
- Response quality analysis
- Memory efficiency comparison
- Tradeoff analysis

---

# System Architecture

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

# Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.13 | Core backend language |
| FastAPI | API framework |
| Ollama | Local LLM serving |
| Pydantic | Schema validation |
| Requests | HTTP communication |
| psutil | System resource monitoring |
| Pandas | Benchmark data processing |
| Uvicorn | FastAPI ASGI server |

---

# Hardware Configuration

| Component | Details |
|---|---|
| Device | MacBook Air M2 |
| RAM | 16 GB Unified Memory |
| OS | macOS |
| Python Version | Python 3.13 |

---

# Project Structure

```text
offline_ai_assistance/

├── app/
│   ├── main.py
│   ├── ollama_client.py
│   ├── benchmark.py
│   ├── model_comparison.py
│   ├── temperature_experiment.py
│   ├── retry_logic.py
│   ├── prompts.py
│   └── schemas.py
│
├── results/
│   └── model_comparison.csv
│
├── reports/
│   └── benchmark_report.md
│
├── test_prompts/
│   └── prompts.txt
│
├── screenshots/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/Dhruta25/offline_ai_assistance.git
cd offline_ai_assistance
```

---

## 2. Create Virtual Environment

```bash
python3 -m venv venv
```

---

## 3. Activate Virtual Environment

### macOS/Linux

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Install Ollama

Download Ollama:

https://ollama.com/download

---

## 6. Pull Models

```bash
ollama pull llama3.2:3b
ollama pull phi3:mini
```

---

## 7. Start Ollama Server

```bash
ollama serve
```

---

## 8. Run FastAPI Server

```bash
uvicorn app.main:app --reload
```

---

# API Documentation

After running FastAPI, open:

```text
http://127.0.0.1:8000/docs
```

Interactive Swagger documentation will be available.

---

# Example API Request

## POST `/chat`

### Request

```json
{
  "prompt": "Explain machine learning"
}
```

---

### Response

```json
{
  "topic": "Machine Learning",
  "summary": "Machine learning enables systems to learn from data.",
  "confidence": 0.93
}
```

---

# Benchmarking Results Summary

## Llama 3.2 3B

| Metric | Observation |
|---|---|
| Better reasoning | Yes |
| Longer responses | Yes |
| Higher latency | Yes |
| More detailed explanations | Yes |

---

## Phi-3 Mini

| Metric | Observation |
|---|---|
| Faster inference | Yes |
| Lower latency | Yes |
| Lightweight behavior | Yes |
| Shorter responses | Yes |

---

# Key Insights

The experiments revealed important tradeoffs between:

```text
Speed ↔ Quality ↔ Resource Usage
```

### Observations

- Phi-3 Mini performed better for low-latency local inference.
- Llama 3.2 generated more detailed and structured explanations.
- Smaller models are faster but may sacrifice reasoning depth.
- Larger models improve response quality at the cost of computation time.

---

# Reliability Engineering Features

The system includes:

- Retry handling
- Structured validation
- JSON enforcement
- Streaming inference
- Automated benchmarking
- Modular architecture

These features simulate real-world production AI backend systems.

---

# Learning Outcomes

This project helped explore:

- Local LLM deployment
- FastAPI backend engineering
- AI inference pipelines
- LLM benchmarking
- Structured AI workflows
- Reliability engineering
- Stochastic generation behavior
- Multi-model evaluation
- Performance tradeoff analysis

---

# Future Improvements

Potential future upgrades include:

- Quantized GGUF model benchmarking
- GPU benchmarking support
- Docker deployment
- Frontend integration
- Graph-based benchmark visualization
- Automated quality scoring
- Multi-user API serving
- Distributed inference benchmarking

---

# Author

Dhrutabrata Biswal
National Institute of Technology, Rourkela
```