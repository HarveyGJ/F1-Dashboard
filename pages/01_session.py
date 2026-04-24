import fastf1
import streamlit as st
from core.loader import load_session
from core.timing import process_fp_timing, process_race_timing, process_quali_timing


st.title("Session Results")
st.text("Search through Free Practice, Qualifying and Races, from 2018 to current day.")
year = st.selectbox("Year", range(2018, 2027))
race = st.text_input("Weekend (e.g Australia)")
session_type = st.selectbox(
    "Session",
    [
        "FP1",
        "FP2",
        "FP3",
        "Qualifying",
        "Sprint Shootout",
        "Sprint Qualifying",
        "Race",
        "Sprint",
    ],
)

if st.button("Load Session"):
    with st.spinner("Fetching Results"):
        try:
            match session_type:
                case "FP1" | "FP2" | "FP3":
                    fp_session = load_session(year, race, session_type)
                    print(fp_session)
                    fp_results = process_fp_timing(fp_session)

                    st.success("Session Loaded!")
                    st.write(f"{session_type} Results")

                    st.dataframe(fp_results, hide_index=True)

                case "Race" | "Sprint":
                    race_session = load_session(year, race, session_type)
                    race_results = process_race_timing(race_session)

                    st.success("Session Loaded!")
                    st.write(f"{session_type} Results")

                    st.dataframe(race_results, hide_index=True)

                case "Qualifying" | "Sprint Shootout" | "Sprint Qualifying":
                    quali_session = load_session(year, race, session_type)
                    quali_results = process_quali_timing(quali_session)

                    st.success("Session Loaded!")
                    st.write(f"{session_type} Results")

                    st.dataframe(quali_results, hide_index=True)
                case _:
                    st.error(f"Unknown session type: {session_type}")
        except ValueError as e:
            st.error(
                f"Session not available:\n\n {session_type} may not exist for {race} {year}.\n\n Sprint Shootout is only valid the year 2023.\n\n Sprint Qualifying is valid for the year 2024.\n\n {str(e)}"
            )
        except Exception as e:
            st.error(f"Error loading session: {str(e)}")
