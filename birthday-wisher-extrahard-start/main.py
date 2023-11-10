##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib
import os
from dotenv import load_dotenv

# create letter templates
letters = []
with open("letter_templates/letter_1.txt") as file:
    letter_1 = file.read()
    letters.append(letter_1)

with open("letter_templates/letter_2.txt") as file:
    letter_2 = file.read()
    letters.append(letter_2)

with open("letter_templates/letter_3.txt") as file:
    letter_3 = file.read()
    letters.append(letter_3)

# open birthdays.csv
data = pandas.read_csv("birthdays.csv")
# set today's date
today = dt.datetime.now().date()
# load email and password from .env file
load_dotenv()

my_email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

# 2. Check if today matches a birthday in the birthdays.csv and if so, pick a random letter template and replace the [NAME] with the person's actual name from birthdays.csv
for index, row in data.iterrows():
    if today.day == row.day and today.month == row.month:
        recipient = row["name"]
        random_letter = random.choice(letters)
        random_letter = random_letter.replace("[NAME]", recipient)
        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="jonathandedman@googlemail.com", msg=f"Subject:Happy Birthday\n\n{random_letter}")
