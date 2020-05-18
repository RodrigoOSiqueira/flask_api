from flask import jsonify


class CursoSerializer:
    def serialize_curso(self, curso):
        return {
            "id": curso['id'],
            "nome": curso['nome'],
            "descricao": curso['descricao']
        }

    def serialize_lista_cursos(self, cursos):
        return jsonify(list(map(
            lambda curso: {
                "id": curso['id'],
                "nome": curso['nome'],
                "descricao": curso['descricao']
            }, cursos
        )))

    def serialize(self, cursos):
        if isinstance(cursos, list):
            return self.serialize_lista_cursos(cursos)
        else:
            return self.serialize_curso(cursos)
