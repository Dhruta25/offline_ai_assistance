import json

from app.ollama_client import generate_response
from app.prompts import JSON_PROMPT_TEMPLATE
from app.schemas import AIResponseSchema


def generate_validated_response(
    user_prompt,
    retries=3
):

    formatted_prompt = JSON_PROMPT_TEMPLATE.format(
        user_prompt=user_prompt
    )

    for attempt in range(retries):

        try:

            response = generate_response(formatted_prompt)

            parsed_json = json.loads(response)

            validated_data = AIResponseSchema(**parsed_json)

            return validated_data.model_dump()

        except Exception as error:

            print(f"\nAttempt {attempt + 1} failed")
            print(error)

    return {
        "error": "Failed to generate valid structured response"
    }