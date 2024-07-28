# import 

import requests
import json
import win32com.client
import win32com.client

api_key = "9e9620c1f8b0433ba2a142509242707"

def speak(text):
    
    #create a win32com.clinet Dispatch object and adding the voice command 
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    
    #speaker calling speak function and passing data as text 
    speaker.speak(text)


city = str(input("Enter city name or place name :"))

url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=yes"

data = requests.get(url)

wdata = json.loads(data.text)

temp_c = wdata["current"] ["temp_c"]
temp_f = temp_c * 10

location = wdata["location"]["name"]

print ( f"Temperature sample data  {temp_f}")
print (f"location {location}")
print (wdata["current"] ["temp_c"] )

speak(f"using weather api the Weather Data is Loaction : {location} and tempeture is {temp_c}")



