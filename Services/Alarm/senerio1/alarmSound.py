from playsound import playsound
from flask import Flask

app = Flask(__name__)
@app.route('/alarm')
def alarm():
    playsound('Battlefield-3-M-COM-alarm-sound.mp3')

app.run(host='0.0.0.0', debug=False)
