import boto3
from datetime import datetime
import requests
from api_keys import WEATHER_API_KEY
session = boto3.Session(region_name="us-west-2")

# Initialize the Lex client
lex_client = session.client('lexv2-runtime')

# User input
user_input = input("Q: ")

# Send user input to Lex
response = lex_client.recognize_text(
    botId='9IQHMYCHRN',
    botAliasId='TSTALIASID',
    localeId="en_US",
    sessionId="randomsession",
    text=user_input
)

def sortByConfidence(interpretation):
    if "nluConfidence" in interpretation:
        return interpretation["nluConfidence"]["score"]
    else:
        return 0

response["interpretations"].sort(key=sortByConfidence)
response["interpretations"].reverse()

intent = response["interpretations"][0]["intent"]["name"]

if intent == "Weather":
    #get ip address
    ip = requests.get("https://api.ipify.org?format=json").json()["ip"]
    #get location from ip
    location_json = requests.get(f"http://ip-api.com/json/{ip}").json()
    lat = location_json["lat"]
    lon = location_json["lon"]
    #get weather from location
    weather_json = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather"+
        f"?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}&units=imperial"
    ).json()
    location_name = weather_json["name"]
    temp_real = int(weather_json["main"]["temp"])
    temp_feels_like = int(weather_json["main"]["feels_like"])
    print(f"Right now in {location_name}, the temperature is {temp_real}° and it feels like {temp_feels_like}°")
if intent == "Time":
    #get the current date and time information
    now = datetime.now()
    #make sure it's in this order or it won't work
    # get the hour, it will be in 24 hour format
    hour = now.hour 
    #convert it to 12 hour format here
    AM_or_PM = "AM"
    if hour > 11:
        AM_or_PM = "PM"
    hour = hour % 12
    if hour == 0:
        hour = 12
    
    #respond to the user
    print(f"The time is {hour}:{now.minute} {AM_or_PM}")