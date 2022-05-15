from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment


db = SQLAlchemy()
mail = Mail()
bootstrap = Bootstrap()
moment = Moment()


def create_app(config_name):
    # initialize Flask app object
    app = Flask(__name__)

    # provide configuration to be used with app
    app.config.from_object(config[config_name])

    # initialize flask extensions with app
    db.init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)

    # register blueprint
    from .main import main
    from .auth import auth
    app.register_blueprint(main)
    app.register_blueprint(auth, url_prefix='/auth')

    return app
