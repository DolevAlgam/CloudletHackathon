### Html server
----------
This app is built based on Django.

Control the Smart Video Car via the gravity sensor on a cell phone - control the car and the camera onside, as well as view the camera video in real time. What's more, on the app, you can conveniently calibrate the car turning and the pan-tilt. 

This server runs on Raspberry Pi, and is controlled by the Android app.

Download the app from [Google Play](https://play.google.com/store/apps/details?id=appinventor.ai_cavonxx.SunFounder_Smart_Video_Car)

####Setup:
1. Install Django:

	sudo pip install django
2. Then, at `http_server/` run:

	sudo python manage.py runserver 0.0.0.0:8000
