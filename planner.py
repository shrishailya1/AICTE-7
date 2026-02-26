import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

def generate_itinerary(destinations, days, budget, preferences):

    url = "https://openrouter.ai/api/v1/chat/completions"

    prompt = f"""
    You are a smart AI travel planner.

    Plan a {days}-day trip for:
    {", ".join(destinations)}

    Budget: ₹{budget}
    Preferences: {preferences}

    Provide:
    - Day-wise itinerary (Day 1 to Day {days})
    - Budget-friendly suggestions
    - Travel between cities
    - Food and attractions
    """

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=data)

        print("Status:", response.status_code)
        print("Response:", response.text)

        if response.status_code != 200:
            return f"❌ API Error:\n{response.text}"

        result = response.json()

        return result['choices'][0]['message']['content']

    except Exception as e:
        return f"Error: {e}"