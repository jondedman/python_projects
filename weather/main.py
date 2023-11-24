import requests
from dotenv import load_dotenv
import os
import datetime as dt
from twilio.rest import Client





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

# print(f"Connecting to openweather api with status code: {response.status_code}")
data = response.json()
print(data)
weather_slice = data['hourly'][:12]
print(weather_slice[0])

    # Twillio API

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN
client = Client(account_sid, auth_token)



with open('/Users/jondedman/code/jondedman/python_projects/weather/output.txt', 'w') as f:
    f.write(f"{now} Rain report\n____________________\n")

for hour_data in weather_slice:
    time = dt.datetime.fromtimestamp(hour_data['dt'])
    probability = (hour_data['pop']) * 100
    if hour_data['pop'] > 0.6 and time > now and hour_data['weather'][0]['id'] < 700:
        time = dt.datetime.fromtimestamp(hour_data['dt'])
        description = hour_data['weather'][0]['description']
        message = client.messages.create(
        from_='+447481343542',
        body=(f'IT IS GOING TO RAIN AT {time} WITH {probability}% CHANCE\nDESCRIPTION: {description} ☔️'),
        to='+447932563406'
        )

        print(message.sid)
        try:
            with open('/Users/jondedman/code/jondedman/python_projects/weather/output.txt', 'a') as f:
                f.write(f"Rain at {time} with {probability}% chance\n Description: {description} ☔️\n")
        except:
            print("An error occurred")

try:
    with open('/Users/jondedman/code/jondedman/python_projects/weather/output.txt', 'a') as f:
        f.write(f"_______________\n{now} End of rain report\n")
except Exception as e:
    print(f"An error occurred: {e}")



# ----------------------------- PLIST FILE saved in /Library/LaunchAgents for reference -----------------------------

# <?xml version="1.0" encoding="UTF-8"?>
# <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
# <plist version="1.0">
# <dict>
#     <key>Label</key>
#     <string>com.jondedman.weatherchecker</string>
#     <key>ProgramArguments</key>
#     <array>
#         <string>full path</string>
#         <string>full path</string>
#     </array>
#     <key>EnvironmentVariables</key>
#     <dict>
#         <key>API_KEY</key>
#         <string>in full</string>
#     </dict>
#     <key>StartInterval</key>
#     <integer>3600</integer>
#     <key>RunAtLoad</key>
#     <true/>
#     <key>StandardErrorPath</key>
#     <string>full path to log file</string>
# </dict>
# </plist>
