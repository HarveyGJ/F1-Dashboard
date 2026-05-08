import fastf1
import streamlit as st
import matplotlib
from core.loader import load_session_tel

# from core.telemetry import process_fp_telemetry

st.set_page_config(layout="wide")

col1, col2 = st.columns([4, 8])

col1.subheader("Search through Sessions\n\n 2018 - Current Day.", divider="grey")

col2.subheader("Session Results", text_alignment="center")

with col1:
    year = st.selectbox("Year", range(2018, 2027))
    race = st.text_input("Weekend", placeholder="e.g British Grand Prix or Silverstone")
    session_type = st.selectbox(
        "Session",
        [
            "FP1",
            "FP2",
            "FP3",
            "Qualifying",
            "Race",
            "Sprint Shootout",
            "Sprint Qualifying",
            "Sprint",
        ],
    )
    # fast load to get drivers names to input into driver_select

    driver_select = st.multiselect("Driver", ["HAM", "VER", "LEC", "NOR"])

    print(driver_select)
