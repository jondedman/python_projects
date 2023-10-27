from tkinter import *
import os
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200,highlightthickness=0)

#---------------------------- Set up for packaging ------------------- #
script_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the relative path to the image file
rel_path = "logo.png"

# Construct the absolute file path
abs_file_path = os.path.join(script_dir, rel_path)

# image set up
padlock = PhotoImage(file=abs_file_path)
canvas.create_image(100, 100, image=padlock)


# Labels

website_label = Label(text="Website:")
email_username_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

# inputs

website_entry =Entry(width=38)
email_username_entry = Entry(width=38)
password_entry = Entry(width=21)

# buttons

generate_button = Button(text="Generate Password")
add_button = Button(text="Add", width=36)

# laying out the page

canvas.grid(column=1, row=0)

website_label.grid(column=0, row=1)
email_username_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

website_entry.grid(column=1, row=1, columnspan=2)
email_username_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)

generate_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
