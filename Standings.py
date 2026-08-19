import fastf1
import streamlit as st
from core.config import CACHE_DIR
from core.wdc import get_drivers_standings
from datetime import datetime

fastf1.Cache.enable_cache(str(CACHE_DIR))



st.title("F1 Dashboard", text_alignment='center')


current_year = datetime.now().year
schedule = fastf1.events.get_event_schedule(current_year)


today = datetime.now().strftime("%Y-%m-%d")
completed_rounds = schedule[schedule["EventDate"] <= today]

if not completed_rounds.empty:

    latest_round = completed_rounds.iloc[-1]["RoundNumber"]

    standings = get_drivers_standings(current_year, latest_round)
    
    df_display = standings[['position', 'givenName', 'familyName', 'points']].copy()
    df_display['Driver'] = df_display['givenName'] + ' ' + df_display['familyName']
    df_display = df_display[['position', 'Driver', 'points']]
    df_display.columns = ['Position', 'Driver', 'Points']
    
    st.subheader(f"Driver Standings - Round {latest_round}", text_alignment='center')
    st.dataframe(df_display, hide_index=True, use_container_width="True" )
    
else:
    st.info("No rounds have been completed yet this season.")


st.text("Navigate through the pages to find; Session Results, Telemetry Data, Lap Analysis, Who can still win the World Drivers Championship and Standings.", text_alignment='center')

