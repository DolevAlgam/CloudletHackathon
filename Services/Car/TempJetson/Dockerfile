FROM resin/raspberrypi3-python

#RUN [ "cross-build-start" ]

RUN pip install requests
RUN pip install flask

ADD ./app /home/pi/app
WORKDIR /home/pi/app

#RUN [ "cross-build-end" ]

CMD python jetson.py
