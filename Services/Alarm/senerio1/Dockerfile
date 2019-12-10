FROM resin/raspberrypi3-python
RUN [ "cross-build-start" ]
RUN pip install --no-cache-dir pygame
COPY alarmSound.py .
COPY Battlefield-3-M-COM-alarm-sound.mp3 .
RUN [ "cross-build-end" ]
CMD ["/usr/bin/python", "alarmSound.py"] 
