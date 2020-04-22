from flask import Blueprint, request, jsonify, url_for

from . import db
from .models import Curso


curso = Blueprint('curso', __name__, url_prefix='/curso')


@curso.route('/criar', methods=['POST'])
def create_curso():
    data = request.json
    novo_curso = Curso(**data)

    novo_curso.save()

    return request.json, 201


@curso.route('/<int:curso_id>/delete', methods=['DELETE'])
def delete_curso(curso_id):
    curso = Curso.query.get(curso_id)
    db.session.delete(curso)
    db.session.commit()

    return 'Deleted', 200


@curso.route('/<int:curso_id>', methods=['GET'])
def get_curso(curso_id):
    curso = Curso.query.get(curso_id)

    return curso.data()


@curso.route('/', methods=['GET'])
def list_curso():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    cursos = Curso.query.paginate(page, per_page)

    next_page = (
        url_for('curso.list_curso', page=cursos.next_num, per_page=per_page)
        if cursos.has_next else None
    )
    prev_page = (
        url_for('curso.list_curso', page=cursos.prev_num, per_page=per_page)
        if cursos.has_prev else None
    )

    return jsonify({
        "data": list(map(lambda curso: curso.data(), cursos.items)),
        "current_page": page,
        "next_page": next_page,
        "prev_page": prev_page,
        "first_page": url_for('curso.list_curso', page=1),
        "total": cursos.total,
        "pages": cursos.pages
    })
