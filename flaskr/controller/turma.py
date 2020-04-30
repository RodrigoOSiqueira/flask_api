from flask import jsonify
from flaskr.db import get_db


class Turma:
    def pega_turma_id(self, turma_id: int):
        db = get_db()
        turma = db.execute(
            'SELECT * FROM Turma WHERE id = ?', (turma_id,)
        ).fetchone()

        return turma

    def pega_turma_nome(self, turma_nome: str):
        db = get_db()
        turma = db.execute(
            'SELECT * FROM Turma WHERE nome = ?', (turma_nome, )
        ).fetchone()

        return turma

    def lista_turma(self, limit, offset):
        db = get_db()
        lista_turma = db.execute(
            f'SELECT * FROM Turma LIMIT {offset}, {limit}'
        ).fetchall()

        return jsonify(list(map(
            lambda turma: {
                "id": turma['id'],
                "nome": turma['nome'],
                "curso_id": turma['curso_id']
            }, lista_turma
        )))

    def cria_turma(self, dados_turma: dict):
        db = get_db()
        nome_turma = dados_turma.get('nome')
        curso_id = dados_turma.get('curso_id')

        if not nome_turma or not curso_id:
            return 'Dados incompletos', 400

        if self.pega_turma_nome(nome_turma):
            return 'Turma já cadastrada', 422

        db.execute(
            'INSERT INTO Turma (nome, curso_id) VALUES (?, ?)',
            (nome_turma, curso_id)
        )
        db.commit()

        return dados_turma, 201

    def atualiza_turma(self, turma_id: id, dados_turma: dict):
        db = get_db()
        nome_turma = dados_turma.get('nome')

        if not self.pega_turma_id(turma_id):
            return 'Turma não existente', 404

        if not nome_turma:
            return 'Dados incompletos', 400

        if self.pega_turma_nome(nome_turma):
            return 'Turma já cadastrada', 422

        db.execute(
            'UPDATE Turma set nome = ? WHERE id = ?',
            (nome_turma, turma_id)
        )
        db.commit()
        turma_atualizada = self.pega_turma_id(turma_id)

        return {
            'id': turma_atualizada['id'],
            'nome': turma_atualizada['nome'],
            'curso_id': turma_atualizada['curso_id']
        }

    def deleta_turma(self, turma_id):
        if not self.pega_turma_id(turma_id):
            return 'Turma não existe!', 404

        db = get_db()
        db.execute('DELETE FROM Turma WHERE id = ?', (turma_id,))
        db.commit()

        return 'Turma deletada', 200
