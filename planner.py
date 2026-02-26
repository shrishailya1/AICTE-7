import requests
import os
import re
from dotenv import load_dotenv


load_dotenv(dotenv_path=".env")

API_KEY = os.getenv("OPENROUTER_API_KEY")
print("Loaded API KEY:", API_KEY) 

# CLEAN TEXT FUNCTION

def clean_text(text):
    """
    Removes markdown symbols like ** and __
    """
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"__(.*?)__", r"\1", text)
    return text.strip()

# MAIN ITINERARY GENERATOR

def generate_itinerary(boarding_point, destinations, days, budget, preferences, optimize_budget):

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:3000",
        "X-Title": "Test"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": "Say hello"}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    print("Status Code:", response.status_code)
    print("Raw Response:", response.text)

    return response.text

