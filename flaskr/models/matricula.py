from flaskr.db import get_db


class Matricula:
    def pega_matricula_id(self, matricula_id: int):
        db = get_db()
        matricula = db.execute(
            'SELECT * FROM Matricula WHERE id = ?', (matricula_id,)
        ).fetchone()

        return matricula

    def verifica_matricula_turma(self, turma_id: int, matricula_id: int):
        db = get_db()
        matricula = db.execute(
            'SELECT * FROM Matricula WHERE id = ? AND turma_id = ?',
            (matricula_id, turma_id,)
        ).fetchone()

        return matricula

    def cria_matricula(self, turma_id: int, nome_aluno: str):
        db = get_db()

        db.execute(
            'INSERT INTO Matricula (nome_aluno, turma_id) VALUES (?, ?)',
            (nome_aluno, turma_id)
        )
        db.commit()

        return {
            "nome_aluno": nome_aluno,
            "turma_id": turma_id
        }

    def atualiza_matricula(self, matricula_id: id, nome_aluno: str):
        db = get_db()

        db.execute(
            'UPDATE Matricula set nome_aluno = ? WHERE id = ?',
            (nome_aluno, matricula_id)
        )
        db.commit()
        matricula_atualizada = self.pega_matricula_id(matricula_id)

        return matricula_atualizada

    def deleta_matricula(self, matricula_id):
        db = get_db()
        db.execute('DELETE FROM Matricula WHERE id = ?', (matricula_id,))
        db.commit()

        return 'Matricula deletada'
