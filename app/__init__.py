from flask import Flask
from config import config


def create_app(config_name):
    # initialize Flask app object
    app = Flask(__name__)

    # provide configuration to be used with app
    app.config.from_object(config[config_name])

    # initialize flask extensions with app

    # register blueprint

    return app
