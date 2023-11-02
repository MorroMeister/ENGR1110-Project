from matplotlib import ticker
import matplotlib.pyplot as plt
from pandas import DataFrame

"""
Plots the given columns from the dataframe and saves it to the specified file as a PNG

Returns true on success, false on failure
"""
def plot(data: DataFrame, columns: list[str], file_name: str) -> bool:
    
    #creates a figure and axis
    fig, ax = plt.subplots(layout='constrained')

    ax.xaxis.set_major_locator(ticker.MultipleLocator(12*5))
    ax.tick_params(labelrotation=90)

    for x in columns:
        
        ax.plot(data['date'], data[x])



    fig.savefig(file_name + ".png")
