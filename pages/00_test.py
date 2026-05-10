import streamlit as st
from core.loader import load_session, driver_abb_fast_loader
from core.telemetry import process_tel

st.set_page_config(layout="wide")

col1, col2 = st.columns([4, 8])

col1.subheader(
    "Search through sessions\n\n Choose drivers you'd like to compare Fastests laps of a selected session.\n\n 2018 - Current Day.",
    divider="grey",
)

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

    driver_selection = st.multiselect(
        "Driver", driver_abb_fast_loader(year, race, session_type)
    )

    if st.button("Load Session"):
        with st.spinner("Fetching Results"):
            try:
                with col2:
                    match session_type:
                        case (
                            "FP1"
                            | "FP2"
                            | "FP3"
                            | "Qualifying"
                            | "Race"
                            | "Sprint Shootout"
                            | "Sprint Qualifying"
                            | "Sprint"
                        ):

                            session = load_session(year, race, session_type)
                            session_results = process_tel(session, driver_selection)
                            st.pyplot(session_results)
                            st.warning(
                                "Drivers that are not displayed would be down as a DNS and have no fastest lap data"
                            )
                        case _:
                            pass
                            st.error(f"Unknown session type: {session_type}")
            except ValueError as e:
                st.error(
                    f"Session not available:\n\n {session_type} may not exist for {race} {year}.\n\n Sprint Shootout is only valid the year 2023.\n\n Sprint Qualifying is valid for the year 2024.\n\n {str(e)}"
                )
            except Exception as e:
                st.error(f"Error loading session: {str(e)}")
