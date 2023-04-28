from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

from setup import db


class User(UserMixin, db.Model):
    #__bind_key__   = 'auth'
    __tablename__  = 'user'
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email    = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))


