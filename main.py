import fastf1
import streamlit as st
from core.loader import load_session
from core.timing import process_race_timing

fastf1.Cache.enable_cache("cache/")

st.title("F1 Dashboard")

st.text("Find Results of Free Practice, Qualifying and Races!")
year = st.selectbox("Year", range(2018, 2027))
race = st.text_input("Race (e.g. 'Australia')")
session_type = st.selectbox(
    "Session",
    ["FP1", "FP2", "FP3", "Sprint Shootout", "Sprint", "Qualifying", "Race"],
)


# To-Do: Refactor with match case statements - want to get basic functionaility down first

if st.button("Load Session"):
    with st.spinner("Fetching Results"):

        if session_type in ["FP1", "FP2", "FP3"]:
            print("Free Practice")
            fp_session = load_session(year, race, session_type)
            fp_results = process_race_timing(fp_session)
            st.success("Session Loaded!")
            st.write(f"{session_type} Results")
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

            st.dataframe(fp_results, hide_index=True)
        elif session_type in ["Race", "Sprint"]:
            session = load_session(year, race, session_type)
            st.write(f"{session_type} Results")
            st.success("Session loaded!")
            processed_results = process_race_timing(session)
