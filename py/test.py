import sys
import os
import json

from time import time

import requests
import googlemaps


tic=time()


#Select the files with the creedentials
print(os.getcwd())
config_file="../../configuration/log_credential/api_credentials.json"
with open(config_file) as json_data:
    data_config = json.load(json_data)


api_access_googlegeoloc=data_config["google_geoloc"]#api key geolocation app of google
api_access_darksky=data_config["dark_sky"]#dark sky api key

latitude_longitude=None

location="Hove,UK"#test location
try:
    gmaps = googlemaps.Client(key=api_access_googlegeoloc)  # Opening of the google maps client from https://github.com/googlemaps/google-maps-services-python
    geocode_result=gmaps.geocode(location)#GET the informations from the google maps api for the specific location by gmaps
    latitude_longitude=geocode_result[0]["geometry"]["location"]#Select the geolocation(latitude and longitude) data from the google maps api response
    print(latitude_longitude)
except:
    print("Problem to collect the data from the google maps api")

if latitude_longitude!=None:
    darksky_request="https://api.darksky.net/forecast/"#Basic url to collect to the api for the get request
    darksky_request_api=darksky_request+api_access_darksky+"/"#Add the api key to the basic url
    darksky_request_api_complete=darksky_request_api+str(latitude_longitude['lat'])+","+str(latitude_longitude['lng'])#Add the latitude and longitude to the url for the get request
    response=(requests.get(darksky_request_api_complete).json())#Execute the get request + transforn the response in json
    print(response)



toc=time()
print("ES(s):"+str(toc-tic))