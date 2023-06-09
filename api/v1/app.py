#!/usr/bin/python3

"""
This is the main module of the Flask application
"""

from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify, make_response
from flask_cors import CORS
from os import getenv
from flask_session import Session

app = Flask(__name__)
app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.secret_key = 'your_secret_key_here'
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Configure Flask Session
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_FILE_THRESHOLD'] = 100
app.config['SESSION_FILE_MODE'] = 384
app.config['SESSION_FILE_DIR'] = '/tmp/flask_session'
app.config['SESSION_COOKIE_NAME'] = 'flask_session'
app.config['SESSION_COOKIE_DOMAIN'] = None
app.config['SESSION_COOKIE_PATH'] = None
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SECURE'] = False
app.config['SESSION_REFRESH_EACH_REQUEST'] = True
sess = Session()
sess.init_app(app)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Closes the storage"""
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """Handles 404 error"""
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    host = getenv('HUDUMA_API_HOST')
    port = getenv('HUDUMA_API_PORT')

    if not host:
        host = '0.0.0.0'

    if not port:
        port = 5000

    app.run(host=host, port=port, threaded=True)
