import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # Change to work with ORM
from flask_migrate import Migrate  # Change to work with ORM

from .config import Config  # Change to work with ORM

db = SQLAlchemy()  # Change to work with ORM


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)  # Change to work with ORM
    db.init_app(app)  # Change to work with ORM
    Migrate(app, db)  # Change to work with ORM

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import models  # Change to work with ORM
    from . import views

    app.register_blueprint(views.curso)

    return app
