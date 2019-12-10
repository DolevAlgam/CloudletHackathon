import simpleaudio as sa
import time
import flask

app = flask.Flask(__name__)
@app.route('/on')
def on():
    wave_obj = sa.WaveObject.from_wave_file("Battlefield-3.wav")
    play_obj = wave_obj.play()
    time.sleep(10)
    play_obj.stop()
    return flask.Response(response="on", status=200, mimetype='text/xml')

app.run(host='0.0.0.0', debug=False)
