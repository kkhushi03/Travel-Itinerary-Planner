import streamlit as st
from user_input import get_user_input
from itinerary_generator import generate_itinerary

def main():
    """Main function to run the Streamlit app."""
    user_details = get_user_input()

    if user_details:
        # Generate itinerary using the user's manually entered attractions
        itinerary = generate_itinerary(user_details)

        # Display user-inputted attractions
        st.subheader("Top Attractions 🏞️")
        for attr in user_details["attractions"]:
            st.write(f"🔹 {attr}")

        # Display the generated itinerary
        st.subheader("Your Personalized Travel Itinerary 📜")
        st.write(itinerary)

if __name__ == "__main__":
    main()
