from flask_migrate import Migrate
from models import db
from flask import Flask

def init_db(app: Flask):
    db.init_app(app)
    migrate = Migrate(app, db)
    return db
