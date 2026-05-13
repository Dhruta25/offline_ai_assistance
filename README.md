# Local Offline AI Assistant

A local AI assistant backend built using Ollama, FastAPI, and open-source Large Language Models (LLMs).  
This project focuses on running AI models completely offline while exploring concepts like local inference, backend integration, benchmarking, and reliable AI system design.

---

# Project Objective

The goal of this project is to:

- Run open-source LLMs locally using Ollama
- Build a FastAPI backend for AI interaction
- Benchmark inference performance
- Explore model reliability and structured AI workflows
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
- Added retry mechanism for failed generations
- Implemented basic benchmarking support

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

- llama3.2:3b

Future planned models:

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
  "prompt": "Explain machine learning",
  "model": "llama3.2:3b",
  "temperature": 0.2
}
```

---

### Response

```json
{
  "prompt": "Explain machine learning",
  "response": "Machine learning is a branch of AI...",
  "model": "llama3.2:3b"
}
```

---

# Benchmarking

Current benchmark system measures:

- Total Latency
- Approximate Tokens/sec

Future benchmarking improvements:

- TTFT (Time To First Token)
- CPU Usage
- RAM Usage
- Multi-model comparison
- CSV result logging
- Quantized model evaluation

---

# Retry Logic

The project includes retry handling for failed or invalid model generations.

Purpose:
- improve reliability
- handle temporary inference failures
- avoid empty or invalid responses

---

# Current Status

Completed:
- Local LLM setup
- FastAPI backend
- Ollama integration
- Modular architecture
- Basic benchmarking
- Retry mechanism

In Progress:
- Advanced benchmarking system
- Structured JSON output validation
- Multi-model comparison study
- Quantized model benchmarking

---

# Future Improvements

- Streaming responses
- Structured JSON generation
- Pydantic output validation
- Advanced benchmark metrics
- CSV export support
- Benchmark visualization graphs
- Docker deployment
- Frontend integration

---

# Learning Outcomes

This project explores:

- Local LLM inference
- AI backend engineering
- FastAPI development
- AI benchmarking
- Reliability engineering
- Modular backend architecture
- Offline AI systems

---

# Author

Dhrutabrata Biswal