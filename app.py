from flask import Flask, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

from auth.auth import auth_blueprint
from models.LoginForm import LoginForm
from models.SignUpForm import SignUpForm
from setup import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'


app.register_blueprint(auth_blueprint, url_prefix='/auth')

with app.app_context():
    db.init_app(app)
    from models.User import User
    db.create_all()
    db.session.commit()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html",message="Page not found")

@app.errorhandler(500)
def page_not_found(e):
    return render_template("error.html", message=str(e))
    # try:
    #     if e.original_exception:
    #         original_message = str(e.original_exception)
    #         return render_template("error.html", message=str(e), original_message=original_message)
    #     else:
    #         return render_template("error.html", message=str(e))
    # except Exception as ex:
    #     return render_template("error.html", message=str(e))


if __name__ == '__main__':
    app.run(debug=True)