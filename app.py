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

from flask import Flask,request

app = Flask(__name__)
@app.route('/')
def hello_world():
    return("Welcome, please smile more")


if __name__ =="__main__":
    app.run(host='0.0.0.0', port=8080)
