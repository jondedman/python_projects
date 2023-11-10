import requests
from datetime import datetime

MY_LAT = 51.507351
MY_LONG = -0.127758
def get_sunrise_sunset():
    response = requests.get(url=f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LONG}&formatted=0")
    response.raise_for_status()
    data = response.json()
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    print(sunset)
    print(sunrise)
    time_now = datetime.now()
    print(time_now.hour)

get_sunrise_sunset()
