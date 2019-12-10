import flask
import requests
import os

HOSTIP = os.getenv('HOSTIP')
GETURL = "http://{}:4000/alarmon".format(HOSTIP)

app = flask.Flask(__name__)

@app.route('/on', methods=['GET'])
def on():
	return flask.Response(response="on", status=200, mimetype='text/xml')
	r = requests.get(GETURL)

app.run(host='0.0.0.0', port=5000, debug=False)
