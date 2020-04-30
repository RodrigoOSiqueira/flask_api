from flask import jsonify
from flaskr.db import get_db


class Matricula:
    def pega_matricula_id(self, matricula_id: int):
        db = get_db()
        matricula = db.execute(
            'SELECT * FROM Matricula WHERE id = ?', (matricula_id,)
        ).fetchone()

        return matricula

    def pega_matricula_aluno(self, nome_aluno: str):
        db = get_db()
        matricula = db.execute(
            'SELECT * FROM Matricula WHERE nome_aluno = ?', (nome_aluno, )
        ).fetchone()

        return matricula

    def lista_matricula(self, limit, offset):
        db = get_db()
        lista_matricula = db.execute(
            f'SELECT * FROM Matricula LIMIT {offset}, {limit}'
        ).fetchall()

        return jsonify(list(map(
            lambda matricula: {
                "id": matricula['id'],
                "nome": matricula['nome_aluno'],
                "curso_id": matricula['turma_id']
            }, lista_matricula
        )))

    def cria_matricula(self, dados_matricula: dict):
        db = get_db()
        nome_aluno = dados_matricula.get('nome_aluno')
        turma_id = dados_matricula.get('turma_id')

        if not nome_aluno or not turma_id:
            return 'Dados incompletos', 400

        db.execute(
            'INSERT INTO Matricula (nome, turma_id) VALUES (?, ?)',
            (nome_aluno, turma_id)
        )
        db.commit()

        return dados_matricula, 201

    def atualiza_matricula(self, matricula_id: id, dados_matricula: dict):
        db = get_db()
        nome_aluno = dados_matricula.get('nome')

        if not self.pega_matricula_id(matricula_id):
            return 'Matricula não existente', 404

        if not nome_aluno:
            return 'Dados incompletos', 400

        if self.pega_matricula_aluno(nome_aluno):
            return 'Aluno já cadastrado', 422

        db.execute(
            'UPDATE Matricula set nome_aluno = ? WHERE id = ?',
            (nome_aluno, matricula_id)
        )
        db.commit()
        matricula_atualizada = self.pega_matricula_id(matricula_id)

        return {
            'id': matricula_atualizada['id'],
            'nome': matricula_atualizada['nome'],
            'curso_id': matricula_atualizada['curso_id']
        }

    def deleta_matricula(self, matricula_id):
        if not self.pega_matricula_id(matricula_id):
            return 'Matricula não existe!', 404

        db = get_db()
        db.execute('DELETE FROM Matricula WHERE id = ?', (matricula_id,))
        db.commit()

        return 'Matricula deletada', 200
