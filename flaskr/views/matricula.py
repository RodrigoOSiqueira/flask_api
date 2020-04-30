from flask import Blueprint, request

from flaskr.controller import Matricula

bp_matricula = Blueprint('matricula', __name__, url_prefix='/matricula')


@bp_matricula.route('/criar', methods=['POST'])
def cria_matricula():
    dados = request.json
    resposta = Matricula().cria_matricula(dados)

    return resposta


@bp_matricula.route('/<int:matricula_id>', methods=['GET'])
def pega_matricula(matricula_id):
    matricula = Matricula().pega_matricula_id(matricula_id)
    if not matricula:
        return '', 204

    return {
        "id": matricula['id'],
        "nome_aluno": matricula['nome_aluno'],
        "turma_id": matricula['turma_id']
    }


@bp_matricula.route('/', methods=['GET'])
def lista_matricula():
    query_string = request.args
    page = query_string.get('page', 1, type=int)
    per_page = query_string.get('per_page', 10, type=int)

    limit = per_page
    offset = (page - 1) * per_page
    matriculas = Matricula().lista_matricula(limit, offset)

    return matriculas


@bp_matricula.route('/<int:matricula_id>', methods=['PUT'])
def atualiza_matricula(matricula_id):
    dados = request.json
    matricula_atualizada = Matricula.atualiza_matricula(matricula_id, dados)

    return matricula_atualizada


@bp_matricula.route('/<int:matricula_id>', methods=['DELETE'])
def deleta_matricula(matricula_id):
    return Matricula().deleta_matricula(matricula_id)
