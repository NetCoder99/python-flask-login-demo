# --------------------------------------------------------------
# Init sqlalchemy here to prevent circular references
# --------------------------------------------------------------
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
