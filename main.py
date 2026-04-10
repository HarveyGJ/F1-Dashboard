import fastf1
import streamlit as st
from core.loader import load_session
from core.timing import process_race_timing

fastf1.Cache.enable_cache("cache/")

st.title("F1 Dashboard")

st.text(
    "Navigate through the pages to find; Session Results, Telemetry Data, Lap Analysis and Strategy Data"
)
