FROM matancarmeli7/rpi-raspbian-opencv:latest
RUN [ "cross-build-start" ]
RUN apt-get update
RUN apt-get install moc
RUN pip install flask 
COPY alarmSound.py .
COPY Battlefield-3-M-COM-alarm-sound.mp3 .
RUN [ "cross-build-end" ]
EXPOSE 5000
CMD ["/usr/bin/python", "alarmSound.py"] 
