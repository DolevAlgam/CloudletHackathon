FROM resin/raspberrypi3-python

RUN apt-get update

RUN pip install requests flask

ADD ./app /home/pi/app
WORKDIR /home/pi/app

CMD python alarm_api_server.py
