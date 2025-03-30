import streamlit as st

def get_user_input():
    """Collects user input via Streamlit UI."""
    st.title("AI Travel Planner 🌍✈️")

    destination = st.text_input("Enter your destination:")
    trip_duration = st.number_input("Number of days:", min_value=1, step=1)
    budget = st.selectbox("Budget preference:", ["Budget", "Mid-range", "Luxury"])
    preferences = st.multiselect("Select your interests:", 
                                 ["Nature", "Culture", "Adventure", "Food", "Shopping", "Relaxation"])
    
    # Manually input attractions (comma-separated)
    attractions = st.text_area("Enter top attractions (comma-separated):")
    attraction_list = [attr.strip() for attr in attractions.split(",") if attr.strip()]

    if st.button("Generate Itinerary"):
        return {
            "destination": destination,
            "trip_duration": trip_duration,
            "budget": budget,
            "preferences": preferences,
            "attractions": attraction_list  # Stores manually entered attractions
        }
    
    return None
