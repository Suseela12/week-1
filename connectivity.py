from google.colab import userdata
from google import genai
import time

try:
    # Load API key
    api_key = userdata.get("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY not found.")

    print("✅ Environment ready. Sending prompt...")

    # Initialize Gemini client
    client = genai.Client(api_key=api_key)

    # First prompt
    prompt = "What is prompt engineering? Answer in one sentence."

    print("\nPrompt:")
    print(prompt)

    # Generate response with retry
    for attempt in range(5):
        try:
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt
            )

            print("\nResponse:")
            print(response.text)
            break

        except Exception as e:
            if "503" in str(e) and attempt < 4:
                print("Server busy. Retrying...")
                time.sleep(10)
            else:
                raise e

    # Second prompt: optional connectivity test
    second_prompt = "Explain AI in one sentence."

    print("\nSecond prompt:")
    print(second_prompt)

    response2 = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=second_prompt
    )

    print("\nSecond response:")
    print(response2.text)

except ValueError as e:
    print("❌ Configuration Error:", e)

except Exception as e:
    print("❌ Gemini API/Network Error:", e)
