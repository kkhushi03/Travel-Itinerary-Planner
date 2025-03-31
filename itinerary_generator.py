import streamlit as st
import requests
import json

# Retrieve API key from Streamlit secrets
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

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
    
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": prompt}]
    }
    
    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=data
        )
        
        response.raise_for_status()  # Raise an exception for HTTP errors
        result = response.json()
        
        return result['choices'][0]['message']['content']
    
    except Exception as e:
        return f"Error generating itinerary: {str(e)}"
