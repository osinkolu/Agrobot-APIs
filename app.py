# -*- coding: utf-8 -*-
"""
@author: Professor
"""

"""
{
"raw_values":[
    {
        "N":9000,
        "P":4200,
        "K":4300,
        "temperature":200.87974371,
        "humidity":802.00274423,
        "ph":60.502985292,
        "rainfall":2020.9355362
    }
        ]
}
"""

# Lazy Format

"""
{
    "lat":7.4905, 
    "lon":4.5521
}
"""

import json
from flask import Flask, request
from classifier import classify
import pandas as pd
import json
import os
import requests

Open_weathermaps_api_key = "253c41dfcc642a2a76ef235ad92ab00c" #os.environ['Open_weathermaps_api_key']
print(Open_weathermaps_api_key)
all_data = pd.read_csv("Victor_Nigerian_soil_database.csv")

def get_parameters(coordinates,all=False):
    nearest_coordinates = get_nearest_coordinates(coordinates)
    if all:
        return(all_data[all_data['coordinates']==str(nearest_coordinates)].to_json(orient='records'))
    else:
        return(all_data[all_data['coordinates']==str(nearest_coordinates)][['N','P','K','pH']].values[0])


def get_nearest_coordinates(coordinates):
    coordinates_list = [(all_data["X"][i],all_data["Y"][i]) for i in range(len(all_data))]
    return(min(coordinates_list, key=lambda c: (c[0]- coordinates[0])**2 + (c[1]-coordinates[1])**2))

def get_weather_params(coordinates, all=False):
    lat, lon = coordinates
    url = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(lat,lon,Open_weathermaps_api_key)
    response = requests.request("GET", url, headers={}, data={})
    if all:
        return(json.loads(response.text))
    else:
        if 'rain' in json.loads(response.text):
            rain = json.loads(response.text)['rain']['1h']
        else:
            rain = 0
        humidity  = json.loads(response.text)['main']['humidity']
        temperature_K = json.loads(response.text)['main']['temp']
        temperature_c = temperature_K - 273.15
        return(rain, humidity, temperature_c)

def collate_data(coordinates):
    N,P,K,pH = get_parameters(coordinates)
    rain, humidity, temperature_c = get_weather_params(coordinates)
    dictionary =     { "raw_values":[ {
        "N":N,
        "P":P,
        "K":K,
        "temperature":temperature_c,
        "humidity":humidity,
        "ph":pH,
        "rainfall": rain
    }
        ]}
    return(dictionary)

def dump_all_data(coordinates):
    dump = {
    "#### climate ####":(get_weather_params((7.196450,9.048933), all=True)),
    "#### Soil ####": json.loads(get_parameters((7.196450,9.048933), all=True)),
    "#### Description ####": "The climate data is pulled from open weather maps API, the soil data is a local data base which is still growing, we may have altered your location slightly to the closest location in the database while trying to pull up soil data for you."
}
    return dump










app = Flask(__name__)
@app.route('/')
def hello_world():
    return("Welcome, please smile more")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    raw_data = request.get_json(force=True)
    return (classify(raw_data))

@app.route("/easy_predict", methods=["GET", "POST"])
def easy_predict():
    data = request.get_json(force=True)
    coordinates = (data['lat'], data['lon'])
    print(coordinates)
    raw_data = collate_data(coordinates)
    return (classify(raw_data))

@app.route("/data_dump", methods=["GET", "POST"])
def data_dump():
    data = request.get_json(force=True)
    coordinates = (data['lat'], data['lon'])
    print(coordinates)
    raw_data = dump_all_data(coordinates)
    return (raw_data)


if __name__ =="__main__":
    app.run(host='0.0.0.0', port=8080)
