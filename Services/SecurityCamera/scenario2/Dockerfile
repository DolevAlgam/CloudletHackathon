FROM matancarmeli7/rpi-raspbian-opencv:latest
RUN [ "cross-build-start" ]
RUN pip3 install --upgrade pip
RUN pip install --no-cache-dir flask jsonpickle PiCamera numpy requests picamera[array]
RUN mkdir ./models ./templates
COPY models ./models
COPY templates ./templates
COPY camera.py .
COPY main.py .
RUN chmod +x main.py
RUN chmod +x camera.py
RUN [ "cross-build-end" ]
EXPOSE 5000
CMD ["/usr/bin/python3", "main.py"] 
