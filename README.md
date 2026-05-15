# Local Offline AI Assistant

A local AI assistant backend built using Ollama, FastAPI, and open-source Large Language Models (LLMs).  
This project focuses on running AI models completely offline while exploring concepts like local inference, backend integration, benchmarking, structured output validation, and reliable AI system design.

---

# Project Objective

The goal of this project is to:

- Run open-source LLMs locally using Ollama
- Build a FastAPI backend for AI interaction
- Benchmark inference performance
- Enforce structured JSON outputs
- Validate AI responses using Pydantic
- Implement retry mechanisms for robust AI pipelines
- Understand real-world AI infrastructure concepts

---

# Features Implemented

## Phase 1 — Setup & Local Inference

- Installed and configured Ollama locally
- Pulled and ran local LLMs
- Connected Python backend with Ollama API
- Successfully generated local AI responses

---

## Phase 2 — Backend Integration

- Built FastAPI backend server
- Created `/chat` API endpoint
- Added modular project structure
- Implemented reusable Ollama client
- Added request validation using Pydantic
- Implemented retry mechanism for failed generations

---

## Phase 3 — Advanced Benchmarking

Implemented advanced benchmarking system with:

- Total Latency Measurement
- TTFT (Time To First Token)
- Tokens/sec calculation
- CPU Usage Monitoring
- RAM Usage Monitoring
- Streaming token generation support

---

## Phase 4 — Structured Output Validation

Implemented structured AI response pipeline using:

- JSON-based LLM outputs
- Pydantic response validation
- Retry mechanism for invalid outputs
- Strict schema enforcement
- Robust structured AI workflow

---

# Tech Stack

- Python 3.13
- FastAPI
- Ollama
- Pydantic
- Requests
- Uvicorn
- psutil

---

# Models Used

Current:

- llama3.2:3b

Planned:

- Phi-3 Mini
- Mistral 7B
- Quantized GGUF models

---

# Project Architecture

```text
User
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
```

---

# Project Structure

```text
offline_ai_assistance/

├── app/
│   ├── main.py
│   ├── ollama_client.py
│   ├── benchmark.py
│   ├── schemas.py
│   ├── retry_logic.py
│   └── prompts.py
│
├── reports/
├── results/
├── screenshots/
├── test_prompts/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Setup Instructions

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

### Mac/Linux

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

Download and install Ollama:

https://ollama.com/download

---

## 6. Pull Model

```bash
ollama pull llama3.2:3b
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

After starting FastAPI, open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI documentation will be available there.

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

### Structured Response

```json
{
  "topic": "Machine Learning",
  "summary": "Machine learning is a branch of AI that enables systems to learn from data.",
  "confidence": 0.94
}
```

---

# Benchmarking Metrics

Current benchmarking system measures:

- Total Latency
- TTFT (Time To First Token)
- Tokens/sec
- CPU Usage
- RAM Usage

Future benchmarking improvements:

- CSV result logging
- Multi-model comparison
- Quantized model benchmarking
- Benchmark graphs and visualizations

---

# Retry Logic & Validation

The project includes:

- Automatic retry handling
- Structured JSON validation
- Pydantic schema enforcement
- Error handling for invalid responses

Purpose:
- improve reliability
- avoid malformed outputs
- simulate production AI pipelines

---

# Current Status

Completed:
- Local LLM setup
- FastAPI backend
- Ollama integration
- Modular architecture
- Advanced benchmarking
- Structured JSON generation
- Pydantic validation
- Retry mechanism

In Progress:
- Temperature experiments
- Multi-model comparison study
- Quantized model benchmarking
- Benchmark result storage
- Technical report generation

---

# Future Improvements

- Temperature analysis experiments
- Multiple LLM comparison
- CSV benchmark export
- Graph visualization
- Quantized model evaluation
- Docker deployment
- Frontend integration
- Technical report automation

---

# Learning Outcomes

This project explores:

- Local LLM inference
- AI backend engineering
- FastAPI development
- AI benchmarking
- Structured AI pipelines
- Reliability engineering
- Offline AI systems
- Production-style AI validation

---

# Author

Dhrutabrata Biswal

