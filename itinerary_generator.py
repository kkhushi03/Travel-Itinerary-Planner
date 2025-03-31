import streamlit as st
import requests  # Use requests instead of openai

# Load API key securely from Streamlit secrets
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

# Correct API URL for Groq
GROQ_API_URL = "https://api.groq.com/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

def generate_itinerary(user_details):
    """Generates a personalized travel itinerary using Groq API."""
    
    prompt = f"""
    Generate a {user_details['trip_duration']}-day travel itinerary for {user_details['destination']} 
    based on these details:
    - Budget: {user_details['budget']}
    - Interests: {user_details['preferences']}
    - Suggested Attractions: {', '.join(user_details['attractions'])}

    Ensure a mix of activities per day, proper timing, and logical grouping of activities.
    """

    payload = {
        "model": "llama3-8b-8192",  # Use Groq's model
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = requests.post(GROQ_API_URL, headers=HEADERS, json=payload)
        response_data = response.json()

        if response.status_code != 200:
            return f"Error generating itinerary: {response_data}"

        return response_data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Error: {str(e)}"
