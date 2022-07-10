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

from flask import Flask,render_template,request, jsonify
from models.classifier import classify

app = Flask(__name__)
@app.route('/')
def hello_world():
    return("Welcome, please smile more")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    raw_data = request.get_json(force=True)
    return (classify(raw_data)
)

if __name__ =="__main__":
    app.run()