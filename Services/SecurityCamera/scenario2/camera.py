import cv2
from imutils.video.pivideostream import PiVideoStream
import imutils
import time
import numpy as np
import requests

close_time = 0
delay = 20

class VideoCamera(object):
# initiate the VideoCamera object
    def __init__(self, flip = False):
        self.vs = PiVideoStream().start()
        self.flip = flip
        time.sleep(2.0)
# Deletes VideoCamera object
    def __del__(self):
        self.vs.stop()
# If the argument flip is true, the picture is fliping
    def flip_if_needed(self, frame):
        if self.flip:
            return np.flip(frame, 0)
        return frame
# Recognize a face and call the alarm every 20 seconds
    def get_object(self, classifier):
        global delay
        global close_time
        frame = self.flip_if_needed(self.vs.read()).copy() 
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        objects = classifier.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        if len(objects) > 0 and time.time() > close_time:
	    try:
		requests.get(url= 'http://car:8000/scenario2', timeout=0.00000001)
            except requests.exceptions.ReadTimeout:
		pass
            close_time=time.time()+delay
        # Draw a rectangle around the objects
        for (x, y, w, h) in objects:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        ret, jpeg = cv2.imencode('.jpg', frame)
        return (jpeg.tobytes())


