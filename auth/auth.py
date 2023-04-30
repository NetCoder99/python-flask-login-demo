from flask import Blueprint, redirect, url_for, flash, render_template, request
from flask_login import login_user
from werkzeug.security import check_password_hash, generate_password_hash

from models.LoginForm import LoginForm
from models.SignUpForm import SignUpForm
from models.User import User

from setup import db

auth_blueprint = Blueprint('auth_blueprint',
                           __name__,
                           template_folder='templates',
                           static_folder='static')

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    call_type = request.method

    user_name = form.username.data
    pass_word = form.password.data
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))

        flash("Invalid credentials.")
        return render_template('login.html', form=form)

    return render_template('login.html', form=form)


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


