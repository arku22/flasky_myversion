from . import mail
from flask_mail import Message
from flask import render_template, current_app


def send_email(to, subject, template_name, **kwargs):
    msg = Message(subject=subject,
                  recipients=[to],
                  sender=current_app.config['SENDER_ALIAS']
                  )
    msg.body = render_template(template_name + '.txt', **kwargs)
    msg.html = render_template(template_name + '.html', **kwargs)
    mail.send(msg)
