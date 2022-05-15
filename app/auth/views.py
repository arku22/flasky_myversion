from . import auth
from flask import render_template


@auth.route('/login')
def login():
    render_template('auth/login.html')
