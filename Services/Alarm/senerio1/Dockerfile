FROM resin/raspberrypi3-python
RUN [ "cross-build-start" ]
COPY alarmSound.py .
COPY Battlefield-3-M-COM-alarm-sound.mp3 .
RUN [ "cross-build-end" ]
CMD ["/usr/bin/python", "alarmSound.py"] 
