from playsound import playsound
from flask import Flask

app = Flask(__name__)
@app.route('/alarm')
def alarm():
    playsound('audio.mp3')

app.run(host='0.0.0.0', debug=False)
