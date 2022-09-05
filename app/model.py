from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def configure(app):
    """Este método é responsável por configurar o SQLAlchemy para o flask."""
    db.init_app(app)
    app.db = db


class Pessoa(db.Model):
    """Esta classe é responsável por criar o modelo da tabela Pessoa"""
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
