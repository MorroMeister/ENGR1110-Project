from pandas import DataFrame
from pyray import *
from os import remove
from plotter import plot

TITLE = "Group 3 Project"
FONT_SIZE = 24
PADDING = 8
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
    # Set size
    set_window_size(w, h)

    # Set position
    m = get_current_monitor()
    sw = get_monitor_width(m)
    sh = get_monitor_height(m)
    set_window_position((sw - w) // 2, (sh - h) // 2)

"""
Draws a button
Returns if the button has been clicked
"""
def draw_button(x: int, y: int, text: str, width: int | None = None, highlight: bool = False) -> bool:
    # Measure text size, then use that size if no width was provided
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
Returns the selected columns, or None if the X was clicked
"""
def choose_columns() -> [str]:
    # Setup window size
    WIDTH = 500
    num_rows = 1 + len(COLUMNS) + 1 # header + columns + ok button
    row_height = BUTTON_HEIGHT + (2 * PADDING)
    height = PADDING + (num_rows * row_height) + PADDING
    set_size_and_center(WIDTH, height)

    # Setup some info
    HEADER = "Choose Columns"
    HEADER_X = (WIDTH - measure_text(HEADER, FONT_SIZE)) // 2
    INVALID_SELECTION = "Please select 1 or more columns"
    INVALID_SELECTION_X = (WIDTH - measure_text(INVALID_SELECTION, FONT_SIZE)) // 2

    ok_pressed = False
    selected = [False] * len(COLUMNS)
    while not window_should_close() and not ok_pressed:
        begin_drawing()
        clear_background(WHITE)
        for i in range(num_rows):
            # Draw header
            if i == 0:
                draw_text(HEADER, HEADER_X, PADDING * 2, FONT_SIZE, BLACK)
                continue
            y = PADDING + (row_height * i)
            
            # Draw OK button
            is_valid_selection = False
            for j in selected:
                is_valid_selection |= j
            if i == num_rows - 1:
                if not is_valid_selection:
                    draw_text(INVALID_SELECTION, INVALID_SELECTION_X, y + PADDING, FONT_SIZE, BLACK)
                elif draw_button(PADDING, y, "OK", width=WIDTH - (2 * PADDING)):
                    ok_pressed = True
                    break
                continue

            # Draw column button
            col = COLUMNS[i - 1]
            if draw_button(PADDING, y, col[0], highlight=selected[i - 1]):
                selected[i - 1] = not selected[i - 1]
        end_drawing()

    if not ok_pressed:
        return None

    # Convert bool array to columns  names
    columns = []
    for i, b in enumerate(selected):
        if b:
            columns.append(COLUMNS[i][1])
    return columns

"""
Shows an image to the user
Returns if the X was clicked
"""
def show_image(file: str) -> bool:
    img = load_texture(file)
    set_size_and_center(img.width + (2 * PADDING), PADDING + img.height + PADDING + BUTTON_HEIGHT + PADDING)
    back_pressed = False
    while not window_should_close() and not back_pressed:
        begin_drawing()
        clear_background(WHITE)

        draw_texture(img, PADDING, PADDING, WHITE)
        if draw_button(PADDING, PADDING + img.height + PADDING, "Back", width=img.width):
            back_pressed = True
        
        end_drawing()
    unload_texture(img)
    return not back_pressed

"""
The entrypoint for the GUI
"""
def open_gui(data: DataFrame) -> None:
    print("Setting up gui")
    set_trace_log_level(TraceLogLevel.LOG_NONE)
    # Setup arbitrary size, this will be updated later
    init_window(100, 100, TITLE)
    set_exit_key(0)
    while not window_should_close():
        # Pick columns
        print("Opening column selector")
        set_window_title(f"{TITLE} | Choose columns")
        cols = choose_columns()
        if cols == None:
            print("User pressed the X, exiting")
            break

        # Plot
        print(f"Plotting columns: {cols}")
        set_window_title(f"{TITLE} | View Graph")
        FILE_NAME = "temp_file"
        if not plot(data, cols, FILE_NAME):
            raise "Failed to plot"
        FILE_NAME += ".png"
        
        # Show the image
        print("Showing image")
        x_clicked = show_image(FILE_NAME)
        print("Deleteing temporary image file")
        remove(FILE_NAME)
        if x_clicked:
            print("User pressed the X, exiting")
            break
    print("Cleaning up window")
    close_window()