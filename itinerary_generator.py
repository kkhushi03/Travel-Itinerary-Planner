import streamlit as st
from openai import OpenAI

# Retrieve API key from Streamlit secrets
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

# Create a client with the correct Groq API base
client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/v1"  # Corrected endpoint URL
)

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
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    
    except Exception as e:
        return f"Error generating itinerary: {str(e)}"
