import requests
import os
from datetime import datetime

from dotenv import load_dotenv
load_dotenv()
# db_url = os.getenv('DATABASE_URL')
# print(db_url)

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv('MY_OWM_API_KEY')



weather_params = {
    "lat": 48.6667,
    "lon": 21.3333,
    "appid": api_key,
}



response = requests.get(OWM_Endpoint, weather_params, verify=False)
response.raise_for_status()

data = response.json()

for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    need_umbrella = condition_code < 700
    umbrella_text = "You will need an umbrella ! ☔" if need_umbrella else "No need to take an umbrella 🌂"
    
    date_obj = datetime.strptime(hour_data["dt_txt"], "%Y-%m-%d %H:%M:%S")
    Day = date_obj.strftime("%A")
    TIME = date_obj.strftime("%H:%M")
    
    print(f'{Day:<10} | ⏰: {TIME} | weather: {hour_data["weather"][0]["description"]+".":<20} | {umbrella_text}')
    
