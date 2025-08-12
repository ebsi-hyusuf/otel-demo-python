import datetime
import flask
import logging
import time
import requests



app = flask.Flask(__name__)
start = datetime.datetime.now()

# Disable default werkzeug request logging
log = logging.getLogger("werkzeug")
log.disabled = True

@app.route('/', methods=['GET'])
def root():
    logging.warning('main route was accessed')
    return flask.jsonify({'message': 'flask app root/'}), 200

@app.route('/health', methods=['GET'])
def health():
    now = datetime.datetime.now()
    logging.warning("health route was accessed")
    return flask.jsonify({'message': f'up and running since {(now - start)}'})


    

@app.route('/slow', methods=['GET'])
def slow():
    logging.warning("slow route was accessed, delay will be stimulated")
    time.sleep(10)
    logging.warning("responding after 10 second delay" )
    return flask.jsonify('responding after 10 second delay')


@app.route('/slow-api', methods=['GET'])
def slow_api():
    logging.warning("Simulating slow API call")
    try:
        # Simulate a slow external API call with a delay
        response = requests.get('https://httpbin.org/delay/5')  # 5-second delay
        return flask.jsonify({'message': 'API call completed', 'data': response.json()}), 200
    except Exception as e:
        logging.error(f"API call failed: {e}")
        return flask.jsonify({'error': 'API call failed'}), 500



@app.route('/fail', methods=['GET'])
def fail():
    logging.error('fail route triggered - example')
    raise Exception("simulated application failure for testing")

@app.errorhandler(404)
def page_not_found(error):
    logging.error(f"404 error: {error}")
    return flask.jsonify({'message': 'route not found'}), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
