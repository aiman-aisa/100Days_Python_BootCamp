#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager


dataManager = DataManager()
sheet_data = dataManager.get_destination_data()
print(sheet_data)

for row in sheet_data:
    if not row['iataCode']:
        from flight_search import FlightSearch
        flight_search = FlightSearch()
        row['iataCode'] = flight_search.get_destination_code(row['city'])

print(sheet_data)

dataManager.destination_data = sheet_data
dataManager.update_destination_data()