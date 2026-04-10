import fastf1
import streamlit as st
from core.loader import load_session
from core.timing import process_fp_timing


st.title("Session Results")
st.text("Search through Free Practice, Qualifying and Races, from 2018 to current day.")
year = st.selectbox("Year", range(2018, 2027))
race = st.text_input("Weekend (e.g Australia)")
session_type = st.selectbox("Session", ["FP1", "FP2", "FP3", "Qualifying", "Race"])

if st.button("Load Session"):
    with st.spinner("Fetching Results"):
        match session_type:
            case "FP1" | "FP2" | "FP3":
                fp_session = load_session(year, race, session_type)
                print(fp_session)
                fp_results = process_fp_timing(fp_session)
                st.success("Session Loaded!")
                st.write(f"{session_type} Results")

                st.dataframe(fp_results, hide_index=True)

            case "Race" | "Sprint":
                pass
            case "Qualifying" | "Sprint Shootout":
                quali_session = load_session(year, race, session_type)
                # quali_results = processed_quali_timing(quali_session)
                quali_results = quali_session.results[
                    ["DriverNumber", "FullName", "TeamName", "Q1", "Q2", "Q3"]
                ]
                st.dataframe(quali_results, hide_index=True)
            case _:
                st.error(f"Unknown session type: {session_type}")
