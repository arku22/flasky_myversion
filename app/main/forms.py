from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# Define new name form
class NameForm(FlaskForm):

    name = StringField("What is my name?",
                       validators=[DataRequired()]
                       )
    submit = SubmitField("Submit")
