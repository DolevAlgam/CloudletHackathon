import flask

app = flask.Flask(__name__)

@app.route('/scan', methods=['GET'])
def scan():
    return flask.Response(response="attack", status=200, mimetype='text/xml')

app.run(host='0.0.0.0', port=5000, debug=False)
