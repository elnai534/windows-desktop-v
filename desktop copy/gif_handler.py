import tkinter as tk
import random
import os 

def load_gifs(impath="assets"):
    """
    Load all GIF animations from the assets folder.

    :param impath: Relative path to the assets folder
    :return: Dictionary of loaded animations
    """
    # Construct the full path to the GIF file
    path = os.path.join(impath, "wavingOP.gif")
    print(f"Loading file: {path}")

    # Check if the file exists
    if not os.path.exists(path):
        raise FileNotFoundError(f"The file {path} does not exist.")

    # Load the GIF frames
    return {
        'wavingOP': [tk.PhotoImage(file=path, format=f"gif -index {i}") for i in range(13)],  # Adjust range based on frames in wavingOP.gif
    }

def gif_work(cycle, frames, event_number, first_num, last_num):
    """
    Handle the cycling of frames in the GIF animation.

    :param cycle: Current frame index
    :param frames: List of frames in the GIF
    :param event_number: Current event number
    :param first_num: Minimum random event number
    :param last_num: Maximum random event number
    :return: Updated cycle and event_number
    """
    if cycle < len(frames) - 1:
        cycle += 1
    else:
        cycle = 0
        event_number = random.randint(first_num, last_num)
    return cycle, event_number

def update_frame(cycle, check, event_number, x, window, label, gifs):
   # frames = gifs.get('idle') if check == 0 else gifs.get('walk_positive')  # Add conditions for other actions
    frames = gifs.get('wavingOP')
    frame = frames[cycle]
    cycle, event_number = gif_work(cycle, frames, event_number, 1, 9)

    window.geometry(f'100x100+{x}+1050')
    label.configure(image=frame)
    window.after(100, update_frame, cycle, check, event_number, x, window, label, gifs)