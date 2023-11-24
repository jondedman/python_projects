from google_sheets_client import GoogleSheetsClient
import dotenv
from notification_manager import notication
from flight_search import FlightSearch

# create instances of classes
client = GoogleSheetsClient()
sms = notication()
flight_search = FlightSearch()

# define variables for google sheets
spreadsheet_id = '1xoQrI7jQxPorV-SjXYqwx8n17Yfob3kgsD9yVUhB2ic'
range_name = 'Sheet1!A2:A15'
# read values from google sheets to get a list of cities
values = client.read_spreadsheet(spreadsheet_id, range_name)

# flatten values from google sheets into a list by using list comprehension
flattened_values = [item for sublist in values for item in sublist]

dotenv.load_dotenv()
# read entire spreadsheet into a list of lists
full_values = client.read_spreadsheet(spreadsheet_id, 'Sheet1!A2:C15')

flight_data = {}

for sublist in full_values:
    # create a dictionary of flight data
    flight_data[sublist[0]] = {
        'airport': sublist[1],
        'cost': sublist[2]
    }


for city_code in flight_data:
    try:
        # define variables for flight search
        airport = flight_data[city_code]['airport']
        from_date = '01/01/2024'
        to_date = '01/02/2024'
        # search for flights
        data = flight_search.search_flights('LON', airport, from_date, to_date)
        # define variables for sms
        departure_airport = data['flyFrom']
        arrival_airport = data['flyTo']
        price = data['price']
        departure_date = data['route'][0]['local_departure'].split("T")
        return_date = data['route'][1]['local_departure'].split("T")
        # print results
        print(f'flying from London {data["flyFrom"]} to {city_code} which is {data["cityTo"]} and costs £{data["price"]} on {data["route"][0]["local_departure"].split("T")[0]}')
        # send sms
        sms.send_sms(f'found a cheaper flight to {city_code} for £{price} from {departure_airport} to {arrival_airport} on {departure_date} to {return_date}')
    except IndexError:
        print(f'No flights found for {city_code}')
