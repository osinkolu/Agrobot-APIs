# -*- coding: utf-8 -*-
"""
@author: Professor
"""

"""

{
    "main_word":"Corn leaf blight", 
    "usecase":"crop_disease",
    "language": "en"
}
    
"""

from flask import Flask,request, jsonify
from object_detection_helper import ObjectDetectorOptions, ObjectDetector, visualization_params, Image, np #import everything from object detection 


from settings import model_influencer
from search_and_translate import search_and_translate, translate_alone


app = Flask(__name__)
@app.route('/')
def hello_world():
    return("Welcome, please smile more")

@app.route("/help_me", methods=["GET", "POST"])

def help_me(raw_data):
    try:
        main_word, language, usecase = raw_data["main_word"], raw_data["language"], raw_data["usecase"]
    except Exception:
        return("could not split request into input i require")
    try:
        support = model_influencer(usecase)
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

@app.route("/predict", methods=['GET', 'POST'])

def predict(called_me=True):
    try:
        file = request.files['image']
    except Exception:
        return("Could not read any file")
    try:
        thresh = float(request.headers["threshold"])
    except Exception:
        return("Could not read threshold from header")
    try:
        model_name = str(request.headers["usecase"])
    except:
        return("Use case could not be read")

    # Read the image via file.stream
    try:
        im = Image.open(file.stream).convert('RGB')  #convert in case we have a wierd number of channels in the image.
    except Exception:
        return("PIL could not open image from the file stream")
    try:
        im.thumbnail((512, 512), Image.ANTIALIAS)
    except:
        return("PIL could not thumbnail the Image")
    try:
        image_np = np.asarray(im)
    except Exception:
        return("Numpy could not translate image into array")
    try:
        options = ObjectDetectorOptions(num_threads=4,score_threshold=thresh)
    except Exception:
        return("Object Detector could not resolve requirements of 4 threads")
    try:
        detector = ObjectDetector(model_path='model zoo/'+model_name+'.tflite', options=options)
    except Exception:
        return("Object detector could not initialize model")
    try:
        detections = detector.detect(image_np)
    except Exception:
        return("Dector could not return detections")
    try:
        bounding_box_details, num_detections = visualization_params(image_np, detections)
        print(bounding_box_details)
        if called_me:
            return jsonify({"msg": 'success', "bounding_box_details":bounding_box_details, "number of predictions":num_detections})
        else:
            return (bounding_box_details[0][-2:])
    except Exception:
        if called_me:
            return jsonify({"msg": 'failure', "bounding_box_details":[], "number of predictions":0})
        else:
            return ["Nothing"]

@app.route("/analyze", methods=['GET', 'POST'])
def analyze():
    try:
        language = request.headers["language"]
    except Exception:
        return("I Could not read language from your header")
    try:
        usecase = request.headers["usecase"]
    except Exception:
        return("I couldn't read your usecase")
    
    try:
        main_data = predict(called_me=False)
    except Exception:
        return("The function doing the image prediction is having some errors, I don't know what it is.")

    raw_data = {
    "main_word":main_data[0], 
    "usecase": usecase,
    "language": language}

    print("####################", main_data, "#########################")
    try:
        more_details = help_me(raw_data=raw_data)
    except Exception:
        return("The function checking for details about the detections is having some errors, I don't know what it is.")
    
    try:
        return jsonify ({"main_data":{"label":main_data[0],"confidence":main_data[1]}, "more_details": more_details})    
    except Exception:
        return ("I got all your result, but something happened and I couldn't send them to you.")

if __name__ =="__main__":
    app.run(host='0.0.0.0', port=8080)