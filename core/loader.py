from pathlib import Path
import fastf1
import streamlit as st

from core.config import CACHE_DIR

fastf1.Cache.enable_cache(str(CACHE_DIR))

@st.cache_data(ttl="1h")
def load_event_schedule(year, backend=None):
    return fastf1.events.get_event_schedule(year, backend=backend)


@st.cache_resource
def load_session(year, race, session_type):
    session = fastf1.get_session(year, race, session_type)
    session.load()
    return session

@st.cache_resource
def driver_abb_fast_loader(year, race, session_type):
    session = fastf1.get_session(year, race, session_type)
    session.load(laps=False, telemetry=False, messages=False)
    drivers_abb = session.results["Abbreviation"]

    return [driver for driver in drivers_abb]

@st.cache_resource
def load_session_tel(year, race, session_type):
    session = fastf1.get_session(year, race, session_type)
    session.load(telemetry=True, messages=False)
    return session


@st.cache_data(ttl="1h")
def load_races(year):
    session = load_event_schedule(year)
    gp_names = session["OfficialEventName"].tolist()
    return gp_names


# ToDo: Add a function to add dynamic loading for session types, based on user selected year and race, allows to show only races that are avaliable for that weekend! 
def load_session_types():
    pass