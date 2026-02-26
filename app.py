import streamlit as st
from planner import generate_itinerary
from pdf_utils import generate_pdf
from map_utils import get_coordinates

st.set_page_config(page_title="AI Travel Planner", layout="wide")

st.title("🌍 AI Travel Planner")

# Initialize session state
if "itinerary" not in st.session_state:
    st.session_state.itinerary = None

if "cities" not in st.session_state:
    st.session_state.cities = None

# USER INPUT

boarding_point = st.text_input("Enter Boarding City")

destinations_input = st.text_input("Enter Destinations (comma separated)")

days = st.number_input("Number of Days", min_value=1, max_value=30, value=3)

budget = st.text_input("Total Budget (₹)")

preferences = st.text_area("Travel Preferences")

optimize_budget = st.checkbox("💰 Optimize for Cheapest Travel")

# GENERATE BUTTON

if st.button("Generate Itinerary"):

    if not boarding_point or not destinations_input:
        st.warning("Please enter boarding city and destinations.")
    else:
        destinations = [d.strip() for d in destinations_input.split(",")]

        with st.spinner("Generating itinerary..."):
            itinerary = generate_itinerary(
                boarding_point,
                destinations,
                days,
                budget,
                preferences,
                optimize_budget
            )

        # Save to session state
        st.session_state.itinerary = itinerary
        st.session_state.cities = [boarding_point] + destinations


if st.session_state.itinerary:

    st.subheader("🧳 Your Itinerary")
    st.text(st.session_state.itinerary)

    # PDF Download
    pdf_file = generate_pdf(st.session_state.itinerary)

    st.download_button(
        label="📄 Download Itinerary PDF",
        data=pdf_file,
        file_name="Travel_Itinerary.pdf",
        mime="application/pdf"
    )

    # Map
    st.subheader("🗺 Travel Route Map")

    df = get_coordinates(st.session_state.cities)

    if not df.empty:
        st.map(df)
    else:
        st.warning("Map could not load locations.")
