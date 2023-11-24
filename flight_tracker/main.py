from google_sheets_client import GoogleSheetsClient
import requests
import dotenv
import os
from notification_manager import notication



# -------------- get list of cities from google sheet --------------
# Google Sheets API
client = GoogleSheetsClient()
sms = notication()



spreadsheet_id = '1xoQrI7jQxPorV-SjXYqwx8n17Yfob3kgsD9yVUhB2ic'
range_name = 'Sheet1!A2:A15'

values = client.read_spreadsheet(spreadsheet_id, range_name)

# flattened list of cities
flattened_values = [item for sublist in values for item in sublist]
# print(flattened_values)

dotenv.load_dotenv()
# -------------- call kiwi api with list of cities --------------
# Kiwi API
kiwi_url = 'https://api.tequila.kiwi.com/locations/query'
kiwi_key = os.getenv('KIWI_KEY')


kiwi_headers = {
    'apikey': kiwi_key
}

# # print(kiwi_headers)
# kiwi_params = {
# 'term': '',
# 'location_types': 'airport',
# 'limit': 4,
# }

city_codes = []

# for city in flattened_values:
#     kiwi_params['term'] = city
#     response = requests.get(kiwi_url, params=kiwi_params, headers=kiwi_headers)
#     response.raise_for_status()
#     data = response.json()
#     city_code = data['locations'][0]['code']
#     city_codes.append([city_code])

# print(city_codes)


# new_range_name = 'Sheet1!B2:B15'


# client.write_spreadsheet(spreadsheet_id, new_range_name, city_codes)


# -------------- perform flight search with list of city codes --------------

# Kiwi API

kiwi_url = 'https://api.tequila.kiwi.com/v2/search'

kiwi_headers = {
    'apikey': kiwi_key
}

kiwi_params = {
    'fly_from': 'LON',
    'fly_to': '',
    'date_from': '01/01/2024',
    'date_to': '01/03/2024',
    'flight_type': 'round',
    'adults': 1,
    'curr': 'GBP',
    'max_stopovers': 0,
    'nights_in_dst_from': 7,
    'nights_in_dst_to': 28,
    'one_for_city': 1,
    'price_to': '',
    'sort': 'price',
    'asc': 1,
    'limit': 10,
}


full_values = client.read_spreadsheet(spreadsheet_id, 'Sheet1!A2:C15')

flight_data = {}
for sublist in full_values:
    flight_data[sublist[0]] = {
        'airport': sublist[1],
        'cost': sublist[2]
    }

print(flight_data)


for city_code in flight_data:
    try:
        kiwi_params['fly_to'] = flight_data[city_code]['airport']
        kiwi_params['price_to'] = flight_data[city_code]['cost']
        response = requests.get(kiwi_url, params=kiwi_params, headers=kiwi_headers)
        response.raise_for_status()

        data = response.json()
        departure_airport = data['data'][0]['flyFrom']
        arrival_airport = data['data'][0]['flyTo']
        price = data['data'][0]['price']
        departure_date = data['data'][0]['route'][0]['local_departure'].split("T")[0]
        return_date = data['data'][0]['route'][1]['local_departure'].split("T")[0]
        print(f'flying from London {data["data"][0]["flyFrom"]} to {city_code} which is {data["data"][0]["cityTo"]} and costs £{data["data"][0]["price"]} on {data["data"][0]["route"][0]["local_departure"].split("T")[0]}')
        # if price < flight_data[city_code]['cost']:
        #     print(f'found a cheaper flight to {city_code} for £{price}')
        sms.send_sms(f'found a cheaper flight to {city_code} for £{price} from {departure_airport} to {arrival_airport} on {departure_date} to {return_date}')
    except IndexError:
        print(f'No flights found for {city_code}')




# cost_values = client.read_spreadsheet(spreadsheet_id, 'Sheet1!C2:C15')
# flattened_cost_values = [item for sublist in cost_values for item in sublist]

# The provided code snippet is a for loop that uses the zip function to iterate over two lists simultaneously.

# The zip function takes multiple iterables (in this case, flattened_city_codes and flattened_cost_values) and returns an iterator that generates tuples containing elements from each iterable. Each tuple represents a pair of corresponding elements from the input iterables.

# In the for loop, the loop variable city_code will take on the values from flattened_city_codes, and the loop variable cost will take on the values from flattened_cost_values. The loop will iterate over the length of the shortest input iterable, stopping when either flattened_city_codes or flattened_cost_values is exhausted.


# for city_code, cost in zip(flattened_city_codes, flattened_cost_values):
#     if cost
# sms.send_sms('test message')
