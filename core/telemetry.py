import fastf1.plotting
import matplotlib.pyplot as plt

fastf1.Cache.enable_cache("~/Programming/F1-Dashboard/cache")

fastf1.plotting.setup_mpl(mpl_timedelta_support=True, color_scheme="fastf1")

session = fastf1.get_session(2025, "Silverstone", "Race")
session.load()


ver_lap = session.laps.pick_drivers("VER").pick_fastest()
ham_lap = session.laps.pick_drivers("HAM").pick_fastest()

ver_tel = ver_lap.get_car_data().add_distance()
ham_tel = ham_lap.get_car_data().add_distance()
print(ver_tel, ham_tel)

rbr_color = fastf1.plotting.get_team_color(ver_lap["Team"], session=session)
mer_color = fastf1.plotting.get_team_color(ham_lap["Team"], session=session)

fig, ax = plt.subplots()
ax.plot(ver_tel["Distance"], ver_tel["Speed"], color=rbr_color, label="VER")
ax.plot(ham_tel["Distance"], ham_tel["Speed"], color=mer_color, label="HAM")

ax.set_xlabel("Distance in m")
ax.set_ylabel("Speed in km/h")

ax.legend()
plt.suptitle(
    f"Fastest lap comparison \n"
    f"{session.event["EventName"]} {session.event.year} Race"
)

plt.show()
