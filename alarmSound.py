import pygame
import time
from flask import Flask

app = Flask(__name__)

pygame.init()

@app.route('/alarm')
    pygame.mixer.music.load('/home/pi/Desktop/Battlefield 3 M-COM alarm sound [$
    pygame.mixer.music.play(0)
    time.sleep(10)

app.run(host='0.0.0.0', debug=False)
