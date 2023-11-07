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

def set_size_and_center(w: int, h: int):
    raise "TODO"

def choose_columns() -> [str]:
    raise "TODO"

def open_gui(data: DataFrame):
    raise "TODO"