SYSTEM_PROMPT = """
You are a helpful AI assistant.
Answer clearly and concisely.
"""

JSON_PROMPT = JSON_PROMPT_TEMPLATE = """
You are an AI assistant.

Respond ONLY in valid JSON format.

The JSON must follow this schema:

{
    "topic": "topic name",
    "summary": "short explanation",
    "confidence": 0.95
}

Question:
{user_prompt}
"""
BENCHMARK_PROMPT = """
Explain artificial intelligence in simple terms.
"""