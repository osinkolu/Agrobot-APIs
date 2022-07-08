# -*- coding: utf-8 -*-
"""
@author: Professor
"""
from flask import Flask,request, jsonify
from object_detection_helper import ObjectDetectorOptions, ObjectDetector, visualization_params, Image, np #import everything from object detection 


app = Flask(__name__)
@app.route('/')
def hello_world():
    return("Welcome, please smile more")


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    try:
        file = request.files['image']
    except Exception:
        return("Could not read any file")
    try:
        thresh = float(request.headers["threshold"])
    except Exception:
        return("Could not read threshold from header")
    try:
        model_name = request.headers["use_case"]
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
        return jsonify({'msg': 'success', "bounding_box_details":bounding_box_details, "number of predictions":num_detections})
    except Exception:
        return jsonify({'msg': 'failure', "bounding_box_details":[], "number of predictions":0})


if __name__ =="__main__":
    app.run(host='0.0.0.0', port=8080)