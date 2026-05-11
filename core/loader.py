import fastf1
import streamlit as st


@st.cache_data
def load_session(year, race, session_type):
    session = fastf1.get_session(year, race, session_type)
    session.load()
    return session


def driver_abb_fast_loader(year, race, session_type):
    session = fastf1.get_session(year, race, session_type)
    session.load(laps=False, telemetry=False, messages=False)
    drivers_abb = session.results["Abbreviation"]

    return [driver for driver in drivers_abb]


def load_session_tel(year, race, session_type):
    session = fastf1.get_session(year, race, session_type)
    session.load(telemetry=True, messages=False)
    return session


def load_races(year):
    session = fastf1.get_event_schedule(2018)
    gp_names = session["OfficialEventName"].tolist()
    return gp_names


# ToDo: Add a function to add dynamic loading for session types, based on user selected year and race, allows to show only races that are avaliable for that weekend! 
def load_session_types():
    pass