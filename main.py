import fastf1
import streamlit as st
from core.loader import load_session
from core.timing import timing

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
            st.success("Session Loaded!")
            timing()
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
            print("Race")
            session = load_session(year, race, session_type)
            print(session.results)
            timing(year, race, session_type)
            st.success("Session loaded!")
            st.write(f"{session_type} Results")
            race_results = session.results[
                [
                    "Position",
                    "FullName",
                    "TeamName",
                    "Laps",
                    "Time",
                    "Status",
                    "Points",
                ]
            ].copy()

            race_results = race_results.rename(
                columns={
                    "Position": "Pos",
                    "FullName": "Driver",
                    "TeamName": "Team",
                    "Laps": "Laps",
                    "Time": "Gap",
                    "Status": "Status",
                    "Points": "Points",
                }
            )
            st.dataframe(race_results, hide_index=True)
