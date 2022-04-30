from flask import Flask, render_template, redirect, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
import os
from pathlib import Path
from flask_migrate import Migrate
from flask_mail import Mail, Message


app = Flask(__name__)


app.config['SECRET_KEY'] = "archit"


# initialize flask extensions
bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)


# add objects to be imported by default
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)


# Define new name form
class NameForm(FlaskForm):

    name = StringField("What is my name?",
                       validators=[DataRequired()]
                       )
    submit = SubmitField("Submit")


# define database tables
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    rolename = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return f"{self.name}"


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return f"{self.username}"


def send_email(to, subject, template_name, **kwargs):
    msg = Message(subject=subject,
                  recipients=[to],
                  sender=app.config['SENDER_ALIAS']
                  )
    msg.body = render_template(template_name + '.txt', **kwargs)
    msg.html = render_template(template_name + '.html', **kwargs)
    mail.send(msg)


# define main/home page
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        usr_chk = User.query.filter_by(username=form.name.data).first()
        if usr_chk is None:
            session['known'] = False
            new_user = User(username=form.name.data)
            db.session.add(new_user)
            db.session.commit()
            send_email(app.config['RECEIVE_ADDRESS'],
                       'New User Added',
                       template_name="mail/new_user",
                       user=new_user
                       )
        elif usr_chk is not None:
            session['known'] = True
        session['Name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html',
                           name=session.get('Name'),
                           form=form,
                           known=session.get('known', False)
                           )


# define user page
@app.route('/user/<name>')
def greet_user(name):
    return render_template("user.html", name=name)


# handle "page not found" error
@app.errorhandler(404)
def page_not_found(e):
    return render_template("notfound.html"), 404

