import requests
import dotenv
import os
import json
import time
import datetime

dotenv.load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"

# user_params = {
#     "token": os.getenv("PIXELA_TOKEN"),
#     "username": os.getenv("PIXELA_USERNAME"),
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{os.getenv('PIXELA_USERNAME')}/graphs"

graph_config = {
    "id": "graph3",
    "name": "Coding Graph",
    "unit": "min",
    "type": "int",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": os.getenv("PIXELA_TOKEN")
}



# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{os.getenv('PIXELA_USERNAME')}/graphs/graph3"

today = datetime.datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "60"
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

# My url

# https://pixe.la/v1/users/jonnydedman/graphs/graph3.html

# Put

update_endpoint = f"{pixela_endpoint}/{os.getenv('PIXELA_USERNAME')}/graphs/graph3/{today.strftime('%Y%m%d')}"

update_config = {
    "quantity": "30"
}

# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)

# Delete
response = requests.delete(url=f"{pixel_endpoint}/{today.strftime('%Y%m%d')}", headers=headers)
print(response.text)

# interact
