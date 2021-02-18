import os
import requests
from datetime import datetime

inp = input("Tell me what exercise you did: ")
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
API_PARAMS = {
    "query": inp,
    "gender": "male",
    "weight_kg": 70.3,
    "height_cm": 185.4,
    "age": 30
}

response = requests.post(url=API_ENDPOINT, json=API_PARAMS, headers=headers)
response.raise_for_status()
exercises = response.json()['exercises']

data = []
date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")

url = os.environ.get("url")

header = {
    "Authorization": os.environ.get("Authorization")
}

for i in exercises:
    exercise = i['user_input']
    duration = i['duration_min']
    calories = i['nf_calories']
    json = {
        "sheet1": {
            "date": date,
            "time": time,
            "exercise": exercise.title(),
            "duration": duration,
            "calories": calories
        }
    }
    response = requests.post(url=url, json=json, headers=header)
    response.raise_for_status()
