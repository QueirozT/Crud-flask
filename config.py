from decouple import config


class ProdConf(object):
    DEBUG = False
    SECRET_KEY = config('SECRET_KEY', default="você-nunca-vai-adivinhar")
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URL', default='sqlite:///')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConf(object):
    TESTING = True
    SECRET_KEY = "você-nunca-vai-adivinhar"
    SQLALCHEMY_DATABASE_URI = "sqlite:///"
    SQLALCHEMY_TRACK_MODIFICATIONS = False