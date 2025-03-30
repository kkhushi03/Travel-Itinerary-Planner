import streamlit as st
import openai  # If using Groq API

# Retrieve API key from Streamlit secrets
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

# Initialize OpenAI API with Groq key
openai.api_key = GROQ_API_KEY  

SYSTEM_PROMPT = """
You are an AI-powered travel planner. Your goal is to create a personalized travel itinerary...
Make sure to provide a mix of activities per day, balance sightseeing with relaxation, and consider 
travel time between locations.
"""

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
        response = openai.chat.completions.create(
            model="gpt-4",  # Ensure you're using the right model
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message["content"]
    
    except Exception as e:
        return f"Error generating itinerary: {str(e)}"
