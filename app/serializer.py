from flask_marshmallow import Marshmallow

from .model import Pessoa


ma = Marshmallow()


def configure(app):
    """Este método é responsável por configurar o marshmallow para o flask."""
    ma.init_app(app)


class PessoaSchema(ma.SQLAlchemyAutoSchema):
    """Esta classe configura um serializador para o modelo Pessoa"""
    class Meta:
        model = Pessoa
        load_instance=True
