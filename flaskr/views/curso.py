from flask import Blueprint, request

from flaskr.models import Curso
from flaskr.serializers import CursoSerializer

bp_curso = Blueprint('curso', __name__, url_prefix='/curso')


@bp_curso.route('/criar', methods=['POST'])
def cria_curso():
    dados = request.json

    if not dados.get('nome') or not dados.get('descricao'):
        return 'Dados incompletos', 400

    if Curso().pega_curso_nome(dados.get('nome')):
        return 'Curso já cadastrado', 422

    novo_curso = Curso().cria_curso(dados)

    return novo_curso, 201


@bp_curso.route('/<int:curso_id>', methods=['GET'])
def pega_curso(curso_id):
    curso = Curso().pega_curso_id(curso_id)
    if not curso:
        return '', 204

    return CursoSerializer().serialize(curso)


@bp_curso.route('/', methods=['GET'])
def lista_cursos():
    query_string = request.args
    page = query_string.get('page', 1, type=int)
    per_page = query_string.get('per_page', 10, type=int)

    limit = per_page
    offset = (page - 1)*per_page
    cursos = Curso().lista_cursos(limit, offset)

    return CursoSerializer().serialize(cursos)


@bp_curso.route('/<int:curso_id>', methods=['PUT'])
def atualiza_curso(curso_id):
    dados = request.json

    if not Curso().pega_curso_id(curso_id):
        return 'Curso não existente', 404

    if not dados.get('nome') or not dados.get('descricao'):
        return 'Dados incompletos', 400

    if Curso().pega_curso_nome(dados.get('nome')):
        return 'Curso já cadastrado', 422

    curso_atualizado = Curso().atualiza_curso(curso_id, dados)

    return CursoSerializer().serialize(curso_atualizado)


@bp_curso.route('/<int:curso_id>', methods=['DELETE'])
def deleta_curso(curso_id):
    if not Curso().pega_curso_id(curso_id):
        return 'Curso não existente', 404

    return Curso().deleta_curso(curso_id), 200
