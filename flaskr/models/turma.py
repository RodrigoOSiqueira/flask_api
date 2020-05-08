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
        lista_turmas = db.execute(
            f'SELECT * FROM Turma LIMIT {offset}, {limit}'
        ).fetchall()

        return lista_turmas

    def cria_turma(self, dados_turma: dict):
        db = get_db()
        nome_turma = dados_turma.get('nome')
        curso_id = dados_turma.get('curso_id')

        db.execute(
            'INSERT INTO Turma (nome, curso_id) VALUES (?, ?)',
            (nome_turma, curso_id)
        )
        db.commit()

        return dados_turma

    def atualiza_turma(self, turma_id: id, dados_turma: dict):
        db = get_db()
        nome_turma = dados_turma.get('nome')

        db.execute(
            'UPDATE Turma set nome = ? WHERE id = ?',
            (nome_turma, turma_id)
        )
        db.commit()
        turma_atualizada = self.pega_turma_id(turma_id)

        return turma_atualizada

    def deleta_turma(self, turma_id):
        db = get_db()
        db.execute('DELETE FROM Turma WHERE id = ?', (turma_id,))
        db.commit()

        return 'Turma deletada'
