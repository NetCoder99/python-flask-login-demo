from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length


class SignUpForm(FlaskForm):
    email = StringField('Email Address', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('User Id', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])