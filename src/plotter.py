from matplotlib import ticker
import matplotlib.pyplot as plt
from pandas import DataFrame

"""
Plots the given columns from the dataframe and saves it to the specified file as a PNG

Returns true on success, false on failure
"""
def plot(data: DataFrame, columns: list[str], file_name: str) -> bool:
    # Creates a figure and axis
    fig, ax = plt.subplots(layout="constrained")

    # Setup axis formatting
    ax.xaxis.set_major_locator(ticker.MultipleLocator(12*5))
    ax.tick_params(labelrotation=90)

    # Plot columns
    for y in columns:
        ax.plot(data["date"], data[y])

    #sets x-axis limits to match the data range
    ax.set_xlim(data["date"].min(), data["date"].max())

    #Sets custom range for x-tick marks
    #sets ticks for every 60 units
    ax.set_xticks(range(0, len(data["date"]), 60))



    # Save as image
    fig.savefig(file_name + ".png")
    return True
