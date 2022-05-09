from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(config_name):
    # initialize Flask app object
    app = Flask(__name__)

    # provide configuration to be used with app
    app.config.from_object(config[config_name])

    # initialize flask extensions with app
    db.init_app(app)

    # register blueprint

    return app
