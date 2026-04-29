import fastf1
import streamlit as st


@st.cache_data
def load_session(year, race, session_type):
    session = fastf1.get_session(year, race, session_type)
    session.load()
    return session


def load_session_tel(year, race, session_type):
    session = fastf1.get_session(year, race, session_type)
    session.load(telemetry=True)
    return session
