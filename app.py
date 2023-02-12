# -*- coding: utf-8 -*-
"""
@author: Professor
"""

"""

{
    "main_word":"Corn leaf blight", 
    "use_case":"crop_disease",
    "language": "en"
}
    
"""
from settings import model_influencer
from search_and_translate import search_and_translate, translate_alone
from flask import Flask,request


app = Flask(__name__)
@app.route('/')
def hello_world():
    return("Welcome, please smile more")

@app.route("/help_me", methods=["GET", "POST"])

def help_me():
    try:
        raw_data = request.get_json(force=True)
    except Exception:
        return("Could not load the request")
    try:
        main_word, language, use_case = raw_data["main_word"], raw_data["language"], raw_data["use_case"]
    except Exception:
        return("could not split request into input i require")
    try:
        support = model_influencer(use_case)
    except Exception:
        return("could not initialize the model influencer")
    try:
        support.set_params()
    except Exception:
        return("Could not setup the settings")
    try:
        first_text = search_and_translate(support.string1 + main_word,language)
    except Exception:
        return("could not process first text of my response")
    try:
        second_text = translate_alone(support.string2 + main_word, language)
    except Exception:
        return("could not process first the second of my response")
    try:
        third_text = search_and_translate(support.string3 + main_word,language)
    except Exception:
        return("could not process the third text of my response")
    reply = { 
        "about": first_text,
        "extra_topic": second_text,
        "topic_description": third_text
    }
    return reply

if __name__ =="__main__":
    app.run(host='0.0.0.0', port=8080)