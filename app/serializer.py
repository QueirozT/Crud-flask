from marshmallow import fields, validates, ValidationError
from flask_marshmallow import Marshmallow

from .model import Book


ma = Marshmallow()


def configure(app):
    """Este método é responsável por configurar o marshmallow para o flask."""
    ma.init_app(app)


class BookSchema(ma.SQLAlchemyAutoSchema):
    """Esta classe configura um serializador para o modelo Pessoa"""
    class Meta:
        model = Book
        load_instance=True

    livro = fields.Str(required=True)
    escritor = fields.Str(required=True)

    @validates('id')
    def validate_id(self, value):
        raise ValidationError('Dont send the ID field.')
