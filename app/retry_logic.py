from ollama_client import generate_response


def generate_with_retry(
    prompt,
    retries=3
):

    for attempt in range(retries):

        try:

            response = generate_response(prompt)

            if response and len(response.strip()) > 0:
                return response

        except Exception as error:

            print(f"Attempt {attempt + 1} failed")
            print(error)

    return "Failed to generate response after retries."