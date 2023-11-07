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
BG_COLOR = Color(0x20, 0x20, 0x20, 0xFF) # Dark gray
FG_COLOR = WHITE # Used for text
SELECTED_COLOR = GREEN
HOVER_COLOR = GRAY

"""
Sets the size of the window and exits
"""
def set_size_and_center(w: int, h: int) -> None:
    set_window_size(w, h)
    sw = get_screen_width()
    sh = get_screen_height()
    set_window_position((sw - w) // 2, (sh - h) // 2)

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
    # Setup arbitrary size, this will be updated later
    init_window(100, 100, TITLE)
    while not window_should_close():
        begin_drawing()
        clear_background(BG_COLOR)
        end_drawing()
    close_window()