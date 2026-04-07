import fastf1
import streamlit as st
fastf1.Cache.enable_cache("cache/")

st.title("F1 Dashboard")

st.text("Find Results of Free Practice, Qualifying and Races!")
year = st.selectbox("Year", range(2018, 2027))
race = st.text_input("Race (e.g. 'Australia')")
session_type = st.selectbox("Session", ["FP1", "FP2", "FP3", "Qualifying", "Race"])




# To-Do: Refactor with match case statements - want to get basic functionaility down first

if st.button("Load Session"):
    with st.spinner("Fetching Results"):
        if session_type == 'FP1' or session_type == 'FP2' or session_type == 'FP3':
            print('Free Practice')
            fp_session = fastf1.get_session(year, race, session_type)
            fp_session.load()
        elif session_type == 'Race':
            print('Race')
            session = fastf1.get_session(year, race, session_type)
            session.load()
        
    st.success("Session loaded!")
    
    
 
    fp_results = fp_session.results[['Position', 'FullName', 'TeamName', 'Laps', 'Time']].copy()
    fp_results = fp_results.rename(columns={
        'Position': 'Pos',
        'FullName': 'Driver',
        'TeamName': 'Team',
        'Laps': 'Laps',
        'Time': 'Gap'
    })
    
    st.dataframe(fp_results, hide_index=True)
    

    
    
    race_results = session.results[['Position', 'FullName', 'Abbreviation', 'TeamName', 'Laps', 'Time', 'Status', 'Points']].copy()
    
    race_results = race_results.rename(columns={
        'Position': 'Pos',
        'FullName': 'Driver',
        'Abbreviation': 'Code',
        'TeamName': 'Team',
        'Laps': 'Laps',
        'Time': 'Gap',
        'Status': 'Status',
        'Points': 'Points'
    })
    
    st.dataframe(race_results, hide_index=True)         


