import os


class Config():
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
    app.config['RECEIVE_ADDRESS'] = os.environ.get('RECEIVE_ADDRESS')
    app.config['SENDER_ALIAS'] = "[Flasky app notification]"