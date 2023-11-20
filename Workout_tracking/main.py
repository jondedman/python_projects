import requests
import dotenv
import os
import datetime
from google_sheets_client import GoogleSheetsClient

dotenv.load_dotenv()

# API Key
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("APP_KEY")

DATE = datetime.datetime.now().strftime("%d/%m/%Y")
GENDER = "Male"
WEIGHT_KG = 75
HEIGHT_CM = 173
AGE = 47
# API URL endpoint

end_point = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
}

request_body = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=end_point, json=request_body, headers=headers)
response.raise_for_status()
print(response.status_code)
result = response.json()
print(result)


# example result:
# {'exercises': [{'tag_id': 317, 'user_input': 'run', 'duration_min': 30, 'met': 9.8, 'nf_calories': 367.5, 'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg', 'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg', 'is_user_uploaded': False}, 'compendium_code': 12050, 'name': 'running', 'description': None, 'benefits': None}]}


client = GoogleSheetsClient()
SPREADSHEET_ID = "1hHfy9H14WUrsqvGIgaWG6MvB55h5R-Me_n-fMF8PY8k"
values = [
    [
        "Date",
        "Exercise",
        "Duration",
        "Calories",
    ],
    [
        DATE,
        result["exercises"][0]["name"],
        result["exercises"][0]["duration_min"],
        result["exercises"][0]["nf_calories"],
    ],
]

updated_values = [
    [
        DATE,
        result["exercises"][0]["name"],
        result["exercises"][0]["duration_min"],
        result["exercises"][0]["nf_calories"],
    ],
]
# overwrite the first row
def overwrite_spreadsheet():
    client.write_spreadsheet(SPREADSHEET_ID, "Sheet1!A1", values)

# append a new row
def append_spreadsheet():
    client.append_spreadsheet(SPREADSHEET_ID, "Sheet1!A1", updated_values)

append_spreadsheet()
