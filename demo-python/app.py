import datetime
import flask
import logging

app = flask.Flask(__name__)
start = datetime.datetime.now()

# Disable default werkzeug request logging
log = logging.getLogger("werkzeug")
log.disabled = True

@app.route('/', methods=['GET'])
def root():
    logging.warning('main route was accessed')
    return flask.jsonify({'message': 'flask app root/'})

@app.route('/health', methods=['GET'])
def health():
    now = datetime.datetime.now()
    logging.warning("health route was accessed")
    return flask.jsonify({'message': f'up and running since {(now - start)}'})

@app.errorhandler(404)
def page_not_found(error):
    logging.error(f"404 error: {error}")
    return flask.jsonify({'message': 'route not found'}), 404

# This must be at the root level, not indented inside another function
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
