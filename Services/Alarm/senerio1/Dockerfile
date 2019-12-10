FROM matancarmeli7/rpi-raspbian-opencv:latest
RUN [ "cross-build-start" ]
RUN pip3 install playsound flask gi 
COPY alarmSound.py .
COPY Battlefield-3-M-COM-alarm-sound.mp3 .
RUN [ "cross-build-end" ]
EXPOSE 5000
CMD ["/usr/bin/python3", "alarmSound.py"] 
