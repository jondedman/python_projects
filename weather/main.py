import requests
from dotenv import load_dotenv
import os
import datetime as dt
import json

# Open the JSON file and load the data into a variable
# with open('test_data.json') as f:
#     data = json.load(f)

# Print the data to verify it was loaded correctly


# utc_timestamp = data['hourly'][1]['dt']
# date_time = dt.datetime.fromtimestamp(utc_timestamp)
# print(date_time.strftime("%H:%M"))

now = dt.datetime.now()
# print(now.hour)

# rain_hours = []
# for hour in range(0, 12):
#     # print(data['hourly']['dt'])
#     if data['hourly'][hour]['pop'] > 0.5 and data['hourly'][hour]['dt'] > now.hour:
#         print(f"Rain at {hour}:00 hours")

load_dotenv()

API_KEY = os.getenv("API_KEY")

end_point = "https://api.openweathermap.org/data/3.0/onecall?"

parameters = {
    "lat": 51.472160,
    "lon": -0.165410,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(end_point, params=parameters)

# print(response.status_code)
data = response.json()
# print(data)
weather_slice = data['hourly'][:12]
# print(weather_slice[0])



for hour_data in weather_slice:
    time = dt.datetime.fromtimestamp(hour_data['dt'])
    probability = (hour_data['pop']) * 100
    if hour_data['pop'] > 0.5 and time > now:
        time = dt.datetime.fromtimestamp(hour_data['dt'])
        print(f"Rain at {time} with {probability}% chance")
