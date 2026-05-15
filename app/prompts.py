JSON_PROMPT_TEMPLATE = """
You are an AI assistant.

Respond ONLY in valid JSON format.

The JSON must follow this schema:

{{
    "topic": "topic name",
    "summary": "short explanation",
    "confidence": 0.95
}}

Question:
{user_prompt}
"""