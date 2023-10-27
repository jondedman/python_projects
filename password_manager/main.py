from tkinter import *
from tkinter import messagebox
import pandas as pd
import os
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
# column_names = ["website", "email/username", "password"]
# password_data = pd.DataFrame(columns=column_names)
# password_data.to_csv("passwords.csv", index=False)

def save():


    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email_username} \nPassword: {password} \nIs it ok to save?")

    if is_ok == False:
        return
    else:
        new_data = {
            "website": [website],
            "email/username": [email_username],
            "password": [password]
        }

        df = pd.DataFrame(new_data)
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()
    df.to_csv("passwords.csv", mode="a", header=False, index=False)






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

# entries

website_entry =Entry(width=38)
email_username_entry = Entry(width=38)
password_entry = Entry(width=21)

# buttons

generate_button = Button(text="Generate Password")
add_button = Button(text="Add", width=36, command=save)

# laying out the page

canvas.grid(column=1, row=0)

website_label.grid(column=0, row=1)
email_username_label.grid(column=0, row=2)
email_username_entry.insert(0, "jonathandedman@hotmail.com")
password_label.grid(column=0, row=3)

website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_username_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)

generate_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
