import flask
import os
import simpleaudio as sa
import time

app = flask.Flask(__name__)

@app.route('/alarmon', methods=['GET'])
def alarmon():
	wave_obj = sa.WaveObject.from_wave_file("Battlefield.wav")
	play_obj = wave_obj.play()
	time.sleep(10)
	play_obj.stop()
	return flask.Response(response="alarmon", status=200, mimetype='text/xml')

app.run(host='0.0.0.0', port=4000, debug=False)
