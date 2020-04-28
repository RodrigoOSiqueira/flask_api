from flask import Blueprint, request

from flaskr.controller import Curso

bp_curso = Blueprint('curso', __name__, url_prefix='/curso')


@bp_curso.route('/criar', methods=['POST'])
def cria_curso():
    data = request.json
    resposta = Curso().cria_curso(data)

    return resposta


@bp_curso.route('/<int:curso_id>', methods=['GET'])
def pega_curso(curso_id):
    curso = Curso().pega_curso_id(curso_id)
    if not curso:
        return '', 204

    return {
        "id": curso['id'],
        "nome": curso['nome'],
        "descricao": curso['descricao'],
    }


@bp_curso.route('/', methods=['GET'])
def lista_cursos():
    query_string = request.args
    page = query_string.get('page', 1, type=int)
    per_page = query_string.get('per_page', 10, type=int)

    limit = per_page
    offset = (page - 1)*per_page

    return Curso().lista_cursos(limit, offset)


@bp_curso.route('/<int:curso_id>', methods=['PUT'])
def atualiza_curso(curso_id):
    data = request.json
    curso_atualizado = Curso().atualiza_curso(curso_id, data)

    return curso_atualizado

@bp_curso.route('/<int:curso_id>', methods=['DELETE'])
def deleta_curso(curso_id):
    return Curso().deleta_curso(curso_id)
