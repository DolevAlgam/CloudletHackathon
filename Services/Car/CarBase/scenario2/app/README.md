### Html server
----------
This app is built based on Django.

This server runs on Raspberry Pi, and is controlled by HTTP API.

####Setup:
1. Install Django:

	sudo pip install django
2. Then, at `http_server/` run:

	sudo python manage.py runserver 0.0.0.0:8000
