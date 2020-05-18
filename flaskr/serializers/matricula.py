from flask import jsonify


class MatriculaSerializer:
    def serialize_matricula(self, matricula):
        return {
            "id": matricula['id'],
            "nome": matricula['nome_aluno'],
            "turma_id": matricula['turma_id']
        }

    def serialize_lista_matriculas(self, matriculas):
        return jsonify(list(map(
            lambda matricula: {
                "id": matricula['id'],
                "nome": matricula['nome_aluno'],
                "turma_id": matricula['turma_id']
            }, matriculas
        )))

    def serialize(self, matriculas):
        if isinstance(matriculas, list):
            return self.serialize_lista_matriculas(matriculas)
        else:
            return self.serialize_matricula(matriculas)
