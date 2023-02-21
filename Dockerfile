FROM python:3.8.12-slim

WORKDIR /app

COPY ["requirements.txt", "app.py","object_detection_helper.py","search_and_translate.py","settings.py","./"]

RUN pip install google-search-results==2.4.1
RUN pip install googletrans==4.0.0-rc1 
RUN pip install tensorflow-cpu==2.6.2
RUN pip install Flask==2.0.3 
RUN pip install pillow==8.4.0 
RUN pip install tflite-support==0.3.1
RUN pip install requests==2.11.0
RUN pip install gunicorn==19.9.0
RUN pip install protobuf==3.19.4

COPY ["model zoo/chicken.tflite","model zoo/cropdisease.tflite","model zoo/fruitsharvest.tflite", "model zoo/weeds.tflite","./model zoo/"]

EXPOSE 8080

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:8080", "app:app"]





