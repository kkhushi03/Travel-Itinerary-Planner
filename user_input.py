import streamlit as st

def get_user_input():
    """Collects user input via Streamlit UI."""
    st.title("AI Travel Planner 🌍✈️")

    destination = st.text_input("Enter your destination:")
    trip_duration = st.number_input("Number of days:", min_value=1, step=1)
    budget = st.selectbox("Budget preference:", ["Budget", "Mid-range", "Luxury"])
    preferences = st.multiselect("Select your interests:", 
                                 ["Nature", "Culture", "Adventure", "Food", "Shopping", "Relaxation"])

    if st.button("Generate Itinerary"):
        return {
            "destination": destination,
            "trip_duration": trip_duration,
            "budget": budget,
            "preferences": preferences,
            "attractions": []  # This will be filled dynamically later
        }
    
    return None
