from flask import Blueprint, request

from flaskr.models import Turma, Curso
from flaskr.serializers import TurmaSerializer

bp_turma = Blueprint('turma', __name__, url_prefix='/turma')


@bp_turma.route('/criar/', methods=['POST'])
def cria_turma():
    dados = request.json

    if not dados.get('nome') or not dados.get('curso_id'):
        return 'Dados incompletos', 400

    if not Curso().pega_curso_id(dados.get('curso_id')):
        return 'Curso não cadastrado', 404

    if Turma().pega_turma_nome(dados.get('nome')):
        return 'Turma já cadastrada', 422

    resposta = Turma().cria_turma(dados)

    return resposta, 201


@bp_turma.route('/<int:turma_id>', methods=['GET'])
def pega_turma(turma_id):
    turma = Turma().pega_turma_id(turma_id)
    if not turma:
        return '', 204

    return TurmaSerializer().serialize_turma(turma)


@bp_turma.route('/', methods=['GET'])
def lista_turmas():
    query_string = request.args
    page = query_string.get('page', 1, type=int)
    per_page = query_string.get('per_page', 10, type=int)

    limit = per_page
    offset = (page - 1)*per_page
    turmas = Turma().lista_turma(limit, offset)

    return TurmaSerializer().serialize_lista_turmas(turmas)


@bp_turma.route('/<int:turma_id>', methods=['PUT'])
def atualiza_turma(turma_id):
    dados = request.json

    if not dados.get('nome'):
        return 'Dados incompletos', 400

    if not Turma().pega_turma_id(turma_id):
        return 'Turma não existente', 404

    if Turma().pega_turma_nome(dados.get('nome')):
        return 'Turma já cadastrada', 422

    turma_atualizada = Turma().atualiza_turma(turma_id, dados)

    return TurmaSerializer().serialize_turma(turma_atualizada)


@bp_turma.route('/<int:turma_id>', methods=['DELETE'])
def deleta_turma(turma_id):
    if not Turma().pega_turma_id(turma_id):
        return 'Turma não existe!', 404

    return Turma().deleta_turma(turma_id), 200
