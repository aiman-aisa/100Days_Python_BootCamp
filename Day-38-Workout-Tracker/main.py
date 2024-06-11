import requests
from config import API_KEY, APP_ID, BEARER
from datetime import datetime as dt

exercise_string = input("Tell me which exercise you did: ") 
#Ran 2 miles and walked for 3km.

exercise_endpoints = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/efbbf3aa2103139d2e4fb1ec3c7c4e8d/workoutTracking/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_params = {
    "query": exercise_string
}

response = requests.post(url=exercise_endpoints, json=exercise_params, headers=headers)
exercise_dict_list = response.json()['exercises']
# print(exercise_dict_list)

currentDateAndTime = dt.now()
today_date = currentDateAndTime.strftime("%d/%m/%Y")
time_now = currentDateAndTime.strftime("%H:%M:%S")

headers = {
    "Authorization" : BEARER
}

for exercise_dict in exercise_dict_list:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": time_now,
            "exercise": exercise_dict['name'].title(),
            "duration": exercise_dict['duration_min'],
            "calories": exercise_dict['nf_calories']
            }
        }
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=headers)
    print(sheet_response.text)