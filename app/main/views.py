from . import main
from flask import render_template, redirect, url_for, session
from .forms import NameForm


@main.route('/', ['GET', 'POST'])
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
        return redirect(url_for('main.index'))
    return render_template('index.html',
                           name=session.get('Name'),
                           form=form,
                           known=session.get('known', False)
                           )