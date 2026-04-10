import fastf1
import streamlit as st
from core.loader import load_session
from datetime import timedelta


@st.cache_data
def format_time_to_string(timedelta_obj):
    if timedelta_obj is None or str(timedelta_obj) == "NaT":
        return "DNF"

    total_seconds = timedelta_obj.total_seconds()

    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)
    milliseconds = int((total_seconds % 1) * 1000)

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}"


def process_race_timing(_session):
    results_df = _session.results
    laps_df = _session.laps

    pass


def process_fp_timing(fp_session):
    fp_results = fp_session.results[
        ["Position", "FullName", "TeamName", "Laps", "Time"]
    ].copy()
    fp_results = fp_results.rename(
        columns={
            "Position": "Pos",
            "FullName": "Driver",
            "TeamName": "Team",
            "Laps": "Laps",
            "Time": "Gap",
        }
    )
    return fp_results
