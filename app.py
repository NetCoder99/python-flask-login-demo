from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_login import LoginManager, login_required, logout_user, current_user
from flask_session import Session

from auth.auth      import auth_blueprint
from data.getData   import getData_blueprint
from tabs.tabsProcs import getTabs_blueprint
from flask_cors     import CORS
from github_procs.github_api import gitapi_blueprint

from setup import db

from logging.config import dictConfig
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] :: %(levelname)s :: %(module)s :: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.register_blueprint(auth_blueprint,    url_prefix='/auth')
app.register_blueprint(getData_blueprint, url_prefix='/data')
app.register_blueprint(gitapi_blueprint,  url_prefix='/git')
app.register_blueprint(getTabs_blueprint, url_prefix='/tabs')

CORS(app)

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

@app.route("/favicon.ico")
def favicon():
    return ''

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    app.logger.info(f'index was called')
    return render_template('index.html')

@app.route('/login_ajax')
def login_reroute():
    app.logger.info(f'login_ajax was called')
    return redirect("/auth/login_ajax")

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
    missing_url = None
    try:
        if request is not None:
            missing_url = request.url
    except Exception as ex:
        print(f'exception:{ex}')

    app.logger.error(f"page_not_found:{e}\n{missing_url}")
    if missing_url is None:
        return render_template("error.html",message="Page not found")
    else:
        return render_template("error.html",message="Page not found", original_message=missing_url)

@app.errorhandler(500)
def server_error(e):
    app.logger.error(f"server_error:{e}")
    #return render_template("error.html", message=str(e))
    try:
        if e.original_exception:
            original_message = str(e.original_exception)
            app.logger.error(f"server_error:original_exception:{original_message}")
            return render_template("error.html", message=str(e), original_message=original_message)
        else:
            return render_template("error.html", message=str(e))
    except Exception as ex:
        return render_template("error.html", message=str(ex))


if __name__ == '__main__':
    app.run(debug=True)