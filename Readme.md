# Crop Recommendation API

## Introduction
This is a flask API that recommends what kind of crop to plant, this project is part of the Agrobot project to provide A.I tools to farmers.

### Dependencies

* [Python](https://www.python.org/) - Programming Language
* [Flask](https://flask.palletsprojects.com/) - The framework used
* [Pip](https://pypi.org/project/pip/) - Dependency Management
* [RESTful](https://restfulapi.net/) - REST docs

### Virtual environments

```
$ sudo apt-get install python-virtualenv
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install Flask
```

Install all project dependencies using:

```
$ pip install -r requirements.txt
```
## Support
For API support, please reach out on [LinkedIn](https://www.linkedin.com/in/olufemi-victor-tolulope/) or [Twitter](https://twitter.com/Osinkoluolufemi).

## Basic Authentication

Accesss to the API is granted freely, there is no authentication put in place currently

The API has been deployed on Azure with CI-CD. It is accessible via: https://agrobotfarms-crop-rec-api-v1.azurewebsites.net/predict you'll need to post your input Json format

``` POST
    requests.post(
        url, files=my_img, json = {
"raw_values":[
    {
        "N":90,
        "P":42,
        "K":43,
        "temperature":20.87974371,
        "humidity":82.00274423,
        "ph":60.502985292,
        "rainfall":202.9355362
    }
        ]                           }
                    ) 
```
## Definitions

"N" - Nitrogen level in the soil
"P"  - Phosporus level in the soil
"K" - Potassium level in the soil
"Temperature" - The current temperature of the surroundings in degree celcius.
"Humidiy" - Relative humidity.
"PH" - The PH value of the soil
"rainfall" - the rainfall value in mm

## API Versioning
There will be subsequent versions of this API as frameworks change, models update, use cases expand and as it gets better. However, the API version you wish to access in the format `v{version_number}`

Currently version 1 of the API (most current) is accessible via:
[this link](https://agrobotfarms-crop-rec-api-v1.azurewebsites.net/predict)

## HTTP requests
All API requests are made by sending a secure HTTPS request using one of the following methods, depending on the action being taken:

* `POST` Create a resource
* `GET` Get a resource or list of resources

## HTTP Responses
The HTTP response is very basic, the request returns a list of predictions, one prediction for each input sample.
```
["rice", "orange"]

```
## HTTP Response Codes
Each response will be returned with one of the following HTTP status codes:

* `200` `OK` The request was successful
* `400` `Bad Request` There was a problem with the request (security, malformed, data validation, etc.)
* `404` `Not found` An attempt was made to access a resource that does not exist in the API
* `405` `Method not allowed` The resource being accessed doesn't support the method specified (GET, POST, etc.).
* `500` `Server Error` An error on the server occurred

## Dataset Used to build model.
Dataset is Openly Available on Kaggle - https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset. It was curated for the indian agricultural context. 

## Model Information(coming soon):

The information of the A.I model- training, validation and metrics will be made available soon.