from flask import jsonify


class TurmaSerializer:
    def serialize_turma(self, turma):
        return {
            "id": turma['id'],
            "nome": turma['nome'],
            "curso_id": turma['curso_id']
        }

    def serialize_lista_turmas(self, turmas):
        return jsonify(list(map(
            lambda turma: {
                "id": turma['id'],
                "nome": turma['nome'],
                "curso_id": turma['curso_id']
            }, turmas
        )))

    def serialize(self, turmas):
        if isinstance(turmas, list):
            return self.serialize_lista_turmas(turmas)
        else:
            return self.serialize_turma(turmas)
