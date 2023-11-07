from pandas import DataFrame
from pyray import *
from os import remove
from plotter import plot

TITLE = "Group 3 Project"
FONT_SIZE = 16
PADDING = 4
COLUMNS = [
    ("Total % Unemployment", "unrate"),
    ("Male % Unemployment", "unrate_men"),
    ("Female % Unemployment", "unrate_women"),
    # TODO: more columns here
]
BUTTON_HEIGHT = FONT_SIZE + (2 * PADDING)

"""
Sets the size of the window and exits
"""
def set_size_and_center(w: int, h: int) -> None:
    set_window_size(w, h)
    m = get_current_monitor()
    sw = get_monitor_width(m)
    sh = get_monitor_height(m)
    set_window_position((sw - w) // 2, (sh - h) // 2)

"""
Draws a button
Returns if the button has been clicked
"""
def draw_button(x: int, y: int, text: str, width: int | None = None, highlight: bool = False) -> bool:
    text_w = measure_text(text, FONT_SIZE)
    if width == None:
        width = text_w + (2 * PADDING)
    
    # Outline
    draw_rectangle_lines(x, y, width, BUTTON_HEIGHT, BLACK)

    # Hover + click handler
    clicked = False
    mx = get_mouse_x() - x
    my = get_mouse_y() - y
    if mx >= 0 and mx <= width and my >= 0 and my <= BUTTON_HEIGHT:
        draw_rectangle(x + 1, y + 1, width - 2, BUTTON_HEIGHT - 2, GRAY)
        clicked = is_mouse_button_pressed(MouseButton.MOUSE_BUTTON_LEFT)
    # Highlight
    elif highlight:
        draw_rectangle(x + 1, y + 1, width - 2, BUTTON_HEIGHT - 2, GREEN)

    # Text
    text_x = (width - text_w) // 2
    draw_text(text, x + text_x, y + PADDING, FONT_SIZE, BLACK)

    return clicked

"""
Opens a menu where the user can choose columns to plot
Returns the selected columns
"""
def choose_columns() -> [str]:
    raise "TODO"

"""
Shows an image to the user
"""
def show_image(file: str) -> None:
    img = load_texture(file)
    set_size_and_center(img.width + (2 * PADDING), PADDING + img.height + PADDING + BUTTON_HEIGHT + PADDING)
    back_pressed = False
    while not window_should_close() and not back_pressed:
        begin_drawing()
        clear_background(WHITE)
        draw_texture(img, PADDING, PADDING, WHITE)
        if draw_button(PADDING, PADDING + img.height + PADDING, "Back", width=img.width):
            back_pressed = True
            clear_background(WHITE)
        end_drawing()
    unload_texture(img)

"""
The entrypoint for the GUI
"""
def open_gui(data: DataFrame) -> None:
    # Setup arbitrary size, this will be updated later
    init_window(100, 100, TITLE)
    set_exit_key(0)
    while not window_should_close():
        cols = ["unrate_men", "unrate_women"]#choose_columns()
        # If invalid choice then retry
        if not cols or len(cols) == 0:
            continue

        FILE_NAME = "temp_file"
        if not plot(data, cols, FILE_NAME):
            raise "Failed to plot"
        FILE_NAME += ".png"
        show_image(FILE_NAME)

        remove(FILE_NAME)
        
    close_window()