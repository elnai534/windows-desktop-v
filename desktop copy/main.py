import os
import tkinter as tk
from config import impath, x, cycle, check, event_number
from gif_handler import load_gifs
from events import event

os.environ["TK_SILENCE_DEPRECATION"] = "1"

# Initialize tkinter window
window = tk.Tk()
window.config(highlightbackground="black")
window.overrideredirect(True)
# window.attributes("-alpha", 0.0)#transparency for MAC
window.wm_attributes("-transparentcolor", "black")

# Load GIFs
gifs = load_gifs(impath)

# Create and pack label for displaying GIFs
label = tk.Label(window, bd=0, bg="black")
label.pack()

# Start event loop
window.after(1, event, cycle, check, event_number, x, window, label, gifs)

# Run the main tkinter loop
window.mainloop()