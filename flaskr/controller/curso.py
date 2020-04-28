from flask import jsonify
from flaskr.db import get_db


class Curso:
    def pega_curso_id(self, curso_id: int):
        db = get_db()
        curso = db.execute(
            'SELECT * FROM Curso WHERE id = ?', (curso_id,)
        ).fetchone()

        return curso

    def pega_curso_nome(self, curso_nome: str):
        db = get_db()
        curso = db.execute(
            'SELECT * FROM Curso WHERE nome = ?', (curso_nome,)
        ).fetchone()

        return curso

    def lista_cursos(self, limit, offset):
        db = get_db()
        lista_cursos = db.execute(
            f'SELECT * FROM Curso LIMIT {offset}, {limit}'
        ).fetchall()

        return jsonify(list(map(
            lambda curso: {
                "id": curso['id'],
                "nome": curso['nome'],
                "descricao": curso['descricao']
            }, lista_cursos
        )))

    def cria_curso(self, dados_curso: dict):
        db = get_db()

        if not dados_curso.get('nome') or not dados_curso.get('descricao'):
            return 'Dados incompletos', 400

        if self.pega_curso_nome(dados_curso.get('nome')):
            return 'Curso já cadastrado', 422

        db.execute(
            'INSERT INTO Curso (nome, descricao) VALUES (?, ?)',
            (dados_curso.get('nome'), dados_curso.get('descricao'))
        )
        db.commit()

        return dados_curso, 201

    def atualiza_curso(self, curso_id, dados_curso):
        db = get_db()

        if not self.pega_curso_id(curso_id):
            return 'Curso não existente', 404

        if not dados_curso.get('nome') or not dados_curso.get('descricao'):
            return 'Dados incompletos', 400

        if self.pega_curso_nome(dados_curso.get('nome')):
            return 'Curso já cadastrado', 422

        db.execute(
            'UPDATE Curso set nome = ?, descricao = ?'
            ' WHERE id = ?',
            (dados_curso.get('nome'), dados_curso.get('descricao'), curso_id)
        )
        db.commit()
        curso_atualizado = self.pega_curso_id(curso_id)

        return {
            'id': curso_atualizado['id'],
            'nome': curso_atualizado['nome'],
            'descricao': curso_atualizado['descricao']
        }

    def deleta_curso(self, curso_id):
        if not self.pega_curso_id(curso_id):
            return 'Curso não existente', 404

        db = get_db()
        db.execute('DELETE FROM Curso WHERE id = ?', (curso_id,))
        db.commit()

        return 'Curso deletado', 200
