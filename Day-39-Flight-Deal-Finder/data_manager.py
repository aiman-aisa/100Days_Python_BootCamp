from pprint import pprint
import requests
from config import APIKEY, APISECRET, BEARER

SHEET_ENDPOINT = "https://api.sheety.co/efbbf3aa2103139d2e4fb1ec3c7c4e8d/flightDeals/prices"


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    
    def __init__(self):
        self.headers = {
            "Authorization": BEARER
        }
        self.destination_data = {}
    
    def get_destination_data(self):
        response = requests.get(url=SHEET_ENDPOINT, headers=self.headers)
        #print(response.text)
        data = response.json()
        self.destination_data = data["prices"]
        #pprint(data)
        
        return self.destination_data
    
    def update_destination_data(self):
        for city in self.destination_data:
            new_data = {
                "price":{
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEET_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.headers
                )
            print(response.text)