# PROJETO CRUD COM FLASK

Este é um projeto simples para conhecer o flask e suas ferramentas.

## Ferramentas usadas no projeto

- Flask
- flask_sqlalchemy
- flask_migrate
- flask_marshmallow
- marshmallow_sqlalchemy


## Como rodar?

```sh
python wsgi.py
```

ou

```sh
gunicorn wsgi:app
```

## Como migrar o banco de dados?

```sh
flask db init
flask db migrate
flask db upgrade
```
