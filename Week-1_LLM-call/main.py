
import os
from dotenv import load_dotenv
from google import genai

# Step 1: Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Step 2: Initialize Gemini client
client = genai.Client(api_key=api_key)

print("Connecting to Gemini...")
print("Waiting for response...\n")

try:
    # Step 3: Send request to Gemini
    stream = client.interactions.create(
        model="gemini-3.8-flash",
        input="Explain Artificial Intelligence in simple words.",
        stream=True
    )

    print("Gemini Response:\n")

    # Step 4: Receive streamed response
    for event in stream:
        if event.event_type == "step.delta":
            if event.delta.type == "text":
                print(event.delta.text, end="", flush=True)

    print("\n\nResponse completed!")

except Exception as e:
    print("\nGEMINI API ERROR:")
    print(type(e).__name__)
    print(str(e))