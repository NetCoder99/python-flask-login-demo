# --------------------------------------------------------------
# Various fields to support login form
# --------------------------------------------------------------
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length

class LoginForm(FlaskForm):
    #username = StringField('User Id:', validators=[InputRequired(), Length(min=3, max=15)])
    #password = PasswordField('Password:', validators=[InputRequired(), Length(min=8, max=80)])
    username = StringField('User Id:')
    password = PasswordField('Password:')
    remember = BooleanField('Remember Me: ')