# Crop Analysis API.

## Overview
The crop analysis API is built to perfrom detections on an image based on the selected agricultural use-case. Developers can leverage the API to make detections via the A.I models. This API tool is open source and requires no account setup to use.

## Tutorial
Tutorial on how to use the API is coming soon, however, it is a simple to use API.

## Support
For API support, please reach out on [LinkedIn](https://www.linkedin.com/in/olufemi-victor-tolulope/) or [Twitter](https://twitter.com/Osinkoluolufemi).

## Basic Authentication

Accesss to the API is granted freely, there is no authentication put in place currently

'POST
    requests.post(
        url, files=my_img, headers= {
        'threshold': threshold,
        'use_case': use_case
        }
        )'

## API Versioning
There will be subsequent versions of this API as frameworks change, models update, use cases expand and as it gets better. However, the API version you wish to access in the format `v{version_number}`

Currently version 1 of the API (most current) is accessible via:
........................

## HTTP requests
All API requests are made by sending a secure HTTPS request using one of the following methods, depending on the action being taken:

* `POST` Create a resource
* `GET` Get a resource or list of resources

Please note that the headers are important to pass the use case and the threshold to set the model to.

## HTTP Responses
The response is very basic, for each detection, the API returns the position of the bounding boxes : left, right, top, bottom, prediction, probability of detection. Asides the list, the API also returns the message status and the number of detections found.

'
{
    "bounding_box_details": [
        [
            134,
            296,
            108,
            265,
            "Weeds",
            0.98828125
        ],
        [
            300,
            409,
            143,
            282,
            "Weeds",
            0.9296875
        ]
    ],
    "msg": "success",
    "number of predictions": 2
}
'


## HTTP Response Codes
Each response will be returned with one of the following HTTP status codes:

* `200` `OK` The request was successful
* `400` `Bad Request` There was a problem with the request (security, malformed, data validation, etc.)
* `404` `Not found` An attempt was made to access a resource that does not exist in the API
* `405` `Method not allowed` The resource being accessed doesn't support the method specified (GET, POST, etc.).
* `500` `Server Error` An error on the server occurred

## Model Information(coming soon):

The information of each A.I model training will be made available, including the carbon footprint.
