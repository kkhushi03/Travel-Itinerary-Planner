import streamlit as st
import requests

# App title and description
st.title("AI Travel Itinerary Planner")
st.write("Generate personalized travel itineraries based on your preferences!")

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
        "Authorization": f"Bearer {st.secrets['GROQ_API_KEY']}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": prompt}]
    }
    
    try:
        # Make sure to use POST request method
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=data
        )
        
        # Debug information
        st.write(f"Status Code: {response.status_code}")
        st.write(f"Response: {response.text}")
        
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content']
        else:
            return f"Error: {response.status_code} - {response.text}"
    
    except Exception as e:
        return f"Error generating itinerary: {str(e)}"

# Create form to collect user inputs
with st.form("travel_form"):
    destination = st.text_input("Destination")
    trip_duration = st.number_input("Trip Duration (days)", min_value=1, max_value=30, value=3)
    budget = st.selectbox("Budget", ["Budget", "Moderate", "Luxury"])
    preferences = st.text_input("Your travel interests (e.g., food, history, adventure)")
    
    # Allow multiple attraction selections
    attractions_input = st.text_input("Suggested attractions (comma-separated)")
    attractions = [attr.strip() for attr in attractions_input.split(",")] if attractions_input else []
    
    submitted = st.form_submit_button("Generate Itinerary")
    
    if submitted:
        user_details = {
            "destination": destination,
            "trip_duration": trip_duration,
            "budget": budget,
            "preferences": preferences,
            "attractions": attractions
        }
        
        with st.spinner("Generating your personalized itinerary..."):
            itinerary = generate_itinerary(user_details)
        
        st.markdown("## Your Personalized Travel Itinerary 📜")
        st.markdown(itinerary)
