from tkinter import *
from tkinter import messagebox
import pandas as pd
import random
import string
import pyperclip
import os
import json

# Create a new virtual environment using the python3 -m venv command. For example, to create a new virtual environment named venv, you can run the following command:

# Activate the virtual environment using the source command and the path to the activate script in the virtual environment's bin directory. For example, to activate the venv virtual environment, you can run the following command:

# After running this command, you should see the name of the virtual environment in your terminal prompt, indicating that the virtual environment is active.

# Note that you will need to activate the virtual environment every time you open a new terminal window or start a new session.
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()_+-="
    password_list = [random.choice(alphabet) for _ in range(16)]
    password = "".join(password_list).strip()
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def open_file():
    try:
        with open("data.json", mode="r") as data_file:
            # json.dump(new_data, data_file, indent=4)
            # Reading old data
            data = json.load(data_file)
            # Updating old data with new data
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    return data


def save():

    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email_username,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return
    # else:
    #     is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email_username} \nPassword: {password} \nIs it ok to save?")

    # if is_ok == False:
    #     return
    else:
        try:
            with open("data.json", mode="r") as data_file:
                # json.dump(new_data, data_file, indent=4)
                # Reading old data
                data = json.load(data_file)
                # Updating old data with new data
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        #for csv file
        # new_data = {
        #     "website": [website],
        #     "email/username": [email_username],
        #     "password": [password]
        # }

        # df = pd.DataFrame(new_data, columns=["website", "email/username", "password"])
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()
# for csv file
    # if not os.path.isfile("passwords.csv"):
    #     df.to_csv("passwords.csv", mode="w", header=True, index=False)
    # else:
    #     df.to_csv("passwords.csv", mode="a", header=False, index=False)
    messagebox.showinfo(title="Success", message="Your password has been saved and copied to clipboard!")
    pyperclip.copy(password)

# ---------------------------- FIND PASSWORD -------------------------- #

def find_password():
    data = open_file()
    key = website_entry.get()
    try:
       details = data[key]
       messagebox.showinfo(title="Password found", message=f"website: {key}\n username: {details['email']}\n password: {details['password']}")
    except:
        messagebox.showinfo(title="No password found", message="no details for the website exists")
    # pyperclip.copy({details['password']})
    # messagebox.showinfo(title="password copied to clipboard")

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

website_entry =Entry(width=23)
email_username_entry = Entry(width=38)
password_entry = Entry(width=23)

# buttons

generate_button = Button(text="Generate Password", width=12, command=generate_password)
add_button = Button(text="Add", width=36, command=save)
search_button = Button(text="Search", width=12, command=find_password)

# laying out the page

canvas.grid(column=1, row=0)

website_label.grid(column=0, row=1)
email_username_label.grid(column=0, row=2)
email_username_entry.insert(0, "jonathandedman@hotmail.com")
password_label.grid(column=0, row=3)

website_entry.grid(column=1, row=1)
website_entry.focus()
email_username_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)

generate_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)
search_button.grid(column=2, row=1)


window.mainloop()
