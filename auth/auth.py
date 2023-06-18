import json
import os
from time import sleep

from flask import Blueprint, redirect, url_for, flash, render_template, request, session
from flask_login import login_user
from flask_session import Session

from werkzeug.security import check_password_hash, generate_password_hash

from auth.ldap import CheckUserCreds
from models.LoginForm import LoginForm
from models.SignUpForm import SignUpForm
from models.User import User

from setup import db

auth_blueprint = Blueprint('auth_blueprint',
                           __name__,
                           template_folder='templates',
                           static_folder='static')

@auth_blueprint.route('/login_ajax', methods=['GET', 'POST'])
def login_ajax():
    html_name = "login_ajax.html"
    form = LoginForm()
    if request.method == 'GET':
        flash("Please enter your login credentials.")
        return render_template(html_name, form=form)

    # user_name = form.username.data
    # pass_word = form.password.data
    # if not form.validate_on_submit():
    #     flash("Invalid credentials.")
    #     return render_template(html_name, form=form)
    #
    # valid, session_user = CheckUserCreds(user_name, pass_word)
    # if not valid:
    #     flash("Invalid credentials.")
    #     return render_template(html_name, form=form)
    #
    # login_user(session_user, remember=form.remember.data)
    # session[session_user.uid] = session_user
    # return redirect(url_for('dashboard'))


@auth_blueprint.route('/login_api', methods=['POST'])
def login_api():
    print('login_api - started')
    sleep(3)
    try:
        login_data = str(request.data)
    except Exception as ex:
        print(f'Error: {ex.__str__()}')

    rtn_value = "login succeeded"
    print('login_api - finished')
    return json.dumps(rtn_value)

@auth_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Invalid fields.")
        return render_template('signup.html', form=form)

    return render_template('signup.html', form=form)


