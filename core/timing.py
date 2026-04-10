import fastf1
import streamlit as st


@st.cache_data
def timing(year, race, session_type):
    session = fastf1.get_session(year, race, session_type)
    session.load(laps=True)
    print(session.laps)
    return session


timing(2026, "Australia", "Race")
