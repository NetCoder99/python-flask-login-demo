from flask_login import UserMixin
#from flask_sqlalchemy import SQLAlchemy

from setup import db
# class User(UserMixin, db.Model):
#     __tablename__  = 'user'
#     id       = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(15), unique=True)
#     email    = db.Column(db.String(50), unique=True)
#     password = db.Column(db.String(80))

class User(UserMixin):
    def __init__(self, dn, uid, username, email, active):
        self.dn = dn
        self.username = username
        self.uid      = uid
        self.email    = email
        self.active   = active

    def is_active(self):
        return self.active

    def get_id(self):
        return self.uid

    def __repr__(self):
        return self.dn

