import pygame
import time
from flask import Flask

app = Flask(__name__)

pygame.init()

@app.route('/alarm')
def alarm():
    pygame.mixer.music.load('Battlefield-3-M-COM-alarm-sound.mp3')
    pygame.mixer.music.play(0)
    time.sleep(10)

app.run(host='0.0.0.0', debug=False)
