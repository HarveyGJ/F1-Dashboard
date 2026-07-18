import streamlit as st
from core.loader import load_session, driver_abb_fast_loader, load_races
from core.analysis import lap_time_distributions

st.set_page_config(layout="wide")

col1, col2 = st.columns([2, 8])

col1.subheader(
    "Search through sessions\n\n Lap Time Distributions for Top 10 Finishers.\n\n 2018 - Current Day.",
    divider="grey",
)

col2.subheader("Session Results", text_alignment="center")

with col1:
    year = st.selectbox("Year", range(2018, 2027))
    race = st.selectbox("Weekend", load_races(year))
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

    driver_selection = st.multiselect(
        "Driver", driver_abb_fast_loader(year, race, session_type)
    )

    if st.button("Load Session"):
        with st.spinner("Fetching Results"):
            try:
                with col2:
                    session = load_session(year, race, session_type)
                    session_results = lap_time_distributions(session, driver_selection)
                    st.pyplot(session_results)      
            except ValueError as e:
                st.error(
                    f"Session not available:\n\n {session_type} may not exist for {race} {year}.\n\n Sprint Shootout is only valid the year 2023.\n\n Sprint Qualifying is valid for the year 2024.\n\n {str(e)}"
                )
            
            
            except Exception as e:
                st.error(f"Error loading session: {str(e)}")
