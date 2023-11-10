import smtplib
import datetime as dt
import pandas as pd
import random
from dotenv import load_dotenv
import os

now = dt.datetime.now()
current_dow = dt.datetime.now().weekday()
print(current_dow)

# data = pd.read_csv("birthdays.csv")

with open("quotes.txt") as file:
    list_of_quotes = [line.strip() for line in file.readlines()]

# print(list_of_quotes)
quote = random.choice(list_of_quotes)
print(quote)


load_dotenv()

my_email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

if current_dow == 4:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="jonathandedman@googlemail.com", msg=f"Subject:Hello\n\n{quote}")
