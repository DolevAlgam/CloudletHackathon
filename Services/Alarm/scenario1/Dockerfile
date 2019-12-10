FROM resin/raspberrypi3-python
RUN [ "cross-build-start" ]
#RUN apt-get update

RUN pip install requests flask

ADD ./app /home/pi/app
WORKDIR /home/pi/app
RUN [ "cross-build-end" ]

CMD python alarm_api_server.py
