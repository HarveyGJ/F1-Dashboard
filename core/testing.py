"""import fastf1.plotting
import streamlit as st
import matplotlib.pyplot as plt

# Fastest lap for a any given race - only the fastests of the race, no selection for drivers.


fastf1.Cache.enable_cache("~/Programming/F1-Dashboard/cache")

fastf1.plotting.setup_mpl(mpl_timedelta_support=True, color_scheme="fastf1")

session = fastf1.get_session(2026, "Miami", "Race")
session.load()


fastest_lap = session.laps.pick_fastest()
car_data = fastest_lap.get_car_data().add_distance()

circuit_info = session.get_circuit_info()

team_color = fastf1.plotting.get_team_color(fastest_lap["Team"], session=session)

fig, ax = plt.subplots()
ax.plot(
    car_data["Distance"],
    car_data["Speed"],
    color=team_color,
    label=fastest_lap["Driver"],
)
v_min = car_data["Speed"].min()
v_max = car_data["Speed"].max()
ax.vlines(
    x=circuit_info.corners["Distance"],
    ymin=v_min - 20,
    ymax=v_max + 20,
    linestyles="dotted",
    colors="grey",
)

for _, corner in circuit_info.corners.iterrows():
    txt = f"{corner["Number"]}{corner["Letter"]}"
    ax.text(
        corner["Distance"],
        v_min - 30,
        txt,
        va="center_baseline",
        ha="center",
        size="small",
    )

ax.set_xlabel("Distance in m")
ax.set_ylabel("Speed in km/h")
ax.legend()

ax.set_ylim([v_min - 40, v_max + 20])


st.pyplot(fig)
"""
