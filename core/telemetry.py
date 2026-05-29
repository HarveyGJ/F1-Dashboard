import fastf1.plotting
import matplotlib.pyplot as plt
import streamlit as st

fastf1.Cache.enable_cache("./cache")

fastf1.plotting.setup_mpl(mpl_timedelta_support=True, color_scheme="fastf1")

# dynamically assign variables to names of drivers then discard after ive processed the telemetry


def process_tel(session_tel, driver_selection):

    fig, ax = plt.subplots(figsize=(10, 4))
    for driver in driver_selection:
        try:
            d_laps = driver_laps(session_tel, driver)
            d_telemetry = driver_tel(d_laps)
            d_color = driver_color(d_laps, session_tel)

            ax.plot(
                d_telemetry["Distance"],
                d_telemetry["Speed"],
                color=d_color,
                label=driver,
            )
        except:
            pass
    ax.legend()
    plt.suptitle(
        f"Fastest lap comparison \n"
        f"{session_tel.event["EventName"]} {session_tel.event.year} Race"
    )

    ax.set_xlabel("Distance in m")
    ax.set_ylabel("Speed in km/h")

    return fig


def driver_laps(session_tel, driver_name):

    return session_tel.laps.pick_drivers(driver_name).pick_fastest()


def driver_tel(driver_laps):
    return driver_laps.get_car_data().add_distance()


def driver_color(driver_lap, session_tel):
    return fastf1.plotting.get_team_color(driver_lap["Team"], session=session_tel)
