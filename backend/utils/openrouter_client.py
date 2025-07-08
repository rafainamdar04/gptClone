import requests
import os
from dotenv import load_dotenv

load_dotenv()

def call_openrouter(messages):
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",  # more stable, try this first
        "messages": messages
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=data, headers=headers)

    print("STATUS:", response.status_code)
    print("RESPONSE TEXT:", response.text)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        # Try to extract error message from response
        try:
            return f"OpenRouter Error: {response.json().get('error', 'Unknown error')}"
        except Exception:
            return "OpenRouter Error: Unable to decode response"
