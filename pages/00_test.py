import fastf1
import streamlit as st
import matplotlib
from core.loader import load_session_tel
from core.telemetry import process_fp_telemetry

st.set_page_config(layout="wide")

col1, col2 = st.columns([4, 8])

col1.subheader("Search through Sessions\n\n 2018 - Current Day.", divider="grey")

col2.subheader("Session Results", text_alignment="center")

with col1:
    year = st.selectbox("Year", range(2018, 2027))
    race = st.text_input("Weekend", placeholder="e.g British Grand Prix or Silverstone")
    session_type = st.selectbox(
        "Session",
        [
            "FP1",
            "FP2",
            "FP3",
            "Qualifying",
            "Race",
            "Sprint Shootout",
            "Sprint Qualifying",
            "Sprint",
        ],
    )
    # fast loader to get drivers names - dynamically change upon getting year, race & session_type
    session = fastf1.get_session(year, race, session_type)
    session.load(laps=False, telemetry=False, messages=False)
    drivers_abb = session.results["Abbreviation"]

    drivers = [driver for driver in drivers_abb]

    driver_selection = st.multiselect("Driver", drivers)

    if st.button("Load Session"):
        with st.spinner("Fetching Results"):
            try:
                with col2:
                    match session_type:
                        case "FP1" | "FP2" | "FP3":
                            fp_session_tel = load_session_tel(year, race, session_type)

                            fp_telemetry = process_fp_telemetry(
                                fp_session_tel, driver_selection
                            )

                        case "Race" | "Sprint":
                            pass
                        case "Qualifying" | "Sprint Shootout" | "Sprint Qualifying":
                            pass
                        case _:
                            pass
                            st.error(f"Unknown session type: {session_type}")
            except ValueError as e:
                st.error(
                    f"Session not available:\n\n {session_type} may not exist for {race} {year}.\n\n Sprint Shootout is only valid the year 2023.\n\n Sprint Qualifying is valid for the year 2024.\n\n {str(e)}"
                )
            except Exception as e:
                st.error(f"Error loading session: {str(e)}")
