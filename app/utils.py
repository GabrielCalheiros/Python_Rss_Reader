import shutil


def print_line():
    # Get the width of the screen
    screen_width = shutil.get_terminal_size().columns
    # Print a separator
    print("-" * screen_width)
