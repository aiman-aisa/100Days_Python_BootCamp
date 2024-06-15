#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager

dataManager = DataManager()
sheet_data = dataManager.get_destination_data()
print(sheet_data)