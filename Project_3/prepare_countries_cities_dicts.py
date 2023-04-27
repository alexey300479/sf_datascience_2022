"""
This module must be run before running EDA_Project_3_model_v3.ipynb
to prepare countries and cities dictionaries to add new features
into hotels dataset
"""


import json

import pandas as pd
from geopy.geocoders import ArcGIS
from tqdm import tqdm

hotels = pd.read_csv('hotels.csv')

hotel_names = hotels.hotel_name.unique()

locator = ArcGIS(user_agent='myGeocoder')
countries = {}
cities = {}

for hotel_name in tqdm(hotel_names):
    lat = hotels[hotels.hotel_name == hotel_name].lat.values[0]
    lng = hotels[hotels.hotel_name == hotel_name].lng.values[0]
    location = locator.reverse(f'{lat},{lng}')
    countries[hotel_name] = location.raw['CntryName']
    cities[hotel_name] = location.raw['City']

with open("countries.json", "w", encoding='UTF-8') as outfile:
    json.dump(countries, outfile)

with open("cities.json", "w", encoding='UTF-8') as outfile:
    json.dump(cities, outfile)
