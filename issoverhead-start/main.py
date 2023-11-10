import requests
from datetime import datetime
import smtplib
from dotenv import load_dotenv
import os
import time

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

def is_iss_close():
    if iss_latitude in range(int(MY_LAT - 5), int(MY_LAT + 5)) and iss_longitude in range(int(MY_LONG - 5), int(MY_LONG + 5)):
        return True
    else:
        return False

def is_dark():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True
    else:
        return False

load_dotenv()

def send_email():
    my_email = os.getenv("MY_EMAIL")
    password = os.getenv("PASSWORD")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="jonathandedman@googlemail.com",
            msg="Subject: Look Up\n\nThe ISS is above you in the sky."
        )



response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
while True:
    time.sleep(60)
    print("Checking...")
    print(iss_latitude, iss_longitude)
    print(MY_LAT, MY_LONG)
    if is_iss_close() and is_dark():
        print("Look up!")
        send_email()


# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
