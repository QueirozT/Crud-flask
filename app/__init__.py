from flask import Flask
from flask_migrate import Migrate

from .model import configure as config_db
from .serializer import configure as config_ma

from .books import bp_books


def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)

    config_db(app)
    config_ma(app)

    Migrate(app, app.db)

    app.register_blueprint(bp_books)

    return app
