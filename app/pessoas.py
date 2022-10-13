from flask import Blueprint, current_app, request, jsonify
from flask_marshmallow import exceptions

from .model import Pessoa
from .serializer import PessoaSchema


bp_pessoas = Blueprint('pessoas', __name__)


@bp_pessoas.route('/cadastrar', methods=['POST'])
def cadastrar():
    ps = PessoaSchema()

    try:
        pessoa = ps.load(request.json)
    except exceptions.ValidationError as e:
        err = {"Error": e.messages_dict}
        return jsonify(err), 400
    except Exception as e:
        err = {"Error": {"Requerido": {"nome": "String", "idade": "Integer"}, "Recebido": request.json}}
        return jsonify(err), 400
    else:
        current_app.db.session.add(pessoa)
        current_app.db.session.commit()
        return ps.jsonify(pessoa), 201


@bp_pessoas.route('/mostrar', methods=['GET'])
def mostrar():
    ps = PessoaSchema(many=True)  # many=True para retornar uma lista de pessoas
    pessoas = Pessoa.query.all()

    return ps.jsonify(pessoas), 200


@bp_pessoas.route('/atualizar/<int:id>', methods=['PUT'])
def atualizar(id):
    ps = PessoaSchema()

    query = Pessoa.query.filter(Pessoa.id == id)
    query.update(request.json)
    current_app.db.session.commit()

    resp = 200 if query.first() else 204

    return ps.jsonify(query.first()), resp


@bp_pessoas.route('/remover/<int:id>', methods=['DELETE'])
def remover(id):
    query = Pessoa.query.filter(Pessoa.id == id).delete()

    if query:
        current_app.db.session.commit()
        return jsonify("Removido com sucesso!"), 204
    else:
        return jsonify("ID não encontrado."), 400