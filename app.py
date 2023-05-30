from flask import Flask, render_template, redirect, url_for, flash, session
from flask_login import LoginManager, login_required, logout_user, current_user
from flask_session import Session

from auth.auth import auth_blueprint
from data.getData import getData_blueprint

from setup import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(getData_blueprint, url_prefix='/data')

with app.app_context():
    db.init_app(app)
    from models.User import User
    db.create_all()
    db.session.commit()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login_reroute'

@login_manager.user_loader
def load_user(user_id):
    tmp = session.get(user_id)
    return tmp

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login')
def login_reroute():
    return redirect("/auth/login")

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
    #return render_template("error.html", message=str(e))
    try:
        if e.original_exception:
            original_message = str(e.original_exception)
            return render_template("error.html", message=str(e), original_message=original_message)
        else:
            return render_template("error.html", message=str(e))
    except Exception as ex:
        return render_template("error.html", message=str(ex))


if __name__ == '__main__':
    app.run(debug=True)