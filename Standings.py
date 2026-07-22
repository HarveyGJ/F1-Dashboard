import fastf1
import streamlit as st
from core.wdc import get_drivers_standings
fastf1.Cache.enable_cache("./cache")

st.title("F1 Dashboard")

st.text(
    "Navigate through the pages to find; Session Results, Telemetry Data, Lap Analysis, Who can still win the World Drivers Championship and Standings."
)
col1, col2 = st.columns([2, 8])

col1.subheader(
    "Select current weekend to get drivers standings.", divider="grey"
)

col2.subheader("Results", text_alignment="center")

with col1:
    season = st.selectbox("Season", range(2026, 2027))
    round_number = st.selectbox("Current Round", range(1, 25))

    """if st.button("Calculate"):
        with st.spinner("Calculating Results"):
            with col2:
            # get current date to work out what weekend of the what year it is and what GP num is currently running/not running
            # use that to display standings as soon as the page loads - might be restricted by streamlit functionality"""