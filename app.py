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
from easy_predict_helper import *

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
