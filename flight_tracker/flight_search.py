import requests
import dotenv
import os

dotenv.load_dotenv()
api_key = os.getenv('KIWI_KEY')

kiwi_url = 'https://tequila-api.kiwi.com/v2/search'
kiwi_headers = {
    'apikey': api_key
}


class FlightSearch:
    def __init__(self):
        self.api_url = kiwi_url
        self.headers = kiwi_headers

    def search_flights(self, from_city, to_city, date_from, date_to):
        params = {
            'fly_from': from_city,
            'fly_to': to_city,
            'date_from': date_from,
            'date_to': date_to,
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'flight_type': 'round',
            'adults': 1,
            'curr': 'GBP',
            'max_stopovers': 0,
            'one_for_city': 1,
            'price_to': '',
            'sort': 'price',
            'asc': 1,
            'limit': 1,
        }
        response = requests.get(self.api_url, params=params, headers=self.headers)
        response.raise_for_status()
        return response.json()['data'][0]
