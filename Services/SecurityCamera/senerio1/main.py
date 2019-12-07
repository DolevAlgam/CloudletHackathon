import cv2
import sys
from flask import Flask, render_template, Response
from camera import VideoCamera
from flask_basicauth import BasicAuth
import time
import threading

video_camera = VideoCamera(flip=False) # creates a camera object, flip vertically
object_classifier = cv2.CascadeClassifier("models/haarcascade_frontalface_default.xml") # an opencv classifier

# App Globals
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    #Creates the colored frame around the recognized face
    while True:
        frame = camera.get_object(object_classifier)
        # yield creates a genator but return it like a normal return, it only creates it for a future use
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
# Creates multipart resposes that creates the video streaming with the genator that the gen function created
def video_feed():
    return Response(gen(video_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
