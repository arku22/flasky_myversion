import os
from pathlib import Path


# define any/all config options common across all classes
class Config():
    SECRET_KEY = "archit"
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    RECEIVE_ADDRESS = os.environ.get('RECEIVE_ADDRESS')
    SENDER_ALIAS = "[Flasky app notification]"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


# define development specific config options
class DevelopmentConfig(Config):
    DEBUG = True
    curr_dir = os.getcwd()
    my_db_url = 'sqlite:///' + str(Path(curr_dir, 'data-dev.sqlite'))
    SQLALCHEMY_DATABASE_URI = my_db_url


# define testing specific config options
class TestingConfig(Config):
    TESTING = True
    curr_dir = os.getcwd()
    my_db_url = 'sqlite:///' + str(Path(curr_dir, 'data-test.sqlite'))
    SQLALCHEMY_DATABASE_URI = my_db_url


# define production specific config options
class ProductionConfig(Config):
    curr_dir = os.getcwd()
    my_db_url = 'sqlite:///' + str(Path(curr_dir, 'data.sqlite'))
    SQLALCHEMY_DATABASE_URI = my_db_url


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
