import fastf1.plotting
import matplotlib.pyplot as plt

fastf1.Cache.enable_cache("~/Programming/F1-Dashboard/cache")

fastf1.plotting.setup_mpl(mpl_timedelta_support=True, color_scheme="fastf1")

"""session = fastf1.get_session(2025, "Silverstone", "Race")
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

"""
# dynamically assign variables to names of drivers then discard after ive processed the telemetry
# change it so i can use a function to get the driver_{idx} lap and tel data


def process_tel(session_tel, driver_selection):
    print(session_tel)
    print(driver_selection)

    for idx, driver in enumerate(driver_selection):
        globals()[f"driver_{idx}"] = driver

    driver_0_lap = driver_laps(session_tel, driver_0)
    driver_1_lap = driver_laps(session_tel, driver_1)

    driver_0_tel = driver_tel(driver_0_lap)
    driver_1_tel = driver_tel(driver_1_lap)
    driver_0_color = driver_color(driver_0_lap, session_tel)
    driver_1_color = driver_color(driver_1_lap, session_tel)
    fig, ax = plt.subplots()
    ax.plot(
        driver_0_tel["Distance"],
        driver_0_tel["Speed"],
        color=driver_0_color,
        label=driver_0,
    )
    ax.plot(
        driver_1_tel["Distance"],
        driver_1_tel["Speed"],
        color=driver_1_color,
        label=driver_1,
    )
    ax.legend()
    plt.suptitle(
        f"Fastest lap comparison \n"
        f"{session_tel.event["EventName"]} {session_tel.event.year} Race"
    )

    return fig


def driver_laps(session_tel, driver_name):
    return session_tel.laps.pick_drivers(driver_name).pick_fastest()


def driver_tel(driver_laps):
    return driver_laps.get_car_data().add_distance()


def driver_color(driver_lap, session_tel):
    return fastf1.plotting.get_team_color(driver_lap["Team"], session=session_tel)
