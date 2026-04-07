import fastf1
import streamlit as st

fastf1.Cache.enable_cache("cache/")

st.title("F1 Dashboard")

year = st.selectbox("Year", range(2018, 2026))
race = st.text_input("Race (e.g. 'Australia')")
session_type = st.selectbox("Session", ["FP1", "FP2", "FP3", "Qualifying", "Race"])

if st.button("Load Session"):
    with st.spinner("Fetching Results"):
        session = fastf1.get_session(year, race, session_type)
        session.load()
    st.success("Session loaded!")
    st.dataframe(session.laps[["Driver", "LapTime", "Compound", "TyreLife"]])


