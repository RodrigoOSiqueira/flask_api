from flask import Blueprint, request

from flaskr.controller import Turma

bp_turma = Blueprint('turma', __name__, url_prefix='/turma')


@bp_turma.route('/criar/', methods=['POST'])
def cria_turma():
    dados = request.json
    resposta = Turma().cria_turma(dados)

    return resposta


@bp_turma.route('/<int:turma_id>', methods=['GET'])
def pega_turma(turma_id):
    turma = Turma().pega_turma_id(turma_id)
    if not turma:
        return '', 204

    return {
        "id": turma['id'],
        "nome": turma['nome'],
        "curso_id": turma['curso_id'],
    }


@bp_turma.route('/', methods=['GET'])
def lista_turmas():
    query_string = request.args
    page = query_string.get('page', 1, type=int)
    per_page = query_string.get('per_page', 10, type=int)

    limit = per_page
    offset = (page - 1)*per_page
    turmas = Turma().lista_turma(limit, offset)

    return turmas


@bp_turma.route('/<int:turma_id>', methods=['PUT'])
def atualiza_turma(turma_id):
    dados = request.json
    turma_atualizada = Turma().atualiza_turma(turma_id, dados)

    return turma_atualizada


@bp_turma.route('/<int:turma_id>', methods=['DELETE'])
def deleta_turma(turma_id):
    return Turma().deleta_turma(turma_id)
