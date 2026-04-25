import fastf1
import streamlit as st
import time
from core.loader import load_session
from core.timing import process_fp_timing, process_race_timing, process_quali_timing


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

    if st.button("Load Session"):
        with st.spinner("Fetching Results"):
            try:
                with col2:
                    match session_type:
                        case "FP1" | "FP2" | "FP3":
                            fp_session = load_session(year, race, session_type)
                            print(fp_session)
                            fp_results = process_fp_timing(fp_session)

                            success = st.success("Session Loaded!")

                            st.write(f"{race} {session_type} Results")

                            st.dataframe(fp_results, hide_index=True, width="stretch")

                            time.sleep(1.5)
                            success.empty()
                        case "Race" | "Sprint":
                            race_session = load_session(year, race, session_type)
                            race_results = process_race_timing(race_session)

                            success = st.success("Session Loaded!")

                            st.write(f"{race} {session_type} Results")

                            st.dataframe(race_results, hide_index=True, width="stretch")

                            time.sleep(1.5)
                            success.empty()
                        case "Qualifying" | "Sprint Shootout" | "Sprint Qualifying":
                            quali_session = load_session(year, race, session_type)
                            quali_results = process_quali_timing(quali_session)

                            success = st.success("Session Loaded!")

                            st.write(f"{race} {session_type} Results")

                            st.dataframe(
                                quali_results, hide_index=True, width="stretch"
                            )

                            time.sleep(1.5)
                            success.empty()
                        case _:
                            st.error(f"Unknown session type: {session_type}")
            except ValueError as e:
                st.error(
                    f"Session not available:\n\n {session_type} may not exist for {race} {year}.\n\n Sprint Shootout is only valid the year 2023.\n\n Sprint Qualifying is valid for the year 2024.\n\n {str(e)}"
                )
            except Exception as e:
                st.error(f"Error loading session: {str(e)}")
