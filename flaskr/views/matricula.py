from flask import Blueprint, request

from flaskr.models import Matricula, Turma
from flaskr.serializers import MatriculaSerializer

bp_matricula = Blueprint('matricula', __name__, url_prefix='/matricula')


@bp_matricula.route('/criar', methods=['POST'])
def cria_matricula():
    dados = request.json
    if not dados.get('nome_aluno') or not dados.get('turma_id'):
        return 'Dados incompletos', 400

    if not Turma().pega_turma_id(dados.get('turma_id')):
        return 'Turma não cadastrada', 404

    matricula = Matricula().cria_matricula(dados)

    return matricula, 201


@bp_matricula.route('/<int:matricula_id>', methods=['GET'])
def pega_matricula(matricula_id):
    matricula = Matricula().pega_matricula_id(matricula_id)
    if not matricula:
        return '', 204

    return MatriculaSerializer().serialize(matricula)


@bp_matricula.route('/', methods=['GET'])
def lista_matricula():
    query_string = request.args
    page = query_string.get('page', 1, type=int)
    per_page = query_string.get('per_page', 10, type=int)

    limit = per_page
    offset = (page - 1) * per_page
    matriculas = Matricula().lista_matricula(limit, offset)

    return MatriculaSerializer().serialize(matriculas)


@bp_matricula.route('/<int:matricula_id>', methods=['PUT'])
def atualiza_matricula(matricula_id):
    dados = request.json

    if not Matricula().pega_matricula_id(matricula_id):
        return 'Matricula não existente', 404

    if not dados.get('nome'):
        return 'Dados incompletos', 400

    if Matricula().pega_matricula_aluno(dados.get('nome')):
        return 'Aluno já cadastrado', 422

    matricula_atualizada = Matricula.atualiza_matricula(matricula_id, dados)

    return MatriculaSerializer().serialize(matricula_atualizada)


@bp_matricula.route('/<int:matricula_id>', methods=['DELETE'])
def deleta_matricula(matricula_id):
    if not Matricula().pega_matricula_id(matricula_id):
        return 'Matricula não existe!', 404

    return Matricula().deleta_matricula(matricula_id), 200
