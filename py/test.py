import sys
import os
import json

from time import time

import requests
import googlemaps

def Httprequest(url,mode="POST", param=None,dat=None):
    #Based on lnetatmo
    headers={
        "charset":"UTF-8",
        "cache-control":"no-cache",
        "content-type":"application/x-www-form-urlencoded",
    }
    try:
        response=requests.request(mode,url,params=param,data=dat,heqders=headers)
        return response.json()
    except:
        return None




tic=time()
print(os.getcwd())
config_file="../../configuration/log_credential/api_credentials.json"
with open(config_file) as json_data:
    data_config = json.load(json_data)


api_access_googlegeoloc=data_config["google_geoloc"]
api_access_darksky=data_config["dark_sky"]


gmaps = googlemaps.Client(key=api_access_googlegeoloc)
#https://github.com/googlemaps/google-maps-services-python
# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))


location="Hove,UK"
geocode_result=gmaps.geocode(location)

latitude_longitude=geocode_result[0]["geometry"]["location"]
print(latitude_longitude)

darksky_request="https://api.darksky.net/forecast/"

darksky_request_api=darksky_request+api_access_darksky+"/"

darksky_request_api_complete=darksky_request_api+str(latitude_longitude['lat'])+","+str(latitude_longitude['lng'])
timestamp=time()
req=(requests.get(darksky_request_api_complete).json())
print(req)



toc=time()
print("ES(s):"+str(toc-tic))