import fastf1
from fastf1.ergast import Ergast

   
def get_drivers_standings(season, round_number):
    ergast = Ergast()
    standings = ergast.get_driver_standings(season=season, round=round_number)
    return standings.content[0]


def calculate_max_points_for_remaining_season(season, round_number):
    POINTS_FOR_SPRINT = 8 + 25 
    POINTS_FOR_CONVENTIONAL = 25  
    
    events = fastf1.events.get_event_schedule(season, backend='ergast')
    events = events[events['RoundNumber'] > round_number]
    
    
    sprint_events = len(events.loc[events["EventFormat"] == "sprint_shootout"])
    conventional_events = len(events.loc[events["EventFormat"] == "conventional"])
    
    
    sprint_points = sprint_events * POINTS_FOR_SPRINT
    conventional_points = conventional_events * POINTS_FOR_CONVENTIONAL
    
    return sprint_points + conventional_points


def calculate_who_can_win(driver_standings, max_points):
    leader_points = int(driver_standings.loc[0]['points'])
    results = []

    for i, _ in enumerate(driver_standings.iterrows()):
        driver = driver_standings.loc[i]
        driver_max_points = int(driver["points"]) + max_points
        can_win = 'No' if driver_max_points < leader_points else 'Yes'

        results.append({
            "POS.": driver["position"],
            "Driver": f"{driver['givenName']} {driver['familyName']}",
            "Current Points": int(driver["points"]),
            "Theoretical Max Points": driver_max_points,
            "Can Win?": can_win,
        })

    return results

