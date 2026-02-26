import streamlit as st
from planner import generate_itinerary
from pdf_utils import generate_pdf
from map_utils import get_coordinates
import re
import pandas as pd
import folium
from streamlit_folium import st_folium


st.set_page_config(
    page_title="AI Travel Planner Pro",
    page_icon="🌍",
    layout="wide"
)


st.markdown("""
<style>

/* Background Image */
.stApp {
    background-image: url("https://images.unsplash.com/photo-1507525428034-b723cf961d3e");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Main glass container */
.main {
    background: rgba(255, 255, 255, 0.92);
    padding: 2rem;
    border-radius: 20px;
}

/* Dark Sidebar */
section[data-testid="stSidebar"] {
    background-color: #0f172a;
}

/* Sidebar text white */
section[data-testid="stSidebar"] * {
    color: white !important;
}

/* 🔥 ONLY INPUT TEXT BLACK */
input, textarea {
    color: black !important;
}

div[data-baseweb="input"] input {
    color: black !important;
}

div[data-baseweb="textarea"] textarea {
    color: black !important;
}

/* Buttons */
.stButton>button {
    background-color: #2563eb;
    color: white;
    border-radius: 10px;
    padding: 0.6em 1.2em;
    border: none;
}

.stDownloadButton>button {
    background-color: #16a34a;
    color: white;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# SESSION STATE

if "itinerary" not in st.session_state:
    st.session_state.itinerary = None

if "cities" not in st.session_state:
    st.session_state.cities = None

if "history" not in st.session_state:
    st.session_state.history = []

# HEADER

st.title("🌍 AI Travel Planner Pro")
st.caption("Smart • Budget Aware • AI Powered")
st.divider()

# SIDEBAR

with st.sidebar:
    st.header("🧳 Plan Your Trip")

    boarding = st.text_input("Boarding City")
    destinations_input = st.text_input("Destinations (comma separated)")
    days = st.slider("Number of Days", 1, 25, 3)
    budget = st.number_input("Total Budget (₹)", min_value=1000, step=1000)
    preferences = st.text_area("Preferences")
    optimize = st.toggle("💰 Strict Budget Mode")

    generate_btn = st.button("🚀 Generate Plan")

    st.divider()

    if st.session_state.history:
        st.subheader("📁 Trip History")
        selected_trip = st.selectbox(
            "Select Previous Trip",
            range(len(st.session_state.history)),
            format_func=lambda x: f"Trip {x+1}"
        )

        if st.button("Load Selected Trip"):
            st.session_state.itinerary = st.session_state.history[selected_trip]["itinerary"]
            st.session_state.cities = st.session_state.history[selected_trip]["cities"]

# GENERATE PLAN

if generate_btn:
    if not boarding or not destinations_input:
        st.error("Please enter required fields.")
    else:
        destinations = [d.strip() for d in destinations_input.split(",")]

        with st.spinner("Designing your intelligent travel plan..."):
            itinerary = generate_itinerary(
                boarding,
                destinations,
                days,
                budget,
                preferences,
                optimize
            )

        st.session_state.itinerary = itinerary
        st.session_state.cities = [boarding] + destinations

        st.session_state.history.append({
            "itinerary": itinerary,
            "cities": [boarding] + destinations
        })

# DISPLAY OUTPUT

if st.session_state.itinerary:

    tab1, tab2, tab3 = st.tabs(
        ["🗓 Itinerary", "📊 Budget Dashboard", "🗺 Route Map"]
    )

    # TAB 1 - ITINERARY

    with tab1:
        st.subheader("Your Personalized Travel Plan")

        days_split = re.split(r"(Day \d+.*?)\n", st.session_state.itinerary)

        for i in range(1, len(days_split), 2):
            with st.expander(days_split[i]):
                st.text(days_split[i+1].strip())

        pdf_file = generate_pdf(st.session_state.itinerary)

        st.download_button(
            "📄 Download Full Itinerary PDF",
            pdf_file,
            file_name="Travel_Itinerary.pdf",
            mime="application/pdf"
        )

    # TAB 2 - BUDGET

    with tab2:

        total_match = re.search(
            r"Final Estimated Total Cost:\s*₹?([\d,]+)",
            st.session_state.itinerary
        )

        if total_match:
            estimated = int(total_match.group(1).replace(",", ""))

            col1, col2 = st.columns(2)
            col1.metric("Budget", f"₹{budget}")
            col2.metric("Estimated", f"₹{estimated}")

            progress = min(estimated / budget, 1.0)
            st.progress(progress)

            if estimated <= budget:
                st.success("Trip is within budget ✅")
            else:
                st.error("Budget exceeded ⚠")

    # TAB 3 - MAP

    with tab3:

        df = get_coordinates(st.session_state.cities)

        if not df.empty:

            m = folium.Map(
                location=[df.iloc[0]["latitude"], df.iloc[0]["longitude"]],
                zoom_start=5
            )

            for idx, row in df.iterrows():
                folium.Marker(
                    [row["latitude"], row["longitude"]],
                    tooltip=st.session_state.cities[idx]
                ).add_to(m)

            folium.PolyLine(
                df[["latitude", "longitude"]].values
            ).add_to(m)

            st_folium(m, width=1100, height=500)

        else:
            st.warning("Map data unavailable.")
