
import google.generativeai as genai
import requests


class GeminiProvider:

    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def generate(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text


class OllamaProvider:

    def __init__(self, model_name="llama3.2"):
        self.model_name = model_name
        self.url = "http://localhost:11434/api/generate"

    def generate(self, prompt):
        response = requests.post(
            self.url,
            json={
                "model": self.model_name,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        response.raise_for_status()
        return response.json()["response"]


class LLMClient:

    def __init__(self, provider):
        self.provider = provider

    def generate(self, prompt):
        return self.provider.generate(prompt)