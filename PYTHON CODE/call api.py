import urllib.request as url
import json
from geopy import geocoders

location = input("Enter city/state/country :")
api_key = "cfc853693797a45dc6040da827b46d8f"
gn = geocoders.GeoName("example")
lat = gn.geocode(location)[1][0]
lon = gn.geocode(location)[1][1]

path = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"


responce = url.urlopen(path)
data = json.load(responce)
print(data["main"])