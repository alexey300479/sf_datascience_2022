"""
This module must be run before running EDA_Project_3_model_v2.ipynb
to prepare latitude and longitude dictionaries to replace
missings in hotels.csv by addresses
"""


import json
from time import sleep

import pandas as pd
from geopy.geocoders import ArcGIS
from tqdm import tqdm

hotels = pd.read_csv('hotels.csv')

addresses = hotels[hotels.lat.isna()].hotel_address.values

locator = ArcGIS(user_agent='myGeocoder')
lng_dict = {}
lat_dict = {}

for address in tqdm(addresses):
    location = locator.geocode(address)
    lng_dict[address] = location.longitude
    lat_dict[address] = location.latitude
    sleep(1)

with open("lng_dict.json", "w", encoding='UTF-8') as outfile:
    json.dump(lng_dict, outfile)

with open("lat_dict.json", "w", encoding='UTF-8') as outfile:
    json.dump(lat_dict, outfile)


