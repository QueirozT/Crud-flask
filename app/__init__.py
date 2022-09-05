from flask import Flask
from flask_migrate import Migrate

from .model import configure as config_db
from .serializer import configure as config_ma

from .pessoas import bp_pessoas


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../crud.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    config_db(app)
    config_ma(app)

    Migrate(app, app.db)

    app.register_blueprint(bp_pessoas)

    return app