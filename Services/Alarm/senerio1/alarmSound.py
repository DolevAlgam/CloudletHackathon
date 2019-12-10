import os
import time
from flask import Flask

app = Flask(__name__)
@app.route('/on')
def on():
    os.system('mocp -p Battlefield-3-M-COM-alarm-sound.mp3')
    
@app.route('/off')
def off():
    os.system('mocp -s')

app.run(host='0.0.0.0', debug=False)
