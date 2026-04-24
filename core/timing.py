import fastf1
import streamlit as st
from core.loader import load_session
from datetime import timedelta


@st.cache_data
def format_time_to_string(timedelta_obj):
    if timedelta_obj is None or str(timedelta_obj) == "NaT":
        return "DNF"

    total_seconds = timedelta_obj.total_seconds()

    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)
    milliseconds = int((total_seconds % 1) * 1000)

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}"


def process_fp_timing(fp_session):
    # Get driver info
    drivers_info = fp_session.results[["DriverNumber", "FullName"]].drop_duplicates()
    print(drivers_info)
    # Get best lap time and lap count from laps data
    laps = fp_session.laps
    best_laps = (
        laps.groupby("DriverNumber")
        .agg({"LapTime": "min", "LapNumber": "max", "Team": "first"})
        .reset_index()
    )
    print(best_laps)
    # Merge with driver names
    fp_results = best_laps.merge(drivers_info, on="DriverNumber", how="left")

    # Sort by lap time and add position
    fp_results = fp_results.sort_values("LapTime").reset_index(drop=True)
    fp_results["Position"] = range(1, len(fp_results) + 1)

    # Keep only the columns we need
    fp_results = fp_results[
        ["Position", "FullName", "Team", "LapNumber", "LapTime"]
    ].rename(
        columns={
            "FullName": "Driver",
            "Team": "Team",
            "LapNumber": "Laps",
            "LapTime": "Best Lap Time",
        }
    )

    # Format the best lap time
    fp_results["Best Lap Time"] = fp_results["Best Lap Time"].apply(
        format_time_to_string
    )

    return fp_results


# TODO: finish, quali timing function, return, q1,q2,q3
def process_quali_timing(quali_session):
    quali_results = quali_session.results[
        [
            "Position",
            "DriverNumber",
            "FullName",
            "TeamName",
            "Q1",
            "Q2",
            "Q3",
        ]
    ]
    print(quali_results)
    quali_results = quali_results[
        [
            "Position",
            "DriverNumber",
            "FullName",
            "TeamName",
            "Q1",
            "Q2",
            "Q3",
        ]
    ].rename(
        columns={
            "Position": "Position",
            "DriverNumber": "NO.",
            "FullName": "Driver",
            "TeamName": "Team",
            "Q1": "Q1",
            "Q2": "Q2",
            "Q3": "Q3",
        }
    )
    quali_results["Q1"] = quali_results["Q1"].apply(format_time_to_string)
    quali_results["Q2"] = quali_results["Q2"].apply(format_time_to_string)
    quali_results["Q3"] = quali_results["Q3"].apply(format_time_to_string)
    return quali_results
    pass


def process_race_timing(race_session):
    race_results = race_session.results[
        ["Position", "DriverNumber", "FullName", "TeamName", "Laps", "Time", "Points"]
    ]
    race_results = race_results[
        ["Position", "DriverNumber", "FullName", "TeamName", "Laps", "Time", "Points"]
    ].rename(
        columns={
            "Position": "Position",
            "DriverNumber": "NO.",
            "FullName": "Driver",
            "TeamName": "Team",
            "Laps": "Laps",
            "Time": "Time / Retired",
            "Points": "Points",
        }
    )

    race_results["Time / Retired"] = race_results["Time / Retired"].apply(
        format_time_to_string
    )
    return race_results


print(process_quali_timing(load_session(2026, "Australia", "Qualifying")))
