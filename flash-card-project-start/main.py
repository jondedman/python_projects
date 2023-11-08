from tkinter import *
import os
from tkinter import messagebox
from PIL import Image, ImageTk


BACKGROUND_COLOR = "#B1DDC6"



# ---------------------------- CREATE WINDOW ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0)
canvas.config(background=BACKGROUND_COLOR)
# script_dir = os.path.dirname(os.path.abspath(__file__))

# # Specify the relative path to each image file


# rel_path = "images/card_front.png"


# # Construct the absolute file path
# abs_file_path = os.path.join(script_dir, rel_path)

# image set up
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front)

# ---------------------------- UI SETUP ------------------------------- #


canvas.create_text(400, 50, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

# Buttons
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(column=1, row=1)






canvas.grid(column=0, row=0, columnspan=2)



window.mainloop()
