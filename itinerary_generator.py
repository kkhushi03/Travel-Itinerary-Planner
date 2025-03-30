import groq
from config import GROQ_API_KEY  # Import the API key

client = groq.Client(api_key=GROQ_API_KEY)  # Use the key

SYSTEM_PROMPT = """
You are an AI-powered travel planner. Your goal is to create a personalized travel itinerary...
"""

def generate_itinerary(user_details):
    """Generates a personalized travel itinerary using Groq API."""
    prompt = f"""
    Generate a {user_details['trip_duration']}-day travel itinerary for {user_details['destination']} 
    based on these details:
    Budget: {user_details['budget']}
    Interests: {user_details['preferences']}
    Suggested Attractions: {', '.join(user_details['attractions'])}

    Ensure a mix of activities per day, proper timing, and logical grouping of activities.
    """

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "system", "content": SYSTEM_PROMPT},
                  {"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
