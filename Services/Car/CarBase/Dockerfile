FROM resin/raspberry-pi-alpine-python

ADD ./app /home/pi/app
WORKDIR /home/pi.שפפ

RUN pip2 install django smbus

#RUN python /home/pi/Sunfounder_Smart_Video_Car_Kit_for_RaspberryPi/i2cHelper.py << "y"
CMD python /home/pi/app/manage.py runserver 0.0.0.0:8000
