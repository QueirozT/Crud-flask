from urllib import response
from flask import url_for


def test_rota_mostrar_deve_retornar_200_e_vazio_quando_não_tiver_dados(client):
    response = client.get(url_for('books.mostrar'))

    assert response.status_code == 200
    assert response.json == []


def test_rota_cadastrar_deve_retornar_201_quando_json_enviado_for_valido(client):
    json = {'livro': 'Teste', 'escritor': 'pessoa'}
    
    response = client.post(url_for('books.cadastrar'), json=json)

    json['id'] = 1
    
    assert response.status_code == 201
    assert response.json == json


def test_rota_cadastrar_deve_retornar_400_quando_id_for_enviado_no_json(client):
    json = {'livro': 'xpto', 'escritor': 'pessoa', 'id': 2}

    response = client.post(url_for('books.cadastrar'), json=json)

    retorno_esperado = {'Error': {'id': ['Dont send the ID field.']}}

    assert response.status_code == 400
    assert response.json == retorno_esperado


def test_rota_cadastrar_deve_retornar_400_quando_json_enviado_for_invalido(client):
    json = {'todo': 'vazio'}

    response = client.post(url_for('books.cadastrar'), json=json)
    
    retorno_esperado = {'Error': {'escritor': ['Missing data for required field.'], 'livro': ['Missing data for required field.'], 'todo': ['Unknown field.']}}

    assert response.status_code == 400
    assert response.json == retorno_esperado


def test_rota_cadastrar_deve_retornar_400_quando_não_enviar_dados(client):
    response = client.post(url_for('books.cadastrar'))

    assert response.status_code == 400
    assert response.json == None


def test_rota_mostrar_deve_retornar_200_e_os_dados_cadastrados(client):
    response = client.get(url_for('books.mostrar'))

    retorno_esperado = [{'escritor': 'pessoa', 'id': 1, 'livro': 'Teste'}]

    assert response.status_code == 200
    assert response.json == retorno_esperado


def test_rota_atualizar_deve_retornar_201_quando_dados_forem_alterados(client):
    json = {'livro': 'pessoa', 'escritor': 'Teste'}

    response = client.put(url_for('books.atualizar', id=1), json=json)

    json['id'] = 1

    assert response.status_code == 201
    assert response.json == json


def test_rota_atualizar_deve_retornar_400_quando_dados_forem_invalidos(client):
    json = {'xpto': 'vazio'}

    response = client.put(url_for('books.atualizar', id=1), json=json)

    assert response.status_code == 400
    assert response.json == {'Error': json}


def test_rota_atualizar_deve_retornar_400_quando_id_for_inválido(client):
    json = {'livro': 'teste'}

    response = client.put(url_for('books.atualizar', id=2), json=json)

    assert response.status_code == 400
    assert response.json == {'Error': {'id': 2}}


def test_rota_atualizar_deve_retornar_400_quando_dados_forem_parcialmente_invalidos(client):
    json = {'livro': 'xpto', 'escritor': 'todo', 'extra': 'invalido'}

    response = client.put(url_for('books.atualizar', id=1), json = json)

    assert response.status_code == 400
    assert response.json == {'Error': json}


def test_rota_remover_deve_retornar_400_quando_não_encontrar_o_id(client):
    response = client.delete(url_for('books.remover', id=2))

    assert response.status_code == 400
    assert response.json == {'Error': {'id': 2}}


def test_rota_remover_deve_retornar_204_quando_remover_os_dados(client):
    response = client.delete(url_for('books.remover', id=1))

    assert response.status_code == 204
    assert response.json == None
