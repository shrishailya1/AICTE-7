import requests
import os
import re
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")


def clean_text(text):
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"__(.*?)__", r"\1", text)
    return text


def generate_itinerary(boarding_point, destinations, days, budget, preferences, optimize_budget):

    url = "https://openrouter.ai/api/v1/chat/completions"

    optimization_rules = ""
    if optimize_budget:
        optimization_rules = """
STRICT BUDGET MODE:
- Prefer trains (Sleeper/3AC) instead of flights.
- Prefer buses over taxis.
- Hotels must be under ₹1200 per night.
- Suggest hostels if needed.
- Prefer metro/local transport.
- Suggest street food/local eateries.
"""

    prompt = f"""
You are a professional travel planner.

Create a detailed {days}-day itinerary.

Boarding City: {boarding_point}
Destinations: {", ".join(destinations)}
Total Budget: ₹{budget}
Preferences: {preferences}

{optimization_rules}

Rules:
1. Total cost must NOT exceed ₹{budget}.
2. Provide daily Morning, Afternoon, Evening plan.
3. Provide daily approximate cost.
4. Provide full cost breakdown at end.
5. Do NOT use markdown symbols like ** or __.
6. Use plain text formatting only.

Format:

Day X - City Name

Morning:
- Activity

Afternoon:
- Activity

Evening:
- Activity

Daily Approximate Cost: ₹____

After all days:

TOTAL COST BREAKDOWN:
Transport:
Stay:
Food:
Attractions:
Final Estimated Total Cost: ₹____
"""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:3000",
        "X-Title": "AI Travel Planner"
    }

    data = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.6
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        return f"API Error: {response.text}"

    result = response.json()
    itinerary = result["choices"][0]["message"]["content"]

    return clean_text(itinerary)
