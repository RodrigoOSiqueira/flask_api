from flask import Blueprint, request, jsonify, url_for
from flaskr.db import get_db

bp_curso = Blueprint('curso', __name__, url_prefix='/curso')


@bp_curso.route('/criar', methods=['POST'])
def criar_curso():
    data = request.json
    db = get_db()
    db.execute(
        'INSERT INTO Curso (nome, descricao) VALUES (?, ?)',
        (data.get('nome'), data.get('descricao'))
    )
    db.commit()

    return data


@bp_curso.route('/<int:curso_id>', methods=['GET'])
def pega_curso(curso_id):
    db = get_db()
    curso = db.execute(
        'SELECT * FROM Curso WHERE id = ?', (curso_id,)
    ).fetchone()

    return {
        "id": curso['id'],
        "nome": curso['nome'],
        "descricao": curso['descricao'],
    }
