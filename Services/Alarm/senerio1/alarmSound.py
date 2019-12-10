import os
import time
import flask

app = flask.Flask(__name__)
@app.route('/on')
def on():
    os.system('mocp -p Battlefield-3-M-COM-alarm-sound.mp3')
    return flask.Response(response="on", status=200, mimetype='text/xml')

@app.route('/off')
def off():
    os.system('mocp -s')
    return flask.Response(response="off", status=200, mimetype='text/xml')

app.run(host='0.0.0.0', debug=False)
