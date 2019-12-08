FROM resin/raspberry-pi-alpine-python
ENV INITSYSTEM on

RUN pip install -U setuptools
RUN pip install explorerhat requests django smbus

ADD ./app /home/pi/app
WORKDIR /home/pi/app

RUN chmod +x setup-i2c.sh
RUN ./setup-i2c.sh

RUN python manage.py migrate
CMD python manage.py runserver 0.0.0.0:8000
