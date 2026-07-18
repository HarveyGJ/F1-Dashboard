import streamlit as st
from core.wdc import get_drivers_standings, calculate_max_points_for_remaining_season, calculate_who_can_win

st.set_page_config(layout="wide")

col1, col2 = st.columns([2, 8])

col1.subheader(
    "Who can still win the World Drivers Championship.", divider="grey"
)

col2.subheader("Session Results", text_alignment="center")

with col1:
    season = st.selectbox("Season", range(2018, 2027))
    round_number = st.selectbox("Current Round", range(1, 25))

    if st.button("Calculate"):
        with st.spinner("Calculating Results"):
            try:
                with col2:
                    drivers_standings = get_drivers_standings(season, round_number)
                    points = calculate_max_points_for_remaining_season(season, round_number)
                    results = calculate_who_can_win(drivers_standings, points)
                    st.dataframe(results)
     
            except ValueError as e:
                st.error(
                    f"Session not available:\n\n {round_number} may not exist for yet.\n\n{str(e)}"
                )
            
            
            except Exception as e:
                st.error(f"Error loading session: {str(e)}")
