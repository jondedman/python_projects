import requests

class FlightSearch:
    def __init__(self, api_url, headers):
        self.api_url = api_url
        self.headers = headers

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
