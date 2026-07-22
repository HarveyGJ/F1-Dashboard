import seaborn as sns
import matplotlib.pyplot as plt

import fastf1
import fastf1.plotting

fastf1.plotting.setup_mpl(mpl_timedelta_support=True, color_scheme="fastf1")

def lap_time_distributions(session, driver_selection):
    race = session
    d_selection = driver_selection


    driver_laps = race.laps.pick_drivers(d_selection).pick_quicklaps()
    driver_laps = driver_laps.reset_index()

    finishing_order = [race.get_driver(i)["Abbreviation"] for i in d_selection]
    print(finishing_order)

    fig, ax = plt.subplots(figsize=(10,5))
    driver_laps["LapTime(s)"] = driver_laps["LapTime"].dt.total_seconds()

    sns.violinplot(data=driver_laps,
                x="Driver",
                y="LapTime(s)",
                hue="Driver",
                inner=None,
                density_norm="area",
                order=finishing_order,
                palette=fastf1.plotting.get_driver_color_mapping(session=race))

    sns.swarmplot(data=driver_laps,
                x="Driver",
                y="LapTime(s)",
                order=finishing_order,
                hue="Compound",
                palette=fastf1.plotting.get_compound_mapping(session=race),
                hue_order=["SOFT", "MEDIUM", "HARD"],
                linewidth=0,
                size=4)

    ax.set_xlabel("Driver")
    ax.set_ylabel("Lap Time (s)")
    plt.suptitle(f"{race}, Lap Time Distributions")
    sns.despine(left=True,bottom=True)

    plt.tight_layout()
    return fig 