from ollama_client import generate_response

TEMPERATURES = [0.0, 0.5, 0.7, 1.0]

PROMPT ="Suggest me best AI startup ideas 2 ideas maximum in shortly"
def run_temperature_experiment():

    print("\n===== TEMPERATURE EXPERIMENT =====\n")

    for temp in TEMPERATURES:

        print(f"\n===== Temperature: {temp} =====\n")

        response = generate_response(

            prompt=PROMPT,

            temperature=temp

        )

        print(response)

        print("\n" + "=" * 60 + "\n")

if __name__ == "__main__":

    run_temperature_experiment()