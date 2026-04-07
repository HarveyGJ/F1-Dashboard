import fastf1
import streamlit as st
from core.loader import load_session

fastf1.Cache.enable_cache("cache/")

st.title("F1 Dashboard")

st.text("Find Results of Free Practice, Qualifying and Races!")
year = st.selectbox("Year", range(2018, 2027))
race = st.text_input("Race (e.g. 'Australia')")
session_type = st.selectbox(
    "Session",
    ["FP1", "FP2", "FP3", "Sprint Shootout", "Sprint Race", "Qualifying", "Race"],
)


# To-Do: Refactor with match case statements - want to get basic functionaility down first

if st.button("Load Session"):
    with st.spinner("Fetching Results"):

        if session_type == "FP1" or session_type == "FP2" or session_type == "FP3":
            print("Free Practice")
            fp_session = load_session(year, race, session_type)
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
        elif session_type == "Race":
            print("Race")
            session = load_session(year, race, session_type)
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


match year:
    case 2018:
        pass
    case 2019:
        pass
    case 2020:
        pass
    case 2021:
        match race:
            case ["British", "Imola", "Brazilian"]:
                print("Sprint of 2021")
        pass
    case 2022:
        pass
    case 2023:
        pass
    case 2024:
        pass
    case 2025:
        pass
    case 2026:
        pass
