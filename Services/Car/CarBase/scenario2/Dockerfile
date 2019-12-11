FROM resin/raspberrypi3-python
#ENV INITSYSTEM on
RUN [ "cross-build-start" ]

#RUN apt-get update
#RUN apt-get install python-pip
RUN apt-get install python-smbus

#RUN pip install -U setuptools
RUN pip install explorerhat
RUN pip install requests
RUN pip install django
RUN pip install smbus

ADD ./app /home/pi/app
WORKDIR /home/pi/app

RUN chmod +x getPimoroni.sh
#RUN ./getPimoroni.sh

RUN chmod +x setup-i2c.sh
#RUN ./setup-i2c.sh
RUN [ "cross-build-end" ]
#RUN python3 manage.py migrate
#CMD ./getPimoroni.sh && ./setup-i2c.sh && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
CMD python manage.py runserver 0.0.0.0:8000
