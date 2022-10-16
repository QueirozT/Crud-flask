from flask import Blueprint, current_app, jsonify, request
from flask_marshmallow import exceptions

from .model import Book
from .serializer import BookSchema


bp_books = Blueprint('books', __name__)


@bp_books.route('/cadastrar', methods=['POST'])
def cadastrar():
    bs = BookSchema()
    try:
        book = bs.load(request.json)
    except exceptions.ValidationError as e:
        error = {"Error": e.messages_dict}
        return jsonify(error), 400
    else:
        current_app.db.session.add(book)
        current_app.db.session.commit()
        return bs.jsonify(book), 201


@bp_books.route('/mostrar', methods=['GET'])
def mostrar():
    ps = BookSchema(many=True)  # many=True retorna uma lista
    books = Book.query.all()
    return ps.jsonify(books), 200


@bp_books.route('/atualizar/<int:id>', methods=['PUT'])
def atualizar(id):
    bs = BookSchema()
    query = Book.query.filter_by(id=id)
    try:
        if not query.first():
            raise KeyError
        query.update(request.json)
    except KeyError as e:
        return jsonify({'Error': {'id': id}}), 400
    except:
        return jsonify({'Error': request.json}), 400
    else:
        current_app.db.session.commit()
        return bs.jsonify(query.first()), 201


@bp_books.route('/remover/<int:id>', methods=['DELETE'])
def remover(id):
    query = Book.query.filter(Book.id == id).delete()

    if query:
        current_app.db.session.commit()
        return '', 204
    else:
        return jsonify({'Error': {'id': id}}), 400
