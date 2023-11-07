from pandas import DataFrame
from pyray import *
import plotter

TITLE = "Group 3 Project"
FONT_SIZE = 16
PADDING = 4
COLUMNS = [
    ("Total % Unemployment", "unrate"),
    ("Male % Unemployment", "unrate_men"),
    ("Female % Unemployment", "unrate_women"),
    # TODO: more columns here
]

"""
Sets the size of the window and exits
"""
def set_size_and_center(w: int, h: int) -> None:
    raise "TODO"

"""
Opens a menu where the user can choose columns to plot
Returns the selected columns
"""
def choose_columns() -> [str]:
    raise "TODO"

"""
The entrypoint for the GUI
"""
def open_gui(data: DataFrame) -> None:
    raise "TODO"