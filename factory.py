import os

from flask import Flask

BASE_DIR = os.path.dirname(__file__)
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static')


def create_app():
    app = Flask(__name__)
    app.secret_key = os.urandom(12)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    return app
