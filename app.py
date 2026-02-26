import streamlit as st
from planner import generate_itinerary
from map_utils import create_map
from pdf_utils import create_pdf
from streamlit_folium import st_folium

st.set_page_config(page_title="AI Travel Planner", layout="wide")

st.title("🌍 AI Travel Planner")


# INPUTS


destinations = st.text_input(
    "Enter destinations (comma separated)", 
    "Goa, Mumbai"
)

days = st.number_input("Number of days", min_value=1, value=5)

budget = st.number_input("Budget (₹)", min_value=1000, value=10000)

preferences = st.selectbox(
    "Travel Style",
    ["Budget", "Luxury", "Adventure", "Food", "Relaxation", "Mixed"]
)

destination_list = [d.strip() for d in destinations.split(",") if d.strip()]


# SESSION STATE


if "itinerary" not in st.session_state:
    st.session_state.itinerary = ""


# GENERATE BUTTON


if st.button("Generate Plan"):

    if not destination_list:
        st.warning("Please enter at least one destination")
    else:
        with st.spinner("Generating itinerary using AI..."):
            result = generate_itinerary(
                destination_list, days, budget, preferences
            )
            st.session_state.itinerary = result


# OUTPUT SECTION


if st.session_state.itinerary:

    st.subheader("📋 Your Travel Plan")

    # ✅ Render Markdown properly (no ### or ** visible)
    st.markdown(st.session_state.itinerary)


    # MAP


    st.subheader("🗺️ Route Map")
    try:
        map_obj = create_map(destination_list)
        st_folium(map_obj, width=700, height=500)
    except Exception as e:
        st.warning(f"Map could not be loaded: {e}")


    # PDF DOWNLOAD


    try:
        pdf_bytes = create_pdf(st.session_state.itinerary)

        st.download_button(
            label="📄 Download PDF",
            data=pdf_bytes,
            file_name="Travel_Itinerary.pdf",
            mime="application/pdf"
        )

    except Exception as e:
        st.error(f"PDF generation failed: {e}")