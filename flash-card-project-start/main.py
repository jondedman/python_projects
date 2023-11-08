from tkinter import *
import os
from tkinter import messagebox
import pandas as pd
import random



BACKGROUND_COLOR = "#B1DDC6"

# open csv
try:
    df = pd.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    df = pd.read_csv('./data/french_words.csv')

to_learn = df.to_dict(orient='records')

# french_words = list(df.French)

def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    new_word = current_card["French"]
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=new_word, fill="black")
    canvas.itemconfig(pic, image=card_front)
    flip_timer = window.after(3000, flip)



def correct():
    to_learn.remove(current_card)
    df = pd.DataFrame(to_learn)
    df.to_csv('./data/words_to_learn.csv', index=False)
    next_card()



def flip():
    flip_word = current_card["English"]
    canvas.itemconfig(pic, image=card_back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=flip_word, fill="white")


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
card_back =  PhotoImage(file="images/card_back.png")
pic = canvas.create_image(400, 263, image=card_front)

# ---------------------------- UI SETUP ------------------------------- #


title = canvas.create_text(400, 50, text="French", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))


# Buttons
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=correct)
right_button.grid(column=1, row=1)


canvas.grid(column=0, row=0, columnspan=2)

flip_timer = window.after(3000, flip)
next_card()





window.mainloop()
